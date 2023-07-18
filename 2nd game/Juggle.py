from pygame import *
import sys
from random import choice

class Hand:
    ''' An hand in the game '''
    def __init__(self, path, placement):
        self.__surface = image.load(path).convert_alpha()
        self.__surface = transform.scale_by(self.__surface, 0.2)
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
        self._direction = choice([-1.5, -1, -0.5, 0.5, 1, 1.5])
        self._first_touch = True
    
    @property
    def rect(self):
        return self.__rect
    
    @property
    def surface(self):
        return self.__surface
    
    @property
    def direction(self):
        return self._direction

    @property
    def first_touch(self):
        return self._first_touch

    @direction.setter
    def direction(self):
        self._direction *= -1

    @first_touch.setter
    def first_touch(self, val):
        self._first_touch = val
    
    def move_ball(self):        
        if self._first_touch:
            self.__rect.y += 1
            if self.__rect.x >= 800 or self.__rect.x <= 0: self._direction *= -1
            self.__rect.x += self._direction
        else:
            ball_speed = choice(range(1, 7)) # power of the ball
            ball_gravity = -10 * ball_speed
            for i in range(10 * ball_speed):
                ball_gravity += 1
                self.__rect.y += ball_gravity

                if self.__rect.x >= 800 or self.__rect.x <= 0: self._direction *= -1
                self.__rect.x += self._direction


def game_play():
    screen = display.set_mode((800,500))
    display.set_caption("Juggler")
    clock = time.Clock()

    background_surface = image.load('2nd game/graphics/background/theater_bg.png')
    background_surface = transform.smoothscale(background_surface.convert(), (800,550))

    right_hand = Hand('2nd game/graphics/hands/right_hand.png', (500, 430))    
    left_hand = Hand('2nd game/graphics/hands/left_hand.png', (250, 430))

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
                ball.first_touch(False)
                ball.direction = choice[-1, 1]

        screen.blit(background_surface, (0, 0))
        screen.blit(right_hand.surface, right_hand.rect)
        screen.blit(left_hand.surface, left_hand.rect)
        for ball in balls:
            screen.blit(ball.surface, ball.rect)
        # screen.blit(red_ball.surface ,red_ball.get_rect)
        # screen.blit(blue_ball.surface, blue_ball.get_rect)
        # screen.blit(yellow_ball.surface, yellow_ball.get_rect)
        display.update()
        clock.tick(240)
    # end of while loop

def main():
    init()
    game_play()

if __name__ == '__main__':
    main()
