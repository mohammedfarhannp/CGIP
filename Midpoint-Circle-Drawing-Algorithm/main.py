import turtle

pts = list()

def Arc(Radius, CX, CY):
    x = 0
    y =  Radius
    p0 = 1 - Radius
    
    Get_Points(CX, CY, x, y)
    
    while x < y:
        x += 1
        if p0 < 0:
            p0 += 2* x + 1
        
        else:
            y -= 1
            p0 += 2* (x - y) + 1
    
        Get_Points(CX, CY, x, y)

def Get_Points(CX, CY, X, Y):
    global pts
    pts.append(eval("({0}, {1})".format(CX + X, CY + Y)))
    pts.append(eval("({0}, {1})".format(CX + X, CY - Y)))
    pts.append(eval("({0}, {1})".format(CX - X, CY + Y)))
    pts.append(eval("({0}, {1})".format(CX - X, CY - Y)))
    
    pts.append(eval("({0}, {1})".format(CX + Y, CY + X)))
    pts.append(eval("({0}, {1})".format(CX + Y, CY - X)))
    pts.append(eval("({0}, {1})".format(CX - Y, CY + X)))
    pts.append(eval("({0}, {1})".format(CX - Y, CY - X)))
    

Arc(50, 100, 20)

turtle.speed(0)
turtle.hideturtle()
turtle.pencolor("red")
turtle.penup()

for x, y in pts:
    turtle.goto(x, y)
    turtle.dot(2)

turtle.done()
