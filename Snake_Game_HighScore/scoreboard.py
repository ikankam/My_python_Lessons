from turtle import Turtle

TEXT_ALIGN = "center"
FONT = ('Courier', 12, 'bold')

with open("data.txt", mode="r") as file:
    data = file.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.score = 0
        self.high_score = int(data)
        self.update_score()

    def keep_score(self):
        """Adds 1 when snake scores food"""
        self.score += 1
        self.update_score()

    def update_score(self):
        """Updates with current score and high score"""
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.high_score}", align=TEXT_ALIGN, font=FONT)


    def reset(self):
        """Adding and keeping track of high score"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as score:
                new_score = score.write(str(self.high_score))
        self.score = 0
        self.update_score()

        # def game_over (self):
    #     """Ends game"""
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=TEXT_ALIGN, font=FONT)
