############################################################
#
#    childA
#
############################################################

import sys
import wx

# pick up command line parameters
args = str(sys.argv[1:])

app = wx.PySimpleApp()
z = wx.MessageBox(args, 'This is the child')


