# Z - Buffer
Z-Buffer is a *Image Space Approach* implemented at screen coordination system.
The basic idea is to test z-depth of each surface to determine the surface closest to visible screen.

To override the closer polygon from the far polygon we use two buffers named *frame buffer* and *depth buffer*
- *frame buffer* is used to store intensity of color values of (x, y) positions.
- *depth buffer* is used to store depth value of (x, y) positions.
- Range of depth values is (0, 1)

# Algorithm
1. Set the buffer values,
   - Set depth buffer at (x, y) = 0
   - Set frame buffer at (x, y) = background color
2. Process each polygon at a time, for each (x, y) pixal position of polygon
   - Calculate z-depth
   - if z-depth > depth buffer
   - - compute surface color
     - Set depth buffer = z-depth
     - Set frame buffer = surface color

# Advantages
1. It is easy to implement
2. It reduces speed problem if implemented in hardware
3. It process one polygon at a time

# Disadvantages
1. It requires large memory
2. It is time-consuming process


