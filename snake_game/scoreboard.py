import turtle
from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(-100,270)
        self.write(f"Score: {self.level}", move=False, align='left', font=('Arial', 24, 'normal'))
        self.hideturtle()

    def add_level(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.level}  High Score: {self.high_score}", move=False, align='left', font=('Arial', 24, 'normal'))

    def reset(self):
        if self.level > self.high_score:
            self.high_score = self.level
        self.level = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(-40,0)
        self.write("GAME OVER!", move=False, align='left', font=('Arial', 24, 'normal'))
