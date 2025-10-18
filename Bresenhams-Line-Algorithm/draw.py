from subprocess import check_output
import turtle

Points = eval(check_output(['.\gp.exe', '0', '0', '70', '70']))

turtle.speed(0)
turtle.hideturtle()
turtle.pencolor("blue")
turtle.penup()

for x, y in Points:
    turtle.goto(x, y)
    turtle.dot(2)

turtle.done()