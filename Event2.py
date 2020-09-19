import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QApplication,QGridLayout,QLabel

class Exam(QWidget):   #창으로 만들기
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        grid=QGridLayout()
        grid.setSpacing(10)

        x=0
        y=0

        self.text="x:{0},y:{1}".format(x,y) #마우스를 움직일때마다 좌표가 나오게 만들기

        self.label=QLabel(self.text,self)
        grid.addWidget(self.label,0,0,Qt.AlignTop)

        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300,100,900,900)
        self.setWindowTitle('NCS/EMG')
        self.show()

    def mouseMoveEvent(self,e):
        x=e.x()
        y=e.y()

        text="x:{0},y:{1}".format(x,y)
        self.label.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Exam()
    sys.exit(app.exec_())