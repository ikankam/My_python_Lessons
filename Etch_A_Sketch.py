# Etch-A-Sketch program.
# Uses turtle to make the childhood game.
# To move turtle forward = use w key, backwards = use s key
# Counter-clockwise = a key and clockwise = d key
# Press c key to clear screen to begin a new drawing.

from turtle import Turtle, Screen

tilly = Turtle("turtle")
tilly.color("blue")


def forwards():
    tilly.forward(10)


def backwards():
    tilly.backward(10)


def counter_clockwise():
    tilly.left(10)


def clockwise():
    tilly.right(10)


def clear_screen():
    tilly.clear()
    tilly.penup()
    tilly.home()
    tilly.pendown()


screen = Screen()
screen.onkey(key="w", fun=forwards)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.listen()
screen.exitonclick()
