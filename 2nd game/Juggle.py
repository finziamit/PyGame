from pygame import *
import sys
from random import choice
from datetime import date
import sqlite3

class Hand:
    ''' An hand in the game '''
    def __init__(self, path, placement):
        self.__surface = image.load(path)
        self.__surface = transform.smoothscale(self.__surface.convert_alpha(), (100,80))
        self.__rect = self.__surface.get_rect(midleft=placement)
    
    @property
    def rect(self):
        return self.__rect
    
    @property
    def surface(self):
        return self.__surface
    
    def move_hand_right(self):
        if self.__rect.right < 800: self.__rect.x += 3
    
    def move_hand_left(self):
        if self.__rect.x > 0: self.__rect.x -= 3


class Ball:
    ''' A ball in the game '''
    def __init__(self, path):
        self.__surface = image.load(path)
        self.__surface = transform.smoothscale(self.__surface.convert_alpha(), (50,50))
        self.__rect = self.__surface.get_rect(midleft=(0,0))
        self.__ball_gravity = 0
        self.__direction = choice([-1, 1])
        self.__first_touch = True
        self.__speed = 1
    
    @property
    def rect(self):
        return self.__rect

    @property
    def surface(self):
        return self.__surface

    @property
    def direction(self):
        return self.__direction

    @property
    def first_touch(self):
        return self.__first_touch
    
    @property
    def ball_gravity(self):
        return self.__ball_gravity
    
    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, val):
        self.__speed = val

    @ball_gravity.setter
    def ball_gravity(self, val):
        self.__ball_gravity = val

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
            if self.__rect.top > 800: self.__ball_gravity = 0
            if self.__ball_gravity < 2: self.__ball_gravity += 0.1

            self.__rect.y += self.__ball_gravity

            if self.__rect.right >= 800: self.__direction = -1
            if self.__rect.left <= 0: self.__direction = 1

            self.__rect.x += self.__direction * self.__speed


class ScoresDB:
    def __init__(self):
        self.__connection = sqlite3.connect("scores.db")
        self.__cursor = self.__connection.cursor()
        create_scores_table = """CREATE TABLE IF NOT EXISTS
        scores(score_id INTEGER PRIMARY KEY, score_count INTEGER, date TEXT)"""
        self.__cursor.execute(create_scores_table)
    
    @property
    def cursor(self):
        return self.__cursor

    def get_results(self):
        self.__cursor.execute("SELECT * FROM scores")
        return self.__cursor.fetchall()

    def add_score(self, score):
        row = (score, date.today())
        self.__cursor.execute("INSERT INTO scores(score_count, date) VALUES (?, ?)", row)
        self.__connection.commit()
    
    def get_top_10(self):
        results = self.get_results()
        sorted_results = sorted(results, key=lambda x:x[1], reverse=True)
        if len(sorted_results) <= 10:
            return sorted_results
        else:
            return sorted_results[:10]



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

    test_font = font.Font(None, 50)
    score_display_font = font.Font(None, 40)
<<<<<<< HEAD
    score_table_font = font.Font(None, 30)
=======
>>>>>>> 3524e502bd6dfc6f5b53b3a6d884236fddf515e4

    game_deactivated_screen_color = (255,0,24)
    instructions_text_surface = test_font.render("Select an option and press the space button", False, 'white')
    instructions_text_rect = instructions_text_surface.get_rect(center = (400,50))

    # Choice in main screen
    play_option_surface = score_display_font.render("Play", False, 'white')
    play_option_rect = play_option_surface.get_rect(midleft=(300,170))

    top_scores_option_surface = score_display_font.render("Highest Scores", False, 'white')
    top_scores_option_rect = top_scores_option_surface.get_rect(midleft=(300,220))

    # Highest scores table
<<<<<<< HEAD
    score_display_surface = score_display_font.render("Top Scores (to return to main menu press 'M'):", False, 'white')
    score_display_rect = score_display_surface.get_rect(center = (400,50))
=======
    score_display_surface = score_display_font.render("#    Score   Date", False, 'white')
    score_display_rect = score_display_surface.get_rect(center = (400,100))
>>>>>>> 3524e502bd6dfc6f5b53b3a6d884236fddf515e4

    score_surface = test_font.render(f"Score: 0", False, 'white')
    score_rect = score_surface.get_rect(center = (400, 120))

    balls = [blue_ball, red_ball, yellow_ball]
    game_active = False

    move_right_hand_right = False
    move_right_hand_left = False
    move_left_hand_right = False
    move_left_hand_left = False

    score_added = False
    score_table = False

    scores_DB = ScoresDB()
    score = -1
    player_choice = 1
    while 1:        
        for action in event.get():
                if action.type == QUIT:
                    quit()
                    sys.exit()
                
                if action.type == KEYDOWN and action.key == K_ESCAPE:
                    quit()
                    sys.exit()
            
                if game_active:
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
                # end of if game active block
                else:
                    if action.type == KEYDOWN and action.key == K_UP:
                        player_choice = 1

                    if action.type == KEYDOWN and action.key == K_DOWN:
                        player_choice = 2

<<<<<<< HEAD
                    if action.type == KEYDOWN and action.key == K_m:
                        player_choice = 2
                        score_table = False

=======
>>>>>>> 3524e502bd6dfc6f5b53b3a6d884236fddf515e4
                    if action.type == KEYDOWN and action.key == K_SPACE:
                        if player_choice == 1:
                            game_active = True
                            score_added = False
                            score = 0
                            right_hand.rect.x = 500
                            left_hand.rect.x = 250
                            for ball in balls:
                                ball.first_touch = True
                                start_point = (choice(range(350,450)), 40)
                                ball.rect.midleft=start_point
                                ball.ball_gravity = 0
                                ball.direction = choice([-1, 1])
                                ball.speed = 1
                        else:
<<<<<<< HEAD
                            score_table = True
        # end of the event handler
=======
                            # TODO: display 'highest scores' screen
                            pass
        # end of the event handler
        print(player_choice)
>>>>>>> 3524e502bd6dfc6f5b53b3a6d884236fddf515e4
        if game_active:
            player_choice = 1
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
            for ball in balls:
                if ball.rect.y >=500: game_active = False

            # check if the hand touched the ball
            for ball in balls:
                if left_hand.rect.colliderect(ball.rect) or right_hand.rect.colliderect(ball.rect):
                    ball.first_touch = False
                    ball.direction = choice([-1, 1])
                    ball.rect.bottom = right_hand.rect.top
                    ball.speed = choice(range(2,4)) / 2
                    ball.ball_gravity = choice(range(8,11)) * -1
                    ball.move_ball()
                    score += 1

            score_surface = test_font.render(f"Score: {score}", False, 'white')

            screen.blit(background_surface, (0, 0))
            screen.blit(right_hand.surface, right_hand.rect)
            screen.blit(left_hand.surface, left_hand.rect)
            screen.blit(score_surface, score_rect)
            for ball in balls:
                screen.blit(ball.surface, ball.rect)
        # end of game_active
        else: # if game is not active
            screen.fill(game_deactivated_screen_color)
<<<<<<< HEAD
=======
            screen.blit(instructions_text_surface, instructions_text_rect)
            screen.blit(play_option_surface, play_option_rect)
            screen.blit(top_scores_option_surface, top_scores_option_rect)
            if player_choice == 1: draw.circle(screen, (0,0,0), [280,170], 4, 0)
            else: draw.circle(screen, (0,0,0), [280,220], 4, 0)
>>>>>>> 3524e502bd6dfc6f5b53b3a6d884236fddf515e4

            if score_table:
                screen.blit(score_display_surface, score_display_rect)
                top_10_scores = scores_DB.get_top_10()
                scores_surfaces = [score_table_font.render(f"{i+1}.    {top_10_scores[i][1]}  {top_10_scores[i][2]}", False, 'black') for i in range(10)]
                scores_rects = [scores_surfaces[i].get_rect(midleft=(150, 100 + (i*40))) for i in range(10)] 
                for i in range(10):
                    screen.blit(scores_surfaces[i], scores_rects[i])
            else:
                screen.blit(instructions_text_surface, instructions_text_rect)
                screen.blit(play_option_surface, play_option_rect)
                screen.blit(top_scores_option_surface, top_scores_option_rect)
                if player_choice == 1: draw.circle(screen, (0,0,0), [280,170], 4, 0)
                else: draw.circle(screen, (0,0,0), [280,220], 4, 0)

                final_score_surface = test_font.render(f"Your score: {score}", False, 'white')
                final_score_rect = instructions_text_surface.get_rect(center = (500, 400))

                if score >= 0:
                    screen.blit(final_score_surface, final_score_rect)
                    if not score_added:
                        scores_DB.add_score(score)
                        score_added = True

                move_right_hand_right = False
                move_right_hand_left = False
                move_left_hand_right = False
                move_left_hand_left = False
        display.update()
        clock.tick(240)
    # end of while loop

def main():
    init()
    game_play()

if __name__ == '__main__':
    main()
