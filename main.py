from turtle import Turtle, Screen

thomas = Turtle()
thomas.shape('turtle')
thomas.color('crimson')

for i in range(15):
    thomas.pendown()
    thomas.forward(10)
    thomas.penup()
    thomas.forward(10)

screen = Screen()
screen.exitonclick()
