import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox,QMainWindow,QAction,QMenu
from PyQt5.QtCore import QCoreApplication

class Exam(QMainWindow):   #창으로 만들기
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn=QPushButton('입력하세요',self) #버튼을 '입력하세요'로 만듦
        btn.resize(btn.sizeHint())
        btn.setToolTip('<b>결과를 입력하세요<\b>') #버튼에 갔다대면 '누르는 버튼입니다'라고 나옮
        btn.move(10,20) #버튼위치조정
        btn.clicked.connect(QCoreApplication.instance().quit) #버튼을 누르면 실행되는 동작 설정:끝내기(quit)

        self.statusBar()
        self.statusBar().showMessage("판독기입니다")

        menu=self.menuBar() #메뉴바 추가하기
        menu_file=menu.addMenu('NCS/EMG') #NCS/EMG메뉴 그룹 추가
        menu_edit=menu.addMenu('EP') #EP메뉴 그룹 추가
        menu_add1=menu.addMenu('Blink') #Blink메뉴 그룹 추가
        menu_add2=menu.addMenu('ANSFT') #ANSFT메뉴 그룹 추가
        menu_view=menu.addMenu('View') #View메뉴 그룹 추가

        file_exit=QAction('Exit',self) #메뉴 객체 생성
        file_exit.setShortcut('Ctrl+Q')
        file_exit.setStatusTip('누르면 종료')
        new_txt=QAction("NCS",self)
        new_py=QAction("EMG",self)
        view_stat=QAction('상태표시줄',self,checkable=True) #체크박스 활성화 하기위한 버튼 추가
        view_stat.setChecked(True) #체크박스가 True로 체크된 상태로 default상태 만듦

        file_exit.triggered.connect(QCoreApplication.instance().quit) #file_exit에 할당된 버튼 누르면 종료됨
        view_stat.triggered.connect(self.tglstat)

        file_new=QMenu('New',self)

        file_new.addAction(new_txt)
        file_new.addAction(new_py) #file_new(new)밑으로 텍스트, 파이썬파일을 넣기

        menu_file.addMenu(file_new) #메뉴등록(Rt median sensory 하위 항목으로 new넣기)
        menu_file.addAction(file_exit)
        menu_view.addAction(view_stat)

        self.resize(400,1200)
        self.setGeometry(300,100,1200,900) #창크기 조절, 가로 400, 세로 500, 왼쪽에서
        self.setWindowTitle('NCS/EMG판독기') #창 제목 붙이기
        self.show()

    def tglstat(self,state):
        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()

    def closeEvent(self, QCloseEvent):
        ans=QMessageBox.question(self,"종료 확인","종료하시겠습니까?",QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes) #종료버튼 누르면 종료확인 메세지 나오게
        if ans==QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()  #종료메세지에서 yes누를때는 꺼지고 no누르면 안꺼지게


app=QApplication(sys.argv)
w=Exam()
sys.exit(app.exec_()) #종료할때 하는것,app.exec는 이벤트처리를 위한 루프를 실행하는것