from pygame import *
import sys


def move_ball():
    '''Set ball movement'''
    pass


def update_score():
    ''' Update score for each ball touch'''
    pass


def move_right_hand():
    '''Set right hand movement'''
    pass


def stop_right_hand():
    '''Stop movement of right hand'''
    pass


def move_left_hand():
    '''Set left hand movement'''
    pass


def stop_left_hand():
    '''Stop movement of left hand'''
    pass


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
    # blue_ball = 
    # red_ball = 
    # yellow_ball = 
    pass


def main():
    init()
    game_play()

if __name__ == '__main__':
    main()