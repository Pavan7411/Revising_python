import turtle   #import turtle module for the below code to make sense

turtle.shape("turtle")  #changing the shape of the turtle from arrow to turtle
x=40                    #size of square         

for j in range(36):     #for loop for drawing multiple squares

    for i in range(4):      #for loop for drawing a square
        turtle.forward(x)
        turtle.left(90)

    turtle.left(10)
