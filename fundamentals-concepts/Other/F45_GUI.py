

import sys  
#It's a system package contains python interpretor variables
#Qapplication: It manages events like mouse click, keypresses
#QMainWindow: It manages window styling
#
from PyQt5.QtWidgets import QApplication, QMainWindow 
from PyQt5.QtGui import QIcon
from pathlib import Path

Base = Path(__file__).resolve().parent
image_url = Base/"Icon.JPG"
class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()
        #it sets window title
        self.setWindowTitle("This is my first GUI APP")

        #It sets dimension and position of the window
        self.setGeometry(0,0,500, 500)
        
        #first we set raw string to avoid escape sequence. The we set image, but mac doesn't show
        image_path = r"image_url"
        self.setWindowIcon(QIcon(image_path))

        #so we check if image created 
        icon = QIcon(image_path)
        print(icon.isNull())   # False = icon loaded correctly
        
#Below boiler create an GUi application, opens a window, keeps it running until user closes it
def main():

    #below package manages events like mouse clicks, key presses
    #argv store command line arguments. return Empty string if ntg is passed
    app = QApplication(sys.argv) 

    window = MainWindow()

    window.show()

    #app.exec_ listens for user input like clicks, keypress. It runs in continuos event loop
    #   ends when user input
    # sys.exit the python code when the user enters input
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
