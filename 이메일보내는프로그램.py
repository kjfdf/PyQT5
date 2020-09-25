import sys,os,mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from smtplib import SMTP_SSL
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class main(QWidget,mail.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        super().setupUi(self) #ui함수에 setupUi를 호출해서 기본 레이아웃 구성
        #https://myaccount.google.com/security -> 이 주소로 들어가서 보안수준이 낮은 앱 허용:사용으로 설정해야함
        self.server="smtp.gmail.com"
        self.port=465
        self.id="kjfdf1"
        self.pw=dbdlfgks2
        self.setUi()
        self.setSlot()

        def setUi(self):
            self.txtAtt.setReadOnly(True)  # 내용을 수정할 수 없도록 읽기전용으로 만들어줌

        def setSlot(self):
            self.btnAtt.clicked.connect(self.selectFile)
            self.btnReset.clicked.connect(self.reset)
            self.btnSend.clicked.connect(self.send)

        def selectFile(self):
            att = QFileDialog.getOpenFileName(self, "파일선택")[0]  # 파일선택을 누르면 튜플중에서 0번째 값인 파일 경로만 불러옴
            if not att == '':  # 선택하지 않으면 빈칸이므로 빈칸이 아닐 경우에만 값을 불러옴
                self.txtAtt.setText(att)

        def reset(self):  # 어떤값이 입력되어있어도 reset을 누르면 빈칸으로 만들어줌
            self.txtAtt.setText('')
            self.txtCont.setText('')
            self.txtTitle.setText('')
            self.txtTo.setText('')

        def send(self):
            add = self.txtTo.text()
            title = self.txtTitle.text()
            cont = self.txtCont.toPlainText()
            att = False if self.txtAtt.text() == '' else self.txtAtt.text()
            msg = MIMEMultipart('mixed') if att else MIMEMultipart('alternative')
            msg['From'] = 'aaa'
            msg['To'] = add
            msg['subject'] = title
            msg.attach(MIMEText(cont))

            if att:
                file_data = MIMEBase('application', 'octet-stream')
                f = open(att, 'rb')
                file_contents = f.read()
                file_data.set_payload(file_contents)
                encoders.encode_base64(file_data)

                file_data.add_header('Content-Disposition', 'attachment', filename=os.path.basename(att))
                msg.attach(file_data)

            smtp = SMTP_SSL(self.server, self.port)
            smtp.login(self.id, self.pw)
            smtp.sendmail(self.id + "@gmail.com", add, msg.as_string())
            smtp.close()

app=QApplication([])
ex=main()
ex.show()
sys.exit(app.exec_())