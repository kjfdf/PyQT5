import sys
from PyQt5.QtWidgets import (QPushButton,QWidget,
                             QLineEdit,QApplication)

class Button(QPushButton):
    def __init__(self,title,parent):
        super().__init__(title,parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.mimeData().text())

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self): #네모박스안에 글을 쓰고 옆에 버튼으로 드래그하면 글이 들어감
        edit=QLineEdit('',self)
        edit.setDragEnabled(True)
        edit.move(30,65)

        button=Button("Button",self)
        button.move(190,65)

        self.setWindowTitle("NCS/EMG")
        self.setGeometry(300,100,800,800)

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Exam()
    ex.show()
    app.exec_()