# 🧠 **Module 3: Introduction to Image Processing**

---

## 📘 1. Introduction to Image Processing

**Definition:**
Image Processing is a method to perform operations on an image to enhance it or extract useful information.

**Objective:**

* Improve image quality (enhancement, restoration)
* Extract meaningful data (analysis, recognition)
* Transform image formats (compression, encoding)

**Applications:**

* Medical Imaging (CT, MRI, X-rays)
* Satellite Imaging and Remote Sensing
* Industrial Automation and Quality Inspection
* Face and Object Recognition
* Surveillance and Security Systems
* Document Scanning and OCR
* Robotics and Autonomous Vehicles

---

## 🖼️ 2. Image as 2D Data

An **image** can be represented as a **2D function**:
$$f(x, y)$$
where

* (x, y) → spatial coordinates
* (f(x, y)) → intensity (gray level) at that point.

Digital images are **samples** of this function at discrete points.

---

## 🌈 3. Image Representation

### (a) **Gray Scale Image**

* Each pixel represents an intensity level (brightness).
* Usually 8-bit → 256 levels (0 = black, 255 = white).

### (b) **Binary Image**

* Each pixel has only two values:
  0 → Black, 1 → White.
* Used in shape detection, thresholding, etc.

### (c) **Color Image**

* Represented using three components: Red, Green, Blue (RGB).
* Each pixel → (R, G, B) triple.
* 24-bit color = 8 bits per channel → 16.7 million colors.

---

## 🧩 4. Fundamental Steps in Image Processing

1. **Image Acquisition**

   * Capturing image through a camera/scanner.

2. **Preprocessing**

   * Noise removal, contrast adjustment, filtering.

3. **Segmentation**

   * Partitioning image into regions/objects.

4. **Representation & Description**

   * Converting image data into suitable form for analysis.

5. **Feature Extraction**

   * Deriving key characteristics (edges, shapes, textures).

6. **Recognition & Interpretation**

   * Assigning labels or meanings to objects.

7. **Compression & Storage**

   * Reducing data size for efficient storage/transmission.

---

## ⚙️ 5. Components of Image Processing System

1. **Image Sensors** – Cameras, scanners, sensors.
2. **Image Digitizer** – Converts analog signal → digital image.
3. **Computer/Processor** – Performs computations.
4. **Software** – Algorithms for processing and analysis.
5. **Mass Storage** – For saving images and data.
6. **Display** – Monitors or output devices.
7. **Hard Copy Devices** – Printers, plotters, etc.
8. **Network Interface** – For data transfer and communication.

---

## 🧭 6. Coordinate Conventions

* The **origin (0,0)** is at the **top-left corner** of the image.
* The **x-axis** increases to the **right**.
* The **y-axis** increases **downward**.
* Pixel coordinates are integer values:
  ( (x, y) = (column, row) )

---

## 🎚️ 7. Sampling and Quantization

**Sampling:**
Converts a continuous image into a grid of discrete pixels — defines the image’s **spatial resolution**.

**Quantization:**
Assigns a finite number of intensity values to pixels — determines **gray-level resolution**.

Together, they turn analog images into digital form.

---

## 🔍 8. Spatial and Gray-Level Resolution

**Spatial Resolution:**
Refers to the number of pixels used to represent the image — higher means finer details.

**Gray-Level Resolution:**
Refers to the number of intensity levels per pixel — higher gives smoother intensity transitions.

---

## 🔗 9. Basic Relationships Between Pixels

### (a) **Neighborhood**

* The group of pixels surrounding a given pixel.

**Types:**

1. **4-neighbors (N4):** Up, Down, Left, Right.
2. **Diagonal neighbors (ND):** 4 diagonals.
3. **8-neighbors (N8):** Combination of both.

### (b) **Adjacency**

* Two pixels are **adjacent** if they share a boundary and satisfy intensity conditions.

### (c) **Connectivity**

* Describes how pixels are connected to form regions:

  * **4-connectivity**
  * **8-connectivity**
  * **m-connectivity** (mixed)

---

## 🔧 10. Fundamentals of Spatial Domain – Convolution Operation

**Spatial Domain:**

* Image operations performed directly on pixel values.

**Convolution:**

* A mathematical operation combining two functions (image and filter/kernel) to produce a modified image.

**Formula:**

$$g(x, y) = \sum_m \sum_n f(x - m, y - n) \cdot h(m, n)$$

where

* (f(x,y)) → input image
* (h(m,n)) → filter (mask/kernel)
* (g(x,y)) → output image

**Uses of Convolution:**

* Blurring / Smoothing
* Edge Detection
* Sharpening
* Noise Reduction

---

## 🧾 Summary Table

| Concept               | Description           | Example                |
| --------------------- | --------------------- | ---------------------- |
| Image                 | 2D intensity function | f(x, y)                |
| Sampling              | Pixel selection       | 512×512 pixels         |
| Quantization          | Intensity levels      | 8-bit = 256 levels     |
| Spatial Resolution    | Pixel density         | 1080×720               |
| Gray-Level Resolution | Intensity depth       | 8-bit grayscale        |
| Neighborhood          | Surrounding pixels    | N4, N8                 |
| Connectivity          | Linkage of pixels     | 4-, 8-, m-connectivity |
| Convolution           | Spatial filtering     | Edge detection mask    |

---
