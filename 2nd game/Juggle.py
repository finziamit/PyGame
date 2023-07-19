from pygame import *
import sys
from random import choice

class Hand:
    ''' An hand in the game '''
    def __init__(self, path, placement):
        self.__surface = image.load(path).convert_alpha()        
        transform.smoothscale(self.__surface.convert_alpha(), (80,80))
        self.__rect = self.__surface.get_rect(midleft=placement)
    
    @property
    def rect(self):
        return self.__rect
    
    @property
    def surface(self):
        return self.__surface
    
    def move_hand_right(self):
        if self.__rect.right < 800: self.__rect.x += 1
    
    def move_hand_left(self):
        if self.__rect.x > 0: self.__rect.x -= 1


class Ball:
    ''' A ball in the game '''
    def __init__(self, path):
        self.__surface = image.load(path)
        self.__surface = transform.smoothscale(self.__surface.convert_alpha(), (40,40))
        self.__rect = self.__surface.get_rect(midleft=(400,40))
        self.__ball_gravity = 0
        self.__vertical_fall = True
        self.__direction = choice([-1, 1])
        self.__first_touch = True
    
    @property
    def rect(self):
        return self.__rect
    
    @property
    def surface(self):
        return self.__surface
    
    @property
    def vertical_fall(self):
        return self.__vertical_fall

    @property
    def direction(self):
        return self.__direction

    @property
    def first_touch(self):
        return self.__first_touch
    
    @property
    def ball_gravity(self):
        return self.__ball_gravity
    
    @ball_gravity.setter
    def ball_gravity(self, val):
        self.__ball_gravity = val
    
    @vertical_fall.setter
    def vertical_fall(self, val):
        self.__vertical_fall = val

    @direction.setter
    def direction(self, direction):
        self.__direction = direction

    @first_touch.setter
    def first_touch(self, val):
        self.__first_touch = val
    
    def move_ball(self):        
        if self.__first_touch:
            self.__rect.y += 1
            if self.__rect.x >= 800 or self.__rect.x <= 0: self.__direction *= -1
            self.__rect.x += self.__direction
        else:
            ball_speed = choice(range(1,6)) / 10 # power of the ball
            if self.__vertical_fall:                
                # self.__ball_gravity = -30 #* ball_speed
                if self.__rect.top > 900: self.__rect.top = 900
                self.__vertical_fall = False
            else:
                self.__ball_gravity += 1
                self.__rect.y += self.__ball_gravity
                if self.__rect.right >= 800 or self.__rect.left <= 0: self.__direction *= -1
                self.__rect.x += self.__direction * ball_speed


def game_play():
    screen = display.set_mode((800,500))
    display.set_caption("Juggler")
    clock = time.Clock()

    background_surface = image.load('2nd game/graphics/background/theater_bg.png')
    background_surface = transform.smoothscale(background_surface.convert(), (800,550))

    right_hand = Hand('2nd game/graphics/hands/right_hand1.png', (500, 430))    
    left_hand = Hand('2nd game/graphics/hands/left_hand1.png', (250, 430))

    blue_ball = Ball('2nd game/graphics/balls/blue_ball.png')
    red_ball = Ball('2nd game/graphics/balls/red_ball.png')
    yellow_ball = Ball('2nd game/graphics/balls/yellow_ball.png')

    balls = [blue_ball, red_ball, yellow_ball]

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

        # ball movement
        for ball in balls: ball.move_ball()

        # handle hands movement
        if move_right_hand_right: right_hand.move_hand_right()
        if move_right_hand_left: right_hand.move_hand_left()

        if move_left_hand_right: left_hand.move_hand_right()
        if move_left_hand_left: left_hand.move_hand_left()

        # check that hands doesnt change sides
        if left_hand.rect.colliderect(right_hand.rect):
            move_left_hand_right = False
            move_right_hand_left = False

        # check for game-over
        if red_ball.rect.y >= 500: sys.exit()
        if blue_ball.rect.y >= 500: sys.exit()
        if yellow_ball.rect.y >= 500: sys.exit()

        # check if the hand touched the ball
        for ball in balls:
            if left_hand.rect.colliderect(ball.rect) or right_hand.rect.colliderect(ball.rect):
                ball.first_touch = False
                ball.direction = choice([-1.5, -1.25, -1, -0.75, -0.5, -0.25, 0.25, 0.5, 0.75, 1, 1.25, 1.5])
                ball.vertical_fall = True
                ball.ball_gravity = choice([-20, -25, -30, -35])
                ball.move_ball()

        screen.blit(background_surface, (0, 0))
        screen.blit(right_hand.surface, right_hand.rect)
        screen.blit(left_hand.surface, left_hand.rect)
        for ball in balls:
            screen.blit(ball.surface, ball.rect)
        display.update()
        clock.tick(240)
    # end of while loop

def main():
    init()
    game_play()

if __name__ == '__main__':
    main()
