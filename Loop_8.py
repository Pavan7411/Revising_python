import turtle   #import turtle module for the below code to make sense

turtle.shape("turtle")  #changing the shape of the turtle from arrow to turtle
x=10                    #size of circle
n=30                     #n sided regular polygon
th = 360/n              #th is the external angle made by sides
                        #calculation based on property that external angle sum of convex polygon is 360

for j in range(36):         #drawing many circles
    for i in range(n):      #for loop for drawing a regular polygon
        turtle.forward(x)
        turtle.left(th)

    turtle.left(10)         #tilting the turtle a bit


