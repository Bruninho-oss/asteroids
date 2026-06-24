import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Common import gameLog
from code.Consts import WINDOW_WIDTH, FONT_PATH, YELLOW, MENU_OPTIONS, WHITE


class Menu:
    def __init__(self, window):
        gameLog(0, "Carregando menu...")
        self.window = window
        self.surf = pygame.image.load("./assets/initBG.jpg")
        self.rect = self.surf.get_rect(left=0, top=0)
        gameLog(0, "menu carregado!")

    def run(self, ):
        gameLog(0,"iniciando Música...")
        pygame.mixer_music.load('./assets/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            #desenha o fundo
            self.window.blit(source=self.surf, dest=self.rect)
            #escreve o titulo
            self.menuText(50, "Asteroids", YELLOW, ((WINDOW_WIDTH / 2), 70))
            #atualiza a tela

            for i in range(len(MENU_OPTIONS)):
                self.menuText(20, MENU_OPTIONS[i], WHITE, ((WINDOW_WIDTH / 2), (200 + 30 * i)))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameLog(0, "botão de fechamento da janela clicado")
                    pygame.quit()
                    quit()

        pass

    def menuText(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font(FONT_PATH, text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


