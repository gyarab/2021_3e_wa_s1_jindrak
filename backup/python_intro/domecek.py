import turtle
import math
import time

michelangelo = turtle.Turtle()

michelangelo.left(90)
michelangelo.forward(100)
michelangelo.right(90)
michelangelo.forward(100)
michelangelo.left(135)
michelangelo.forward(math.sqrt(2 * (50 ** 2)))
michelangelo.left(90)
michelangelo.forward(math.sqrt(2 * (50 ** 2)))
michelangelo.left(90)
michelangelo.forward(math.sqrt(2 * (100 ** 2)))
michelangelo.right(135)
michelangelo.forward(100)
michelangelo.right(135)
michelangelo.forward(math.sqrt(2 * (100 ** 2)))
michelangelo.right(135)
michelangelo.forward(100)


turtle.Screen().exitonclick()
