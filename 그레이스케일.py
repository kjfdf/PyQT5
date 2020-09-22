import sys
from PyQt5.QtWidgets import QWidget,QApplication,QFileDialog,QPushButton
from PyQt5.QtGui import *

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.sid=QImage("cap.jpg").scaled(120,120)

        btn=QPushButton("이미지 변경",self) #버튼누르고 이미지 파일 불러오면 이미지가 작은 크기로 창안에 들어감
        btn.resize(btn.sizeHint())
        btn.move(20,150)
        btn.clicked.connect(self.openFileNameDialog)

        self.setGeometry(1400,250,320,200)
        self.show()

    def paintEvent(self, event): #이미지를 불러올때마다 바껴야 되므로 정의
        painter=QPainter()
        painter.begin(self)
        self.drawImages(painter) #이미지 그리는 메쏘드 호출
        painter.end()

    def drawImages(self,painter):  #그림 그리려면 painter객체 필요
        painter.drawImage(5,15,self.sid) #그림 위치와 이미지 객체를 넘겨줌
        painter.drawImage(self.sid.width()+20,25, #20,25는 옆에 나올 이미지 크기
                          self.grayScale(self.sid.copy())) #원본이미지옆에 회색이미지 같이 호출

    def grayScale(self,image):
        for i in range(self.sid.width()):
            for j in range(self.sid.height()):
                c=image.pixel(i,j)
                gray=qGray(c)
                alpha=qAlpha(c)
                image.setPixel(i,j,
                               qRgba(gray,gray,gray,alpha))
        return image

    def openFileNameDialog(self): #파일의 (경로=fileName, 타입=_)으로 튜플로 결과를 출력함
        fileName,_=QFileDialog.getOpenFileName(self,"불러올 이미지를 선택하세요.","", #1번째""는 안내문, 2번째는 읽어들인 파일명에 붙일 내용
                                               "All Files (*);;Python Files(*.py)") #3번째는 읽어들일 파일의 확장자 지정
        if fileName:
            print(fileName)
            self.sid=QImage(fileName).scaled(120,120) #디버깅을 위해서 파일명을 출력하고 120*120사이즈의 이미지를 sid변수에 저장함

app=QApplication([])
ex=Exam()
sys.exit(app.exec_())