import pygame
from pygame import mixer
from player import Player
from enemy import Enemy
from bullet import Bullet
from constants import WIDTH, HEIGHT


def start_game_window():
    # Initialize the pygame
    pygame.init()

    create_screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Width, Height

    # Add background
    create_background = pygame.image.load("background.jpg")

    # Title and Icon
    pygame.display.set_caption("Ubivec cudzincov")
    icon = pygame.image.load("space-ship.png")  # 32 px
    pygame.display.set_icon(icon)

    return create_screen, create_background


def show_score(screen_obj, score_val, font_obj, x, y):
    score = font_obj.render("Score: " + str(score_val), True, (255, 255, 255))
    screen_obj.blit(score, (x, y))


def game_over(screen_obj, enemies_list, font_obj, game_end):
    if len(enemies_list) == 0 and game_end is False:
        score = font_obj.render("YOU WIN", True, (255, 255, 255))
        text_rect = score.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen_obj.blit(score, text_rect)
        return [], game_end
    for i in range(len(enemies_list)):
        if enemies_list[i].get_pos()[1] > 480:
            enemies_list.clear()
            game_end = True
            break
    if game_end:
        score = font_obj.render("GAME OVER", True, (255, 255, 255))
        text_rect = score.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen_obj.blit(score, text_rect)
        return [], game_end

    return enemies_list, game_end


if __name__ == "__main__":
    screen, background = start_game_window()

    # Add player ship
    player = Player("arcade-game.png", 370, 520)
    # enemy have random pos
    enemy_num = 6
    enemies = []
    for _ in range(enemy_num):
        enemies.append(Enemy("alien.png"))
    # Add a bullet
    bullet_1 = Bullet("bullet.png")

    # Background music
    mixer.music.load("background.wav")
    mixer.music.play(-1)
    mixer.music.set_volume(0.3)

    # Score
    game_score = 0
    score_font = pygame.font.Font('freesansbold.ttf', 32)
    text_X = 10
    text_Y = 10

    # Game over
    is_game_end = False
    game_over_font = pygame.font.Font('freesansbold.ttf', 64)

    # Game Loop
    running = True
    while running:

        screen.fill((255, 0, 255))  # RGB
        # Draw background
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if bullet_1.can_fire:
                        bullet_1.change_bullet_state()
                        bullet_1.fire_bullet(player.get_pos())

            player.process_pressed_key(event)

        # Collision
        for enemy in enemies:
            if bullet_1.is_hit(enemy.get_pos()):
                bullet_1.is_collided = True
                enemies.remove(enemy)
                game_score += 1

        bullet_1.move(screen)
        player.move(screen)
        [enemy.move(screen) for enemy in enemies]
        show_score(screen, game_score, score_font, text_X, text_Y)
        enemies, is_game_end = game_over(screen, enemies, game_over_font, is_game_end)
        pygame.display.update()
