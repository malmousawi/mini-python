from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# test

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.update()

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()


def move_left():
    snake.pieces[0].left(90)


def move_right():
    snake.pieces[0].right(90)


screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)

is_playing = True
while is_playing:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score.update_scoreboard()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_to_snake()
        score.add_level()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()
    if snake.touch_tail():
        score.reset()
        snake.reset()

screen.exitonclick()

