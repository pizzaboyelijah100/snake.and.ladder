import pygame
import random as r
class Ladder:
    def __init__(self,x,y,height):
        self.height = height
        self.image = pygame.image.load("assets/ladder.png")
        self.rect = self.image.get_rect(height = 25 * height, bottomleft = (x,y))
    def update (self , screen):
        for i in range(self.height):
            screen.blit(self.image , (self.rect.x,self.rect.y + 25 * i))


class Platform:
    def __init__(self , x,y , length):
        self.rect = pygame.Rect(x,y , length * 50 , 30 )
    def update(self , screen):
        pygame.draw.rect(screen, (150, 75, 0) , self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect , 2)
