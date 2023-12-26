# import turtle
#
# turtle.pendown()
# turtle.forward(150)
# turtle.right(90)
# turtle.forward(150)
# turtle.right(90)
# turtle.circle(150)
# turtle.done()

from turtle import *
from math import radians, cos


def square(length: int) -> None:
    """Draws a square of length `length`"""
    inner_foward = forward
    inner_right = right
    for side in range(4):
        forward(length)
        right(90)


def encircled_square(length: int) -> None:
    """Draws a square of length `length`,
    then encloses it in a circle.
"""
    square(length)
    angle = radians(45)
    radius = length * cos(angle)
    right(135)
    circle(radius)
    print(f'Inside function, namespace is: {dir()}')
    print(f'{locals()}')


# encircled_square(300)
speed('fast')
Screen().tracer(0) # disable turtle animation
for s in range(72):
    encircled_square(120)
    left(5)

Screen().update() # update the screen
done()

print(dir())
g = globals()
print(g['square'])

print(dir(__builtins__))
