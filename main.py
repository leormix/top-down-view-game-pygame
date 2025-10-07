import pygame 
from pygame.math import Vector2
from sprites import *
import random
from pytmx.util_pygame import load_pygame
import pytmx

pygame.init()

# vars

WINDOW_WIDTH, WINDOW_HEIGHT = 900, 500
screen = pygame.display.set_mode ((WINDOW_WIDTH, WINDOW_HEIGHT))
FPS = 60 
ANIM_SPEED = 10
running = True

pygame.display.set_caption("test")

class Player:
    def __init__(self, x=300, y=300, speed=1.3, hp=3):
        self.pos = Vector2(x, y)  # вектор шоб он не ганял нахуй
        self.anim_count = 0
        self.walking = False
        self.attacking = False
        self.running = False
        self.direction = "down"
        self.last_horizontal = "right"
        self.attack_start_time = 0
        self.speed = speed
        self.knockback = Vector2(0, 0)   # вектор откидывания
        self.knockback_decay = 0.85   

    def handle_input(self):
        keys = pygame.key.get_pressed()
        vec = Vector2(0, 0)

        # спринт
        self.running = keys[pygame.K_LSHIFT]
        self.speed = 1.7 if self.running else 1.3

        # атака
        if keys[pygame.K_SPACE] and not self.attacking:
            self.attacking = True
            self.attack_start_time = pygame.time.get_ticks()
            self.anim_count = 0

        if not self.attacking:
            if keys[pygame.K_w]:
                vec.y = -1; self.direction = "up"
            if keys[pygame.K_s]:
                vec.y = 1; self.direction = "down"
            if keys[pygame.K_a]:
                vec.x = -1; self.direction = "left"; self.last_horizontal = "left"
            if keys[pygame.K_d]:
                vec.x = 1; self.direction = "right"; self.last_horizontal = "right"

            if vec.length() > 0:  
                vec = vec.normalize() * self.speed #робим швидкість однаковую в усіх напрямах
                self.pos += vec
                self.walking = True
            else:
                self.walking = False

    def update(self):
        
        self.handle_input()

        self.handle_input()

    # применяем отталкивание
        if self.knockback.length() > 0.1:
            self.pos += self.knockback
            self.knockback *= self.knockback_decay  # плавное затухание
        else:
            self.knockback = Vector2(0, 0)
            
        self.anim_count += 2
        

        # границы
        self.pos.x = max(-55, min(self.pos.x, 800))
        self.pos.y = max(-55, min(self.pos.y, 400))

        # спрайтеке
        if self.attacking:
            if self.direction == "left":
                sprites = humanAttackLeft
            elif self.direction == "right":
                sprites = humanAttackRight
            else:
                sprites = humanAttackLeft if self.last_horizontal == "left" else humanAttackRight

            if self.anim_count // ANIM_SPEED >= len(sprites):
                self.attacking = False
                self.anim_count = 0

        elif self.walking:
            if self.running:  # бег
                if self.direction == "left":
                    sprites = humanRunLeft
                elif self.direction == "right":
                    sprites = humanRunRight
                else:
                    sprites = humanRunLeft if self.last_horizontal == "left" else humanRunRight
            else:  # обычная ходьба
                if self.direction == "left":
                    sprites = humanWalkLeft
                elif self.direction == "right":
                    sprites = humanWalkRight
                else:
                    sprites = humanWalkLeft if self.last_horizontal == "left" else humanWalkRight
        else:
            sprites = humanIdleLeft if self.last_horizontal == "left" else humanIdleRight

        # отрисовка
        frame = sprites[(self.anim_count // ANIM_SPEED) % len(sprites)]
        screen.blit(frame, (int(self.pos.x), int(self.pos.y)))

player = Player()
clock = pygame.time.Clock()

class Enemy:
    def __init__(self, x=500, y=300, speed=1, tile_size=32):
        self.pos = Vector2(x, y)
        self.anim_count = 0
        self.walking = False
        self.direction = "left"
        self.last_horizontal = "left"
        self.speed = speed
        self.tile_size = tile_size
        self.target_pos = self.pos.copy()  # куда идем
        self.wait_time = 0  # время ожидания

    def choose_new_action(self):
        """Случайно выбираем: стоять или идти на один квадрат"""
        if random.random() < 0.5:
            # стоим
            self.walking = False
            self.wait_time = random.randint(30, 60)  # 0.5–2 сек
        else:
            # идем
            self.walking = True
            dx, dy = random.choice([(2,0),(-2,0),(0,2),(0,-2)])
            self.target_pos = self.pos + Vector2(dx*self.tile_size, dy*self.tile_size)
            # направление для анимации
            if dx < 0: self.direction, self.last_horizontal = "left", "left"
            if dx > 0: self.direction, self.last_horizontal = "right", "right"
            if dy < 0: self.direction = "up"
            if dy > 0: self.direction = "down"

    def update(self, player):

        self.pos.x = max(-55, min(self.pos.x, 800))
        self.pos.y = max(-55, min(self.pos.y, 400))


        self.anim_count += 2

        if self.walking:
            # двигаемся к цели
            vec = self.target_pos - self.pos
            if vec.length() > self.speed:
                self.pos += vec.normalize() * self.speed
            else:
                self.pos = self.target_pos
                self.walking = False
                self.wait_time = random.randint(30, 120)
        else:
            # стоим и ждем
            self.wait_time -= 1
            if self.wait_time <= 0:
                self.choose_new_action()

        # выбор спрайтов
        if self.walking:
            if self.direction == "left":
                sprites = goblinWalkLeft
            elif self.direction == "right":
                sprites = goblinWalkRight
            else:
                sprites = goblinWalkLeft if self.last_horizontal == "left" else goblinWalkRight
        else:
            sprites = goblinIdleLeft if self.last_horizontal == "left" else goblinIdleRight

        frame = sprites[(self.anim_count // ANIM_SPEED) % len(sprites)]
        screen.blit(frame, (int(self.pos.x), int(self.pos.y)))

        # столкновение с игроком
        player_rect = pygame.Rect(player.pos.x, player.pos.y, 40, 40)
        enemy_rect = pygame.Rect(self.pos.x, self.pos.y, 40, 40)
        if player_rect.colliderect(enemy_rect):
            if player.knockback.length() == 0:  # только если не откидывается уже
                knockback = (player.pos - self.pos).normalize() * 8
                player.knockback = knockback

enemy = Enemy()


while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       

    screen.fill((100, 100, 0))

    player.update()
    enemy.update(player)
    clock.tick(FPS)

    pygame.display.update() 

pygame.quit()