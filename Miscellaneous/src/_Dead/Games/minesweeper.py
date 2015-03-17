#!/usr/bin/python
"""
Mine Sweeper Game
"""
 
import optparse
import sys
import os
import re
import subprocess
import random
from PyQt4 import QtCore, QtGui
 
#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
 
class MyButton(QtGui.QPushButton):
  def __init__(self, parent=None):
    super(MyButton, self).__init__(parent)
  def contextMenuEvent(self, event):
    if self.text() == "?":
      self.setText("")
      self.setPalette(QtGui.QPalette(QtGui.QColor(222,222,222)))
      self.parent.marked -= 1
    else:
      self.setText("?")
      self.setPalette(QtGui.QPalette(QtGui.QColor(222,255,222)))
      self.parent.marked += 1
    self.parent.bombcount.setText("%d/40" %self.parent.marked)
 
#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
class MainWindow(QtGui.QWidget):
  """ Main Wrapper For GUI """
  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)
    setting = QtCore.QSettings()
    tmp = setting.value("position", QtCore.QPoint(0,0))
    self.move(tmp)
    layout = QtGui.QGridLayout()
    layout.setMargin(1)
    layout.setSpacing(1)
    self.button = []
    for rr in range(16):
      self.button.append( [] )
      for cc in range(16):
        self.button[rr].append( MyButton() )
        self.button[rr][cc].setFixedSize(20,20)
        self.button[rr][cc].row = r
        self.button[rr][cc].col = c
        self.button[rr][cc].parent = self
        self.button[rr][cc].revealed = False
        layout.addWidget( self.button[rr][cc], rr, cc)
        QtCore.QObject.connect(self.button[rr][cc], QtCore.SIGNAL("clicked()"), self.revealButtonWrapper )
    layouttop = QtGui.QHBoxLayout()
    layouttop.addWidget(QtGui.QLabel("BombCount"))
    self.bombcount = QtGui.QLabel("0/40")
    layouttop.addWidget(self.bombcount)
    self.timer = QtCore.QTimer()
    self.timelabel = QtGui.QLabel("0.0 secs")
    self.timelabel.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(0,255,0)")
    self.newGame()
    layouttop.addWidget(self.timelabel)
    newgameButton = QtGui.QPushButton("&NewGame")
    newgameButton.setEnabled(True)
    layouttop.addWidget(newgameButton)
    topscore = QtGui.QPushButton("Top&Score>>")
    topscore.setCheckable(True)
    layouttop.addWidget(topscore)
    self.scoreframe = QtGui.QFrame()
    self.scoreframe.setFrameStyle(QtGui.QFrame.StyledPanel|QtGui.QFrame.Sunken)
    scorelayout = QtGui.QVBoxLayout()
    scorelayout.addWidget(QtGui.QLabel("<b>Created By</b> <i>-Lionel Tan-</i> <br><br><br>" +
                                        "Email:<a href=#>yltan@altera.com</a><br>" +
                                        "Ext  :<a href=#>#6315</a> <br><br>" +
                                        "<a href=#>http://lionel.textmalaysia.com</a><br>") )
    self.scoreframe.setLayout(scorelayout)
    self.scoreframe.setVisible(False)
    mainLayout = QtGui.QGridLayout()
    mainLayout.addLayout(layouttop,0,0)
    mainLayout.addLayout(layout,1,0)
    mainLayout.addWidget(self.scoreframe,0,1,2,1)
    self.setLayout(mainLayout)
    self.layout().setSizeConstraint(QtGui.QLayout.SetFixedSize)
    QtCore.QObject.connect(newgameButton, QtCore.SIGNAL("clicked()"), self.newGame)
    QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.updateTime)
    QtCore.QObject.connect(topscore, QtCore.SIGNAL("clicked(bool)"), self.scoreframe.setVisible )
 
#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
  def newGame(self):
    self.populateBombs()
    self.marked = 0
    self.gamestarted = 0
    self.timer.stop()
    self.time = QtCore.QTime(0,0,0)
    self.timelabel.setText("0.0 secs")
    self.bombcount.setText("0/40")
 
    for rr in range(16):
      for cc in range(16):
        self.button[rr][cc].revealed  = False
        self.button[rr][cc].setText("")
        self.button[rr][cc].setFlat(False)
        self.button[rr][cc].setEnabled(True)
        self.button[rr][cc].setPalette(QtGui.QPalette(QtGui.QColor(222,222,222)))
#-----------------------------------------------------
  def disableAll(self):
    for rr in range(16):
      for cc in range(16):
        self.button[rr][cc].setEnabled(False)
        self.button[rr][cc].setFlat(True)
#-----------------------------------------------------
  def updateTime(self):
    tmp = round(self.time.elapsed() / 1000, 1)
    self.timelabel.setText( str(tmp) + " secs" )
#-----------------------------------------------------
  def closeEvent(self, event):
    setting = QtCore.QSettings()
    setting.setValue("position", self.pos())
#-----------------------------------------------------
  def revealButtonWrapper(self):
    if self.gamestarted == 0:
      self.time.start()
      self.timer.start(100)
      self.gamestarted = 1
    button = self.sender()
    self.revealButton( button )
#-----------------------------------------------------
  def revealButton(self, button):
    if button.bomb == True:
      txt = "X"
      color = QtGui.QColor(222,0,0)
      self.timer.stop()
      self.disableAll()
    else:
      txt = str( self.grepSurroundingBombCount(button.row, button.col) )
      color = QtGui.QColor(0,0,222)
    button.revealed = True
    button.setText(txt)
    button.setFlat(True)
    button.setEnabled(False)
    button.setPalette(QtGui.QPalette(color))
    if txt == "0":
      for rr,cc in self.grepSurroundingLocation(button.row, button.col):
        if self.button[rr][cc].revealed == False:
          self.revealButton( self.button[rr][cc] )
#-----------------------------------------------------
  def grepSurroundingBombCount(self, row, col):
    count = 0
    tmp = self.grepSurroundingLocation(row,col)
    for rr,cc in self.grepSurroundingLocation(row,col):
      count = count + 1 if self.button[rr][cc].bomb == True else count
    return(count)
#-----------------------------------------------------
  def grepSurroundingLocation(self, row, col):
    """
    Grep all the surrounding cells, and
    return back the location in a list of [row,col]
    format. e.g:-
    [ [row,col], [r,c], [r,c] ....]
    """
    ret = []
    ttop = row-1
    bot = row+1
    left = col-1
    right = col+1
    ### Getting top 3 cells if available
    if top > -1:
      ret.append( [ttop, col] )      # Top
    if bot < 16:
      ret.append( [bot, col] )      # Bot
    if left > -1:
      ret.append( [row, left] )     # Left
    if right < 16:
      ret.append( [row, right] )    # Right
    if top > -1 and left > -1:
      ret.append( [ttop, left] )   # UpperLeft
    if top > -1 and right < 16:
      ret.append( [ttop, right] )  # UpperRight
    if bot < 16 and left > -1:
      ret.append( [bot, left] )   # LowerLeft
    if bot < 16 and right < 16:
      ret.append( [bot, right] )  # LowerRight
    return(ret)
#-----------------------------------------------------
  def populateBombs(self):
    bomblocation = random.sample(range(256), 40)
    x = 0
    for row in range(16):
      for col in range(16):
        self.button[row][col].bomb = True if x in bomblocation else False
        x = x + 1
#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
 
### Main script
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
#__________________________________________________________________________
#__________________________________________________________________