import FreeCAD as App
import Part
import math
from standards import RailSpecs, Tolerances, Materials

def build_part():
    # 1. Initialize Document
    doc = App.newDocument("Cantilever_Block")

    # 2. Create the Base Stock (2x1x1)
    # Using the 'box' primitive as our starting aluminum bar
    stock = doc.addObject("Part::Box", "Aluminum_Stock")
    stock.Length = 2.0
    stock.Width = 1.0
    stock.Height = 1.0

    # 3. Create the Large Bore (Ø0.715)
    # Positioning: Top of bore 0.250" below the rail
    bore_radius = 0.715 / 2
    # Rail bottom is at Z=1.0.
    # Center = 1.0 - 0.250 (meat) - radius
    bore_z = 1.0 - 0.250 - bore_radius

    bore = doc.addObject("Part::Cylinder", "Main_Bore")
    bore.Radius = bore_radius
    bore.Height = 1.0  # Depth of hole
    bore.Placement = App.Placement(App.Vector(0.66, 0.5, bore_z),
                                   App.Rotation(App.Vector(0, 1, 0), 90))

    # 4. Create the Bottom Tension Slot (0.500 wide)
    slot = doc.addObject("Part::Box", "Tension_Slot")
    slot.Length = 1.0
    slot.Width = 0.500
    slot.Height = 0.500  # Height enough to intersect bore
    slot.Placement = App.Placement(App.Vector(0.66, 0.25, 0), App.Rotation(0, 0, 0))

    # 5. The "Boolean" Logic (The Subtraction)
    # This tells the computer: Part = Stock - Bore - Slot
    cut1 = doc.addObject("Part::Cut", "Part_with_Bore")
    cut1.Base = stock
    cut1.Tool = bore

    final_part = doc.addObject("Part::Cut", "Final_Machined_Part")
    final_part.Base = cut1
    final_part.Tool = slot

    doc.recompute()
    print("Part Geometry Compiled Successfully using Business Standards.")

if __name__ == "__main__":
    build_part()
