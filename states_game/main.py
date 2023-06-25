import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)


data = pd.read_csv("50_states.csv")
states = data.state.tolist()

correct_states = 0


while correct_states < 50:
    answer = screen.textinput(title=f"{correct_states}/50 States correct", prompt="What's another state name?").title()
    if answer in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_info = data[data.state == answer]
        t.goto((int(state_info.x), int(state_info.y)))
        t.write(state_info.state.item())
        correct_states += 1


turtle.mainloop()
screen.exitonclick()