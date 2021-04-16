import turtle
x=1
while True:
    turtle.forward(x)
    turtle.left(10)
    x+=0.1
    if turtle.distance(0,0)>100:
        break

    
