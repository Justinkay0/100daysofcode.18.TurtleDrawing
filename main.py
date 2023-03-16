from turtle import Turtle, Screen
from random import randint

thomas = Turtle()
screen = Screen()
thomas.shape('turtle')
thomas.color('crimson')
screen.colormode(255)

colour = [randint(0, 255),
          randint(0, 255),
          randint(0, 255)]

for sides in range(3, 12):
    rotation = 0
    colour = [randint(0, 255),
              randint(0, 255),
              randint(0, 255)]
    thomas.pencolor(colour)
    while rotation != 360:
        rotation += 360 / sides
        if round(rotation) == 360:
            rotation = 360
        thomas.forward(30)
        thomas.right(360 / sides)
        print(rotation)


screen.exitonclick()
