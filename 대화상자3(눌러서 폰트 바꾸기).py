import sys
from PyQt5.QtWidgets import (QWidget,QVBoxLayout,QPushButton,
                             QSizePolicy,QLabel,QFontDialog,QApplication)

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox=QVBoxLayout()

        btn=QPushButton('Dialog',self)
        btn.setSizePolicy(QSizePolicy.Fixed,
                          QSizePolicy.Fixed)

        btn.move(20,20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lbl=QLabel('Knowledge only matters',self) #dialog밑에 넣을 문장 knowledge~
        self.lbl.move(130,20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300, 100, 900, 900)
        self.setWindowTitle('NCS/EMG')
        self.show()

    def showDialog(self): #font고르면 knowledge문장의 폰트가 바뀜
        font, ok=QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exam()
    sys.exit(app.exec_())