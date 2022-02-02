# Extracting rgb color palette of one of Damien Hirst's spot paintings using colorgram
# import colorgram
#
#
# color_extraction = colorgram.extract('hirst_painting.jpg', 2**32)
#
#
# color_palette = []
#
# for color in color_extraction:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_palette = (r,g,b)
#     color_palette.append(new_palette)
#
# print (color_palette)


# Program to make a replica of one of Damien Hirst's spot paintings.
# It uses colorgram to extract colors from an image from the web
# And uses turtle graphics to draw a 10 x 10 replica of the painting.

import random
import turtle
import turtle as t
from turtle import Turtle, Screen

turtle.colormode(255)
tilly = t.Turtle()
color_list = [(1, 12, 31), (53, 25, 17),
              (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63), (155, 6, 24),
              (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20), (174, 135, 163),
              (1, 61, 145), (7, 172, 216), (3, 213, 207), (159, 33, 24), (8, 140, 85), (145, 227, 217), (122, 193, 147),
              (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178), (252, 197, 0), (29, 84, 92),
              (228, 174, 166), (186, 190, 201), (73, 73, 39)]
turtle.setworldcoordinates(-100, -100, 600, 600)
# print (len(color_list)) #35 colors obtained.


set_pos = 0

for step in range(10):
    set_pos += 50
    tilly.speed("fastest")
    for _ in range(9):
        tilly.dot(20, random.choice(color_list))
        tilly.penup()
        tilly.forward(50)
        tilly.dot(20, random.choice(color_list))
    tilly.setpos(0, set_pos)
tilly.hideturtle()
screen = t.Screen()
screen.exitonclick()
