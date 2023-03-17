from turtle import Turtle, Screen
from random import randint

thomas = Turtle()
screen = Screen()
thomas.shape('turtle')
thomas.color('crimson')
screen.colormode(255)
thomas.pensize(5)
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


def draw_circle(turtle):
    turtle.circle(100)
    turtle.left(10)


for _ in range(36):
    thomas.pencolor(tuple(random_color()))
    draw_circle(thomas)
screen.exitonclick()
