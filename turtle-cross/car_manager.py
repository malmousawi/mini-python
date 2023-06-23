from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def add_car(self):
        num = random.randint(1,6)
        if num == 1:
            temp = Turtle("square")
            temp.shapesize(stretch_wid=1, stretch_len=2)
            temp.penup()
            random_y = random.randint(-230, 230)
            col = random.choice(COLORS)
            temp.color(col)
            temp.goto(300, random_y)
            self.cars.append(temp)

    def move(self):
        for car in self.cars:
            car.backward(self.speed)

    def next_level(self):
        self.speed += MOVE_INCREMENT


