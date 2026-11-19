import pygame
from pygame import Surface, Rect
from pygame.font import Font
from Code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_RED, COLOR_WHITE, MENU
from Code.Entity import Entity
from Code.EntityFactory import EntityFactory


class Menu:

    def __init__(self, window):
        self.window = window
        self.entity_list: list[Entity] = []
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg1'))

    def run(self):
        pygame.mixer_music.load('./Asset/Jigle Bell.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        menu = 0

        while True:

            # Imagens

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

                self.menu_text(50, "Caça Presentes", COLOR_RED, ((WIN_WIDTH / 2), 70))
                self.menu_text(50, "do Papai Noel", COLOR_RED, ((WIN_WIDTH / 2), 120))


            for i in range(len(MENU)):
                if i == menu:
                    self.menu_text(18, MENU[i], COLOR_RED, ((WIN_WIDTH / 2), 250 + 25 * i))
                else:
                    self.menu_text(18,MENU[i], COLOR_WHITE, ((WIN_WIDTH / 2), 250 + 25 * i))
            pygame.display.flip()

            # Todos os eventos

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu < len(MENU) - 1:
                            menu += 1
                        else:
                            menu = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu > 0:
                            menu -= 1
                        else:
                            menu = len(MENU) - 1
                    if event.key == pygame.K_RETURN: # ENTER
                        return MENU[menu]

            clock.tick(60)


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)