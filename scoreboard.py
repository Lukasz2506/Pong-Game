from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_points = 0
        self.r_points = 0
        self.upload_score()

    def upload_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_points, align="center", font=("Arial", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_points, align="center", font=("Arial", 60, "normal"))

    def l_score(self):
        self.l_points += 1
        self.upload_score()

    def r_score(self):
        self.r_points += 1
        self.upload_score()
