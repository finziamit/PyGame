from pygame import *
import sys
from random import randint

def move_ball(ball_rect):
    '''Set ball movement'''
    direction = randint(0,2) # 0 -> right, 1 -> left
    ball_speed = randint(1, 6) # power of the ball
    ball_gravity = -10 * ball_speed
    for i in range(10 * ball_speed):
        ball_gravity += 1
        ball_rect.y += ball_gravity
        ball_rect.x += direction


def move_right_hand(right_hand_rect, direction):
    '''Set right hand movement'''
    if direction == 'right' and right_hand_rect.x <= 800:
        right_hand_rect.x += 1
    if direction == 'left' and right_hand_rect.x >= 0:
        right_hand_rect.x -= 1


def move_left_hand(left_hand_rect, direction):
    '''Set left hand movement'''
    if direction == 'right' and left_hand_rect.x <= 800:
        left_hand_rect.x += 1
    if direction == 'left' and left_hand_rect.x >= 0:
        left_hand_rect.x -= 1


def game_play():
    '''Update screen by how game is going'''
    screen = display.set_mode((800,400))
    display.set_caption("Juggler")
    clock = time.Clock()
    background_surface = image.load('graphics/theater_bg.jpg').convert()

    # TODO: draw hands images and delete their background
    right_hand_surface = image.load('graphics/right_hand.png').convert_alpha()
    right_hand_rect = right_hand_surface.get_rect(midleft=(300, 500))
    left_hand_surface = image.load('graphics/left_hand.png').convert_alpha()
    left_hand_rect = left_hand_surface.get_rect(midleft=(300, 300))
    blue_ball_surface = image.load('graphics/blue_ball.png').convert_alpha()
    blue_ball_rect = blue_ball_surface.get_rect((-50, -50))
    red_ball_surface = image.load('graphics/red_ball.png').convert_alpha()
    red_ball_surface = red_ball_surface.get_rect((-50, -50))
    yellow_ball_surface = image.load('graphics/yellow_ball.png').convert_alpha()
    yellow_ball_rect = yellow_ball_surface.get_rect((-50, -50))
    pass


def main():
    init()
    game_play()

if __name__ == '__main__':
    main()