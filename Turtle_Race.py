from turtle import Turtle, Screen
import random

index = 0
space_between_turtles = 0

is_race_on = False

# Creating screen object and size
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Setting game to start only after user input.
if user_bet:
    is_race_on = True

# Creating empty list of turtles
turtle_list = []

# Creating turtle objects with colors above and setting positions
for turt in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turt])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + space_between_turtles)
    turtle_list.append(new_turtle)
    space_between_turtles += 40

# Starting the race
while is_race_on:
    for turtle in turtle_list:
        turtle_pace = random.randint(0, 10) # setting random paces for the turtles
        turtle.forward(turtle_pace)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()

            if user_bet == winning_turtle:
                print(f"You win! The winning turtle is {winning_turtle}")
            else:
                print(f"You lose. The winning turtle is {winning_turtle}")
screen.exitonclick()
