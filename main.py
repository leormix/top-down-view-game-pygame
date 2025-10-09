import pygame 
from pygame.math import Vector2
from sprites import *
import random
from pytmx.util_pygame import load_pygame
import pytmx
import time

pygame.init()

# vars

WINDOW_WIDTH, WINDOW_HEIGHT = 900, 600
screen = pygame.display.set_mode ((WINDOW_WIDTH, WINDOW_HEIGHT))
FPS = 60
ANIM_SPEED = 10
running = True
font = pygame.font.SysFont(None, 36)

start_time = pygame.time.get_ticks()
# duration = 6000

pygame.font.init()
pygame.display.set_caption("test")



class Player:
    def __init__(self, x=300, y=300, speed=1.3):
        self.pos = Vector2(x, y)  # вектор шоб он не ганял нахуй
        self.anim_count = 0
        self.walking = False
        self.attacking = False
        self.running = False
        self.direction = "down"
        self.last_horizontal = "right"
        self.attack_start_time = 0
        self.speed = speed
        self.knockback = Vector2(0, 0)   # Откид
        self.knockback_decay = 0.85 
        self.hp = 4
        self.dead = False
        self.death_time = None
        self.hurt = False
        self.has_hit = False  # ФИКС: Добавим флаг для отслеживания нанесения урона


    def handle_input(self):
        keys = pygame.key.get_pressed()
        vec = Vector2(0, 0)

        if self.dead: 
            pass
            return

        # спринт
        self.running = keys[pygame.K_LSHIFT]
        self.speed = 1.7 if self.running else 1.3

        # атака
        if keys[pygame.K_SPACE] and not self.attacking:
            self.attacking = True
            self.attack_start_time = pygame.time.get_ticks()
            self.attack_hit_time = self.attack_start_time + 300
            self.anim_count = 0
            self.has_hit = False  

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
        self.anim_count += 2

        # отталкування

        if self.knockback.length() > 0.1:
            self.pos += self.knockback
            self.knockback *= self.knockback_decay
            self.hurt = True
        else:
            self.knockback = Vector2(0, 0)

        # границі
        self.pos.x = max(-55, min(self.pos.x, WINDOW_WIDTH - 100))
        self.pos.y = max(-55, min(self.pos.y, WINDOW_HEIGHT - 100))

        # смерть і боль
        if self.dead:
            sprites = humanDeathLeft if self.last_horizontal == "left" else humanDeathRight
            self.anim_count += 1  # счётчик кадров смерти
            frame_index = self.anim_count // ANIM_SPEED
            if frame_index < len(sprites):
                frame = sprites[frame_index]
            else:
                frame = sprites[-1]
            screen.blit(frame, (int(self.pos.x), int(self.pos.y)))
            return
        if self.hurt:
            sprites = humanHurtLeft if self.last_horizontal == "left" else humanHurtRight
            frame_index = self.anim_count // ANIM_SPEED
            if frame_index < len(sprites):
                frame = sprites[frame_index]
                screen.blit(frame, (int(self.pos.x), int(self.pos.y)))
                self.anim_count += 2
                return
            else:
                self.hurt = False  

        # атака ходьба і просто стоять
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
            if self.running:
                if self.direction == "left":
                    sprites = humanRunLeft
                elif self.direction == "right":
                    sprites = humanRunRight
                else:
                    sprites = humanRunLeft if self.last_horizontal == "left" else humanRunRight
            else:
                if self.direction == "left":
                    sprites = humanWalkLeft
                elif self.direction == "right":
                    sprites = humanWalkRight
                else:
                    sprites = humanWalkLeft if self.last_horizontal == "left" else humanWalkRight
        else:
            sprites = humanIdleLeft if self.last_horizontal == "left" else humanIdleRight

        # отрісовка
        if len(sprites) > 0:
            frame = sprites[(self.anim_count // ANIM_SPEED) % len(sprites)]
            screen.blit(frame, (int(self.pos.x), int(self.pos.y)))


player = Player()
clock = pygame.time.Clock()

class Enemy:
    def __init__(self, x=500, y=300, speed=0.7, tile_size=32):
        self.pos = Vector2(x, y)
        self.anim_count = 0
        self.walking = False
        self.direction = "left"
        self.last_horizontal = "left"
        self.speed = speed
        self.tile_size = tile_size
        self.target_pos = self.pos.copy()  # куда идем
        self.wait_time = 0  
        self.game_over_time = None
        self.hp = 3
        self.hurt = False
        self.hurt_time = 0
        self.hurt_duration = 300
        
        

    def choose_new_action(self):
        # стоїм або ідем
        if random.random() < 0.5:
            # стоїм
            self.walking = False
            self.wait_time = random.randint(30, 60)  # 0.5–2 сек
        else:
            # ідем
            self.walking = True
            dx, dy = random.choice([(2,0),(-2,0),(0,2),(0,-2)])
            self.target_pos = self.pos + Vector2(dx*self.tile_size, dy*self.tile_size)
            # направление для анимации
            if dx < 0: self.direction, self.last_horizontal = "left", "left"
            if dx > 0: self.direction, self.last_horizontal = "right", "right"
            if dy < 0: self.direction = "up"
            if dy > 0: self.direction = "down"


        
    def update(self, player):
        self.anim_count += 2
        if self.hurt:
            sprites = goblinHurtLeft if self.last_horizontal == "left" else goblinHurtRight
            frame_index = (self.anim_count // ANIM_SPEED) % len(sprites)
            frame = sprites[frame_index]
            screen.blit(frame, (int(self.pos.x), int(self.pos.y)))

            # проверяем, прошло ли время анимации
            if pygame.time.get_ticks() - self.hurt_time > self.hurt_duration:
                self.hurt = False
            return  # не двигаемся, пока "болит"

        # направление на игрока
        direction = player.pos - self.pos
        if direction.length() > 1:
            move = direction.normalize() * self.speed
            self.pos += move

            # направление для анимации
            if abs(direction.x) > abs(direction.y):
                if direction.x < 0:
                    self.direction, self.last_horizontal = "left", "left"
                else:
                    self.direction, self.last_horizontal = "right", "right"
            else:
                if direction.y < 0:
                    self.direction = "up"
                else:
                    self.direction = "down"

            walking = True
        else:
            walking = False

        # выбор спрайтов
        if walking:
            sprites = goblinWalkLeft if self.last_horizontal == "left" else goblinWalkRight
        else:
            sprites = goblinIdleLeft if self.last_horizontal == "left" else goblinIdleRight

        frame = sprites[(self.anim_count // ANIM_SPEED) % len(sprites)]
        screen.blit(frame, (int(self.pos.x), int(self.pos.y)))

        # столкновение с игроком (только если он жив)
        if not player.dead:
            player_rect = pygame.Rect(player.pos.x, player.pos.y, 40, 40)
            enemy_rect = pygame.Rect(self.pos.x, self.pos.y, 40, 40)
            if player_rect.colliderect(enemy_rect):
                if player.knockback.length() == 0:
                    knockback = (player.pos - self.pos).normalize() * 8
                    player.knockback = knockback
                    player.hp -= 1
                    player.anim_count = 0
                    player.hurt = True
                    player.walking = False

                    if player.hp <= 0 and not player.dead:
                        player.dead = True
                        player.death_time = pygame.time.get_ticks()
                        player.anim_count = 0

        if self.hp <= 0:
            enemies.remove(self)
            return



                
class UI:
    def __init__(self, player):
        self.player = player
        self.movement_text = font.render("Movement: W,A,S,D  Attack: SPACE  Run: LSHIFT", True, (255, 255, 255))
        self.now = pygame.time.get_ticks()

    def update(self, surface):
        surface.blit(self.movement_text, (20, 25))
        for i in range(4):
            if i < self.player.hp:
                surface.blit(heartSprites[-1], (700 + i * 40, 20))
            else:
                surface.blit(heartSprites[0], (700 + i * 40, 20))

        if player.dead:
            if self.now - player.death_time < 60000:
                lose_text = font.render("GAME OVER", True, (255, 255, 255))
                text_rect = lose_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
                screen.blit(lose_text, text_rect)
   


ui = UI(player)

enemy = Enemy()
enemies = []
next_spawn_time = pygame.time.get_ticks() + random.randint(5000, 10000)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((100, 100, 0))

   
    player.update()
    ui.update(screen)

    if not player.dead:
        current_time = pygame.time.get_ticks()
        if current_time >= next_spawn_time:
            x = random.randint(0, WINDOW_WIDTH - 40)
            y = random.randint(0, WINDOW_HEIGHT - 40)
            enemies.append(Enemy(x, y))
            next_spawn_time = current_time + random.randint(5000, 10000)

        for enemy in enemies:
            enemy.update(player)
    else:
        # если игрок умер — просто отрисовываем врагов без движения
        for enemy in enemies:
            # выбираем статический спрайт (idle)
            sprites = goblinIdleLeft if enemy.last_horizontal == "left" else goblinIdleRight
            frame = sprites[(enemy.anim_count // ANIM_SPEED) % len(sprites)]
            screen.blit(frame, (int(enemy.pos.x), int(enemy.pos.y)))



    if player.attacking and not player.has_hit and current_time >= player.attack_hit_time:
        # напрямок атаки
        attack_direction = player.direction
        if attack_direction in ["up", "down"]:
            attack_direction = player.last_horizontal
            

        for enemy in enemies[:]:  
            distance = (enemy.pos - player.pos).length()
            
            # Проверяем расстояние и направление
            if distance < 60:
                if (attack_direction == 'left' and enemy.pos.x < player.pos.x) or \
                   (attack_direction == 'right' and enemy.pos.x > player.pos.x):
                    # Наносим урон только 1 раз за атаку
                    enemy.hurt = True
                    enemy.hurt_time = pygame.time.get_ticks()
                    enemy.hp -= 1  
                    player.has_hit = True  
                    
                   
                    if enemy.hp <= 0:
                        enemies.remove(enemy)
                    break  


    pygame.display.update()
    clock.tick(FPS)


pygame.quit()