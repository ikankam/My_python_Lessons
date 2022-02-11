from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 1
        self.keep_score()

    def keep_score(self):
        """Writes player level on screen. Increases with each successful reach at the finish line."""
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level:{self.score}", font=FONT)
        self.score += 1

    def game_over(self):
        """Writes game over on screen"""
        self.goto(-80, 0)
        self.write("GAME OVER", font=FONT)
