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
def start():
    
    platforms.append(Platform(0 , 720, 13))
    for i in range (3):
        platforms.append(Platform(100, 620 - 200 * i, 11))
        platforms.append(Platform(0, 520 - 200 * i, 11))
    for j in range (6):
        ladders.append(Ladder(r.randint(100,500) , platforms[j].rect.y , 5))

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
            ladders.clear()

    screen.fill((80, 155, 250))
    keys = pygame.key.get_pressed()
    player.update(screen, keys , platforms)

    for p in platforms:
        p.update(screen)
    for l in ladders:
        l.update(screen)
    pygame.display.flip()
    clock.tick(50)