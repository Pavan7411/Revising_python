
def line_without_moving():
    import turtle
    turtle.forward(20)
    turtle.backward(20)
    
def star_arm():
    import turtle
    line_without_moving()
    turtle.right(360 / 5)

def hexagon():
    import turtle   #import turtle module for the below code to make sense

    x=50                    #length of polygon
    n=6                     #n sided regular polygon
    th = 360/n              #th is the external angle made by sides
                        #calculation based on property that external angle sum of convex polygon is 360


    for i in range(n):      #for loop for drawing a regular polygon
       turtle.forward(x)
       turtle.left(th)

def tilted_line_without_moving(length,angle):
    import turtle
    turtle.left(angle)
    turtle.forward(length)
    turtle.backward(length)

def reg_pol(x,n):
    import turtle   #import turtle module for the below code to make sense

    #x is length of polygon
    #n is number of sides of polygon
    th = 360/n              #th is the external angle made by sides
                        #calculation based on property that external angle sum of convex polygon is 360


    for i in range(n):      #for loop for drawing a regular polygon
       turtle.forward(x)
       turtle.left(th)
    
	
def tilted_shapes(tilt,theta):    #exercise showing that one can pass functions as arguements as well
    import turtle

def move(): #asking for directions and then moving
    direction=input("Go left or right?")
    import turtle
    direction=direction.strip()
    direction=direction.lower()
    if direction == "left":
        turtle.left(60)
        turtle.forward(50)
    if direction =="right":
        turtle.right(60)
        turtle.forward(50)

def prison():
    import turtle
    if turtle.distance(0,0) > 100:
        turtle.setheading(turtle.towards(0,0))
        turtle.forward(turtle.distance(0,0))
