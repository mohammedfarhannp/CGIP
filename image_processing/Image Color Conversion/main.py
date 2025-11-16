# Modules
import cv2

from matplotlib import pyplot as plt

# File Path
Image_Path = r"./image1.png"

# Image Read to 'Image' Variable
Image = cv2.imread(Image_Path)

# Check if Image is read successfully
if Image is None:
    print("Err: Image not Found!")
    exit()

# Convert the image into Gray Scale Image, Binary Image, RGB Image 
Gray_Scaled_Image = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)

_, Binary_Image = cv2.threshold(Gray_Scaled_Image, 127, 255, cv2.THRESH_BINARY)

RGB_Image = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)

Equalized_Image = cv2.equalizeHist(Gray_Scaled_Image)

# Plot All Images

## Set Size of Plot Window or Figure
plt.figure(figsize=(15, 12))

## Plot for RGB Image
plt.subplot(3, 3, 1)
plt.imshow(RGB_Image)
plt.title("RGB Image")
plt.axis("off")

## Plot for Gray Scale Image
plt.subplot(3, 3, 2)
plt.imshow(Gray_Scaled_Image, cmap="gray")
plt.title("Gray Scale Image")
plt.axis("off")

## Plot for Black and White Image
plt.subplot(3, 3, 3)
plt.imshow(Binary_Image, cmap="gray")
plt.title("Binary Image")
plt.axis("off")

## Plot for Histogram
plt.subplot(3, 3, 4)
plt.hist(Gray_Scaled_Image.ravel(), 256, [0, 256], color='blue')
plt.title("Histogram (Gray Image)")
plt.xlabel("Pixel Intensity")
plt.ylabel("Count")

# Plot for Equalized Image
plt.subplot(3, 3, 5)
plt.imshow(Equalized_Image, cmap="gray")
plt.title("Equalized Image")
plt.axis("off")

# Plot for Histogram of Equalized Image
plt.subplot(3, 3, 6)
plt.hist(Equalized_Image.ravel(), 256, [0, 256], color='green')
plt.title("Histogram (Equalized Image)")
plt.xlabel("Pixel Intensity")
plt.ylabel("Count")

## Display
plt.tight_layout()
plt.show()
