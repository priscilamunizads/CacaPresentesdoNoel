import sys

import pygame
from Code.Const import WIN_WIDTH, WIN_HEIGHT, MENU
from Code.Level import Level
from Code.Menu import Menu

class Game:

         def __init__(self, window):
            self.window = window
            self.surf = pygame.image.load('./Asset/Level1Bg1.png').convert_alpha()
            self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT + 80))
            self.rect = self.surf.get_rect(left=0, top=0)

         def __init__(self):
            pygame.init()
            self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

         def run(self):
             while True:
                menu = Menu(self.window)
                menu_return = menu.run()

                if menu_return in [MENU[0], MENU[1], MENU[2]]:
                    level = Level(self.window, 'Level1Bg1', menu_return)
                    level_return = level.run()
                elif menu_return == MENU[4]:
                    pygame.quit() # Close window
                    quit() # end pygame
                else:
                    pass


