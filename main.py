from turtle import Turtle, Screen

# Aliasing module
import turtle as t
import random

tim = t.Turtle()
num_sides = 3
t.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")
tim.pensize(1)

for number in range(1, 72):
    tim.color(random_color())
    tim.circle(100)
    tim.left(5)


screen = Screen()
screen.exitonclick()