import pygame
import sys
from settings import *
from tiles import Tile
from level import Level


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    frame_rate = pygame.time.Clock()
    level = Level(level_map, screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill('black')
        level.run()

        pygame.display.update()
        frame_rate.tick(60)
