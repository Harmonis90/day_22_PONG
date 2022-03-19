# Factoring Pong
# Classes:
#   main_controller
#       PLAYER
#           Paddle, score_board, listener
#       AI/PLAYER_2
#           Paddle, score_board, listener
#       Screen
#           size, color,
#           score_board
#           middle line
#           boundaries:
#               collision boundary (bounce ball)
#               trigger boundary (points)
#           listener:
#               listen for player input:
#                   move paddle accordingly
#       Paddles
#           shape, color, size
#           collision detection with ball
#           locked on the x-axis
#
#       Ball
#           size, shape, color, position, bounce_factor
#           the ball will be the detector of sorts
#           detects if_collided:
#                       with wall to bounce
#                       with wall to score point
#                       with paddle to bounce
#           from bounce create deflection angle from angle of attack

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

DELTA_SPEED = 0.1
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
UNIT_SIZE = 20

PADDLE_PADDING = 50

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Phosphorus Oxygen Nitrogen Gallium")
screen.bgcolor("#000000")
screen.tracer(0)

sb = ScoreBoard()

p1_xpos = int(-SCREEN_WIDTH / 2) + UNIT_SIZE
p1_ypos = 0
paddle_left = Paddle(xpos=p1_xpos, ypos=p1_ypos)


p2_xpos = int(SCREEN_WIDTH / 2) - UNIT_SIZE
p2_ypos = 0
paddle_right = Paddle(xpos=p2_xpos, ypos=p2_ypos)
print(f"LEFT: {paddle_left.pos()}, RIGHT: {paddle_right.pos()}")

def paddle_left_dist_to_ball():
    if paddle_left.distance(ball.pos()) < PADDLE_PADDING:
        return True


def paddle_right_dist_to_ball():
    if paddle_right.distance(ball.pos()) < PADDLE_PADDING:
        return True


ball = Ball()

is_playing = True
while is_playing:
    screen.update()
    time.sleep(ball.delta_speed)
    screen.listen()
    ball.move()
    ball.on_collision()
    if ball.on_point_trigger():
        if ball.xcor() > 0:
            sb.l_add_point()
            ball.reset_ball()
        else:
            sb.r_add_point()
            ball.reset_ball()
    if ball.check_collision_with_paddle():
        if paddle_left_dist_to_ball() or paddle_right_dist_to_ball():
            ball.bounce_x()

    screen.onkeypress(key="w", fun=paddle_left.move_up)
    screen.onkeypress(key="s", fun=paddle_left.move_down)
    screen.onkeypress(key="Up", fun=paddle_right.move_up)
    screen.onkeypress(key="Down", fun=paddle_right.move_down)

screen.exitonclick()
