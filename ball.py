from turtle import Turtle, Screen
import random
import time


BALL_SIZE = 20
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

PADDLE_YPOS = 360


# EAST = 0
# NORTH_EAST = 45
# NORTH = 90
# NORTH_WEST = 135
# WEST = 180
# SOUTH_WEST = 225
# SOUTH = 270
# SOUTH_EAST = 315


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.shape("circle")
        self.color("#ffffff")
        self.direction_x = (BALL_SIZE / 2)
        self.direction_y = (BALL_SIZE / 2)
        self.delta_speed = 0.03
    def move(self):
        new_xpos = self.xcor() - self.direction_x
        new_ypos = self.ycor() - self.direction_y
        self.goto(new_xpos, new_ypos)

    def on_collision(self):
        pos_ybounds = int(SCREEN_HEIGHT / 2) - (BALL_SIZE / 2)
        neg_ybounds = int(-SCREEN_HEIGHT / 2) + (BALL_SIZE / 2)
        if self.ycor() >= pos_ybounds or self.ycor() <= neg_ybounds:
            self.bounce_y()

    def bounce_y(self):
        self.direction_y *= -1

    def bounce_x(self):
        self.direction_x *= -1
        self.delta_speed *= 0.9
    def check_collision_with_paddle(self):
        if self.xcor() <= -PADDLE_YPOS or self.xcor() >= PADDLE_YPOS:
            return True

    def on_point_trigger(self):
        pos_xbounds = int(SCREEN_WIDTH / 2) - (BALL_SIZE / 2)
        neg_xbounds = int(-SCREEN_WIDTH / 2) + (BALL_SIZE / 2)
        if self.xcor() >= pos_xbounds or self.xcor() <= neg_xbounds:
            return True

    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_x()
        self.delta_speed = 0.03
