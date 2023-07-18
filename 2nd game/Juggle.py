from pygame import *
import sys
from random import randint

class Hand:
    ''' An hand in the game '''
    def __init__(self, path, placement):
        self.__surface = image.load(path).convert_alpha()
        self.__surface = transform.scale_by(self.__surface, 0.2)
        self.__rect = self.__surface.get_rect(midleft=placement)
    
    @property
    def get_rect(self):
        return self.__rect
    
    @property
    def get_surface(self):
        return self.__surface
    
    def move_hand_right(self):
        if self.__rect.x < 700: self.__rect.x += 1
    
    def move_hand_left(self):
        if self.__rect.x > 0: self.__rect.x -= 1


class Ball:
    ''' A ball in the game '''
    def __init__(self, path):
        self.__surface = image.load(path).convert_alpha()
        self.__rect = self.__surface.get_rect(midleft=(20,300))
    
    @property
    def get_rect(self):
        return self.__rect
    
    @property
    def get_surface(self):
        return self.__surface
    
    def move_ball(self):
        direction = randint(0,2) # 0 -> right, 1 -> left
        ball_speed = randint(1, 6) # power of the ball
        ball_gravity = -10 * ball_speed
        for i in range(10 * ball_speed):
            ball_gravity += 1
            self.__rect.y += ball_gravity
            
            if self.__rect.x < 800 or self.__rect.x > 0:
                self.__rect.x += direction
            else:
                self.__rect.x -= direction


def game_play():
    screen = display.set_mode((800,500))
    display.set_caption("Juggler")
    clock = time.Clock()

    background_surface = image.load('2nd game/graphics/background/theater_bg.png').convert()
    background_surface = transform.scale_by(background_surface,0.7)

    right_hand = Hand('2nd game/graphics/hands/right_hand.png', (500, 450))    
    left_hand = Hand('2nd game/graphics/hands/left_hand.png', (250, 450))

    blue_ball = Ball('2nd game/graphics/balls/blue_ball.png')
    red_ball = Ball('2nd game/graphics/balls/red_ball.png')
    yellow_ball = Ball('2nd game/graphics/balls/yellow_ball.png')

    move_right_hand_right = False
    move_right_hand_left = False
    move_left_hand_right = False
    move_left_hand_left = False
    while 1:        
        for action in event.get():
                if action.type == QUIT:
                    quit()
                    sys.exit()
            
                if action.type == KEYDOWN:
                    # move right hand right using the right arrow key
                    if action.key == K_RIGHT: move_right_hand_right = True

                    # move right hand left using the left arrow key
                    if action.key == K_LEFT: move_right_hand_left = True

                    # move left hand right using the 'D' key
                    if action.key == K_d: move_left_hand_right = True

                    # move left hand left using the 'A' key
                    if action.key == K_a: move_left_hand_left = True

                if action.type == KEYUP:
                    # move right hand right using the right arrow key
                    if action.key == K_RIGHT: move_right_hand_right = False

                    # move right hand left using the left arrow key
                    if action.key == K_LEFT: move_right_hand_left = False

                    # move left hand right using the 'D' key
                    if action.key == K_d: move_left_hand_right = False

                    # move left hand left using the 'A' key
                    if action.key == K_a: move_left_hand_left = False
        
        # end of the event handler

        if move_right_hand_right: right_hand.move_hand_right()
        if move_right_hand_left: right_hand.move_hand_left()

        if move_left_hand_right: left_hand.move_hand_right()
        if move_left_hand_left: left_hand.move_hand_left()

        # check that hands doesnt change sides
        if left_hand.get_rect.colliderect(right_hand.get_rect):
            move_left_hand_right = False
            move_right_hand_left = False
        
        # check that a ball didn't fall
        if red_ball.get_rect.y >= 500: sys.exit()
        if blue_ball.get_rect.y >= 500: sys.exit()
        if yellow_ball.get_rect.y >= 500: sys.exit()

        screen.blit(background_surface, (0, 0))
        screen.blit(right_hand.get_surface, right_hand.get_rect)
        screen.blit(left_hand.get_surface, left_hand.get_rect)
        display.update()
    # end of while loop

def main():
    init()
    game_play()

if __name__ == '__main__':
    main()
