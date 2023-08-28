from turtle import Turtle
ALIGNMENT = "center"
FONT = "Times New Roman", 45, "normal"


class Score(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setposition(position)
        self.update_score()

    def update_score(self):
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def right_won(self):
        self.setposition(0, 0)
        self.write(f"The Right Player Won", align=ALIGNMENT, font=FONT)

    def left_won(self):
        self.setposition(0, 0)
        self.write(f"The Left Player Won", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.update_score()





