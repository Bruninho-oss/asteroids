import pygame
from code.Menu import Menu
from code.Common import gameLog

class Game:
    def __init__(self):
        gameLog(0, "Setup Start")
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))
        gameLog(0, "Starup End screen size 600x400")

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
#            for event in pygame.event.get():
#               if event.type == pygame.QUIT:
#                   gameLog(0, "botão de fechamento da janela clicado")
#                   pygame.quit()
#                   quit()

