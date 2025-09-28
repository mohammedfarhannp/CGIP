# Import Section 
from subprocess import check_output
from matplotlib import pyplot as plt

# Get Points from C Code Compiled (For Faster Calculation)
Points_to_Plot = eval(
        check_output(
            ['.\gp.exe', '10', '12', '40', '30']
        ).decode()
    )

# Split Recived Coordinates to X, Y Lists
x, y = [], []

for coord in Points_to_Plot:
    _0, _1 = coord
    x.append(_0)
    y.append(_1)

# Plot Coordinates
plt.plot(x, y, marker="o")

plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.title("DDA Line Drawing Algorithm")

plt.grid(True)
plt.show()