import pygame

# Игрок

# Игрок стоит

humanIdleLeft = [
    pygame.image.load('sprites/human/human_idle_left/image_part_001.png'),
    pygame.image.load('sprites/human/human_idle_left/image_part_002.png'),
    pygame.image.load('sprites/human/human_idle_left/image_part_003.png'),
    pygame.image.load('sprites/human/human_idle_left/image_part_004.png'),
    pygame.image.load('sprites/human/human_idle_left/image_part_005.png'),
    pygame.image.load('sprites/human/human_idle_left/image_part_006.png'),
    pygame.image.load('sprites/human/human_idle_left/image_part_007.png'),
    pygame.image.load('sprites/human/human_idle_left/image_part_008.png'),
]

humanIdleLeft = [pygame.transform.scale_by(frame, 2) for frame in humanIdleLeft]

humanIdleRight = [
    pygame.image.load('sprites/human/human_idle_right/image_part_001.png'),
    pygame.image.load('sprites/human/human_idle_right/image_part_002.png'),
    pygame.image.load('sprites/human/human_idle_right/image_part_003.png'),
    pygame.image.load('sprites/human/human_idle_right/image_part_004.png'),
    pygame.image.load('sprites/human/human_idle_right/image_part_005.png'),
    pygame.image.load('sprites/human/human_idle_right/image_part_006.png'),
    pygame.image.load('sprites/human/human_idle_right/image_part_007.png'),
    pygame.image.load('sprites/human/human_idle_right/image_part_008.png'),
]

humanIdleRight = [pygame.transform.scale_by(frame, 2) for frame in humanIdleRight]

# игрок идет

humanWalkLeft = [
    pygame.image.load('sprites/human/human_walk_left/image_part_001.png'),
    pygame.image.load('sprites/human/human_walk_left/image_part_002.png'),
    pygame.image.load('sprites/human/human_walk_left/image_part_003.png'),
    pygame.image.load('sprites/human/human_walk_left/image_part_004.png'),
    pygame.image.load('sprites/human/human_walk_left/image_part_005.png'),
    pygame.image.load('sprites/human/human_walk_left/image_part_006.png'),
    pygame.image.load('sprites/human/human_walk_left/image_part_007.png'),
    pygame.image.load('sprites/human/human_walk_left/image_part_008.png'),
]

humanWalkLeft = [pygame.transform.scale_by(frame, 2) for frame in humanWalkLeft]

humanWalkRight = [
    pygame.image.load('sprites/human/human_walk_right/image_part_001.png'),
    pygame.image.load('sprites/human/human_walk_right/image_part_002.png'),
    pygame.image.load('sprites/human/human_walk_right/image_part_003.png'),
    pygame.image.load('sprites/human/human_walk_right/image_part_004.png'),
    pygame.image.load('sprites/human/human_walk_right/image_part_005.png'),
    pygame.image.load('sprites/human/human_walk_right/image_part_006.png'),
    pygame.image.load('sprites/human/human_walk_right/image_part_007.png'),
    pygame.image.load('sprites/human/human_walk_right/image_part_008.png'),
]

humanWalkRight = [pygame.transform.scale_by(frame, 2) for frame in humanWalkRight]

# Игрок атакует

humanAttackLeft = [
    pygame.image.load('sprites/human/human_attack_left/image_part_010.png'),
    pygame.image.load('sprites/human/human_attack_left/image_part_009.png'),
    pygame.image.load('sprites/human/human_attack_left/image_part_008.png'),
    pygame.image.load('sprites/human/human_attack_left/image_part_007.png'),
    pygame.image.load('sprites/human/human_attack_left/image_part_006.png'),
    pygame.image.load('sprites/human/human_attack_left/image_part_005.png'),
    pygame.image.load('sprites/human/human_attack_left/image_part_004.png'),
    pygame.image.load('sprites/human/human_attack_left/image_part_003.png'),
    pygame.image.load('sprites/human/human_attack_left/image_part_002.png'),
    pygame.image.load('sprites/human/human_attack_left/image_part_001.png'),
]

humanAttackLeft = [pygame.transform.scale_by(frame, 2) for frame in humanAttackLeft]

humanAttackRight = [
    pygame.image.load('sprites/human/human_attack_right/image_part_001.png'),
    pygame.image.load('sprites/human/human_attack_right/image_part_002.png'),
    pygame.image.load('sprites/human/human_attack_right/image_part_003.png'),
    pygame.image.load('sprites/human/human_attack_right/image_part_004.png'),
    pygame.image.load('sprites/human/human_attack_right/image_part_005.png'),
    pygame.image.load('sprites/human/human_attack_right/image_part_006.png'),
    pygame.image.load('sprites/human/human_attack_right/image_part_007.png'),
    pygame.image.load('sprites/human/human_attack_right/image_part_008.png'),
    pygame.image.load('sprites/human/human_attack_right/image_part_009.png'),
    pygame.image.load('sprites/human/human_attack_right/image_part_010.png'),
]

humanAttackRight = [pygame.transform.scale_by(frame, 2) for frame in humanAttackRight]

# Игрок бежит

humanRunLeft = [
    pygame.image.load('sprites/human/human_run_left/image_part_008.png'),
    pygame.image.load('sprites/human/human_run_left/image_part_007.png'),
    pygame.image.load('sprites/human/human_run_left/image_part_006.png'),
    pygame.image.load('sprites/human/human_run_left/image_part_005.png'),
    pygame.image.load('sprites/human/human_run_left/image_part_004.png'),
    pygame.image.load('sprites/human/human_run_left/image_part_003.png'),
    pygame.image.load('sprites/human/human_run_left/image_part_002.png'),
    pygame.image.load('sprites/human/human_run_left/image_part_001.png'),
]

humanRunLeft = [pygame.transform.scale_by(frame, 2) for frame in humanRunLeft]

humanRunRight = [
    pygame.image.load('sprites/human/human_run_right/image_part_001.png'),
    pygame.image.load('sprites/human/human_run_right/image_part_002.png'),
    pygame.image.load('sprites/human/human_run_right/image_part_003.png'),
    pygame.image.load('sprites/human/human_run_right/image_part_004.png'),
    pygame.image.load('sprites/human/human_run_right/image_part_005.png'),
    pygame.image.load('sprites/human/human_run_right/image_part_006.png'),
    pygame.image.load('sprites/human/human_run_right/image_part_007.png'),
    pygame.image.load('sprites/human/human_run_right/image_part_008.png'),
]

humanRunRight = [pygame.transform.scale_by(frame, 2) for frame in humanRunRight]

# Враг
# Враг стоит


goblinIdleLeft = [
    pygame.image.load('sprites/goblin/goblin_idle_left/image_part_001.png'),
    pygame.image.load('sprites/goblin/goblin_idle_left/image_part_002.png'),
    pygame.image.load('sprites/goblin/goblin_idle_left/image_part_003.png'),
    pygame.image.load('sprites/goblin/goblin_idle_left/image_part_004.png'),
    pygame.image.load('sprites/goblin/goblin_idle_left/image_part_005.png'),
    pygame.image.load('sprites/goblin/goblin_idle_left/image_part_006.png'),
    pygame.image.load('sprites/goblin/goblin_idle_left/image_part_007.png'),
    pygame.image.load('sprites/goblin/goblin_idle_left/image_part_008.png'),
]
goblinIdleLeft = [pygame.transform.scale_by(frame, 2) for frame in goblinIdleLeft]

goblinIdleRight = [
    pygame.image.load('sprites/goblin/goblin_idle_right/image_part_001.png'),
    pygame.image.load('sprites/goblin/goblin_idle_right/image_part_002.png'),
    pygame.image.load('sprites/goblin/goblin_idle_right/image_part_003.png'),
    pygame.image.load('sprites/goblin/goblin_idle_right/image_part_004.png'),
    pygame.image.load('sprites/goblin/goblin_idle_right/image_part_005.png'),
    pygame.image.load('sprites/goblin/goblin_idle_right/image_part_006.png'),
    pygame.image.load('sprites/goblin/goblin_idle_right/image_part_007.png'),
    pygame.image.load('sprites/goblin/goblin_idle_right/image_part_008.png'),
]
goblinIdleRight = [pygame.transform.scale_by(frame, 2) for frame in goblinIdleRight]

# Враг идет
goblinWalkLeft = [
    pygame.image.load('sprites/goblin/goblin_walk_left/image_part_001.png'),
    pygame.image.load('sprites/goblin/goblin_walk_left/image_part_002.png'),
    pygame.image.load('sprites/goblin/goblin_walk_left/image_part_003.png'),
    pygame.image.load('sprites/goblin/goblin_walk_left/image_part_004.png'),
    pygame.image.load('sprites/goblin/goblin_walk_left/image_part_005.png'),
    pygame.image.load('sprites/goblin/goblin_walk_left/image_part_006.png'),
    pygame.image.load('sprites/goblin/goblin_walk_left/image_part_007.png'),
    pygame.image.load('sprites/goblin/goblin_walk_left/image_part_008.png'),
]
goblinWalkLeft = [pygame.transform.scale_by(frame, 2) for frame in goblinWalkLeft]

goblinWalkRight = [
    pygame.image.load('sprites/goblin/goblin_walk_right/image_part_001.png'),
    pygame.image.load('sprites/goblin/goblin_walk_right/image_part_002.png'),
    pygame.image.load('sprites/goblin/goblin_walk_right/image_part_003.png'),
    pygame.image.load('sprites/goblin/goblin_walk_right/image_part_004.png'),
    pygame.image.load('sprites/goblin/goblin_walk_right/image_part_005.png'),
    pygame.image.load('sprites/goblin/goblin_walk_right/image_part_006.png'),
    pygame.image.load('sprites/goblin/goblin_walk_right/image_part_007.png'),
    pygame.image.load('sprites/goblin/goblin_walk_right/image_part_008.png'),
]
goblinWalkRight = [pygame.transform.scale_by(frame, 2) for frame in goblinWalkRight]

