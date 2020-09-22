import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,100,800,800)

        self.btnList=[]
        self.btnTop=100 #첫버튼이 생성될 시작위치
        self.cnt=0 #버튼갯수를 저장하는 변수

        self.lbl=QLabel("생성될 버튼의 수를 입력하세요",self) #빈칸위에 안내문 넣기
        self.lbl.move(10,10)

        self.txt=QLineEdit("",self) #빈칸만들어서 숫자 넣을수있게
        self.txt.move(10,self.lbl.height())

        self.btn=QPushButton("버튼생성",self) #레이블의 탑위치
        self.btn.resize(QSize(80,25))
        self.btn.move(10,self.lbl.height()+self.txt.height())

        self.btn.clicked.connect(self.createBtn)

        self.show()

    def createBtn(self):
        self.cnt=int(self.txt.text())
        for i in range(self.cnt):
            self.btnList.append(QPushButton(str(i+1)+" 번째 버튼",self))
            self.btnList[i].resize(QSize(80,25))
            self.btnList[i].move(10,self.btnTop+(i*25))
            self.btnList[i].show()

app=QApplication([])
ex=Exam()
sys.exit(app.exec_())