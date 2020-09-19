import sys
from PyQt5.QtWidgets import QMainWindow,QPushButton,QApplication

class Exam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1=QPushButton("Button 1",self) #상단에 버튼2개 만들기
        btn1.move(30,50)

        btn2=QPushButton("Button2",self)
        btn2.move(150,50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked) #버튼 누르면 발생하는 이벤트 정의

        self.statusBar()

        self.setGeometry(300, 100, 900, 900)
        self.setWindowTitle('NCS/EMG')
        self.show()

    def buttonClicked(self): #buttonClicked함수정의, 하단의 statusbar에 메세지가 나오게 함
        sender=self.sender()
        self.statusBar().showMessage(sender.text()+' was pressed')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Exam()
    sys.exit(app.exec_())