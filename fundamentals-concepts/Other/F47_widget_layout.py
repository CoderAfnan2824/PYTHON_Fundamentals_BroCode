

import sys  #It's a system package contains python interpretor variables
#Qapplication: It manages events like mouse click, keypresses
#QMainWindow: It manages window styling
#
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                            QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)
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
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("1.#")
        label2 = QLabel("2.#")
        label3 = QLabel("3.#")

        label1.setStyleSheet("Background-color: Yellow")
        label2.setStyleSheet("Background-color: Red")
        label3.setStyleSheet("Background-color: Green")

        grid = QGridLayout()
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 1, 1)
        grid.addWidget(label3, 4, 3)
        central_widget.setLayout(grid)
        '''
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        central_widget.setLayout(vbox)

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        central_widget.setLayout(vbox)'''
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
