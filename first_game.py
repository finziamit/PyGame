import pygame
from sys import exit

screen_height = 400
screen_width = 800
surface_width = 100
surface_height = 200
w = 0
h = 0
w_dir = 1
h_dir = 1
rnd = 0


pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height)) # set screen size
pygame.display.set_caption("first game") # give a title to the screen
clock = pygame.time.Clock() # set a clock

test_surface = pygame.Surface((surface_width,surface_height))
test_surface.fill('Red') #color the surface with red color


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface,(w,h))
    if w+surface_width == 800:
        w_dir = -1
    if w == 0:
        w_dir = 1
    if h+surface_height == 400:
        h_dir = -1
    if h == 0:
        h_dir = 1

    if w_dir == -1 and w == 1:        
        rnd = (rnd+1) % 2
    if rnd % 2 == 1:
        test_surface.fill('Blue')
    else:
        test_surface.fill('Red')
    w += w_dir
    h += h_dir
    pygame.display.update()
    clock.tick(120) # set how much time per sec the loop will run, in this case 60.