from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coor):
        super().__init__()
        self.create_paddle(coor)

    def create_paddle(self, coor):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(coor)

    def move_up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def move_down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)


