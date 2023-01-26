# General modules

import Part, Draft
from FreeCAD import Base
import math
import numpy as np
import os

# Alias for active Document
doc = App.activeDocument()
# Alias for gui active Document
gui = Gui.activeDocument()

# Global dimensions
Si_Cell_width = 156750 * 1E-3
Si_Cell_length = Si_Cell_width
Si_Cell_height = 170 * 1E-3
N_interconnections = 5
Interconnection_width = 1000 * 1E-3
Interconnection_height = 200 * 1E-3
N_fingers = 120
Fingers_width = 35 * 1E-3
Fingers_height = 20 * 1E-3
Front_ARC_thicknes = 74 * 1E-6
Rear_R_thicknes = 10 * 1E-6


# define the Global BOX
box_Width = Si_Cell_width
box_Length = box_Width
#####
# add a Part Box object type for the rear material and assign the parameters
#####
Rear_R_Width = box_Width
Rear_R_Length = box_Width
Rear_R_Height = Rear_R_thicknes
Rear_R_z_position =  0.0
doc.addObject("Part::Box","Box_Rear_R")
doc.Box_Rear_R.Label='Box_Rear_R(Box_Rear_R_mat)'
doc.Box_Rear_R.Width = Rear_R_Width
doc.Box_Rear_R.Length = Rear_R_Length
doc.Box_Rear_R.Height = Rear_R_Height
doc.Box_Rear_R.Placement=Base.Placement(Base.Vector(0, 0, Rear_R_z_position),App.Rotation(App.Vector(0,0,1),0))
gui.getObject("Box_Rear_R").ShapeColor = (1.0, 1.0, 1.0)
gui.getObject("Box_Rear_R").Transparency = 80
#####
# add a Face object type for the specular/lambertian rear material and assign the parameters
#####
solid_selected = doc.Box_Rear_R
objs = solid_selected.Shape.Faces
selected_face = objs[5]
Rear_R_z_position =  0.0
doc.addObject("Part::Feature","Layer_Rear_R")
doc.Layer_Rear_R.Label='Layer_Rear_R(Layer_Rear_R_mat)'
doc.Layer_Rear_R.Shape = selected_face
doc.Box_Rear_R.Placement=Base.Placement(Base.Vector(0, 0, Rear_R_z_position),App.Rotation(App.Vector(0,0,1),0))
gui.getObject("Box_Rear_R").ShapeColor = (1.0, 1.0, 1.0)

#####
# add a Part Box object type to the document for the cell and assign the parameters
#####
Cell_Width = Si_Cell_width
Cell_Length = Si_Cell_width
Cell_Height = Si_Cell_height
Cell_z_position = Rear_R_Height + Rear_R_z_position
doc.addObject("Part::Box","Box_Cell")
doc.Box_Cell.Label='Glass_ARC(Box_Cell_mat)'
doc.Box_Cell.Width = Cell_Width
doc.Box_Cell.Length = Cell_Length
doc.Box_Cell.Height = Cell_Height
doc.Box_Cell.Placement=Base.Placement(Base.Vector(0, 0, Cell_z_position),App.Rotation(App.Vector(0,0,1),0))
gui.getObject("Box_Cell").ShapeColor = (0.0, 0.0, 1.0)
gui.getObject("Box_Cell").Transparency = 80
#####
# add a Part Box object type for the front ARC material and assign the parameters
#####
Front_ARC_Width = Si_Cell_width
Front_ARC_Length = Si_Cell_width
Front_ARC_Height = Front_ARC_thicknes
Front_ARC_z_position = Cell_Height + Cell_z_position
doc.addObject("Part::Box","Box_Front_ARC")
doc.Box_Front_ARC.Label='Box_Front_ARC(Box_Front_ARC_mat)'
doc.Box_Front_ARC.Width = Front_ARC_Width
doc.Box_Front_ARC.Length = Front_ARC_Length
doc.Box_Front_ARC.Height = Front_ARC_Height
doc.Box_Front_ARC.Placement=Base.Placement(Base.Vector(0, 0, Front_ARC_z_position),App.Rotation(App.Vector(0,0,1),0))
gui.getObject("Box_Front_ARC").ShapeColor = (0.5, 0.5, 0.5)
gui.getObject("Box_Front_ARC").Transparency = 0
#####
# add Part Box objects type to the document for the front connectors and assign the parameters
#####
Connector_Width = Interconnection_width
Connector_Length = Si_Cell_length
Connector_Height = Interconnection_height
Connector_z_position = Front_ARC_Height + Front_ARC_z_position
gap_connectors = Si_Cell_width / ( N_interconnections + 1)
for i in np.arange(1, N_interconnections + 1, 1):
    Label_actual = 'Box_Connector_{0}'.format(int(abs(i)))
    actual_connector = doc.addObject("Part::Box",Label_actual)
    actual_connector.Label = Label_actual.__add__("(Box_Connector_mat)")
    actual_connector.Width = Connector_Width
    actual_connector.Length = Connector_Length
    actual_connector.Height = Connector_Height
    y_position = i * gap_connectors - Connector_Width / 2
    actual_connector.Placement=Base.Placement(Base.Vector(0, y_position, Connector_z_position),App.Rotation(App.Vector(0,0,1),0))
    gui.getObject(Label_actual).ShapeColor = (0.5, 0.5, 0.5)
    gui.getObject(Label_actual).Transparency = 0

#####
# add Part Box objects type to the document for the front fingers and assign the parameters
#####
Finger_Width = Fingers_width
Finger_Length = Si_Cell_length
Finger_Height = Fingers_height
Finger_z_position = Connector_z_position
gap_fingers = Si_Cell_width / ( N_fingers + 1)
for i in np.arange(1, N_fingers + 1, 1):
    Label_actual = 'Box_Finger_{0}'.format(int(abs(i)))
    actual_finger = doc.addObject("Part::Box",Label_actual)
    actual_finger.Label = Label_actual.__add__("(Box_Finger_mat)")
    actual_finger.Width = Finger_Length
    actual_finger.Length = Finger_Width
    actual_finger.Height = Fingers_height
    x_position = i * gap_fingers - Finger_Width / 2
    actual_finger.Placement=Base.Placement(Base.Vector(x_position, 0, Finger_z_position),App.Rotation(App.Vector(0,0,1),0))
    gui.getObject(Label_actual).ShapeColor = (0.5, 0.5, 0.5)
    gui.getObject(Label_actual).Transparency = 0


#####
# add  a face object to the document for calculating the reflectance of the cell
#####

trans_abs_z = Connector_z_position + Connector_Height + 100 * 1E-6
solid_selected = doc.Box_Rear_R
objs = solid_selected.Shape.Faces
selected_face = objs[5]
actual_face = doc.addObject('Part::Feature','Trans_Abs')
actual_face.Label = 'Trans_Abs(Trans_Abs)'
actual_face.Shape = selected_face	
actual_face.Placement=Base.Placement(Base.Vector(0, 0, trans_abs_z),App.Rotation(App.Vector(0,0,1),0))

#####
# add  a face objects to the document in order to close the cell with ideal mirrors
#####


A = doc.Box_Rear_R.Shape.BoundBox
B = doc.Box_Cell.Shape.BoundBox
C = doc.Box_Front_ARC.Shape.BoundBox
D = doc.Trans_Abs.Shape.BoundBox

A.add(B)
A.add(C)
A.add(D)

A_XMin = A.XMin
A_XMax = A.XMax
A_YMin = A.YMin
A_YMax = A.YMax
A_ZMin = A.ZMin
A_ZMax = A.ZMax

A_XLength = A.XLength
A_YLength = A.YLength
A_ZLength = A.ZLength

mirror_1 = Part.makePlane(A_ZLength, A_XLength, Base.Vector(A_XMin,A_YMin,A_ZMin), Base.Vector(0,1,0))
mirror_2 = mirror_1.copy()
mirror_2.translate(Base.Vector(0,A_YMax,0))
mirror_3 = mirror_1.copy()
mirror_3.rotate(App.Vector(0,0,0),App.Vector(0,0,1),90)
mirror_3 = Part.makePlane(A_ZLength, A_XLength, Base.Vector(A_XMax,A_YMax,A_ZMin), Base.Vector(1,0,0))
mirror_4 = mirror_3.copy()
mirror_4.translate(Base.Vector(-A_XMax,0,0))

doc.recompute()

doc.addObject("Part::Feature","Mirror_1")
doc.Mirror_1.Shape = mirror_1
doc.Mirror_1.Label='Mirror_1(Mirror)'
gui.getObject("Mirror_1").ShapeColor = (1.0,1.0,1.0)


doc.addObject("Part::Feature","Mirror_2")
doc.Mirror_2.Shape = mirror_2
doc.Mirror_2.Label='Mirror_2(Mirror)'
gui.getObject("Mirror_2").ShapeColor = (1.0,1.0,1.0)

doc.addObject("Part::Feature","Mirror_3")
doc.Mirror_3.Shape = mirror_3
doc.Mirror_3.Label='Mirror_3(Mirror)'
gui.getObject("Mirror_3").ShapeColor = (1.0,1.0,1.0)

doc.addObject("Part::Feature","Mirror_4")
doc.Mirror_4.Shape = mirror_4
doc.Mirror_4.Label='Mirror_4(Mirror)'
gui.getObject("Mirror_4").ShapeColor = (1.0,1.0,1.0)

# for better visualization
Gui.activeDocument().activeView().viewAxonometric()
Gui.SendMsgToActiveView("ViewFit")
Gui.ActiveDocument.ActiveView.setAxisCross(True)

# doc.removeObject('Box_Rear_R') # we can remove this volume material

# to recalculate the whole document
doc.recompute()