# Import Section 
from subprocess import check_output

import turtle

# Get Points from C Code Compiled (For Faster Calculation)
Points_to_Plot = eval(
        check_output(
            ['.\gp.exe', '10', '12', '40', '30']
        ).decode()
    )

turtle.speed(0)
turtle.hideturtle()
turtle.pencolor("green")
turtle.penup()

for x, y in Points_to_Plot:
    turtle.goto(x,y)
    turtle.dot(2)
