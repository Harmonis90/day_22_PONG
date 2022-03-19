from turtle import Turtle, Screen

UNIT_SIZE = 40
PADDLE_MAX = 300 - 100
PADDLE_MIN = -300 + 100
class Paddle(Turtle):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(xpos, ypos)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        if self.ycor() <= PADDLE_MAX:
            new_ypos = self.ycor() + UNIT_SIZE
            self.goto(self.xcor(), new_ypos)

    def move_down(self):
        if self.ycor() >= PADDLE_MIN:
            new_ypos = self.ycor() - UNIT_SIZE
            self.goto(self.xcor(), new_ypos)
