import arcade
import random
from point import Point
from velocity import Velocity

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
BALL_RADIUS = 10

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
MOVE_AMOUNT = 5

SCORE_HIT = 1
SCORE_MISS = 5

class Ball:
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.center.x = BALL_RADIUS
        self.center.y = random.uniform(BALL_RADIUS, SCREEN_HEIGHT - BALL_RADIUS)
        self.velocity.dx = random.uniform(1, 5)
        self.velocity.dy = random.uniform(1, 5)
        
    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, BALL_RADIUS, arcade.color.ORANGE)
    
    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
    
    def bounce_horizontal(self):
        self.velocity.dx *= -1
    
    def bounce_vertical(self):
        self.velocity.dy *= -1
    
    def restart(self):
        self.center.x = BALL_RADIUS
        self.center.y = random.uniform(BALL_RADIUS, SCREEN_HEIGHT - BALL_RADIUS)