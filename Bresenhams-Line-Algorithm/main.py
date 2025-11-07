import turtle

def Bresenhams_Line_Algo(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1
    
    err = dx - dy
    
    tmp = []
    
    while True:
        tmp.append((x1, y1))
        
        if (x1 == x2) and (y1 == y2):break
        
        e2 = 2 * err
        
        if(e2 > -dy):
            err -= dy
            x1 += sx
            
        if(e2 < dx):
            err += dx
            y1 += sy

    return tmp

pts = Bresenhams_Line_Algo(0, 9, -5, 100)

turtle.speed(0)
turtle.hideturtle()
turtle.pencolor("blue")
turtle.penup()

for x, y in pts:
    turtle.goto(x, y)
    turtle.dot(2)

turtle.done()