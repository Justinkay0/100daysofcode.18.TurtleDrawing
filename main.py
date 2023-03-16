from turtle import Turtle, Screen
from random import randint

thomas = Turtle()
screen = Screen()
thomas.shape('turtle')
thomas.color('crimson')
screen.colormode(255)
thomas.pensize(15)
thomas.speed(10)


def random_color():
    colour = [randint(0, 255),
              randint(0, 255),
              randint(0, 255)]
    return colour


def random_move(turtle):
    direction = randint(1, 2)
    if direction == 1:
        turtle.left(90)
        turtle.forward(20)
    elif direction == 2:
        turtle.right(90)
        turtle.forward(20)


for _ in range(100):
    thomas.pencolor(random_color())
    random_move(thomas)

screen.exitonclick()
