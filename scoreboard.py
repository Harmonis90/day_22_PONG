from turtle import Turtle

L_SCORE = (-100, 180)
R_SCORE = (100, 180)
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.color("#ffffff")
        self.penup()

        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(L_SCORE)
        self.write(self.l_score, align="center", font=("Monospace", 80, "normal"))
        self.goto(R_SCORE)
        self.write(self.r_score, align="center", font=("Monospace", 80, "normal"))

    def l_add_point(self):
        self.l_score += 1
        self.update_score()

    def r_add_point(self):
        self.r_score += 1
        self.update_score()
