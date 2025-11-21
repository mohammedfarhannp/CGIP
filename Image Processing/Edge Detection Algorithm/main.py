# Import Modules
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading of Image
Image = cv2.imread("image1.jpg")

# -- Sobel Operator --
sobelx = cv2.Sobel(Image, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(Image, cv2.CV_64F, 0, 1, ksize=3)

sobel_edges = np.sqrt(sobelx ** 2, sobely ** 2)
sobel_edges = np.uint8(np.clip(sobel_edges, 0, 255))

# -- Prewitt Operator (manual convolution) --
prewitt_kx = np.array([[-1, 0, 1],
                       [-1, 0, 1],
                       [-1, 0, 1]], dtype=np.float32)

prewitt_ky = np.array([[-1, -1, -1],
                       [ 0,  0,  0],
                       [ 1,  1,  1]], dtype=np.float32)

prewittx = cv2.filter2D(Image, -1, prewitt_kx)
prewitty = cv2.filter2D(Image, -1, prewitt_ky)

prewitt_edges = np.sqrt(prewittx ** 2 + prewitty ** 2)
prewitt_edges = np.uint8(np.clip(prewitt_edges, 0, 255))

# Display Results
plt.figure(figsize=(14, 6))

plt.subplot(1, 3, 1)
plt.title("Original")
plt.imshow(Image, cmap="gray")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Sobel Edges")
plt.imshow(sobel_edges, cmap="gray")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Prewitt Edges")
plt.imshow(prewitt_edges, cmap="gray")
plt.axis('off')

plt.show()