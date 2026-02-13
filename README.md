# Hardware — Official Business Standards

Verified dimensions and tolerances for CNC machining and FreeCAD scripts.

## standards.py

- **RailSpecs** — MIL-STD-1913 Picatinny (inches)
- **Tolerances** — Press fit, slip fit, clearance
- **Materials** — AL 6061, 4140 Steel (density for weight calc)

Usage in FreeCAD scripts:
```python
from standards import RailSpecs, Tolerances, Materials, calculate_weight
```
