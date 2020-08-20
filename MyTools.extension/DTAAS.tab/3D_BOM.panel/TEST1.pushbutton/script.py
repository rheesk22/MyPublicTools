__title__ = "Solidify Bounding Box"
__doc__ = "Creates a Generic model Direct Shape"

from Autodesk.Revit.UI import *
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *

uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document

import clr
clr.AddReference("RevitAPI")

from System.Collections.Generic import List


selection = [doc.GetElement(elem_id) for elem_id in uidoc.Selection.GetElementIds()]
first_selected = selection[0]
solid_opt = SolidOptions(ElementId.InvalidElementId, ElementId.InvalidElementId)

bbox = first_selected.get_BoundingBox(None)
bottom_z_offset = 0.1
bbox.Min = XYZ(bbox.Min.X, bbox.Min.Y, bbox.Min.Z - bottom_z_offset)
b1 = XYZ(bbox.Min.X, bbox.Min.Y, bbox.Min.Z)
b2 = XYZ(bbox.Max.X, bbox.Min.Y, bbox.Min.Z)
b3 = XYZ(bbox.Max.X, bbox.Max.Y, bbox.Min.Z)
b4 = XYZ(bbox.Min.X, bbox.Max.Y, bbox.Min.Z)
bbox_height = bbox.Max.Z - bbox.Min.Z

lines = List[Curve]()
lines.Add(Line.CreateBound(b1, b2))
lines.Add(Line.CreateBound(b2, b3))
lines.Add(Line.CreateBound(b3, b4))
lines.Add(Line.CreateBound(b4, b1))
rectangle = [CurveLoop.Create(lines)]

extrusion = GeometryCreationUtilities.CreateExtrusionGeometry(List[CurveLoop](rectangle),XYZ.BasisZ,bbox_height,solid_opt)

category_id = ElementId(BuiltInCategory.OST_GenericModel)

from rpw import db, ui, doc, uidoc

with db.Transaction("solid_bbox_direct_shape") as tx:
    direct_shape = DirectShape.CreateElement( doc, category_id)
#   direct_shape = DirectShape.CreateElement( doc, category_id, "A", "B" )    
    direct_shape.SetShape([extrusion])

#TaskDialog.Show("done", str(category_id) )