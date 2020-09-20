import sys
from PyQt5.QtWidgets import (QWidget, QCalendarWidget, QLabel,
                             QLineEdit,QApplication, QVBoxLayout)
from PyQt5.QtCore import QDate


class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl=QLabel(self)
        qle=QLineEdit(self)

        qle.move(60,100)
        self.lbl.move(60,40)

        qle.textChanged[str].connect(self.onChanged) #입력된 문자열을 onchanged와 연결시킴

        self.setGeometry(300, 100, 900, 900)
        self.setWindowTitle('NCS/EMG')
        self.show()

    def onChanged(self,text): #label의 문자열을 입력된 문자열과 연결시킴
        self.lbl.setText(text)
        self.lbl.adjustSize() #입력된 문자가 길어질수록 size를 조정하여 크기가 커짐 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exam()
    sys.exit(app.exec_())