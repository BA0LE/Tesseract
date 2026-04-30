# Tesseract 4D Simulator

A simple real-time visualization of a **4D hypercube (Tesseract)** using Python, NumPy, and Pygame.

This project demonstrates how to:

* Rotate objects in 4D space
* Project 4D → 3D → 2D
* Render dynamic wireframes with perspective

---

## Features

* 6-axis rotation in 4D:

  * XY, XZ, YZ (3D-like)
  * XW, YW, ZW (true 4D rotations)
* Perspective projection (4D → 3D → 2D)
* Real-time rendering with depth-based brightness
* Interactive controls

---

## Demo Controls

| Key   | Action                        |
| ----- | ----------------------------- |
| W / S | Rotate XZ                     |
| A / D | Rotate XY                     |
| Q / E | Rotate YZ                     |
| R / T | Rotate XW                     |
| F / G | Rotate YW                     |
| V / B | Rotate ZW                     |
| [ / ] | Adjust W perspective distance |
| ESC   | Exit                          |

---

## How It Works

### 1. Tesseract Generation

The hypercube is generated using all combinations of:
(-1, 1) in 4 dimensions → 16 vertices.

Edges are created between points that differ by exactly one coordinate.

### 2. 4D Rotation

Rotation matrices are applied across:

* XY, XZ, YZ (classic 3D)
* XW, YW, ZW (4th dimension)

### 3. Projection Pipeline

4D point → 3D:

```
d = 1 / (w_dist - w)
(x, y, z) = (x, y, z) * d
```

3D point → 2D:

```
x_screen = x * fov / z
y_screen = y * fov / z
```

---

## Installation

```bash
pip install pygame numpy
```

Run:

```bash
python main.py
```

---

## Project Structure

```
.
├── main.py          # Main loop & rendering
├── Caculator.py     # Math & projection functions
```

---

## Requirements

* Python 3.8+
* pygame
* numpy

---

## Future Improvements

* Camera movement in 3D space
* Face rendering (not only edges)
* Hidden surface removal
* Shading & lighting models
* GPU acceleration (OpenGL)

---

## Author

Built for learning advanced math, graphics, and higher-dimensional visualization.

---

## License

MIT License

