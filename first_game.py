import pygame
from sys import exit

screen_height = 400
screen_width = 800
ground_height = 300
snail_x_pos = 600
snail_step_size = 4

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height)) # set screen size
pygame.display.set_caption("first game") # give a title to the screen
clock = pygame.time.Clock() # set a clock
test_font = pygame.font.Font(None, 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My game', False, 'Black')

snail_surface = pygame.image.load('graphics/Snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (snail_x_pos, ground_height))

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(bottomright = (80,ground_height))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos): print('collision')

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface, (0,ground_height))
    screen.blit(text_surface, (300, 50))

    snail_rect.x -= snail_step_size
    if snail_rect.right <= 0: snail_rect.left = screen_width
    screen.blit(snail_surface, snail_rect)

    screen.blit(player_surface, player_rect)
    

    pygame.display.update()
    clock.tick(60) # set how much time per sec the loop will run, in this case 60.