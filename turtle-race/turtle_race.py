from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
screen.colormode(255)

race_on = False
user = screen.textinput(title="Make your bet: ", prompt="Which colour will win the race?: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = -70
turtles = []


for i in range(0,6):
    a = Turtle("turtle")
    a.penup()
    a.color(colors[i])
    a.goto(x = -230,y = y_pos)
    y_pos += 30
    turtles.append(a)

if user:
    race_on = True

while race_on:
    dist = random.randint(0,10)
    for i in turtles:
        if i.xcor() >= 230:
            winner = i.pencolor()
            race_on = False
            if winner == user:
                print("You won!")
            else:
                print("You lost!")
            print(f"The {i.pencolor()} turtle won!")
            break

        i.forward(dist)


screen.exitonclick()

