import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load grayscale image
img = cv2.imread("image.jpg", 0)

# Global Thresholding
ret1, th_global = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

# Intensity-based thresholding (multiple thresholds)
ret2, th_low = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)
ret3, th_high = cv2.threshold(img, 160, 255, cv2.THRESH_BINARY)

# Histogram
hist = cv2.calcHist([img], [0], None, [256], [0,256])

# Plotting
plt.figure(figsize=(12,8))

plt.subplot(2,3,1); plt.imshow(img, cmap='gray'); plt.title("Original"); plt.axis('off')
plt.subplot(2,3,2); plt.imshow(th_global, cmap='gray'); plt.title("Global Threshold 128"); plt.axis('off')
plt.subplot(2,3,3); plt.imshow(th_low, cmap='gray'); plt.title("Low Threshold (80)"); plt.axis('off')
plt.subplot(2,3,4); plt.imshow(th_high, cmap='gray'); plt.title("High Threshold (160)"); plt.axis('off')

plt.subplot(2,3,5)
plt.plot(hist)
plt.title("Histogram")
plt.xlabel("Intensity")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
