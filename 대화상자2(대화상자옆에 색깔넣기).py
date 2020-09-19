import sys
from PyQt5.QtWidgets import (QWidget,QPushButton,QFrame,
                             QColorDialog,QApplication)
from PyQt5.QtGui import QColor

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        col=QColor(0,0,0) #각각 R,G,B를 의미, 초기색깔을 검은색으로 설정하는것

        self.btn=QPushButton('Dialog',self)
        self.btn.move(20,20)

        self.btn.clicked.connect(self.showDialog)

        self.frm=QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }"  #색깔을 눌러서 코드가 나오면 해당코드의 색깔을 네모박스에 넣어준다는 것
                               % col.name())
        self.frm.setGeometry(130,22,100,100)

        self.setGeometry(300, 100, 900, 900)
        self.setWindowTitle('NCS/EMG')
        self.show()

    def showDialog(self):
        col=QColorDialog.getColor()

        if col.isValid():  #ok를 눌러줄 경우에 true가 되서 출력이됨. 
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                                   % col.name())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exam()
    sys.exit(app.exec_())