import pygame
import constants
from sys import exit
from random import choice
from player import Player
from obstacle import Obstacle


def display_score():
    current_time = int((pygame.time.get_ticks() - start_time) / 1000)
    score_surf = main_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time


def intro_score(score):
    intro_text_3_surf = main_font.render(f"Your score is {score}", False, (111, 196, 169))
    intro_text_3_rect = intro_text_3_surf.get_rect(center=(400, 350))
    return intro_text_3_surf, intro_text_3_rect


# def obstacle_movement(obstacle_list):
#     if obstacle_list:
#         for obstacle in obstacle_list:
#             obstacle.x -= 5
#             if obstacle.bottom == 300:
#                 screen.blit(snail_surf, obstacle)
#             else:
#                 screen.blit(fly_surf, obstacle)
#         obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
#
#         return obstacle_list
#     else:
#         return []


# def collisions(player, obstacles):
#     if obstacles:
#         for obstacle in obstacles:
#             if player.colliderect(obstacle):
#                 return False
#     return True


# def player_animation():
#     global player_surf, player_index
#     if player_rect.bottom < 300:
#         # jump
#         player_surf = player_jump
#     else:
#         player_index += 0.1
#         if player_index >= len(player_walk):
#             player_index = 0
#         player_surf = player_walk[int(player_index)]


def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
    pygame.display.set_caption("Dino")
    # pygame.display.set_icon()
    clock = pygame.time.Clock()
    main_font = pygame.font.Font('font/Pixeltype.ttf', 50)
    game_active = False
    start_time = 0
    score = 0
    bg_music = pygame.mixer.Sound('audio/music.wav')
    bg_music.set_volume(0.8)
    bg_music.play(loops=-1)

    # Groups
    # Player
    player = pygame.sprite.GroupSingle()
    player.add(Player())

    # Obstacle Group
    obstacle_group = pygame.sprite.Group()

    # Text, AntiAliasing (True, False) (smoothing), Color
    # score_surf = score_font.render('My game', False, (64, 64, 64))
    # score_rect = score_surf.get_rect(center=(400, 50))

    # convert - convert images to pygame format for better performance
    # convert_alpha - convert with respect to alpha channels
    sky_surf = pygame.image.load('graphics/Sky.png').convert()
    ground_surf = pygame.image.load('graphics/ground.png').convert()

    # Enemies
    # Snail
    # snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
    # snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
    # snail_frames = [snail_frame_1, snail_frame_2]
    # snail_frame_index = 0
    # snail_surf = snail_frames[snail_frame_index]
    # snail_rect = snail_surf.get_rect(midbottom=(800, 300))

    # Fly
    # fly_frame_1 = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
    # fly_frame_2 = pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
    # fly_frames = [fly_frame_1, fly_frame_2]
    # fly_frame_index = 0
    # fly_surf = fly_frames[fly_frame_index]
    # fly_rect = fly_surf.get_rect(midbottom=(800, 150))

    # obstacle_rect_list = []

    # player_walk_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
    # player_walk_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
    # player_walk = [player_walk_1, player_walk_2]
    # player_index = 0
    # player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()
    # player_surf = player_walk[player_index]
    # player_rect = player_surf.get_rect(midbottom=(80, 300))
    # player_gravity = 0
    # Intro screen
    player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
    player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
    player_stand_rect = player_stand.get_rect(center=(400, 200))
    # Intro screen text

    intro_text_1_surf = main_font.render("Welcome to the game Stolen Dinosaur", False, (111, 196, 169))
    intro_text_1_rect = intro_text_1_surf.get_rect(center=(400, 50))
    intro_text_2_surf = main_font.render("Press SPACE to start", False, (111, 196, 169))
    intro_text_2_rect = intro_text_2_surf.get_rect(center=(400, 350))

    # Timer
    obstacle_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(obstacle_timer, 1600)

    while True:
        # Get all events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # Close program with
                exit()
            if not game_active and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()
            if game_active:
                if event.type == obstacle_timer:
                    obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))

        if game_active:
            screen.blit(sky_surf, (0, 0))
            screen.blit(ground_surf, (0, 300))
            score = display_score()

            # Player
            player.draw(screen)
            player.update()

            # Obstacle
            obstacle_group.draw(screen)
            obstacle_group.update()

            # Collision with enemy
            game_active = collision_sprite()
        else:
            screen.fill((94, 129, 162))
            screen.blit(player_stand, player_stand_rect)
            screen.blit(intro_text_1_surf, intro_text_1_rect)
            if score == 0:
                screen.blit(intro_text_2_surf, intro_text_2_rect)
            else:
                surf, rect = intro_score(score)
                screen.blit(surf, rect)

        # Draw all our elements
        # Update everything
        pygame.display.update()
        # Lock on 60 frame per second (max framerate)
        clock.tick(60)
