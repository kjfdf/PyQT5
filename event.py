import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget,QLCDNumber,QSlider,
                             QVBoxLayout,QApplication)

class Exam(QWidget):   #창으로 만들기
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        lcd=QLCDNumber(self) #창 하단에 슬라이드 바를 움직이면 숫자가 증가함
        sld=QSlider(Qt.Horizontal, self)

        vbox=QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld) #창을 배치시키는 명령문

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display) #lcd라는 함수를 보여줌.

        self.setGeometry(300, 100, 1200, 900)  # 창크기 조절, 가로 400, 세로 500, 왼쪽에서
        self.setWindowTitle('NCS/EMG판독기')  # 창 제목 붙이기
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Exam()
    sys.exit(app.exec_())