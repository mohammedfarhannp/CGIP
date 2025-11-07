# -------------------------------
# 4-Connected Boundary Fill Algorithm
# -------------------------------
# Note: 8-connected version may differ in behavior.
#
# Example illustration:
# 1 = Boundary pixel
# 2 = Seed/fill pixel
#
# 1 0 0 0 0     | 1 0 2 2 2     | 1 2 2 2 2
# 0 1 0 2 0     | 0 1 2 2 2     | 0 1 2 2 2
# 0 0 1 0 0  -->| 0 0 1 2 2  -->| 0 2 1 2 2
# 0 0 0 1 0     | 0 0 0 1 0     | 0 0 2 1 2
# 0 0 0 0 1     | 0 0 0 0 1     | 0 0 0 0 1
#
# The fill expands from the seed point until it reaches boundary pixels.

# -------------------------------
# Import modules
# -------------------------------
import turtle

# -------------------------------
# Global variables
# -------------------------------
STEP = 1
pts = list()

# -------------------------------
# Boundary Fill Algorithm function
# -------------------------------
def BFA(x, y, pen, boundary):
    global pts
    
    stack = [(x, y)]
    
    while stack:
        x, y = stack.pop()
        
        if (x, y) in boundary or (x, y) in pts:
            continue
        
        pts.append((x, y))
        pen.goto(x, y)
        pen.dot(2)
        
        # Add 4-connected neighbors around the current pixel
        neighbors = [(x + STEP, y), (x - STEP, y), (x, y + STEP), (x, y - STEP)]
        for nx, ny in neighbors:
            if (nx, ny) not in pts and (nx, ny) not in boundary:
                stack.insert(0, (nx, ny))

# -------------------------------
# Bresenham's Line Algorithm for polygon drawing
# -------------------------------
def Bresenhams_Line(x1, y1, x2, y2):
    Line = list()
    
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    
    err = dx - dy
    
    while True:
        Line.append((x1, y1))
        
        if (x1 == x2 and y1 == y2): break
        
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
            
        if e2 < dx:
            err += dx
            y1 += sy

    return Line

# -------------------------------
# Turtle pen setup
# -------------------------------
Pen = turtle.Turtle()
Pen.speed(0)
Pen.hideturtle()
Pen.pencolor("orange")
Pen.penup()

# -------------------------------
# Draw polygon using Bresenham's lines
# -------------------------------
Polygon = Bresenhams_Line(0, 0, -20, 30) + Bresenhams_Line(-20, 30, 10, 60) + Bresenhams_Line(10, 60, 40, 30) + Bresenhams_Line(40, 30, 20, 0) + Bresenhams_Line(20, 0, 0, 0)
Seed_Point = (5, 5)

for x, y in Polygon:
    Pen.goto(x, y)
    Pen.dot(2)

# -------------------------------
# Apply boundary fill
# -------------------------------
BFA(Seed_Point[0], Seed_Point[1], Pen, Polygon)

# -------------------------------
# Finish
# -------------------------------
turtle.done()
