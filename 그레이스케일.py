import sys
from PyQt5.QtWidgets import QWidget,QApplication,QFileDialog,QPushButton
from PyQt5.QtGui import *

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn=QPushButton("이미지 변경",self)
        btn.resize(btn.sizeHint())
        btn.move(20,150)
        btn.clicked.connect(self.openFileNameDialog)

        self.setGeometry(1400,250,320,200)
        self.show()

    def openFileNameDialog(self): #파일의 (경로=fileName, 타입=_)으로 튜플로 결과를 출력함
        fileName,_=QFileDialog.getOpenFileName(self,"불러올 이미지를 선택하세요.","", #1번째""는 안내문, 2번째는 읽어들인 파일명에 붙일 내용
                                               "All Files (*);;Python Files(*.py)") #3번째는 읽어들일 파일의 확장자 지정
        if fileName:
            print(fileName)
            self.sid=QImage(fileName).scaled(120,120) #디버깅을 위해서 파일명을 출력하고 120*120사이즈의 이미지를 sid변수에 저장함

app=QApplication([])
ex=Exam()
sys.exit(app.exec_())