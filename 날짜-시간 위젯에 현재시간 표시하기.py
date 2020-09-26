import sys, datetime
import date_1
from PyQt5.QtWidgets import QWidget,QApplication

class main(QWidget, date_1.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnNow.clicked.connect(self.now)
        self.btnTime.clicked.connect(self.time)
        self.btnDate.clicked.connect(self.date)
        self.btnAll.clicked.connect(self.all)

        #self.timeEdit.setDisplayFormat("AP h:mm")
        self.timeEdit.setDisplayFormat("hh:mm:ss")

    def now(self):
        now=datetime.datetime.now()
        self.dateTimeEdit.setDateTime(now)
        #self.dateEdit.setDate(datetime.date(2019,4,5))
        self.dateEdit.setDate(now.today())
        self.timeEdit.setTime(now.time())

    def time(self):
        now=datetime.datetime.now()
        #self.lineEdit.setText(self.timeEdit.text())
        self.lineEdit.setText(now.strftime("%H:%M:%S"))

    def date(self):
        now=datetime.datetime.now()
        #self.lineEdit.setText(self.dateEdit.text())
        self.lineEdit.setText(now.strftime("%Y-%m-%d")) #대문자 Y는 연도를 4자리로, y는 2자리로

    def all(self):
        now=datetime.datetime.now()
        #self.lineEdit.setText(self.dateTimeEdit.text())
        self.lineEdit.setText(now.strftime("%Y-%m-%d\n"
                                           "%H:%M:%S"))

app = QApplication([])
ex = main()
ex.show()
sys.exit(app.exec_())