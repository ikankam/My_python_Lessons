from turtle import Turtle

TEXT_ALIGN = "center"
FONT = ('Courier', 12, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.score = 0
        self.keep_score()

    def keep_score(self):
        """Adds 1 when snake scores food"""
        self.write(f"Score:{self.score} ", align=TEXT_ALIGN, font=FONT)
        self.score += 1

    def game_over (self):
        """Ends game"""
        self.goto(0, 0)
        self.write("GAME OVER", align=TEXT_ALIGN, font=FONT)
