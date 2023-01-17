import pygame
from support import import_folder
from settings import *



class Projectile(pygame.sprite.Sprite):
    def __init__(self, player, groups, vector, selected_weapon, sprite_type):
        super().__init__(groups)
        self.straight_vector = pygame.math.Vector2(1, 0)
        self.image = pygame.transform.scale(pygame.image.load(selected_weapon).convert_alpha(), (48, 48))
        self.image = pygame.transform.rotate(self.image, vector.angle_to(self.straight_vector))
        self.rect = self.image.get_rect()
        # self.hitbox = self.rect.inflate(0, -10)
        self.rect.center = (player.rect.centerx, player.rect.centery)
        self.display_surface = pygame.display.get_surface()
        self.vector = vector
        self.speed = 15*(self.vector.magnitude()/700.0)
        self.damage = 50
        self.sprite_type = sprite_type
        self.selectedweapon = selected_weapon

    def move(self):
        self.rect.centerx += self.speed*self.vector.normalize().x
        self.rect.centery += self.speed*self.vector.normalize().y

    def destroy(self):
        if self.rect.centerx < 0 or self.rect.centerx > 3700 or self.rect.centery<0 or self.rect.centery>3300:
            self.kill()

    def update(self):
        self.move()
        self.destroy()




