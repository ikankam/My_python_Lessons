from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        """Clears and writes current score on screen"""
        self.clear()
        self.goto(-150, 200)
        self.write(f"{self.l_score} ", align="center", font=("Courier", 80, "normal"))
        self.goto(150, 200)
        self.write(f"{self.r_score} ", align="center", font=("Courier", 80, "normal"))

    def keep_l_score(self):
        """Adds 1 when right player goes out of bounds"""
        self.l_score += 1
        self.update_score()

    def keep_r_score(self):
        """Adds 1 when left player goes out of bounds"""
        self.r_score += 1
        self.update_score()
