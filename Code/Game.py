import pygame
from Code.Const import WIN_WIDTH, WIN_HEIGHT
from Code.Menu import Menu

class Game:

         def __init__(self, window):
            self.window = window
            self.surf = pygame.image.load('./Asset/BG_03.png').convert_alpha()
            self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT + 80))
            self.rect = self.surf.get_rect(left=0, top=0)

         def __init__(self):
            pygame.init()
            self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

         def run(self, ):
             while True:
                menu = Menu(self.window)
                menu.run()

