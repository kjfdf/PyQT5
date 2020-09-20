import sys
from PyQt5.QtWidgets import (QWidget,QPushButton,
                             QFrame,QApplication,QProgressBar)
from PyQt5.QtCore import QBasicTimer

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pbar=QProgressBar(self)
        self.pbar.setGeometry(30,40,200,25)

        self.btn=QPushButton('Start',self)
        self.btn.move(40,80)
        self.btn.clicked.connect(self.doAction)

        self.timer=QBasicTimer()
        self.step=0

        self.setGeometry(300, 100, 900, 900)
        self.setWindowTitle('NCS/EMG')
        self.show()

    def timerEvent(self,e): #101이 되는순간 멈추고 finished로 바꿈.
        if self.step>= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step=self.step+1 #100미만이면 step값을 1씩 증가시킴
        self.pbar.setValue(self.step)

    def doAction(self): #누르면 타이머가 활성화됨
        if self.timer.isActive(): #stop을 누르면 버튼이 start로 바뀜
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(10,self) #10/1000초마다 타이머를 실행해줌
            self.btn.setText('Stop') #버튼을 stop으로 바꿔줌

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exam()
    sys.exit(app.exec_())