#Alejandro Alvarez
#6/7/2023
#Uses turtle module to allow user to create a shape and input its size

import turtle

side_length = float(input("Enter the length of a side: "))

fill_color = input("Enter the fill color: ")

shape_choice = input("Enter the shape to draw (triangle or square): ")

screen = turtle.Screen()

t = turtle.Turtle()

t.fillcolor(fill_color)

if shape_choice.lower() == "triangle":
    for _ in range(3):
        t.forward(side_length)
        t.left(120)
else:
    for _ in range(4):
        t.forward(side_length)
        t.left(90)

t.begin_fill()

t.end_fill()

t.hideturtle()


screen.exitonclick()

