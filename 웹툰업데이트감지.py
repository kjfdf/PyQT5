from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt5.QtCore import QTimer
from bs4 import BeautifulSoup as bs
import urllib.request as req,sys,time
from scrap_01 import Ui_MainWindow

class Exam(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timer=QTimer()
        self.timer.timeout.connect(self.chk)
        self.timer.setInterval(5*60*1000)
        self.rb_5min.setChecked(True)
        self.show()

    def setCycle(self):
        if self.rb_10min.isChecked():
            self.timer.setInterval(10*60*1000)
        elif self.rb_5min.isChecked():
            self.timer.setInterval(5*60*1000)
        elif self.rb_3min.isChecked():
            self.timer.setInterval(3*60*1000)
        else:
            self.timer.setInterval(1*60*1000)

    def startChk(self):
        self.url.setEnabled(False)
        self.timer.start()

    def stopChk(self):
        self.url.setEnabled(True)
        self.timer.stop()

    def chk(self): #사이트에서 f12눌러서 코드나오게 하고 ctrl+shift+C누르고 업데이트 아이콘 부분 누른뒤 나오는 alt=up을 이용
        self.rsp=req.urlopen(self.url.text())
        self.html=bs(self.rsp,"html.parser")
        try:
            self.test=self.html.find(alt="UP").attrs['alt'] #alt속성인 값을 찾고 그 값을 저장
        except:
            self.test="XX"
        self.t=time.localtime()
        self.lbl_print.setText("{}:{}:{} 체크결과:{}".format(self.t.tm_hour,self.t.tm_min,self.t.tm_sec,self.test))

app=QApplication([])
ex=Exam()
sys.exit(app.exec_())