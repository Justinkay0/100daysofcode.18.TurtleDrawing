import colorgram
import random
import turtle

color = colorgram.extract('hirst-painting.jpeg', 15)
print(color)

color_list = []
for _ in color:
    color_input = []
    for rgb in _.rgb:
        color_input.append(rgb)
    color_input = tuple(color_input)
    color_list.append(color_input)


def paint(tortoise, color_bank):
    for _ in range(10):
        tortoise.dot(20, random.choice(color_bank))
        tortoise.forward(50)
        tortoise.up()


kratos = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)
kratos.up()
screen.setworldcoordinates(-20, -20, 500, 300)

zero = 0
for i in range(10):
    kratos.up()
    paint(kratos, color_list)
    kratos.setpos(0, zero + ((i + 1) * 30))

screen.exitonclick()
