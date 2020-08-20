__title__ = "Display Name"
__doc__ = "Select multiple elements, display name"

from Autodesk.Revit.UI import *
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *

uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document

selectionIds = uidoc.Selection.PickObjects(ObjectType.Element)

for id in selectionIds:
    element = doc.GetElement(id)
    TaskDialog.Show("ThisIsElement", element.Name)