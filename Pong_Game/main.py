import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
# Right player controls (up, down keys on keyboard)
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

# Left player controls (w, s keys on keyboard)
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    # Detect wall collisions:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect paddle collisions:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 315 or ball.distance(l_paddle) < 50 and ball.xcor() < -315:
        ball.bounce_x()


    # Detect when ball goes out of bounds on right side:
    if ball.xcor() > 370:
        scoreboard.keep_l_score()
        ball.reset_ball()

    # Detect when ball goes out of bounds on left side:
    if ball.xcor() < -370:
        scoreboard.keep_r_score()
        ball.reset_ball()

screen.exitonclick()
