#Alejando Alvarez
#6/15/2023
#P5, draws 5 sqaures using turtle module

import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

size = 100

for i in range(5):
    drawSquare(alex, size)
    alex.penup()
    alex.backward(20)  
    alex.right(90)
    alex.forward(20) 
    alex.left(90) 
    alex.pendown()
    size += 40

wn.exitonclick()



