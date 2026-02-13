"""
OFFICIAL BUSINESS STANDARDS - HARDWARE V1.0
Property of: [Your Business Name]
Description: Verified dimensions for recurring features.
"""

class RailSpecs:
    # MIL-STD-1913 Picatinny Standard (Inches)
    WIDTH_TOP = 0.835
    WIDTH_NECK = 0.625
    GROOVE_WIDTH = 0.206
    GROOVE_DEPTH = 0.118
    RIDGE_SPACING = 0.394  # Center-to-center
    ANGLE = 45.0  # Degrees for the dovetail

class Tolerances:
    # Standard machining offsets for Ubuntu/FreeCAD engine
    PRESS_FIT = -0.001   # Tight
    SLIP_FIT = 0.002     # Smooth sliding
    CLEARANCE = 0.010    # Loose/General

class Materials:
    # Density and properties for weight calculations
    AL_6061 = {"density": 0.0975, "name": "6061-T6 Aluminum"}
    STEEL_4140 = {"density": 0.284, "name": "4140 Steel"}

def calculate_weight(volume, material):
    return volume * material["density"]
