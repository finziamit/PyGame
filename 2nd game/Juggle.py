from pygame import *
import sys
from random import randint

class Hand:
    ''' An hand in the game '''
    def __init__(self, path, placement):
        self.__surface = image.load(path).convert_alpha()
        self.__rect = self.__surface.get_rect(midleft=placement)
    
    @property
    def get_rect(self):
        return self.__rect
    
    @property
    def get_surface(self):
        return self.__surface
    
    def move_hand_right(self):
        if self.__rect.x <800: self.__rect.x += 1
    
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
    screen = display.set_mode((800,600))
    display.set_caption("Juggler")
    clock = time.Clock()

    background_surface = image.load('2nd game/graphics/background/theater_bg.jpg').convert()

    right_hand = Hand('2nd game/graphics/hands/right_hand.png', (300, 500))
    left_hand = Hand('2nd game/graphics/hands/left_hand.png', (300, 300))

    blue_ball = Ball('2nd game/graphics/balls/blue_ball.png')
    red_ball = Ball('2nd game/graphics/balls/red_ball.png')
    yellow_ball = Ball('2nd game/graphics/balls/yellow_ball.png')

    while 1:
        for action in event.get():
                if action.type == QUIT:
                    quit()
                    sys.exit()
            
                if action.type == KEYDOWN:
                    # move right hand right using the right arrow key
                    if action.key == K_RIGHT: right_hand.move_hand_right()

                    # move right hand left using the left arrow key
                    if action.key == K_LEFT: right_hand.move_hand_left()

                    # move left hand right using the 'D' key
                    if action.key == K_d: left_hand.move_hand_right()

                    # move left hand left using the 'A' key
                    if action.key == K_a: left_hand.move_hand_left()
        
        # end of the event handler
        screen.blit(background_surface, (0, 0))
        screen.blit(right_hand.get_surface, right_hand.get_rect)
        screen.blit(left_hand.get_surface, left_hand.get_rect)

def main():
    init()
    game_play()

if __name__ == '__main__':
    main()


# class JuggleGame:
#     def __init__(self):
#         self.__screen = display.set_mode((800,600))
#         display.set_caption("Juggler")
#         self.__clock = time.Clock()
#         self.__background_surface = image.load('graphics/background/theater_bg.jpg').convert()
#         self.__right_hand_surface = image.load('graphics/hands/right_hand.png').convert_alpha()
#         self.__right_hand_rect = self.__right_hand_surface.get_rect(midleft=(300, 500))
#         self.__left_hand_surface = image.load('graphics/hands/left_hand.png').convert_alpha()
#         self.__left_hand_rect = self.__left_hand_surface.get_rect(midleft=(300, 300))
#         self.__blue_ball_surface = image.load('graphics/balls/blue_ball.png').convert_alpha()
#         self.__blue_ball_rect = self.__blue_ball_surface.get_rect(midleft=(-50, -50))
#         self.__red_ball_surface = image.load('graphics/balls/red_ball.png').convert_alpha()
#         self.__red_ball_rect = self.__red_ball_surface.get_rect(midleft=(-50, -50))
#         self.__yellow_ball_surface = image.load('graphics/balls/yellow_ball.png').convert_alpha()
#         self.__yellow_ball_rect = self.__yellow_ball_surface.get_rect(midleft=(-50, -50))


#     def __move_blue_ball(self):
#         '''Set blue ball movement'''
#         direction = randint(0,2) # 0 -> right, 1 -> left
#         ball_speed = randint(1, 6) # power of the ball
#         ball_gravity = -10 * ball_speed
#         for i in range(10 * ball_speed):
#             ball_gravity += 1
#             self.__blue_ball_rect.y += ball_gravity
#             self.__blue_ball_rect.x += direction
    

#     def __move_red_ball(self):
#         '''Set red ball movement'''
#         direction = randint(0,2) # 0 -> right, 1 -> left
#         ball_speed = randint(1, 6) # power of the ball
#         ball_gravity = -10 * ball_speed
#         for i in range(10 * ball_speed):
#             ball_gravity += 1
#             self.__red_ball_rect.y += ball_gravity
#             self.__red_ball_rect.x += direction
    

#     def __move_yellow_ball(self):
#         '''Set yellow ball movement'''
#         direction = randint(0,2) # 0 -> right, 1 -> left
#         ball_speed = randint(1, 6) # power of the ball
#         ball_gravity = -10 * ball_speed
#         for i in range(10 * ball_speed):
#             ball_gravity += 1
#             self.__yellow_ball_rect.y += ball_gravity
#             self.__yellow_ball_rect.x += direction


#     def __move_right_hand(self, direction):
#         '''Set right hand movement'''
#         if direction == 'right' and self.__right_hand_rect.x <= 800:
#             self.__right_hand_rect.x += 1
#         if direction == 'left' and self.__right_hand_rect.x >= 0 and self.__right_hand_rect.x > self.__left_hand_rect.x:
#             self.__right_hand_rect.x -= 1


#     def __move_left_hand(self, direction):
#         '''Set left hand movement'''
#         if direction == 'right' and self.__left_hand_rect.x <= 800 and self.__right_hand_rect.x > self.__left_hand_rect.x:
#             self.__left_hand_rect.x += 1
#         if direction == 'left' and self.__left_hand_rect.x >= 0:
#             self.__left_hand_rect.x -= 1   
        


#     def game_play(self):
#         while 1:
#             for event in event.get():
#                 if event.type == QUIT:
#                     quit()
#                     sys.exit()
            
#                 # move right hand right using the right arrow key
#                 if event.key == K_RIGHT: self.__move_right_hand('right')

#                 # move right hand left using the left arrow key
#                 if event.key == K_LEFT: self.__move_right_hand('left')

#                 # move left hand right using the 'D' key
#                 if event.key == K_d: self.__move_left_hand('right')

#                 # move left hand left using the 'A' key
#                 if event.key == K_a: self.__move_left_hand('left')


#             self.__screen.blit(self.__background_surface,(0, 0))

# def main():
#     init()
#     game = JuggleGame()
#     game.game_play()
    

# if __name__ == '__main__':
#     main()