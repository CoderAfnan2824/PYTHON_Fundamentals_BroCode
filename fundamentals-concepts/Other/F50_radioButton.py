

import sys  #It's a system package contains python interpretor variables
#Qapplication: It manages events like mouse click, keypresses
#QMainWindow: It manages window styling
#QRadioButton: create button(can select anyone out of multiple)
#QButtonGroup: It groups particular buttons into one group
#
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                            QRadioButton, QButtonGroup)

from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt #used for alignment

from pathlib import Path

Base = Path(__file__).resolve().parent
image_url = Base/"Icon.JPG"
class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()
        #it sets window title
        self.setWindowTitle("This is my first GUI APP")

        #It sets dimension and position of the window
        self.setGeometry(500,250,500, 500)

        #Create radioButton object
        self.radiobutton1 = QRadioButton("Visa",self)
        self.radiobutton2 = QRadioButton("Mastercard",self)
        self.radiobutton3 = QRadioButton("GiftCard",self)
        self.radiobutton4 = QRadioButton("Online",self)
        self.radiobutton5 = QRadioButton("instore",self)
        
        self.buttonGroup1 = QButtonGroup(self)
        self.buttonGroup2 = QButtonGroup(self)
        self.initUI()

    def initUI(self):
        self.radiobutton1.setGeometry(10,0,200,200)
        self.radiobutton2.setGeometry(10,50,200,200)
        self.radiobutton3.setGeometry(10,100,200,200)
        self.radiobutton4.setGeometry(10,150,200,200)
        self.radiobutton5.setGeometry(10,200,200,200)

        self.buttonGroup1.addButton(self.radiobutton1)
        self.buttonGroup1.addButton(self.radiobutton2)
        self.buttonGroup1.addButton(self.radiobutton3)
        self.buttonGroup2.addButton(self.radiobutton4)
        self.buttonGroup2.addButton(self.radiobutton5)

        self.setStyleSheet("QRadioButton{"
                           "font-size: 30px;""}")
        
        self.radiobutton1.toggled.connect(self.radio_selected)
        self.radiobutton2.toggled.connect(self.radio_selected)
        self.radiobutton3.toggled.connect(self.radio_selected)
        self.radiobutton4.toggled.connect(self.radio_selected)
        self.radiobutton5.toggled.connect(self.radio_selected)
    
    def radio_selected(self):
        button = self.sender()
        if button.isChecked():
            print(f"{button.text()} is selected")
    
    def state_changed(self, state):
        if state == Qt.Checked:
            print("You like food!") #print message in console
        else:
            print("You don't like food!")
        

        

    #Below boiler create an GUi application, opens a window, keeps it running until user closes it
def main():

    #below package manages events like mouse clicks, key presses
    #argv store command line arguments. Empty string if ntg is passed
    app = QApplication(sys.argv) 

    window = MainWindow()

    window.show()

    #app.exec_ listens for user input like clicks, keypress. It runs in continuos event loop
    #   ends when user input
    # sys.exit the python code when the user enters input
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
