import pygame
from support import import_folder
from settings import *



class Projectile(pygame.sprite.Sprite):
    def __init__(self, player, groups, vector, selected_weapon):
        super().__init__(groups)

        self.image = pygame.image.load(selected_weapon).convert_alpha()
        self.straight_vector = pygame.math.Vector2(1, 0)
        self.image = pygame.transform.rotate(self.image, vector.angle_to(self.straight_vector))
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.centerx = player.rect.centerx
        self.rect.centery += player.rect.centery
        self.display_surface = pygame.display.get_surface()
        self.speed = 7
        self.vector = vector

    def move(self):
        self.rect.centerx += self.speed*self.vector.normalize().x
        self.rect.centery += self.speed*self.vector.normalize().y

    def destroy(self):
        if self.rect.centerx < 0 or self.rect.centerx > 3700 or self.rect.centery<0 or self.rect.centery>3300:
            self.kill()

    def update(self):
        self.move()
        self.destroy()




