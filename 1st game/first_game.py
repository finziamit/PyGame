import pygame
from sys import exit
import os

def display_score():
    current_time = (pygame.time.get_ticks() - start_time) // 1000
    score_surface = test_font.render(f"Score: {current_time}", False, my_game_text_color)
    score_rect = score_surface.get_rect(center = (screen_width//2,50))
    screen.blit(score_surface, score_rect)
    return current_time

screen_height = 400
screen_width = 800
ground_height = 300
snail_x_pos = 800
step_size = 4
start_time = 0

my_game_text_color = (64,64,64)
my_game_text_bg_color = '#c0e8ec'

game_deactivated_screen_color = (94,129,162)
game_deactivated_text_color = (0, 164, 100)

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height)) # set screen size
pygame.display.set_caption("first game") # give a title to the screen
clock = pygame.time.Clock() # set a clock
test_font = pygame.font.Font(None, 50)

sky_surface = pygame.image.load(str(os.getcwd())+'/1st game/graphics/Sky.png').convert()
ground_surface = pygame.image.load(str(os.getcwd())+'/1st game/graphics/ground.png').convert()

snail_surface = pygame.image.load(str(os.getcwd())+'/1st game/graphics/Snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (snail_x_pos, ground_height))

player_surface = pygame.image.load(str(os.getcwd())+'/1st game/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(bottomright = (80,ground_height))

# Grenade logo
grenade_logo_surface = pygame.image.load(str(os.getcwd())+'/1st game/graphics/Grenade/grenade.png').convert_alpha()
grenade_logo_surface = pygame.transform.scale_by(grenade_logo_surface, 0.08)
grenade_logo_rect = grenade_logo_surface.get_rect(topleft=(20,20))

# Grenade
grenade_surface = pygame.image.load(str(os.getcwd())+'/1st game/graphics/Grenade/grenade.png').convert_alpha()
grenade_surface = pygame.transform.scale_by(grenade_surface, 0.1)
grenade_rect = grenade_surface.get_rect(midleft=(-100, -100))

player_gravity = 0
player_walking_mod = 1
top_score = 0
# Intro screen
player_stand = pygame.image.load(str(os.getcwd())+'/1st game/graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (screen_width//2, screen_height//2))
instructions_text_surface = test_font.render("To start a game press space button", False, game_deactivated_text_color)
instructions_text_rect = instructions_text_surface.get_rect(center = (screen_width//2,50))

game_active = False
move_right = False
move_left = False

# Grenade factors
grenade_throw = False
has_grenade = False

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            if  event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
                    player_surface = pygame.image.load(str(os.getcwd())+'/1st game/graphics/Player/player_walk_2.png').convert_alpha()
                    if player_rect.bottom >= 300: player_surface = pygame.image.load(str(os.getcwd())+'/1st game/graphics/Player/player_walk_1.png').convert_alpha()
                
            # move right
                if event.key == pygame.K_RIGHT: move_right = True
            # move left
                if event.key == pygame.K_LEFT: move_left = True

            # stop moving right
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT: move_right = False

            # stop moving left
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT: move_left = False
            
            # grenade throw
            if event.type == pygame.KEYDOWN and has_grenade and not grenade_throw:
                if event.key == pygame.K_f:
                    grenade_bounce_dir = 1
                    grenade_throw = True
                    has_grenade = False

        else:
            if  event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.right = snail_x_pos
                player_rect.left = 0
                has_grenade = False
                start_time = pygame.time.get_ticks()
                
            if  event.type == pygame.KEYUP and event.key == pygame.K_SPACE: top_score = 0

            if  event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface, (0,ground_height))
        screen.blit(grenade_surface, grenade_rect)

        top_score = display_score()
        if top_score != 0 and top_score % 10 == 0 and not has_grenade: has_grenade = True

        # Show if player has a grenade
        if has_grenade:
            screen.blit(grenade_logo_surface, grenade_logo_rect)
        else:
            screen.blit(grenade_logo_surface, (-50, -50))

        snail_rect.x -= step_size
        if snail_rect.right <= 0: snail_rect.left = screen_width
        screen.blit(snail_surface, snail_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300            
        screen.blit(player_surface, player_rect)

        # collisions
        if snail_rect.colliderect(player_rect): game_active = False

        # functionality of movement
        if move_right:
            if player_rect.right <= 800: player_rect.x += step_size
            if player_walking_mod == 1:
                player_surface = pygame.image.load(str(os.getcwd())+'/1st game/graphics/Player/player_walk_2.png').convert_alpha()
                player_walking_mod = 2
            elif player_walking_mod == 2:
                player_surface = pygame.image.load(str(os.getcwd())+'/1st game/graphics/Player/player_walk_1.png').convert_alpha()
                player_walking_mod = 1
        
        if move_left:
            if player_rect.left >= 0: player_rect.x -= step_size
            if player_walking_mod == 1:
                player_surface = pygame.image.load(str(os.getcwd())+'/1st game/graphics/Player/player_walk_2.png').convert_alpha()
                player_walking_mod = 2
            elif player_walking_mod == 2:
                player_surface = pygame.image.load(str(os.getcwd())+'/1st game/graphics/Player/player_walk_1.png').convert_alpha()
                player_walking_mod = 1

        # Functionality of grenade
        if grenade_throw:
            if grenade_rect.x >=800:
                grenade_throw = False
                grenade_rect.x = -100
                grenade_rect.y = -100
            elif grenade_rect.x <=0:
                grenade_rect = grenade_surface.get_rect(center=player_rect.midright)
            grenade_rect.x += 2*step_size
            if grenade_bounce_dir == 1:
                if grenade_rect.bottom >= ground_height-40: grenade_rect.y -= 2
                else: grenade_bounce_dir = 0
            elif grenade_bounce_dir == 0:
                if grenade_rect.bottom <= ground_height: grenade_rect.y += 2
                else: grenade_bounce_dir = 1

            if snail_rect.colliderect(grenade_rect):
                snail_rect.x = snail_rect.x + 800
                grenade_throw = False
                grenade_rect.x = -100
                grenade_rect.y = - 100

            
    else:
        screen.fill(game_deactivated_screen_color)
        screen.blit(player_stand, player_stand_rect)
        screen.blit(instructions_text_surface, instructions_text_rect)
        final_score_surface = test_font.render(f"Your score: {top_score}", False, game_deactivated_text_color)
        final_score_rect = instructions_text_surface.get_rect(center = (screen_width//2,screen_height - 50))
        move_right = False
        move_left = False
        player_walking_mod = 1
        player_surface = pygame.image.load(str(os.getcwd())+'/1st game/graphics/Player/player_walk_1.png').convert_alpha()
        if top_score: screen.blit(final_score_surface, final_score_rect)

    pygame.display.update()
    clock.tick(60) # set how much time per sec the loop will run, in this case 60.