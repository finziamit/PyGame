from pygame import *
import sys
from random import randint

class JuggleGame:
    def __init__(self):
        self.__right_hand_surface = image.load('graphics/hands/right_hand.png').convert_alpha()
        self.__right_hand_rect = self.__right_hand_surface.get_rect(midleft=(300, 500))
        self.__left_hand_surface = image.load('graphics/hands/left_hand.png').convert_alpha()
        self.__left_hand_rect = self.__left_hand_surface.get_rect(midleft=(300, 300))
        self.__blue_ball_surface = image.load('graphics/balls/blue_ball.png').convert_alpha()
        self.__blue_ball_rect = self.__blue_ball_surface.get_rect((-50, -50))
        self.__red_ball_surface = image.load('graphics/balls/red_ball.png').convert_alpha()
        self.__red_ball_rect = self.__red_ball_surface.get_rect((-50, -50))
        self.__yellow_ball_surface = image.load('graphics/balls/yellow_ball.png').convert_alpha()
        self.__yellow_ball_rect = self.__yellow_ball_surface.get_rect((-50, -50))

    def move_blue_ball(self):
        '''Set blue ball movement'''
        direction = randint(0,2) # 0 -> right, 1 -> left
        ball_speed = randint(1, 6) # power of the ball
        ball_gravity = -10 * ball_speed
        for i in range(10 * ball_speed):
            ball_gravity += 1
            self.__blue_ball_rect.y += ball_gravity
            self.__blue_ball_rect.x += direction
    

    def move_red_ball(self):
        '''Set red ball movement'''
        direction = randint(0,2) # 0 -> right, 1 -> left
        ball_speed = randint(1, 6) # power of the ball
        ball_gravity = -10 * ball_speed
        for i in range(10 * ball_speed):
            ball_gravity += 1
            self.__red_ball_rect.y += ball_gravity
            self.__red_ball_rect.x += direction
    

    def move_yellow_ball(self):
        '''Set yellow ball movement'''
        direction = randint(0,2) # 0 -> right, 1 -> left
        ball_speed = randint(1, 6) # power of the ball
        ball_gravity = -10 * ball_speed
        for i in range(10 * ball_speed):
            ball_gravity += 1
            self.__yellow_ball_rect.y += ball_gravity
            self.__yellow_ball_rect.x += direction


    def move_right_hand(self, direction):
        '''Set right hand movement'''
        if direction == 'right' and self.__right_hand_rect.x <= 800:
            self.__right_hand_rect.x += 1
        if direction == 'left' and self.__right_hand_rect.x >= 0:
            self.__right_hand_rect.x -= 1


    def move_left_hand(self, direction):
        '''Set left hand movement'''
        if direction == 'right' and self.__left_hand_rect.x <= 800:
            self.__left_hand_rect.x += 1
        if direction == 'left' and self.__left_hand_rect.x >= 0:
            self.__left_hand_rect.x -= 1


    def game_play():
        '''Update screen by how game is going'''
        screen = display.set_mode((800,400))
        display.set_caption("Juggler")
        clock = time.Clock()
        background_surface = image.load('graphics/background/theater_bg.jpg').convert()
        pass


def main():
    init()
    game = JuggleGame()
    game.game_play()

if __name__ == '__main__':
    main()