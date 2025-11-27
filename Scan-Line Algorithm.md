# Scan-Line Algorithm
Scan-Line Algorithm is an Image Space approach that processes the scene one scan line at a time.

# How it works 
1. Scan each horizontal line (one by one).
2. Find all polygons that intersect that scan line.
3. Calculate the intersections, creating a set of spans.
4. For each span, determine which polygon is closest by depth (z-values) and fill the pixel with the polygon's color.

# Advantage
1. Can be memory efficient as it doesn't require a full frame-depth buffer.

# Disadvantages
1. More complex to implement than Z-Buffer.
