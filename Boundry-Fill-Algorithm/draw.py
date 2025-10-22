from subprocess import check_output
import turtle

Points = eval(check_output(['.\gp.exe', '0', '0', '50', '0', '50', '50', '0', '50']))

turtle.speed(0)
turtle.hideturtle()
turtle.pencolor("green")
turtle.penup()

for lines in Points.keys():
    for line in lines:
        for x,y in line:
            turtle.goto(x,y)
            turtle.dot(2)

for val in Points.values():
    for x, y in val:
        turtle.goto(x,y)
        turtle.dot(2)


turtle.done()