from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

pad = Paddle((350, 0))
pad2 = Paddle((-350, 0))
ball = Ball()

p1 = ScoreBoard(-200,200)
p2 = ScoreBoard(100,200)

screen.listen()
screen.onkey(key="Up", fun=pad.move_up)
screen.onkey(key="Down", fun=pad.move_down)
screen.onkey(key="w", fun=pad2.move_up)
screen.onkey(key="s", fun=pad2.move_down)


is_on = True
while is_on:
    time.sleep(ball.speed)
    ball.move()
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(pad) < 50 and ball.xcor() > 320 or ball.distance(pad2) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()
    if ball.xcor() > 380:
        p1.add_point()
        ball.reset_pos()
    if ball.xcor() < -380:
        p2.add_point()
        ball.reset_pos()

screen.exitonclick()
