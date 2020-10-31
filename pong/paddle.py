import arcade
from point import Point

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
BALL_RADIUS = 10

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
MOVE_AMOUNT = 5

SCORE_HIT = 1
SCORE_MISS = 5

class Paddle:
    def __init__(self):
        self.center = Point()
        self.center.x = SCREEN_WIDTH - (PADDLE_WIDTH/2)
        self.center.y = 0 + (PADDLE_HEIGHT/2)
        
    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, PADDLE_WIDTH, PADDLE_HEIGHT, arcade.color.BLACK)
    
    def move_up(self):
        if(self.center.y > SCREEN_HEIGHT - (PADDLE_HEIGHT/2)):
            pass
        else:
            self.center.y += MOVE_AMOUNT
            
    def move_down(self):
        if(self.center.y < 0 + (PADDLE_HEIGHT/2)):
            pass
        else:
            self.center.y -= MOVE_AMOUNT