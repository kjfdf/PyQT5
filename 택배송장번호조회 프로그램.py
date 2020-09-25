import sys
from PyQt5.QtWidgets import *
from deliv import Ui_MainWindow #QtDesigner로 만든 class에서 form을 import해서 기본형태로 사용
import os
import webbrowser as web #import문을 한줄에 1개씩 PEP8방식으로 도입


class main(QWidget,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.rds=[]
        self.url=[]
        self.path="data.txt"

        self.set_ui()
        self.set_slot()

    def set_ui(self): #체크된 부분을 빠르게 찾기위해 리스트안에 넣어주는것
        self.rds.append(self.rdHan) #택배배송조회 사이트에서 배송넘버를 {}로 비워두고 채우기
        self.url.append(
            'http://www.hanjin.co.kr/Delivery_html/inquiry/result_waybill.jsp?wbl_num={}')
        self.rds.append(self.rdCJ)
        self.url.append(
            'http://www.doortodoor.co.kr/parcel/doortodoor.do?'+
            'fsp_action=PARC_ACT_002&fsp_cmd=retrieveInvNoACT&invc_no={}')
        self.rds.append(self.rdLot)
        self.url.append(
            'http://www.hanjin.co.kr/Delivery_html/inquiry/result_waybill.jsp?wbl_num={}')
        self.rds.append(self.rdLog)
        self.url.append(
            'http://www.hanjin.co.kr/Delivery_html/inquiry/result_waybill.jsp?wbl_num={}')
        self.rds.append(self.rdDhl)
        self.url.append(
            'http://www.hanjin.co.kr/Delivery_html/inquiry/result_waybill.jsp?wbl_num={}')
        self.rds.append(self.rdUps)
        self.url.append(
            'http://www.hanjin.co.kr/Delivery_html/inquiry/result_waybill.jsp?wbl_num={}')
        self.rds.append(self.rdFedex)
        self.url.append(
            'http://www.hanjin.co.kr/Delivery_html/inquiry/result_waybill.jsp?wbl_num={}')

        if os.path.exists(self.path):
            f_in=open(self.path,'r') #파일이 존재하면 읽기모드로 불러옴
            ls=f_in.readlines()
            if len(ls)==2:
                self.txtNum.setText(ls[0].replace('\n',''))
                self.rds[int(ls[1])].setChecked(True)
            f_in.close()

    def set_slot(self):
        self.btnSearch.clicked.connect(self.run)

    def run(self):
        if self.txtNum.text()=='':
            QMessageBox.information(self,"입력오류","송장번호를 입력하세요",
                                    QMessageBox.Yes,QMessageBox.Yes)
            pass
        if not (self.rds[0].isChecked() or self.rds[1].isChecked() or self.rds[2].isChecked()):
            QMessageBox.information(self,"입력오류","택배사를 선택하세요",
                                    QMessageBox.Yes,QMessageBox.Yes)
            pass
        f_out=open(self.path,'w')
        f_out.write(self.txtNum.text()+'\n')
        for i, v in enumerate(self.rds):
            if v.isChecked():
                f_out.write(str(i))
                web.open_new(self.url[i].format(self.txtNum.text()))
        f_out.close()

app = QApplication([])
ex = main()
ex.show()
sys.exit(app.exec_())