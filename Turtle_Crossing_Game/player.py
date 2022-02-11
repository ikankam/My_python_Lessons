from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# Create a turtle player that starts at the bottom of the screen and listen
# for the "Up" keypress to move the turtle north.
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_player(self):
        """Moves player along the y-axis in increment of 10"""
        y_change = self.ycor() + MOVE_DISTANCE
        print(y_change)  # debugging purposes
        self.goto(self.xcor(), y_change)



