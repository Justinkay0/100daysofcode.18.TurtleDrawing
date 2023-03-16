from turtle import Turtle, Screen

thomas = Turtle()
thomas.shape('turtle')
thomas.color('crimson')

for i in range(4):
    thomas.forward(100)
    thomas.right(90)

screen = Screen()
screen.exitonclick()
