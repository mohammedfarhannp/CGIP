import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image in grayscale
img = cv2.imread("image.jpg", 0)

# 1. Sobel Gradients
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# 2. Prewitt Gradient (manual kernels)
prewitt_x = cv2.filter2D(img, -1, np.array([[-1,0,1],[-1,0,1],[-1,0,1]]))
prewitt_y = cv2.filter2D(img, -1, np.array([[-1,-1,-1],[0,0,0],[1,1,1]]))
prewitt_combined = cv2.magnitude(prewitt_x.astype('float'), prewitt_y.astype('float'))

# 3. Laplacian (2nd derivative)
laplacian = cv2.Laplacian(img, cv2.CV_64F)

# Plot results
plt.figure(figsize=(12,8))
plt.subplot(2,3,1); plt.imshow(img, cmap='gray'); plt.title("Original"); plt.axis('off')
plt.subplot(2,3,2); plt.imshow(sobel_x, cmap='gray'); plt.title("Sobel X"); plt.axis('off')
plt.subplot(2,3,3); plt.imshow(sobel_y, cmap='gray'); plt.title("Sobel Y"); plt.axis('off')
plt.subplot(2,3,4); plt.imshow(sobel_combined, cmap='gray'); plt.title("Sobel Combined"); plt.axis('off')
plt.subplot(2,3,5); plt.imshow(prewitt_combined, cmap='gray'); plt.title("Prewitt Combined"); plt.axis('off')
plt.subplot(2,3,6); plt.imshow(laplacian, cmap='gray'); plt.title("Laplacian"); plt.axis('off')

plt.tight_layout()
plt.show()
