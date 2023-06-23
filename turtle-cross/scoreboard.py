from turtle import Turtle

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-280,270)
        self.write(f"Level: {self.level}", move=False, align='left', font=FONT)
        self.hideturtle()

    def add_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", move=False, align='left', font=FONT)

    def game_over(self):
        self.goto(-50,0)
        self.write("GAME OVER!", move=False, align='left', font=FONT)
