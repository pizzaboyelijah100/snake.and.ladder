import pygame
import random as r
from level import *
from player import *
pygame.init()
game_width = 650
game_height = 750
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True
platforms = []
ladders = []
player = Player()
snakes = []
snaketimermax = 100
snaketimer = snaketimermax
maxsnakes = 8
spawnchance = 40
def spawn_snakes():
    for i in range(1, 6):
        # controlls the spawn chance
        if r.randint(1, 100) <= spawnchance:
            if len(snakes) < maxsnakes:
                # if i is a even number
                if i % 2 == 0:
                    snakes.append(Snake(0, platforms[i].rect.y +1, 1))
                else:                   # flips direction with the -1
                    snakes.append(Snake(600, platforms[i].rect.y +1,  -1))

def start():
    ladders.clear()
    snakes.clear()
    platforms.clear()
    platforms.append(Platform(0 , 720, 13))
    for i in range (3):
        platforms.append(Platform(100, 620 - 200 * i, 11))
        platforms.append(Platform(0, 520 - 200 * i, 11))
    for j in range (6):
        l= Ladder(r.randint(100,500) , platforms[j].rect.y , 5)
        while l.rect.collidelist(ladders) >-1:
            l = Ladder(r.randint(100, 500), platforms[j].rect.y, 5)
        ladders.append(l)
    player.reset(0, 720 )

# Main Loop
start()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:

            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            # Reset the level
            start()
    screen.fill((80, 155, 250))
    keys = pygame.key.get_pressed()
    snaketimer -= 1
    if snaketimer <= 0:
        snaketimer = snaketimermax
        spawn_snakes()

    for p in platforms:
        p.update(screen)
    for l in ladders:
        l.update(screen)
    for s in snakes:
        s.update(screen , platforms)
    for s in snakes:
        if s.rect.y >= game_height:
            snakes.remove(s)


    player.update(screen, keys, platforms , ladders , snakes)

    pygame.display.flip()
    clock.tick(50)
