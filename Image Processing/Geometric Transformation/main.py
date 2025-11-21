import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

h, w = img.shape[:2]

# 1. Translation
tx, ty = 50, 80
T = np.float32([[1, 0, tx], [0, 1, ty]])
translated = cv2.warpAffine(img_rgb, T, (w, h))

# 2. Scaling
scaled = cv2.resize(img_rgb, None, fx=1.5, fy=1.5)

# 3. Rotation
angle = 45
R = cv2.getRotationMatrix2D((w//2, h//2), angle, 1)
rotated = cv2.warpAffine(img_rgb, R, (w, h))

# Display
plt.figure(figsize=(12,10))

plt.subplot(2,2,1); plt.imshow(img_rgb); plt.title("Original"); plt.axis('off')
plt.subplot(2,2,2); plt.imshow(translated); plt.title("Translated (50,80)"); plt.axis('off')
plt.subplot(2,2,3); plt.imshow(scaled); plt.title("Scaled x1.5"); plt.axis('off')
plt.subplot(2,2,4); plt.imshow(rotated); plt.title("Rotated 45°"); plt.axis('off')

plt.tight_layout()
plt.show()
