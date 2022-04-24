import pygame
import sys
from level import Level
from settings import *
from debug import debug


class Game:
    def __init__(self):
        # Start pygame
        pygame.init()

        # Basic screen setup
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        ico = pygame.image.load('../graphics/screen/screen_ico.png').convert_alpha()
        pygame.display.set_icon(ico)
        pygame.display.set_caption('Dark Zenda')
        self.framerate = pygame.time.Clock()

        # Initialize a level
        self.level = Level()

        # sound
        main_sound = pygame.mixer.Sound('../audio/main.ogg')
        main_sound.set_volume(0.6)
        main_sound.play(loops=-1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()
            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.framerate.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
