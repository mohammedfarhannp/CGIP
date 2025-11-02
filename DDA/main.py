# Import Section 
from subprocess import check_output

import turtle

# Vars
Points_to_Plot = []

# Functions
def DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    
    k = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    
    x_inc = abs(dx) / k
    y_inc = abs(dy) / k
    
    x = x1
    y = y1
    
    tmp = [(int(x), int(y))]
    for i in range(k):
        x += x_inc
        y += y_inc
        tmp.append((int(x),int(y)))
    return tmp

# Main
Points_to_Plot = DDA(10, 10, 20, 40)

# Graphics
turtle.speed(0)
turtle.hideturtle()
turtle.pencolor("green")
turtle.penup()

for x, y in Points_to_Plot:
    turtle.goto(x,y)
    turtle.dot(2)

turtle.done()
