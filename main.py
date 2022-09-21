from turtle import Screen
from division_line import Line
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong Game")
screen.tracer(0)
line = Line()
line.draw_the_line(600)
scoreboard = Scoreboard()


# Create and move the paddles.
r_paddle = Paddle(position=(350, 0))
l_paddle = Paddle(position=(-350, 0))

# Create a ball.
ball = Ball()

# Create the screen.
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


move_speed = 0.1
# Loop the game
game_is_on = True
while game_is_on:
    screen.update()
    sleep(move_speed)
    ball.move()

    # Wall collision detection.
    if ball.xcor() > 390:
        ball.wall_collision()
        scoreboard.l_score()
        move_speed = 0.5

    if ball.xcor() < -390:
        ball.wall_collision()
        scoreboard.r_score()

    # Ceil and floor collision detection.
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()

    # Paddles collision detection.
    if (ball.distance(l_paddle) < 50 and ball.xcor() <= -340) or (ball.distance(r_paddle) < 50 and ball.xcor() >= 340):
        print('contact')
        ball.paddle_contact()
        move_speed /= 1.2

screen.exitonclick()