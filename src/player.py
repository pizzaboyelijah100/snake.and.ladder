import pygame
import level
# Player class
class Player:
    def __init__(self):
        self.image = pygame.image.load('assets/player_A.png')
        self.image2 = pygame.image.load('assets/player_B.png')
        self.image_in_air = pygame.image.load('assets/player_InAir.png')
        self.image_climb = pygame.image.load('assets/player_climb_A.png')
        self.image_climb2 = pygame.image.load('assets/player_climb_B.png')
        self.rect = self.image.get_rect()
        self.move_speed = 3
        self.y_speed_max = 2
        self.y_speed = 0
        self.jump_power = 5
        self.grounded = True
        self.climbing = False
        self.alive = True
        self.lives = 3
        self.has_won = False
        self.gravity = .250
        self.animation_timer_max = 10
        self.animation_timer = self.animation_timer_max
        self.animation_frame = 0
        self.animations = {}
        self.animations["walk"] = (self.image, self.image2)
        self.animations["jump"] = (self.image_in_air, self.image_in_air)
        self.animations["climb"] = [self.image_climb , self.image_climb2]
        self.current_animation  = self.animations['walk']
        self.facing_left = False


    def set_animation (self, name):
        self.current_animation = self.animations[name]

    def update(self, screen, keys , platforms , ladders , snakes ,):



        if not self.alive:

            self.rect.y += self.move_speed
        else:

            if self.climbing:
                if keys[pygame.K_UP]:

                    self.rect.y -= self.move_speed
                if keys[pygame.K_DOWN]:
                    self.rect.y += self.move_speed
            else:
                if keys[pygame.K_LEFT]:
                    self.rect.x -= self.move_speed
                    self.animation_timer -= 1
                    self.facing_left = True
                if keys[pygame.K_RIGHT]:
                    self.rect.x += self.move_speed
                    self.animation_timer -=1
                    self.facing_left = False
                if keys[pygame.K_SPACE] and self.grounded :
                    self.y_speed = -self.jump_power
                    self.grounded = False
                if keys[pygame.K_DOWN] and not self.grounded:
                    self.rect.y += 5

                if self.rect.x < 0 :
                    self.rect.x = 0
                if self.rect.right > screen.get_width():
                    self.rect.right = screen.get_width()
            if not self.grounded and not self.climbing:
                self.set_animation("jump")
                if self.y_speed < self.y_speed_max:
                    self.y_speed += self.gravity
            elif not self.climbing:
                self.set_animation("walk")
                self.y_speed = 0
            hit = self.rect.collidelist(platforms)
            if hit > -1 and not self.climbing:
                if self.rect.bottom < platforms[hit].rect.centery:
                    self.grounded = True
            else:
                self.grounded = False
            for ladder in ladders:
                if self.rect.colliderect(ladder.climb_rect):
                    if (keys[pygame.K_UP] and self.rect.bottom > ladder.climb_rect.bottom
                            or keys[pygame.K_DOWN] and self.rect.top < ladder.climb_rect.top):
                        self.climbing = True
                        self.y_speed = 0
                        self.rect.centerx = ladder.rect.centerx
                        self.set_animation("climb")
                    elif keys[pygame.K_UP] and self.rect.centery < ladder.climb_rect.top or \
                            keys[pygame.K_DOWN] and self.rect.bottom > ladder.climb_rect.bottom:
                            self.climbing = False

            self.rect.move_ip(0, self.y_speed)
        if self.animation_timer <= 0:
            self.animation_timer = self.animation_timer_max

            if self.animation_frame <= 0:
                self.animation_frame += 1

            else:
                self.animation_frame -= 1

        image_to_draw = self.current_animation[self.animation_frame]
        if self.facing_left:
            image_to_draw = pygame.transform.flip(image_to_draw, True , False)

        screen.blit(image_to_draw ,self.rect)

    def reset(self, x, y):
        self.rect.bottomleft = x, y
        self.grounded = True
        self.climbing = False
        self.alive = True
        self.has_won = False
    def bop(self):
        if not self.climbing:
            self.y_speed = -self.jump_power / 2
