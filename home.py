import turtle
import math

turtle.shape("turtle")

x=40
d=math.sqrt(x**2 + x**2)

turtle.forward(x)
turtle.left(90)
turtle.forward(x)
turtle.left(90)
turtle.forward(x)
turtle.left(90)
turtle.forward(x)
turtle.left(90)

turtle.left(45)
turtle.forward(d)
turtle.left(90)
turtle.forward(d/2)
turtle.left(90)
turtle.forward(d/2)
turtle.left(90)
turtle.forward(d)
