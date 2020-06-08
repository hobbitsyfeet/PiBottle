import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication)
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys 

class Window(QWidget): 
    def __init__(self):
        super().__init__()

        self.initUI()
        

    def initUI(self):
        self.showMaximized()

        self.can_count = -1
        self.plastic_count = -1
        self.plastic2_count = -1
        self.glass_count = -1
        self.milk_count = -1
  
        self.can_label = QLabel()
        self.plastic_label = QLabel()
        self.plastic2_label = QLabel()
        self.glass_label = QLabel()
        self.milk_label = QLabel()
        

        # setting geometry 
        self.grid = QGridLayout()
        self.grid.setSpacing(10) 
  
        # calling method
        self.can, self.can_label = self.UI_Button("Aluminum Can", "images/can.png", self.clickcan)
        self.plastic, self.plastic_label = self.UI_Button("Plastic", "images/plastic.png", self.clickplastic) 
        self.plastic2, self.plastic2_label =  self.UI_Button("Plastic 2L", "images/plastic2L.png",self.clickplastic2)
        self.glass, self.glass_label = self.UI_Button("Glass", "images/glass.png", self.clickglass)
        self.milk, self.milk_label = self.UI_Button("Milk", "images/milk.png", self.clickmilk)
        
        self.grid.addWidget(self.can,0,0)
        self.grid.addWidget(self.can_label,1,0)

        self.grid.addWidget(self.plastic,0,1)
        self.grid.addWidget(self.plastic_label,1,1)

        self.grid.addWidget(self.plastic2,0,2)
        self.grid.addWidget(self.plastic2_label,1,2)

        self.grid.addWidget(self.glass,0,3)
        self.grid.addWidget(self.glass_label,1,3)
        
        self.grid.addWidget(self.milk,0,4)
        self.grid.addWidget(self.milk_label,1,4)

        self.setLayout(self.grid)

        # showing all the widgets
        self.setWindowTitle("PiBottle")  
        self.show()


    def clickcan(self):
        self.can_count += 1 
        self.update()
        self.can_label.setText(str(self.can_count))
        return self.can_count

    def clickplastic(self):
        self.plastic_count += 1 
        self.update()
        self.plastic_label.setText(str(self.plastic_count))
        return self.plastic_count

    def clickplastic2(self):
        self.plastic2_count += 1 
        self.update()
        self.plastic2_label.setText(str(self.plastic2_count))
        return self.plastic2_count

    def clickglass(self):
        self.glass_count += 1 
        self.update()
        self.glass_label.setText(str(self.glass_count))
        return self.glass_count

    def clickmilk(self):
        self.milk_count += 1 
        self.update()
        self.milk_label.setText(str(self.milk_count))
        return self.milk_count

  
    # method for widgets 
    def UI_Button(self,name, image, func): 
        count = func()
        # creating a push button 
        button = QPushButton(self)

        #Set Icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(image), QtGui.QIcon.Selected, QtGui.QIcon.On)
        button.setIcon(icon)
        button.setIconSize(QSize(300, 300))

        text = QLabel(str("0"))
        text.setFont(QtGui.QFont('SansSerif', 16))
        text.setAlignment(Qt.AlignCenter)
        button.clicked.connect(func)

        return button, text


if __name__ == "__main__":
    # # create pyqt5 app 
    App = QApplication(sys.argv) 
    # # create the instance of our Window 
    window = Window() 
    # # start the app 
    sys.exit(App.exec()) 
