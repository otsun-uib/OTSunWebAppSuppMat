import Part
from FreeCAD import Base
import numpy as np
import os
import pathlib as Path
cwd = Path.Path().resolve()
import sys


# Alias for active Document
doc = App.activeDocument()
# Alias for gui active Document
gui = Gui.activeDocument()

# heliostats dimension
width_heliostat = 10 * 1000
length_heliostat = 10 * 1000
my_file = '/heliostats_field.txt'
data_heliostats = np.loadtxt(my_file, usecols=(0, 1, 2, 3, 4))
label_heliostat = data_heliostats[:, 0]
X_heliostat = data_heliostats[:, 1] * 1000
Y_heliostat = data_heliostats[:, 2] * 1000
Z_heliostat = data_heliostats[:, 3] * 1000
Focus_heliostat = data_heliostats[:, 4] * 1000

X_heliostat_dict = dict(zip(label_heliostat,X_heliostat))
Y_heliostat_dict = dict(zip(label_heliostat,Y_heliostat))
Z_heliostat_dict = dict(zip(label_heliostat,Z_heliostat))
Focus_heliostat_dict = dict(zip(label_heliostat,Focus_heliostat))

number_heliostats = len(label_heliostat) # number of heliostats
 
for i in label_heliostat:

	# labels for the optical and mechanical objects
	Label_Sphere_i = 'Sphere_{0}'.format(int(abs(i)))
	Label_Heliostat_i = 'Heliostat_{0}'.format(int(abs(i)))
	Label_Normal_i = 'Normal_{0}'.format(int(abs(i)))
	Label_Axis1_i = 'Axis_1_{0}'.format(int(abs(i)))
	Label_Axis2_i = 'Axis_2_{0}'.format(int(abs(i)))
	Label_Target = 'Target_{0}'.format(int(abs(i)))

    # creating the sphere for the actual mirror shape
	radius = 2 * Focus_heliostat_dict[i]
	Sphere = doc.addObject("Part::Sphere",Label_Sphere_i)
	doc.ActiveObject.Radius = radius

	# creating the box to cut the sphere, this is the mirror shape
	Width = width_heliostat
	Length = length_heliostat
	Height = width_heliostat 
	box = doc.addObject("Part::Box","box")
	box.Width = Width
	box.Length = Length
	box.Height = Height
	box.Placement=Base.Placement(App.Vector(-Length/2,-Width / 2 + radius,-Height/2),App.Rotation(App.Vector(0,0,1),0))
	gui.getObject("box").ShapeColor = (0.0, 0.0, 1.0)
	gui.getObject("box").Transparency = 80

	# creating the mirror shape with common tool
	doc.addObject("Part::MultiCommon","common")
	doc.common.Shapes = [doc.box,doc.getObject(Label_Sphere_i)]
	FreeCAD.ActiveDocument.recompute()

	# this is the spherical face for the heliostat well positioned
	face = doc.common.Shape.Faces[2]
	CoMFace = face.CenterOfMass
	face.translate(-CoMFace)
	vector = App.Vector(X_heliostat_dict[i], Y_heliostat_dict[i], Z_heliostat_dict[i])
	face.translate(vector)
	
    # creating the Heliostat part and its axis	
	doc.addObject("Part::Feature",Label_Heliostat_i)
	doc.ActiveObject.Label = Label_Heliostat_i.__add__("(Mirror,") \
										.__add__(Label_Axis1_i).__add__(",") \
										.__add__(Label_Axis2_i).__add__(",") \
										.__add__(Label_Normal_i).__add__(",") \
										.__add__("Target_point").__add__(")")
	doc.ActiveObject.Shape=face
	gui.ActiveObject.ShapeColor = (0.0,0.0,1.0)
	actual_Line = doc.addObject("Part::Line",Label_Normal_i)
	actual_Line.X1 = X_heliostat_dict[i]
	actual_Line.Y1 = Y_heliostat_dict[i]
	actual_Line.Z1 = Z_heliostat_dict[i]
	actual_Line.X2 = X_heliostat_dict[i]
	actual_Line.Y2 = Y_heliostat_dict[i] - 1000
	actual_Line.Z2 = Z_heliostat_dict[i]
	actual_Line = doc.addObject("Part::Line",Label_Axis1_i)
	actual_Line.X1 = X_heliostat_dict[i]
	actual_Line.Y1 = Y_heliostat_dict[i]
	actual_Line.Z1 = Z_heliostat_dict[i]
	actual_Line.X2 = X_heliostat_dict[i]
	actual_Line.Y2 = Y_heliostat_dict[i] 
	actual_Line.Z2 = Z_heliostat_dict[i] - 1000
	actual_Line = doc.addObject("Part::Line",Label_Axis2_i)
	actual_Line.X1 = X_heliostat_dict[i]
	actual_Line.Y1 = Y_heliostat_dict[i]
	actual_Line.Z1 = Z_heliostat_dict[i]
	actual_Line.X2 = X_heliostat_dict[i] - 1000
	actual_Line.Y2 = Y_heliostat_dict[i] 
	actual_Line.Z2 = Z_heliostat_dict[i]

	doc.removeObject(Label_Sphere_i)
	doc.removeObject('common')
	doc.removeObject('box')

# Target, that is a point on the focus
target_tilt = 90
target_height = 62000
target_width = 6000
taraget_length = 8000
v = Base.Vector(0, 0, target_height)
point = Part.Vertex(v)
obj = doc.addObject("Part::Feature", "Target_point")
obj.Label = f"Target_point"
obj.Shape = point
gui.getObject("Target_point").PointSize = 5.00

doc.addObject("Part::Plane","Receiver")
doc.Receiver.Length = taraget_length #x 
doc.Receiver.Width = target_width #y 
doc.Receiver.Label='Receiver(Abs)'
doc.Receiver.Placement=Base.Placement(Base.Vector(-taraget_length/2, -target_width/2, target_height),App.Rotation(0,0,target_tilt), App.Vector(0,target_width/2,0))
gui.getObject("Receiver").ShapeColor = (1.0,0.0,0.0)

doc.addObject("Part::Box","Tower")
doc.Tower.Label='Tower(Opaque)'
doc.Tower.Width = target_width
doc.Tower.Length = taraget_length
doc.Tower.Height = target_height
doc.Tower.Placement=Base.Placement(Base.Vector(-taraget_length/2, -taraget_length * 1.2, 0),App.Rotation(App.Vector(0,0,1),0))
gui.getObject("Tower").ShapeColor = (1.0, 0.5, 0.5)

# for better visualization
Gui.activeDocument().activeView().viewAxonometric()
Gui.SendMsgToActiveView("ViewFit")
Gui.ActiveDocument.ActiveView.setAxisCross(True)
# to recalculate the whole document
doc.recompute()

