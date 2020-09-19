import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication

class Communicate(QObject): #pyqtsignal:신호방출이 가능한 객체 생성
    closeApp=pyqtSignal()

class Exam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):   #마우스 클릭하면 창 닫히게 하기 
        self.c=Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 100, 900, 900)
        self.setWindowTitle('NCS/EMG')
        self.show()

    def mousePressEvent(self, event): #마우스를 눌렀을때 발생하는 이벤트 정의 함수,emit가 중요:눌렀을때 event가 발생해서 슬롯에게 신호 전달
        self.c.closeApp.emit()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Exam()
    sys.exit(app.exec_())