import sys,pickle
from PyQt5.QtWidgets import QApplication,QWidget,QTableWidget,QTableWidgetItem,QVBoxLayout,QPushButton

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.size=4 #table size를 지정, 4칸테이블
        self.initUI()

    def initUI(self):
        self.setWindowTitle('NCS/EMG')
        self.setGeometry(50,50,660,240)

        self.createTable() #테이블 생성
        self.btn=QPushButton('저장')
        self.btn.clicked.connect(on_cl)

        self.layout=QVBoxLayout()
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.btn)

        self.setLayout(self.layout)
        self.show()

    def createTable(self):
        self.table=QTableWidget()
        self.table.setRowCount(self.size)
        self.table.setColumnCount(self.size)
        self.table.setHorizontalHeaderLabels(('이름','A','B','C'))
        try: #예외처리, open함수로 out.txt파일을 읽기모드(rb)로 불러옴, out.txt파일이 없으면 except구간으로 이동함
            fp=open('out.txt','rb')
            for r in range(self.size):
                for c in range(self.size):
                    self.table.setItem(r,c,
                                       QTableWidgetItem(str(pickle.load(fp)))) #중복값을 차례로 읽어오고 테이블에 차례로 세팅함
                fp.close()  #파일을 읽어오면 반드시 닫아줄것.
        except:
            for r in range(self.size):
                for c in range(self.size):
                    self.table.setItem(r,c,QTableWidgetItem("")) #불러들일게 없으면 공백으로 모든셀을 초기화 시킴
def on_cl():
    fp=open('out.txt','wb')
    for r in range(ex.size):
        for c in range(ex.size):
            pickle.dump(ex.table.item(r,c).text(),fp) #셀의 텍스트값을 파일에 쓰고 파일을 닫아줌
    fp.close()

if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=Exam()
    sys.exit(app.exec_())
