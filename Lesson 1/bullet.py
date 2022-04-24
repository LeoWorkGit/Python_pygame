from actor import Actor
from pygame import mixer
import math


class Bullet(Actor):
    def __init__(self, image_path: str):
        super().__init__(
            image_path
        )
        self.can_fire = True
        self.is_collided = False

    def change_bullet_state(self):
        if self.can_fire:
            self.can_fire = False

    def fire_bullet(self, ship_pos):
        if not self.can_fire:
            bullet_sound = mixer.Sound("laser.wav")
            bullet_sound.play()
            bullet_sound.set_volume(0.5)
            self._y_update = 0.3
            self._pos_x = ship_pos[0] + 20
            self._pos_y = ship_pos[1] - 10

    def is_hit(self, enemy_pos):
        distance = math.sqrt(math.pow(int(enemy_pos[0]) + 20 - int(self._pos_x), 2) +
                             math.pow(int(enemy_pos[1]) - int(self._pos_y), 2))
        if distance < 33:
            collision_sound = mixer.Sound("explosion.wav")
            collision_sound.play()
            collision_sound.set_volume(0.7)
            return True
        return False

    def bullet_reset(self):
        self._pos_x = 0
        self._pos_y = 0
        self._y_update = 0
        self.can_fire = True
        self.is_collided = False

    def move(self, screen):
        if not self.can_fire:
            self._pos_y -= self._y_update
            self.pos_update(screen)
        if self._pos_y <= 0 or self.is_collided:
            self.bullet_reset()
