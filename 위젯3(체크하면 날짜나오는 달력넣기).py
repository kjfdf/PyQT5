import sys
from PyQt5.QtWidgets import (QWidget,QCalendarWidget,QLabel,QApplication,QVBoxLayout)
from PyQt5.QtCore import QDate

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox=QVBoxLayout(self) #달력밑에 클릭한 날짜 나오게 하려고 vbox로 수직으로 배치

        cal=QCalendarWidget(self) #달력추가
        cal.setGridVisible(True) #달력이 격자로 보이도록 하기
        cal.clicked[QDate].connect(self.showDate) # 누르는 날짜 나오게

        vbox.addWidget(cal)

        self.lbl=QLabel(self) #선택한 날짜가 달력밑에 문자로 들어가도록 label설정
        date=cal.selectedDate()
        self.lbl.setText(date.toString()) #선택한 날짜를 문자열로 바꾸기

        vbox.addWidget(self.lbl)

        self.setGeometry(300, 100, 900, 900)
        self.setWindowTitle('NCS/EMG')
        self.show()

    def showDate(self,date):
        self.lbl.setText(date.toString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exam()
    sys.exit(app.exec_())