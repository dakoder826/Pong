from turtle import Turtle
STARTING_POSITIONS = [(350, 0)]


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, to_position):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(to_position)

    def up(self):
        if self.ycor() < 245:
            new_y_position = self.ycor() + 20
            self.goto(self.xcor(), new_y_position)

    def down(self):
        if self.ycor() > -240:
            new_y_position = self.ycor() - 20
            self.goto(self.xcor(), new_y_position)


