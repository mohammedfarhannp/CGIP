# Cohen-Sutherland Line Clipping Algorithm Implementation
import turtle

# Define region codes
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

# Define the clipping window boundaries
x_min, y_min = 10, 10
x_max, y_max = 200, 150

# Function to compute the region code for a point (x, y)
def compute_code(x, y):
    code = INSIDE
    if x < x_min:
        code |= LEFT

    elif x > x_max:
        code |= RIGHT

    if y < y_min:
        code |= BOTTOM

    elif y > y_max:
        code |= TOP

    return code

def cohen_sutherland_clip(x1, y1, x2, y2):
    pt1_code = compute_code(x1, y1)
    pt2_code = compute_code(x2, y2)
    accept = False

    while True:
        # Both points inside the clipping window
        if pt1_code == 0 and pt2_code == 0:
            accept = True
            break

        # Both points outside the clipping window
        elif (pt1_code & pt2_code) != 0:
            break

        else:
            code_out = pt1_code if pt1_code != 0 else pt2_code

            if code_out & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min

            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max

            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

            if code_out == pt1_code:
                x1, y1 = x, y
                pt1_code = compute_code(x1, y1)

            else:
                x2, y2 = x, y
                pt2_code = compute_code(x2, y2)
            
    if accept:
        print(f"Line Clipped to: A({x1}, {y1}), B({x2}, {y2})")
        return (x1, y1, x2, y2)
    else:
        print("Line rejected")
        return None

# Set up turtle window
turtle.setworldcoordinates(0, 0, 300, 200)
turtle.speed(0)

# Draw clipping window
turtle.penup()
turtle.goto(x_min, y_min)
turtle.pendown()
for _ in range(2):
    turtle.forward(x_max - x_min)
    turtle.left(90)
    turtle.forward(y_max - y_min)
    turtle.left(90)

# Original line (in red)
turtle.pencolor("red")
turtle.penup()
turtle.goto(5, 5)
turtle.pendown()
turtle.goto(250, 180)

# Clipped line (in green)
result = cohen_sutherland_clip(5, 5, 250, 180)
if result:
    x1, y1, x2, y2 = result
    turtle.pencolor("green")
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

turtle.done()
