import sys
from PyQt5.QtWidgets import (QWidget,QPushButton,
                             QFrame,QApplication)
from PyQt5.QtGui import QColor

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.col=QColor(0,0,0)

        redb=QPushButton('Red',self)
        redb.setCheckable(True) #버튼을 누를수있게 함
        redb.move(10,10)

        redb.clicked.connect(self.setColor)

        greenb=QPushButton('Green',self)
        greenb.setCheckable(True) #버튼을 누를수있게 함
        greenb.move(10,30)

        greenb.clicked.connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)  # 버튼을 누를수있게 함
        blueb.move(10, 50)

        blueb.clicked.connect(self.setColor)

        self.square=QFrame(self)
        self.square.setGeometry(150,20,100,100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %  #색깔을 넣어주는것
                                  self.col.name())
        self.setGeometry(300, 100, 900, 900)
        self.setWindowTitle('NCS/EMG')
        self.show()

    def setColor(self,pressed):
        source=self.sender()
        if pressed:
            val=255
        else:
            val=0

        if source.text()=="Red":
            self.col.setRed(val)
        elif source.text()=="Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("QFrame { background-color: %s }" %  #색깔을 넣어주는것
                                  self.col.name())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exam()
    sys.exit(app.exec_())