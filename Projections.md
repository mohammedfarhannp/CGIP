### **Projection in Computer Graphics**

Projection is the process of transforming a 3D world into a 2D representation for display on a viewport. It is a fundamental step in the graphics pipeline, as all rendering ultimately occurs on a 2D screen. There are two primary types of projection: Perspective and Parallel.

---

### **1. Perspective Projection**

**Definition:**
Perspective projection mimics the way the human eye perceives the real world. It creates a realistic view by making objects that are farther from the viewer appear smaller than those that are closer.

**Key Characteristics:**
*   **Realism:** It produces a natural and realistic image with a sense of depth and distance.
*   **Foreshortening:** The size of an object is inversely proportional to its distance from the center of projection (the viewer's eye or camera lens).
*   **Vanishing Point:** Lines that are parallel in the 3D world converge at a point (or points) on the horizon, known as the vanishing point. This is why train tracks appear to meet in the distance.

**Mathematical Principle:**
It uses a **viewing frustum** (a truncated pyramid) to define the visible volume. Objects are projected onto the view plane through lines emanating from a single point (the center of projection).

**Applications:**
*   Video games (FPS, RPGs, racing games)
*   Simulations and virtual reality
*   Architectural visualizations
*   Any application where visual realism is the primary goal.

---

### **2. Parallel Projection**

**Definition:**
Parallel projection projects 3D points onto a 2D view plane using parallel projectors. It preserves the relative proportions of objects, but does not provide a realistic representation of depth.

**Key Characteristics:**
*   **Constant Scaling:** The size of an object remains constant regardless of its distance from the viewer. There is no foreshortening.
*   **Preserved Parallelism:** Lines that are parallel in the 3D world remain parallel in the projected 2D view. There are no vanishing points.
*   **Measurement:** It maintains accurate dimensions and angles for faces aligned with the projection plane, making it suitable for technical drawings.

**Mathematical Principle:**
It uses a rectangular **view volume** (a parallelepiped). Projectors are parallel lines, typically perpendicular or oblique to the view plane.

**Types:**
*   **Orthographic Projection:** Projectors are perpendicular to the view plane (e.g., top, front, and side views in engineering drawings).
*   **Oblique Projection:** Projectors are not perpendicular to the view plane (e.g., Cavalier and Cabinet projections).

**Applications:**
*   Engineering and architectural blueprints (CAD)
*   Technical illustrations
*   2D and isometric video games (e.g., *SimCity*, *Civilization*)
*   Any application where accurate measurement and scale are critical.

---

### **Summary of Differences**

| Feature | Perspective Projection | Parallel Projection |
| :--- | :--- | :--- |
| **Projectors** | Converge at a single point (Center of Projection) | Are parallel to each other |
| **Realism** | High, provides a realistic view | Low, provides a schematic view |
| **Size/Distance** | Objects farther away appear smaller | Size remains constant regardless of distance |
| **Parallel Lines** | Converge at a vanishing point | Remain parallel |
| **Primary Use** | Realism, visualization, games | Measurement, technical drawings, blueprints |
