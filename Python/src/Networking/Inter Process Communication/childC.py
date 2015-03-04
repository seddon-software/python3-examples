############################################################
#
#    childC
#
############################################################

import sys
import wx


# pick up command line parameters
args = str(sys.argv[1:])

app = wx.PySimpleApp()
dial = wx.MessageDialog(None, 'Download completed', 'Info', wx.YES_NO)
result = dial.ShowModal()
sys.exit(result)

