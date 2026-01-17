

import sys  #It's a system package contains python interpretor variables
#Qapplication: It manages events like mouse click, keypresses
#QMainWindow: It manages window styling
#
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                            QCheckBox)
from PyQt5.QtCore import Qt
#Above line imported are used in this program

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

        #Create button object
        self.checkbox = QCheckBox("Do you like food?",self)
        self.initUI()

    def initUI(self):
        #set positioning and styling for button
        self.checkbox.setGeometry(50,0,250,250)
        self.checkbox.setStyleSheet("font-size: 30px;")
        self.checkbox.setChecked(False)

        #clicked: is an event trigger which send signal when button is clicked
        #connect: it connects event to the slot (self.onclick)
        #so when click occurs, we perform onclick operations
        self.checkbox.stateChanged.connect(self.state_changed)
    
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
