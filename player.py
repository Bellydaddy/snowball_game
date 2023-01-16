import pygame
from support import import_folder
from settings import *
from entity import Entity
class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites, shoot_func):
        super().__init__(groups)
        self.display_surface = pygame.display.get_surface()

        #Projectile variables
        self.shoot_arrow = shoot_func
        self.selected_weapon = "corgi.png"
        self.weapons = {'corgi.png': 50, 'graham.png': 40, 'reuben.png':20}

        #player info
        self.image = pygame.image.load('graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -26)

        self.shooting = False

        #graphics
        self.import_player_assets()
        self.status = 'down'

        #attack
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None
        self.draw = False

        #stats
        self.stats = {'health': 100, 'mana':100, 'attack':10, 'speed':4}
        self.health = self.stats['health']
        self.mana = self.stats['mana']
        self.exp = 123
        self.speed = self.stats['speed']
        self.obstacle_sprites = obstacle_sprites

    def import_player_assets(self):
        character_path = "graphics/player/"
        self.animations = {'up': [],'down': [],'left': [],'right': [],
                           'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
                           'right_attack':[],'left_attack':[],'up_attack':[],'down_attack':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def input(self):
        keys = pygame.key.get_pressed()
        if not self.attacking:
            #movement input
            if keys[pygame.K_w]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pygame.K_s]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0

            if keys[pygame.K_d]:
                self.direction.x = 1
                self.status = 'right'
            elif keys[pygame.K_a]:
                self.direction.x = -1
                self.status = 'left'
            else:
                self.direction.x = 0

            #attack input
            if keys[pygame.K_SPACE]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()

            #magic input
            if keys[pygame.K_LCTRL]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False

    def get_full_weapon_damage(self, attack_type):
        if attack_type in self.weapons:
            return self.weapons[attack_type]
        else:
            return 0

    def get_status(self):
        #idle
        if self.direction.x ==0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'
        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle in self.status':
                    self.status = self.status.replace('_idle', '_attack')
                else:
                    self.status = self.status + "_attack"
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack', '')

    def shoot(self, cursor):
        self.shooting = True
        pygame.draw.line(pygame.display.get_surface(), 'black', (640, 360), cursor, width=2)
        if not pygame.mouse.get_pressed()[0]:
            vector = pygame.math.Vector2((cursor[0]-640)*-1,(cursor[1]-360)*-1)
            self.shoot_arrow(vector, self.selected_weapon)
            self.shooting = False

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)

    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)




