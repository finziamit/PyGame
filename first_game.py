import pygame
from sys import exit

def display_score():
    current_time = (pygame.time.get_ticks() - start_time) // 1000
    score_surface = test_font.render(f"Score: {current_time}", False, my_game_text_color)
    score_rect = score_surface.get_rect(center = (screen_width//2,50))
    screen.blit(score_surface, score_rect)

screen_height = 400
screen_width = 800
ground_height = 300
snail_x_pos = 800
snail_step_size = 4
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

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

snail_surface = pygame.image.load('graphics/Snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (snail_x_pos, ground_height))

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(bottomright = (80,ground_height))
player_gravity = 0
player_walking_mod = 1

# Intro screen
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (screen_width//2, screen_height//2))
instructions_text_surface = test_font.render("To start a game press space button", False, game_deactivated_text_color)
instructions_text_rect = instructions_text_surface.get_rect(center = (screen_width//2,50))


game_active = False

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            if  event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
                    player_surface = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
                    if player_rect.bottom >= 300: player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
                
                # move right
                if event.key == pygame.K_RIGHT and player_rect.right <= 800:
                    player_rect.x += 8
                    if player_walking_mod == 1:
                        player_surface = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
                        player_walking_mod = 2
                    elif player_walking_mod == 2:
                        player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
                        player_walking_mod = 1

                # move left
                if event.key == pygame.K_LEFT and player_rect.left >= 0:
                    player_rect.x -= 8
                    if player_walking_mod == 1:
                        player_surface = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
                        player_walking_mod = 2
                    elif player_walking_mod == 2:
                        player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
                        player_walking_mod = 1
        else:
            if  event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.right = snail_x_pos
                player_rect.left = 0
                start_time = pygame.time.get_ticks()

            if  event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface, (0,ground_height))

        display_score()

        snail_rect.x -= snail_step_size
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
    else:
        screen.fill(game_deactivated_screen_color)
        screen.blit(player_stand, player_stand_rect)
        screen.blit(instructions_text_surface, instructions_text_rect)

    pygame.display.update()
    clock.tick(60) # set how much time per sec the loop will run, in this case 60.