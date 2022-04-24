import random
from actor import Actor
from constants import WIDTH


class Enemy(Actor):
    def __init__(self, image_path: str):
        super().__init__(
            image_path
        )
        self._pos_x = random.randint(0, WIDTH-self._image_width)
        self._pos_y = random.randint(50, 150)

    def move(self, screen):
        if self._x_update == 0 or self._pos_x <= 0:
            self._x_update = 0.2
            if self._pos_x <= 0:
                self._pos_y += 40
        elif self._pos_x >= WIDTH - self._image_width:
            self._x_update = -0.2
            self._pos_y += 40

        self._pos_x += self._x_update
        self.check_borders()
        self.pos_update(screen)

    def respawn(self):
        self._pos_x = random.randint(0, WIDTH - self._image_width)
        self._pos_y = random.randint(50, 150)
