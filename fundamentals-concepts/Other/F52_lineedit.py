'''
'''
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(500,250,500,500)
        
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
                                        
        self.initUI()
        
    def initUI(self):
        self.line_edit.setGeometry(20,20,200,50)
        self.line_edit.setStyleSheet(   "font-size: 25px;"
                                        "font-family: Arial;")
                                        
        self.button.setGeometry(250,20,150,50)
        self.button.setStyleSheet(   "font-size: 25px;"
                                        "font-family: Arial;")
        self.line_edit.setPlaceholderText("Enter Your Name")
        
        self.button.clicked.connect(self.submit)
    
    def submit(self):
        text = self.line_edit.text()
        print(f"Hello {text}")
        

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    app_window = MainWindow()
    app_window.show()
    
    sys.exit(app.exec_())
    