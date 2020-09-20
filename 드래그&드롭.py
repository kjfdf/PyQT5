import sys
from PyQt5.QtWidgets import QPushButton,QWidget,QApplication
from PyQt5.QtCore import Qt,QMimeData
from PyQt5.QtGui import QDrag

class Button(QPushButton):
    def __init__(self,title,parent):
        super().__init__(title,parent)

    def mouseMoveEvent(self, e):  #마우스가 움직이는 동안 발생하는 이벤트 정의, 오른쪽 버튼이 눌린상태가 아니면 이벤트가 종료
        if e.buttons()!=Qt.RightButton:
            return

        mimeData=QMimeData() #다양한 멀티미디어 데이터를 다룰수 있음.

        drag=QDrag(self)
        drag.setMimeData(mimeData)

        drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e): #마우스가 클릭됐을때 발생하는 이벤트 정의
        super().mousePressEvent(e) #마우스 눌렀을때 색깔변화나 애니메이션 나타나게 함

        if e.button()==Qt.LeftButton:
            print('press')

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True) #drop event활성화 시킴

        self.button=Button('Button',self)
        self.button.move(100,65)

        self.setWindowTitle('NCS/EMG')
        self.setGeometry(300,100,800,800)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self,e): #마우스 오른쪽 버튼으로 drag하다가 버튼을 놓으면 drop위치에 버튼을 옮겨줌
        position=e.pos()
        self.button.move(position)

        e.accept()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Exam()
    ex.show()
    app.exec_()