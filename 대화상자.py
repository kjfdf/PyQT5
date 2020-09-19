import sys
from PyQt5.QtWidgets import (QWidget,QPushButton,QLineEdit,
                             QInputDialog,QApplication)

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn=QPushButton('Dialog',self) #Dialog버튼 만들어줌.
        self.btn.move(20,20)
        self.btn.clicked.connect(self.showDialog)

        self.le=QLineEdit(self)
        self.le.move(130,22)

        self.setGeometry(300, 100, 900, 900)
        self.setWindowTitle('NCS/EMG')
        self.show()

    def showDialog(self): #Dialog를 누르면 빈칸이 나오고 거기에 텍스트를 넣으면 Dialog옆 빈칸에 텍스트가 삽입됨.
        text, ok=QInputDialog.getText(self,'Input Dialog',
                                      'Enter your name: ') #Dialog누르면 나오는 네모박스의 큰 창에 뜨는 이름(타이틀)이 Input, 그 밑에 빈칸위 기록된 항목(프롬프트)이 Enter
        if ok:  #기록하고 ok를 누르면 삽입되고 cancel누르면 삽입되지 않음. str안에 넣어서 문자열로 변환해서 넣어줌 
            self.le.setText(str(text))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exam()
    sys.exit(app.exec_())