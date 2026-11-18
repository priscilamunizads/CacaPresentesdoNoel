import pygame
from pygame import Surface, Rect
from pygame.font import Font
from Code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_RED, COLOR_WHITE, MENU


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./Asset/BG_03.png').convert()
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT + 90))
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./Asset/Jigle Bell.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Caça Presentes", COLOR_RED, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "do Papai Noel", COLOR_RED, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU)):
                self.menu_text(20,MENU[i], COLOR_WHITE, ((WIN_WIDTH / 2), 270 + 25 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            clock.tick(60)

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)