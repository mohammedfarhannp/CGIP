import numpy as np
import matplotlib.pyplot as plt

def transform(points, translation=(0, 0), scale=1, rotation=0):
    translate_matrix = np.array([[1, 0, translation[0]],
    [0, 1, translation[1]],
    [0, 0, 1]])
    scale_matrix = np.array([[scale, 0, 0],
    [0, scale, 0],
    [0, 0, 1]])
    theta = np.radians(rotation)
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta), np.cos(theta), 0],
    [0, 0, 1]])
    transformation_matrix = translate_matrix @ scale_matrix @ rotation_matrix
    points_homogeneous = np.hstack((points, np.ones((points.shape[0], 1))))
    transformed_points = points_homogeneous @ transformation_matrix.T
    return transformed_points[:, :2]
    
def plot_shape(points, title="2D Object"):
	plt.figure()
	plt.fill(*zip(*points), alpha=0.5)
	plt.xlim(-10, 10)
	plt.ylim(-10, 10)
	plt.axhline(0, color='black', lw=0.5, ls='--')
	plt.axvline(0, color='black', lw=0.5, ls='--')
	plt.title(title)
	plt.grid()
	plt.gca().set_aspect('equal', adjustable='box')
	plt.show()
triangle = np.array([[0, 0], [2, 0], [1, 2]])
plot_shape(triangle, title="Initial Triangle")
	
while True:
	print("\nChoose a transformation:")
	print("1: Translate")
	print("2: Scale")
	print("3: Rotate")
	print("4: Exit")
	choice = input("Enter your choice (1-4): ")
	if choice == '1':
		tx, ty = map(float, input("Enter translation (tx, ty) separated by space: ").split())
		transformed_triangle = transform(triangle, translation=(tx, ty))
		plot_shape(transformed_triangle, title="Translated Triangle")
	elif choice == '2':
		scale = float(input("Enter scaling factor (e.g., 2 for double size): "))
		transformed_triangle = transform(triangle, scale=scale)
		plot_shape(transformed_triangle, title="Scaled Triangle")
	elif choice == '3':
		rotation = float(input("Enter rotation angle in degrees (e.g., 45): "))
		transformed_triangle = transform(triangle, rotation=rotation)
		plot_shape(transformed_triangle, title="Rotated Triangle")
	elif choice == '4':
		print("Exiting.")
		break
	else:
		print("Invalid choice. Please select a valid option.")
