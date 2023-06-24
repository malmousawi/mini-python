from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.level = 0
        self.color("white")
        self.penup()
        self.goto(x,y)
        self.write(f"Score: {self.level}", move=False, align='left', font=('Arial', 24, 'normal'))
        self.hideturtle()

    def add_point(self):
        self.clear()
        self.level += 1
        self.write(f"Score: {self.level}", move=False, align='left', font=('Arial', 24, 'normal'))