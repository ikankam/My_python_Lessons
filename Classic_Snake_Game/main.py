from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setting up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

# Setting up the snake, food, scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Starting the game
game_on = True
while game_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

# Detect collision with food
    if snake.head.distance(food) < 13:
        scoreboard.clear()
        food.refresh()
        snake.extend()
        scoreboard.keep_score()

# Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

# Detect collision with tail
    for snake_seg in snake.segment[1:]:   # List slicing to remove head in first case
        if snake.head.distance(snake_seg) < 10:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()
