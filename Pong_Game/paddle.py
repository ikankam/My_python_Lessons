from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, paddle_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(paddle_pos)

    def up(self):
        y_change = self.ycor() + 20
        self.goto(self.xcor(), y_change)

    def down(self):
        y_change = self.ycor() - 20
        self.goto(self.xcor(), y_change)
