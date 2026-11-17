import pygame

from Code.Menu import Menu

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self, ):

        while True:
            Menu = Menu(self.window)
            Menu.run()
            pass
            # Check for all events
            # for event in pygame.event.get():
            #   if event.type == pygame.QUIT:
            #       pygame.QUIT  # Close Window
            #       quit()  # end pygame