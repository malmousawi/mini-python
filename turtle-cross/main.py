import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")

player = Player()
car = CarManager()
score = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.add_car()
    car.move()
    if player.ycor() > 280:
        player.next_level()
        car.next_level()
        score.add_level()
    for i in car.cars:
        if i.distance(player) < 20:
            score.game_over()
            game_is_on = False


screen.exitonclick()