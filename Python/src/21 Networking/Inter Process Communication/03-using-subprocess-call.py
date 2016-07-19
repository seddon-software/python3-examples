############################################################
#
#    creating processes
#
############################################################

import subprocess
import wx

args = ("python", "childC.py", "Monday", "Tuesday", "Wednesday")
retcode = subprocess.call(args)

if retcode == wx.ID_YES:
    result = "Yes button pressed"
elif retcode == wx.ID_NO:
    result = "No button pressed"
else:
    result = "Don't know what was pressed"

print result

1

