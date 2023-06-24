from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 15


class Snake:
    def __init__(self):
        self.pieces = []
        self.create_snake()
        self.head = self.pieces[0]
        self.speed = DISTANCE

    def create_snake(self):
        for coordinates in START_POSITIONS:
            self.add_piece(coordinates)

    def add_piece(self,pos):
        a = Turtle("square")
        a.color("white")
        a.penup()
        a.goto(pos)
        self.pieces.append(a)

    def reset(self):
        for i in self.pieces:
            i.goto(1000,1000)
        self.pieces.clear()
        self.create_snake()
        self.head = self.pieces[0]

    def add_to_snake(self):
        self.add_piece(self.pieces[-1].position())

    def move(self):
        for piece in range(len(self.pieces) - 1, 0, -1):
            temp_x = self.pieces[piece - 1].xcor()
            temp_y = self.pieces[piece - 1].ycor()
            self.pieces[piece].goto(temp_x, temp_y)
        # self.increase_level()
        self.pieces[0].forward(self.speed)

    def touch_tail(self):
        for i in self.pieces[1:]:
            if self.head.distance(i) < 10:
                return True
        return False

    # def increase_level(self):
    #     if len(self.pieces) == self.speed:
    #         self.speed += 10

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

