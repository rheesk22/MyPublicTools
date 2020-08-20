__title__ = "Test Tool"                                         
__doc__= "This tool creates a dialog window"                    

#__title__ : the text on revit program with icon
#__doc__ : appearing text when the mouse is placed on the icon
#korean words in script occur error

from Autodesk.Revit.UI import TaskDialog
import os

str1 = os.path.abspath("")

TaskDialog.Show("Hello World", str1 )
TaskDialog.Show("Hello World", "Thanks a lot! \nTESTING 1,2,3")
# popping the alarm window more than once is available