import pygame
from sys import exit
import level
from random import randint, choice

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720), pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.game_active = True
        pygame.display.set_caption("Snowball Fight")
        self.level = level.level()
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.screen.fill('Black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(60)



if __name__ == '__main__':
    game = Game()
    game.run()


#
#
# class Player(pygame.sprite.Sprite)
#     def __init__(self):
#         super().__init__()

