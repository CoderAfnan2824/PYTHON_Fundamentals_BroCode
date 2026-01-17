
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

from pathlib import Path

base = Path(__file__).resolve().parent
font_path = base/"font.TTF"
class digitalClock(QWidget):

    def __init__(self):
        super().__init__()

        self.time_label = QLabel(self)
        self.timer = QTimer(self)

        self.initUI()
        
    
    def initUI(self):

        self.setWindowTitle("Digital Clock")
        self.setGeometry(500,250,300,150)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 80px;"
                                      
                                      "color: hsv(90, 88%, 99%)")
        self.setStyleSheet("Background-color: black;")
        
        font_id = QFontDatabase.addApplicationFont(str(font_path))
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)


        self.timer.timeout.connect(self.define_time)
        self.timer.start(1000)

        self.define_time()
        

    def define_time(self):

        current_time = QTime().currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)
        

if __name__ == "__main__":

    app = QApplication(sys.argv)
    clock = digitalClock()
    clock.show()
    sys.exit(app.exec_())