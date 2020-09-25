import sys,os,shutil,random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class main(QWidget):
    def __init__(self):
        super().__init__()
        self.srcDir='c:\\test\\' #C드라이브의 test디렉토리를 파일을 생성하고 분류할 디렉토리로 정함 \\를 2개해야함
        self.desDir='c:\\des\\' #목적지 디렉토리임
        self.year=['2016','2017','2018']
        self.month=['{0:02}'.format(x+1) for x in range(0,12)] #변수 x가 0부터 11까지가 할당되는데 그 값에 1을 더해서 할당하고 1~9는 01~09로 표현해줌
        self.tv=QTableView(self) #데이터를 나타내주는 틀을 테이블 형태로 해줌
        self.model=QStandardItemModel(12,3) #데이터를 12개의 행과 3개의 열로 나타내서 생성
        self.btnRnd=QPushButton("랜덤파일생성(1000)")
        self.btnClss=QPushButton("파일분류")
        self.setUi()
        self.setSlot()

    def setUi(self):
        self.setGeometry(300,100,800,800)
        self.setWindowTitle("NCS/EMG")

        self.tv.setModel(self.model)
        self.model.setHorizontalHeaderLabels(self.year)
        self.model.setVerticalHeaderLabels(self.month)
        vbox=QVBoxLayout()
        vbox.addWidget(self.btnRnd)
        vbox.addWidget(self.btnClss)
        vbox.addWidget(self.tv)
        self.setLayout(vbox)

    def setSlot(self):
        self.btnRnd.clicked.connect(self.rndCrtFile)
        self.btnClss.clicked.connect(
            lambda s, srcDir=self.srcDir, desDir=self.desDir: #lambda를 이용해서 형태가 없는 함수를 만든것
            self.classify(s,srcDir,desDir))

    def classify(self,s,srcDir,desDir):
        fileList=os.listdir(srcDir)

        for name in fileList: #테스트 디렉토리에 있는 파일을 전부 리스트 형태로 읽어오고 파일들의 이름을 하나씩 전부 for문으로 실행
            y=name[5:9] #srcDir디렉토리인 test디렉토리에 있는 파일의 이름이 처음부터 5번째부터 9번째 까지가 연도고 10번째부터 12번째 까지가 월이므로 y,m에 각각 그 값을 저장
            m=name[10:12]

            export=desDir+y+'\\'+m
            if not os.path.isdir(export):
                os.makedirs(export)
            shutil.copyfile(srcDir+name,export+'\\'+name)
        for yidx, y in enumerate(self.year):
            for midx, m in enumerate(self.month):
                self.model.setData(self.model.index(midx,yidx),
                                   len(os.listdir(self.desDir+y+'\\'+m)))

    def rndCrtFile(self): #2016년부터 2018년까지의 날짜로 파일을 1000개를 랜덤으로 만듦
        for i in range(1000):
            y=random.randint(2016,2018)
            m=random.randint(1,12)
            d=random.randint(1,30)
            tmp=random.randrange(9999) # 0은 y,1은 m,2는 d, 3은 tmp를 대입시키고 :02는 숫자를 2자리로 표현해달라는 뜻(1은 01로, 2는 02로)
            f=open(self.srcDir+'text_{0}-{1:02}-{2:02}({3}).txt'.format(y,m,d,tmp),'w') #파일을 쓰기모드로 열어서 없는파일 생성 시킴
            f.close()

app=QApplication([])
ex=main()
ex.show()
sys.exit(app.exec_())