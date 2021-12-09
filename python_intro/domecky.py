import math
import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
turtle.color("white")

def domecek(size):
    domecekNormal(size, 1)

def domecekPlanet(size, angles):
    
    turtle.left(90)
    turtle.penup()
    print(size/(2*math.tan(((2*math.pi)/angles)/2)))
    turtle.forward(size/(2*math.tan((2*math.pi/angles)/2)))
    
    
    turtle.left(90)
    turtle.forward(size/2)
    turtle.right(180)
    turtle.pendown()
    for i in range (angles):
        domecekNormal(size, angles)

def domecekNormal(size, angles):
    side = size
    diagonal = (side) * math.sqrt(2)
    roofLeft = (side / 2) * math.sqrt(2)
    roofRightTop = (side / 5) * math.sqrt(2)
    roofRightBottom = ((side / 10) * 1.5) * math.sqrt(2)
    chimneyLeft = (side / 10) * 1.5
    chimneyTop = chimneyLeft
    chimneyRight = 2 * chimneyLeft

    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.right(135)
    turtle.forward(roofLeft)
    turtle.right(90)

    # chimney
    turtle.forward(roofRightTop)

    turtle.left(135)
    turtle.forward(chimneyLeft)
    turtle.right(90)
    turtle.forward(chimneyTop)
    turtle.right(90)
    turtle.forward(chimneyRight)
    turtle.left(45)

    turtle.forward(roofRightBottom)
    # chimney
    turtle.right(90)
    turtle.forward(diagonal)
    turtle.right(135)
    turtle.forward(side)
    turtle.right(135)
    turtle.forward(diagonal)
    turtle.left(45 - (360/angles))

# domecekPlanet(40, 24)
domecek(50)

turtle.mainloop()
turtle.exitonclick()