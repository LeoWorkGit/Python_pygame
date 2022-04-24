import pygame
import sys
from debug import debug

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    cat_surf = pygame.image.load('cat.png').convert_alpha()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill('white')
        screen.blit(cat_surf, (50, 50))
        debug(pygame.mouse.get_pos())
        debug(pygame.mouse.get_pressed(), 40)
        debug('mouse!', pygame.mouse.get_pos()[1]-15, pygame.mouse.get_pos()[0])
        pygame.display.update()
        clock.tick(60)
