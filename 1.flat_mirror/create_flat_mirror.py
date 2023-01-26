# General modules

import Part
from FreeCAD import Base
import math
import numpy as np
import os

# Alias for active Document
doc = App.activeDocument()
# Alias for gui active Document
gui = Gui.activeDocument()

Mirror_Width = 1000.0 # mm
L = 1.0 # factor in length dimension
Mirror_Length = Mirror_Width * L
z_position_reference = 0.0


Trans_Abs_Width = Mirror_Width * 1.1
Trans_Abs_Length = Mirror_Length * 1.1
Trans_Abs_Height = 100 # 50 nm
Trans_Abs_z_position = z_position_reference + Trans_Abs_Height
# adds a Part Plane object type to the document and assigns the parameters
doc.addObject("Part::Plane","Trans_Abs")
doc.Trans_Abs.Length = Trans_Abs_Length
doc.Trans_Abs.Width = Trans_Abs_Width
doc.Trans_Abs.Placement=Base.Placement(Base.Vector(- Trans_Abs_Length / 2.0, - Trans_Abs_Width / 2.0, Trans_Abs_z_position),App.Rotation(App.Vector(0,0,1),0))
doc.Trans_Abs.Label='Trans_Abs(Trans_Abs)'
# to change the color of Trans_Abs
gui.getObject("Trans_Abs").ShapeColor = (1.0,1.0,1.0)


Mirror_Width = Mirror_Width
Mirror_Length = Mirror_Length

Mirror_z_position = z_position_reference  # mm

# adds a Part Box object type to the document and assigns the parameters
doc.addObject("Part::Plane","Flat_Mirror")
doc.Flat_Mirror.Length = Mirror_Length
doc.Flat_Mirror.Width = Mirror_Width
doc.Flat_Mirror.Placement=Base.Placement(Base.Vector(- Mirror_Length / 2.0, - Mirror_Width / 2.0, Mirror_z_position),App.Rotation(App.Vector(0,0,1),0))
doc.Flat_Mirror.Label='Flat_Mirror(Mirror)'
gui.getObject("Flat_Mirror").ShapeColor = (0.0,0.0,1.0)

FreeCAD.ActiveDocument.recompute()
Gui.activeDocument().activeView().viewAxonometric()
Gui.SendMsgToActiveView("ViewFit")



