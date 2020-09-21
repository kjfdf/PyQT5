import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget,QGridLayout,QLabel,QApplication)

class Exam(QWidget):   #창으로 만들기
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        grid=QGridLayout()  #마우스 움직일때마다 좌표나오게 하는 기능 추가 
        grid.setSpacing(10)

        x=0
        y=0

        self.text="x:{0}, y:{1}".format(x,y)

        self.label=QLabel(self.text,self)
        grid.addWidget(self.label,0,0,Qt.AlignTop)

        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 100, 1200, 900)  # 창크기 조절, 가로 400, 세로 500, 왼쪽에서
        self.setWindowTitle('NCS/EMG판독기')  # 창 제목 붙이기
        self.show()

    def mouseMoveEvent(self, e):
        x=e.x()
        y=e.y()

        text="x:{0}, y{1}".format(x,y)
        self.label.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Exam()
    sys.exit(app.exec_())