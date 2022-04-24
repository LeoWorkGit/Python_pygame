import pygame
from actor import Actor


class Player(Actor):
    def __init__(self, image_path: str, pos_x: int, pos_y: int):
        super().__init__(
            image_path, pos_x, pos_y
        )

    def move(self, screen):
        self._pos_x += self._x_update
        self.check_borders()
        self.pos_update(screen)

    def process_pressed_key(self, event):
        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self._x_update = -0.3
            if event.key == pygame.K_RIGHT:
                self._x_update = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self._x_update = 0
