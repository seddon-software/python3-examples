import sys
from PyQt4 import Qt, QtGui, QtCore

class Computer:
    # used to determine strategy
    def __init__(self, buttons):
        self.buttons = buttons
    
    def getResponse(self):
        for button in self.buttons:
            if button.text() == Qt.QString(""):
                button.setText("O")
                break

class MyButton(QtGui.QPushButton):
    def __init__(self, text, parent):
        super(QtGui.QPushButton, self).__init__(text, parent)
        self.setFixedHeight(50)
        self.setFixedWidth(50)
        self.setFont(QtGui.QFont('SansSerif', 20))
             
    def onClick(self):
        self.setText("X")
        self.parent().computer.getResponse()

class MainLayout(QtGui.QWidget):
    
    def __init__(self):
        super(MainLayout, self).__init__()        
        self.initUI()
            
    def initUI(self):
        self.setWindowTitle('tic-tac-toe')
        self.setWindowIcon(QtGui.QIcon('web.png'))
        
        gridLayout = QtGui.QGridLayout()
        gridLayout.setContentsMargins(25, 25, 25, 25)
        gridLayout.setSpacing(0)
        self.setLayout(gridLayout)
        
        # create 9 buttons
        buttons = []
        for row in (0,1,2):
            for col in (0,1,2):
                buttons.append(MyButton('', self))
                b = buttons[-1]
                b.row = row
                b.col = col
                Qt.QObject.connect(b, Qt.SIGNAL("clicked()"), b.onClick)
                gridLayout.addWidget(b, row, col)

        # keep track of buttons with computer
        self.computer = Computer(buttons)
        self.show()
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = MainLayout()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
