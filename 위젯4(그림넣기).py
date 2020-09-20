import sys
from PyQt5.QtWidgets import (QWidget,QHBoxLayout,
                             QLabel,QApplication)
from PyQt5.QtGui import QPixmap

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox=QHBoxLayout(self)
        pixmap=QPixmap("IMG_2651.jpg")

        lbl=QLabel(self)
        lbl.setPixmap(pixmap) #label대신에 글자대신 그림파일을 넣은것

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(100,100)
        self.setWindowTitle('영길도')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exam()
    sys.exit(app.exec_())