from turtle import Turtle
from random import choice


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1, 1)
        self.penup()
        self.increment_x_list = 12, -12
        self.increment_y_list = 10, -10
        self.increment_x = choice(self.increment_x_list)
        self.increment_y = choice(self.increment_y_list)

    def move(self):

        new_x = self.xcor() + self.increment_x
        new_y = self.ycor() + self.increment_y
        self.goto(new_x, new_y)

    def wall_collision(self):
        self.goto(0, 0)

    def bounce(self):
        self.increment_y *= -1

    def paddle_contact(self):
        self.increment_x *= -1
