import pygame
import random as r



class Ladder:
    def __init__(self,x,y,height):
        self.height = height
        self.image = pygame.image.load("assets/ladder.png")
        self.rect = self.image.get_rect(height = 25 * height, bottomleft = (x,y))
        self.climb_rect = self.rect.inflate(-20 , -10)

    def update (self , screen):

        for i in range(self.height):
            screen.blit(self.image , (self.rect.x,self.rect.y + 25 * i))

class Platform:
    def __init__(self , x,y , length):
        self.rect = pygame.Rect(x,y , length * 50 , 30 )
    def update(self , screen):
        pygame.draw.rect(screen, (150, 75, 0) , self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect , 2)
class Snake:
    def __init__(self,x,y,direction ):
        self.image = pygame.image.load("assets/snake_A.png")
        self.image2 = pygame.image.load("assets/snake_B.png")
        self.images = [self.image , self.image2]
        self.rect = self.image.get_rect(bottomleft = (x , y))
        self.grounded =True
        self.direction = direction
        self.speed = 2
        self.alive = True
        self.animation_timer_max = 10
        self.animation_timer = self.animation_timer_max
        self.animation_frame = 0
        if self.direction == -1:
            self.images[0]=pygame.transform.flip(self.images[0],True , False )
            self.images[1]=pygame.transform.flip(self.images[1],True , False )
    def update(self, screen, platforms):
        if not self.alive:
            self.rect.move_ip(0, self.speed)
        else:
            # Check platform collision
            hit = self.rect.collidelist(platforms)
            if hit > -1:
                if not self.grounded:
                    self.direction *= -1
                    self.images[0] = pygame.transform.flip(self.images[0], True, False)
                    self.images[1] = pygame.transform.flip(self.images[1], True, False)
                self.grounded = True
            else:
                self.grounded = False

            if not self.grounded:
                self.rect.move_ip(0, self.speed)
            else:
                self.rect.move_ip(self.speed * self.direction, 0)

            self.animation_timer -= 1
            if self.animation_timer <= 0:
                self.animation_timer = self.animation_timer_max
                self.animation_frame += 1
                if self.animation_frame >= len(self.images):
                    self.animation_frame = 0

        screen.blit(self.images[self.animation_frame], self.rect)