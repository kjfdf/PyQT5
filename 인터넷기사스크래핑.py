import sys, requests
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QDesktopServices as qd
from PyQt5.QtCore import QDate,QUrl
from bs4 import BeautifulSoup as bs, element

class main(QWidget):
    def __init__(self):
        super().__init__()
        self.qf=QFrame(self)
        self.btn1=QPushButton('사건사고',self) #2차카테고리값을 넣어줌 (사회내의 사건사고,교육,식품/의료 섹션)
        self.btn2=QPushButton('교육',self)
        self.btn3=QPushButton('식품/의료',self)
        self.dte=QDateEdit(QDate.currentDate(),self) #기사의 날짜값을 넣어주기위해
        self.lv=QListView(self.qf) #기사를 리스트의 형태로 불러오기위해, 부모객체를 리스트가 아닌 프레임으로 하겠다는 의미
        self.model=QStandardItemModel()
        self.subTitle=QLabel(self)
        self.subCont=QPlainTextEdit(self)
        self.lst=[] #읽어온 뉴스목록을 저장할 리스트값
        self.category={'사건사고':249, '교육':250, '식품/의료':255} #문자로 인덱싱이 가능한 딕셔너리형태로 만듦(sid2= 뒤의 숫자값)
        self.curCat='' #현재 선택된 카테고리를 설정하는 변수
        self.setUi()
        self.setSlot()

    def setUi(self):
        self.setGeometry(300,100,800,800)
        self.qf.setGeometry(0,30,400,400)
        self.lv.setGeometry(0,0,400,400)
        self.lv.setModel(self.model)
        self.btn1.move(0,0)
        self.btn2.move(80,0)
        self.btn3.move(160,0)
        self.dte.move(510,5)
        self.subTitle.move(510,5)
        self.subTitle.setFixedSize(590,50)
        self.subTitle.setStyleSheet("font-size:15px; font-weight:bold;")
        self.subCont.move(610,50)
        self.subCont.setFixedSize(590,480)
        self.subCont.setStyleSheet("font-size:13px;")

    def setSlot(self):
        #self.lv.clicked.connect(self.artSel)
        self.lv.doubleClicked.connect(self.visit)
        self.btn1.clicked.connect(self.catSel)
        self.btn2.clicked.connect(self.catSel)
        self.btn3.clicked.connect(self.catSel)

    def visit(self):
        qd.openUrl(QUrl(self.lst[self.lv.currentIndex().row()][0]))

    def catSel(self):
        self.curCat=self.sender().text()
        self.urlSet()

    def artSel(self):
        self.subTitle.setText(self.lv.currentIndex().data())
        url=self.lst[self.lv.currentIndex().row()][0]
        html=bs(requests.get(url).content,"html.parser",from_encoding="utf-8")
        tag=html.select("#articleBodyContents")
        joinTxt=''

        for a in range(9, len(tag[0].contents)-2):
            if isinstance(tag[0].contents[a],element.NavigableString):
                joinTxt+=str(tag[0].contents[a])+'\n\n'

        joinTxt.replace('&apos',"'")
        self.subCont.setPlainText(joinTxt)

    def urlSet(self):
        page=1
        date=self.dte.text().replace('-','') #replace를 이용해서 원래값에서 날짜사이의 -를 없애줌
        self.lst.clear() #다른 카테고리의 기사를 볼때 리스트를 초기화 해줘야 하므로 추가
        baseUrl="https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2={0}&sid1=102&date={1}&page={2}" #섹션내의 2페이지로 가서 sid2,날짜,page값을 할당해줌 
        url=baseUrl.format(self.category[self.curCat],date,page)
        html=bs(requests.get(url).content, "html.parser", from_encoding="utf-8")
        page=len(html.select("#main_content>div.paging>a"))+1
        for i in range(1, page+1):
            url=baseUrl.format(self.category[self.curCat],date,i)
            html=bs(requests.get(url).content,"html.parser",from_encoding="utf-8")
            tag=html.select("#main_content > div > ul > li")

            for s in tag:
                li=s.find_all('a')
                self.lst.append([])
                self.lst[-1].append(li[0].attrs['href']) #href는 뉴스기사 링크주소임
                if len(li)==2:
                    self.lst[-1].append(li[1].string.strip().replace('&apos',"'")) #작은따옴표가 &apos로 변해서 들어가는데 이것을 다시 '로 바꿔줌
                else:
                    self.lst[-1].append(li[0].string.strip().replace('&apos',"'"))

        self.model.clear()
        for s in self.lst:
            self.model.appendRow(QStandardItem(s[1]))

app=QApplication([])
ex=main()
ex.show()
sys.exit(app.exec_())