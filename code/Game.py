import pygame
from code.Menu import Menu
from code.Common import gameLog
from code.Consts import WINDOW_HEIGHT, WINDOW_WIDTH

class Game:
    def __init__(self):
        gameLog(0, "Setup Start")
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        gameLog(0, f"Starup End screen size {WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()


