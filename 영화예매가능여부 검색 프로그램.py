import sys
import requests
import movie
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QTimer,QUrl
from bs4 import BeautifulSoup as bs

class main(QWidget,movie.Ui_Form):  #영화예매가 나오는 곳으로 가서 주소 넣고 누르면 예매 가능한지 여부 나오고 버튼 누르면 사이트로 연결됨
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.timer=QTimer()
        self.timer.setInterval(1000*60)

        self.timer.timeout.connect(self.chk)
        self.btnOn.clicked.connect(self.on)
        self.btnOff.clicked.connect(self.off)
        self.btnLink.clicked.connect(self.open)

    def chk(self):
        url=self.txtUrl.text()
        html=bs(requests.get(url).content,"html.parser",from_encoding="utf-8")
        res=html.select("#select_main > div.sect-base-movie > div.box-contents > span.like > a.link-reservation")
        if len(res)==1:
            self.btnLink.setText("예매가능")
        else:
            self.btnLink.setText("예매불가")

    def on(self):
        if self.txtUrl.text()!="":
            url=self.txtUrl.text()
            html=bs(requests.get(url).content,"html.parser",from_encoding="utf-8")
            res=html.select("#select_main > div.sect-base-movie > div.box-contents > div.title > strong")
            self.setWindowTitle("{} 예매 가능 여부 검색 중 입니다.(주기:1분)"
                .format(res[0].contents))
            self.timer.start()
            self.btnLink.setText("확인 중. 1분 뒤부터 결과가 나타납니다.")

    def off(self):
        self.setWindowTitle("영화예매 가능여부 확인 프로그램")
        self.timer.stop()
        self.btnLink.setText("")

    def open(self):
        if self.btnLink.text()=="예매가능":
            url=QUrl(self.txtUrl.text())
            QDesktopServices.openUrl(url)

app = QApplication([])
ex = main()
ex.show()
sys.exit(app.exec_())