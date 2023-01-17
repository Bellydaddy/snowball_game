import pygame
from settings import *

class UI:
    def __init__(self):
        #general
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        #bar setup
        self.health_bar_rect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.energy_bar_rect = pygame.Rect(10, 34, ENERGY_BAR_WIDTH, BAR_HEIGHT)

        self.weapon_list = ['corgi.png', 'graham.png', 'reuben.png']
        self.weapon_surfs = ['']*len(self.weapon_list)
        self.weapon_rects = ['']*len(self.weapon_list)

    def show_bar(self, current, max_amount, bg_rect, color):
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
        ratio = current/max_amount
        current_width = bg_rect.width*ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)


    def show_weapons(self, weapon_list, selected_weapon):

        x_value = 20
        for i, weapon in enumerate(self.weapon_list):
            self.weapon_surfs[i] = pygame.image.load(weapon)
            self.weapon_rects[i] = self.weapon_surfs[i].get_rect()
            self.weapon_rects[i].topleft = (x_value, HEIGHT-80)
            if weapon==selected_weapon:
                pygame.draw.rect(self.display_surface, 'gold', self.weapon_rects[i].copy(), 3)
            else:
                pygame.draw.rect(self.display_surface, 'black', self.weapon_rects[i].copy(), 3)
            self.display_surface.blit(self.weapon_surfs[i], self.weapon_rects[i])
            x_value += 80

    def drag_shoot(self, player):
        mouse = pygame.mouse.get_pressed()
        shooting_button = pygame.Rect(608, 328, 64, 64)
        if mouse:
            cursor_pos = pygame.mouse.get_pos()
            if mouse[0]:
                if shooting_button.collidepoint(cursor_pos):
                    player.shooting = True
        if player.shooting == True:
            player.shoot(cursor_pos)

    def select_weapon(self, player):
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            cursor_pos = pygame.mouse.get_pos()
            for i, rect in enumerate(self.weapon_rects):
                if rect.collidepoint(cursor_pos):
                    player.selected_weapon = self.weapon_list[i]


    def display(self, player):
        self.show_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOR)
        self.show_bar(player.mana, player.stats['mana'], self.energy_bar_rect, MANA_COLOR)
        self.show_weapons(self.weapon_list, player.selected_weapon)
        self.select_weapon(player)

