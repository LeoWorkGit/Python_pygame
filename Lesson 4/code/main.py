import pygame
import sys
from settings import *
from overworld import Overworld
from level import Level
from ui import UI


class Game:
    def __init__(self):
        # game attributes
        self.max_level = 5
        self.max_health = 100
        self.cur_health = 100
        self.coins = 0

        # audio
        self.level_bg_music = pygame.mixer.Sound('../audio/level_music.wav')
        self.overworld_bg_music = pygame.mixer.Sound('../audio/overworld_music.wav')

        # overload creations
        self.overworld = Overworld(0, self.max_level, screen, self.create_level)
        self.status = 'overworld'
        self.overworld_bg_music.play(loops=-1)
        self.overworld_bg_music.set_volume(0.8)

        # UI
        self.ui = UI(screen)

    def create_level(self, current_level):
        self.test_level = Level(current_level, screen, self.create_overworld, self.change_coins, self.change_health)
        self.status = 'level'
        self.overworld_bg_music.stop()
        self.level_bg_music.play(loops=-1)
        self.level_bg_music.set_volume(0.8)

    def create_overworld(self, current_level, new_max_level):
        if new_max_level > self.max_level:
            self.max_level = new_max_level
        self.overworld = Overworld(current_level, self.max_level, screen, self.create_level)
        self.status = 'overworld'
        self.level_bg_music.stop()
        self.overworld_bg_music.play(loops=-1)
        self.overworld_bg_music.set_volume(0.8)

    def change_coins(self, amount):
        self.coins += amount

    def change_health(self, amount):
        self.cur_health += amount

    def check_game_over(self):
        if self.cur_health <= 0:
            self.cur_health = 100
            self.coins = 0
            self.max_level = 0

            self.overworld = Overworld(0, self.max_level, screen, self.create_level)
            self.status = 'overworld'

            self.level_bg_music.stop()
            self.overworld_bg_music.play(loops=-1)
            self.overworld_bg_music.set_volume(0.8)

    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
        else:
            self.test_level.run()
            self.ui.show_health(self.cur_health, self.max_health)
            self.ui.show_coins(self.coins)
            self.check_game_over()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill('grey')
        game.run()

        pygame.display.update()
        clock.tick(60)
