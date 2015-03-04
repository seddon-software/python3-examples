############################################################
#
#    childB
#
############################################################

import sys
import wx


# pick up parameters from stdin
print "Enter parameters: "
sys.stdout.flush()
data = "Params:" + sys.stdin.readline()[:-1]

app = wx.PySimpleApp()
wx.MessageBox(data, 'This is the child')
