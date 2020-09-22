import sys
import time

from PyQt5.QtCore import QTimer, Qt, QTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QPushButton, QCheckBox, QTimeEdit, QSpinBox,QDial
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QSoundEffect

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0,0,500,520) #전체 창 크기
        self.setWindowTitle("타임벨")

        self.lblTitle=QLabel("타임벨 정지",self) #제일 상단의 상태표시문장
        self.lblTitle.setFont(QFont("맑은고딕",35))
        self.lblTitle.setAlignment(Qt.AlignCenter)
        self.lblTitle.resize(350,40)
        self.lblTitle.move(75,10)

        self.lblNow=QLabel("",self) #상태표시문자 밑에 나오는 현재시각
        self.lblNow.setFont(QFont("맑은고딕",45))
        self.lblNow.setAlignment(Qt.AlignCenter)
        self.lblNow.resize(350,46)
        self.lblNow.move(75,60)

        self.on=QPushButton("ON",self)
        self.on.setFont(QFont("맑은고딕",24))
        self.on.resize(170,35)
        self.on.move(75,116)
        self.on.clicked.connect(self.timerStart)

        self.off=QPushButton("OFF",self)
        self.off.setFont(QFont("맑은고딕",24))
        self.off.resize(170,35)
        self.off.move(255,116)
        self.off.clicked.connect(self.timerStop)

        self.lbl=QLabel("        요일         시작         종료        수업"
                        "         휴식       점심시작      점심종료",self)

        self.lbl.move(10,170)

        self.day_txt=["","월","화","수","목","금","토","일"]
        # self.day_lbl=[]
        self.day_chk=[] #요일 옆에 체크추가, 그 요일에 벨소리 울리게 할지
        self.day_chk.append(0)

        self.time_st=[] #벨소리가 시작되는 구간
        self.time_st.append(0)

        self.time_ed=[] #벨소리가 끝나는 구간
        self.time_ed.append(0)

        self.time_ls=[] #수업시간
        self.time_ls.append(0)

        self.time_rs=[] #휴식시간
        self.time_rs.append(0)

        self.time_lch_st=[] #점심시간 시작
        self.time_lch_st.append(0)

        self.time_lch_ed=[] #점심시간 종료
        self.time_lch_ed.append(0)

        self.lch_chk=[] #점심시간옆에 체크,점심시간에 벨소리 울리게 할지
        self.lch_chk.append(0)

        for r in range(1,8): #1~7까지 반복하는 문장
            self.day_chk.append(QCheckBox(self.day_txt[r]+"요일",self)) #월요일부터 일요일까지 나오게 만들기
            self.day_chk[r].move(20,165+r*28) #요일에 추가될때마다 간격이 증가되도록 하기, 요일간의 간격이 28임
            self.day_chk[r].setChecked(True) #체크된 상태가 default값으로 되도록
            self.time_st.append(QTimeEdit(self))
            self.time_st[r].setDisplayFormat("hh:mm") #시간과 분을 2자리로 표시하기
            self.time_st[r].setTime(QTime(9,00)) #기준시각정하기 9시0분으로
            self.time_st[r].move(20+70,165+r*28) #시각이 요일에 비해 옆으로 더 가도록 간격 70만큼 설정
            self.time_ed.append(QTimeEdit(self))
            self.time_ed[r].setDisplayFormat("hh:mm")
            self.time_ed[r].setTime(QTime(22,00))
            self.time_ed[r].move(20+70+70,165+r*28)
            self.time_ls.append(QSpinBox(self))
            self.time_ls[r].move(20+70+70+70,165+r*28)
            self.time_ls[r].setValue(10) #기본 수업시작시간인 10분 설정
            self.time_rs.append(QSpinBox(self))
            self.time_rs[r].move(20+70+70+70+55,165+r*28)
            self.time_rs[r].setValue(55) #기본 수업 종료 및 휴식시작시간 55분 설정
            self.time_lch_st.append(QTimeEdit(self))
            self.time_lch_st[r].setDisplayFormat("hh:mm")
            self.time_lch_st[r].setTime(QTime(13,00)) #점심시작시간 설정
            self.time_lch_st[r].move(20+70+70+70+55+55,165+r*28)
            self.time_lch_ed.append(QTimeEdit(self))
            self.time_lch_ed[r].setDisplayFormat("hh:mm")
            self.time_lch_ed[r].setTime(QTime(15,00)) #점심 종료시간 설정
            self.time_lch_ed[r].move(20+70+70+70+55+55+70,165+r*28)
            self.lch_chk.append(QCheckBox("",self)) #점심시작과 종료시간에 벨이 울릴지 말지를 체크박스로 설정하게
            self.lch_chk[r].move(20+70+70+70+55+55+70+55,165+r*28)
            self.lch_chk[r].setChecked(True)

        self.lbl_bell=QLabel("벨 음량",self)
        self.lbl_bell.move(35,400)
        self.bell_vol=QDial(self)
        self.bell_vol.move(5,410)
        self.bell_vol.setValue(50)
        self.bell_vol.valueChanged.connect(self.ch_bell_vol)

        self.timer=QTimer()
        self.timer.timeout.connect(self.tChk)

        self.bell=QSoundEffect() #벨소리 객체 생성
        self.bell.setSource(QUrl.fromLocalFile('bell.wav')) #벨소리는 wav파일만 재생 가능?

        self.show()
        self.timerStart()

    def ch_bell_vol(self): #소리를 0~1까지인데 100으로 나눠서 세분화시켜서 조절하기 
        self.bell.setVolume(self.bell_vol.value()/100)

    def timerStop(self): #off버튼을 누르면 시각이 사라지고 글자가 정지중으로 나오는 이벤트 생성
        self.timer.stop()
        self.lblTitle.setText("타임벨 정지중")
        self.lblNow.setText("")

    def timerStart(self): #1000밀리초마다 타임첵 메쏘드가 실행되게 하기
        self.lblTitle.setText("타임벨 작동중")
        self.timer.start(1000)

    def tChk(self): #현재시각 나타나게 하기
        t=time.localtime()
        self.lblNow.setText("{}:{}:{}".format(t.tm_hour,t.tm_min,t.tm_sec)) #현재시각 나타나는 포맷에 시간,분,초 넣어주기
        w=t.tm_wday+1 #종료시간 직전까지만 종이치게 미만으로, 매0초에 종이 울리게 설정
        if self.day_chk[w].isChecked() and self.time_st[w].time().hour() <= t.tm_hour and \
                        self.time_ed[w].time().hour() > t.tm_hour and t.tm_sec == 0 and \
                (t.tm_min==self.time_ls[w].value() or t.tm_min==self.time_rs[w].value()):
            if self.lch_chk[w].isChecked() and self.time_lch_st[w].time().hour() <= t.tm_hour and \
                            self.time_lch_ed[w].time().hour() > t.tm_hour:
                return
            self.play()

    def play(self):
        self.bell.play()

app=QApplication([])
ex=Exam()
ex.move(app.desktop().screen().rect().center()-ex.rect().center())
sys.exit(app.exec_())