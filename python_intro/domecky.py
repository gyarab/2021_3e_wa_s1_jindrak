import math
import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
turtle.color("white")

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.right(135)
turtle.forward(50 * math.sqrt(2))
turtle.right(90)

# chimney
turtle.forward(20 * math.sqrt(2))

turtle.left(135)
turtle.forward(15)
turtle.right(90)
turtle.forward(15)
turtle.right(90)
turtle.forward(30)
turtle.left(45)

turtle.forward(15 * math.sqrt(2))
# chimney
turtle.right(90)
turtle.forward(100 * math.sqrt(2))
turtle.right(135)
turtle.forward(100)
turtle.right(135)
turtle.forward(100 * math.sqrt(2))

turtle.mainloop()
