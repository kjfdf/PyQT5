import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QMessageBox,QMainWindow,QAction,QMenu,qApp,QHBoxLayout,QVBoxLayout,QApplication)
from PyQt5.QtCore import QCoreApplication

class Exam(QWidget):   #창으로 만들기
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        Button1=QPushButton("Rt median sensory")
        Button2=QPushButton("Rt ulnar sensory")

        hbox=QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(Button1)
        hbox.addWidget(Button2)

        vbox=QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300,100,1200,900) #창크기 조절, 가로 400, 세로 500, 왼쪽에서
        self.setWindowTitle('NCS/EMG판독기') #창 제목 붙이기
        self.show()

if __name__== '__main__':
    app = QApplication(sys.argv)
    w = Exam()
    sys.exit(app.exec_())