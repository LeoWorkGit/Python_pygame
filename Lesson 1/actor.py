import pygame
from constants import WIDTH
from abc import ABC, abstractmethod


class Actor(ABC):
    def __init__(self, image_path: str, pos_x=0, pos_y=0):
        self.__image_path = image_path
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._x_update = 0
        self._y_update = 0
        self._player_update = pygame.image.load(self.__image_path)
        self._image_width = self._player_update.get_width()
        self._image_height = self._player_update.get_height()

    def pos_update(self, object_screen):
        # blit = draw
        object_screen.blit(self._player_update, (self._pos_x, self._pos_y))

    def get_pos(self):
        return self._pos_x, self._pos_y

    def check_borders(self):
        if self._pos_x <= 0:
            self._pos_x = 0
        elif self._pos_x >= WIDTH - self._image_width:
            self._pos_x = WIDTH - self._image_width

    @abstractmethod
    def move(self, screen):
        """Move method"""
