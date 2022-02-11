from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

# Setting up the screen
screen = Screen()
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.setup(height=600, width=600)
screen.tracer(0)

player = Player() # Setting up the player turtle

car_manager = CarManager()  # Setting up the cars

scoreboard = Scoreboard() # Setting up the scoreboard

# Listening for keyboard input to move player up the screen
screen.listen()
screen.onkey(player.move_player, "Up")

# Setting up the game
game_on = True

while game_on:

    time.sleep(0.1)  # screen sleeps for 0.1 and refreshes
    screen.update()
    car_manager.create_new_car()
    car_manager.move_cars()

    # Checking distance from player to car
    for car in car_manager.car_list:
        if player.distance(car) < 15:
            game_on = False
            scoreboard.game_over()
    # Checking if player has successfully reached the finish line
    if player.ycor() > 280:
        player.goto(0, -280)
        car_manager.level_up()
        scoreboard.keep_score()

screen.exitonclick()
