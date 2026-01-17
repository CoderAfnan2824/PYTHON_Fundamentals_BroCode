
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton

from PyQt5.QtCore import QTimer, QTime, Qt


class stopWatch(QWidget):

    def __init__(self):
        super().__init__()

        self.time = QTime(0,0,0,0)
        self.time_label = QLabel("00:00:00:00",self)
        self.timer = QTimer(self)

        self.start = QPushButton("Start", self)
        self.stop = QPushButton("Stop", self)
        self.reset = QPushButton("Reset", self)

        self.initUI()
        
    
    def initUI(self):

        self.setWindowTitle("StopWatch Timer")
        self.setGeometry(500,250,300,150)

        
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start)
        hbox.addWidget(self.stop)
        hbox.addWidget(self.reset)

        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setStyleSheet('''
                           
                           QPushButton, QLabel{
                           padding: 5px;
                           font-weight: bold;
                           font-family: calibri;
                           }
                           QPushButton{
                                font-size: 25px;
                                }
                           QLabel{
                                font-size: 70px;
                                background-color: hsl(200,100%,55%);
                                border-radius: 10px;}''')
        
        self.start.clicked.connect(self.startM)
        self.stop.clicked.connect(self.stopM)
        self.reset.clicked.connect(self.resetM)
        self.timer.timeout.connect(self.update_display)

    
    def startM(self):
        self.timer.start(10)

    def stopM(self):
        self.timer.stop()

    def resetM(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        mins = time.minute()
        secs = time.second()
        milli = time.msec()//10

        return f"{hours:02}:{mins:02}:{secs:02}:{milli:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))   

if __name__ == "__main__":

    app = QApplication(sys.argv)
    clock = stopWatch()
    clock.show()
    sys.exit(app.exec_())