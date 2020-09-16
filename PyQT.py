import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn=QPushButton('입력하세요',self) #버튼을 '입력하세요'로 만듦
        btn.resize(btn.sizeHint())
        btn.setToolTip()
        btn.move(25,30) #버튼위치조정
        self.show()

app=QApplication(sys.argv)
w=Exam()
sys.exit(app.exec_()) #종료할때 하는것,app.exec는 이벤트처리를 위한 루프를 실행하는것
