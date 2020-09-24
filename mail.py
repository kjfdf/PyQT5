import sys,os,mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from smtplib import SMTP_SSL
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class main(QWidget,mail.Ui_Form):
    def __init__(self):
        super().__init()
        super().setupUi(self) #ui함수에 setupUi를 호출해서 기본 레이아웃 구성
        #https://myaccount.google.com/security -> 이 주소로 들어가서 보안수준이 낮은 앱 허용:사용으로 설정해야함
        self.server="smtp.gmail.com"
        self.port=465
        self.id="kjfdf1"
        self.pw=dbdlfgks2
        self.setUi()
        self.setSlot()

    def setUi(self):
        self.txtAtt.setReadOnly(True) #내용을 수정할 수 없도록 읽기전용으로 만들어줌

    def setSlot(self):
        self.btnAtt.clicked.connect(self.selectFile)
        self.btnReset.clicked.connect(self.reset)
        self.btnSend.clicked.connect(self.send)

    def selectFile(self):
        att=QFileDialog.getOpenFileName(self,"파일선택")[0] #파일선택을 누르면 튜플중에서 0번째 값인 파일 경로만 불러옴
        if not att=='': #선택하지 않으면 빈칸이므로 빈칸이 아닐 경우에만 값을 불러옴
            self.txtAtt.setText(att)

    def reset(self):  #어떤값이 입력되어있어도 reset을 누르면 빈칸으로 만들어줌
        self.txtAtt.setText('')
        self.txtCont.setText('')
        self.txtTitle.setText('')
        self.txtTo.setText('')

    def send(self):
        add=self.txtTo.text()
        title=self.txtTitle.text()
        cont=self.txtCont.toPlainText()
        att=False if self.txtAtt.text()=='' else self.txtAtt.text()
        msg=MIMEMultipart('mixed') if att else MIMEMultipart('alternative')
        msg['From']='aaa'
        msg['To']=add
        msg['subject']=title
        msg.attach(MIMEText(cont))

        if att:
            file_data=MIMEBase('application','octet-stream')
            f=open(att,'rb')
            file_contents=f.read()
            file_data.set_payload(file_contents)
            encoders.encode_base64(file_data)

            file_data.add_header('Content-Disposition', 'attachment',filename=os.path.basename(att))
            msg.attach(file_data)

        smtp=SMTP_SSL(self.server,self.port)
        smtp.login(self.id,self.pw)
        smtp.sendmail(self.id+"@gmail.com",add,msg.as_string())
        smtp.close()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 41, 31))
        self.label.setObjectName("label")
        self.txtTo = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTo.setGeometry(QtCore.QRect(70, 30, 681, 31))
        self.txtTo.setObjectName("txtTo")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 41, 31))
        self.label_2.setObjectName("label_2")
        self.txtTitle = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTitle.setGeometry(QtCore.QRect(70, 70, 681, 31))
        self.txtTitle.setObjectName("txtTitle")
        self.txtAtt = QtWidgets.QLineEdit(self.centralwidget)
        self.txtAtt.setGeometry(QtCore.QRect(80, 110, 681, 31))
        self.txtAtt.setObjectName("txtAtt")
        self.btnAtt = QtWidgets.QPushButton(self.centralwidget)
        self.btnAtt.setGeometry(QtCore.QRect(0, 110, 75, 23))
        self.btnAtt.setObjectName("btnAtt")
        self.txtCont = QtWidgets.QTextEdit(self.centralwidget)
        self.txtCont.setGeometry(QtCore.QRect(10, 150, 751, 361))
        self.txtCont.setObjectName("txtCont")
        self.btnReset = QtWidgets.QPushButton(self.centralwidget)
        self.btnReset.setGeometry(QtCore.QRect(10, 530, 75, 23))
        self.btnReset.setObjectName("btnReset")
        self.btnSend = QtWidgets.QPushButton(self.centralwidget)
        self.btnSend.setGeometry(QtCore.QRect(690, 530, 75, 23))
        self.btnSend.setObjectName("btnSend")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "메일전송"))
        self.label.setText(_translate("MainWindow", "받는이"))
        self.label_2.setText(_translate("MainWindow", "제목"))
        self.btnAtt.setText(_translate("MainWindow", "파일첨부"))
        self.btnReset.setText(_translate("MainWindow", "초기화"))
        self.btnSend.setText(_translate("MainWindow", "전송"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
