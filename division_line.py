from turtle import Turtle

DISTANCE = 20


class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=-280)
        self.pendown()
        self.pensize(5)

    def draw_the_line(self, screen_height):
        self.seth(90)
        for draw in range (0, (screen_height) // ((DISTANCE * 2)-2)):
            self.forward(DISTANCE)
            self.penup()
            self.forward(DISTANCE)
            self.pendown()
