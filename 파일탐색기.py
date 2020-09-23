import sys, os, shutil
from PyQt5.QtWidgets import QWidget,QApplication,QTreeView,\
    QFileSystemModel, QVBoxLayout, QPushButton,QInputDialog,QLineEdit

class main(QWidget):
    def __init__(self):
        super().__init__()
        self.path="C:"
        self.index=None

        self.tv=QTreeView(self) #C드라이브 하위에 계층화시켜서 표시함
        self.model=QFileSystemModel() #파일구조를 표현함
        self.btnRen=QPushButton("이름바꾸기")
        self.btnDel=QPushButton("파일삭제")
        self.layout=QVBoxLayout() #파일창, 파일삭제창, 이름바꾸기 창을 세로로 배치하기위해

        self.setUi()
        self.setSlot()

    def setUi(self):
        self.setGeometry(300,100,800,800)
        self.setWindowTitle('NCS/EMG')
        self.model.setRootPath(self.path)
        self.tv.setModel(self.model)
        self.tv.setColumnWidth(0,250) #name, size, type등이 있는데 name이 0번째 칼럼으로 폭을 250으로 만들어줘서 네임이 잘보이게 만듦

        self.layout.addWidget(self.tv)
        self.layout.addWidget(self.btnDel)
        self.layout.addWidget(self.btnRen)
        self.setLayout(self.layout)

    def setSlot(self):
        self.tv.clicked.connect(self.setIndex)
        self.btnRen.clicked.connect(self.ren)
        self.btnDel.clicked.connect(self.rm)

    def setIndex(self,index):
        self.index=index

    def ren(self):
        os.chdir(self.model.filePath(self.model.parent(self.index))) #클릭한 파일의 상위 디렉토리를 가리키고 filePath가 그 경로를 구함
        fname=self.model.fileName(self.index)
        text,res=QInputDialog.getText(self,"이름 바꾸기","바꿀 이름을 넣어주세요", #이름바꾸기는 이름바꾸는 창의 제목, 바꿀이름을 넣어주세요는 그 밑에 빈칸위에
                                      QLineEdit.Normal,fname) #바꿀이름 넣을때 기본값으로 기존 파일이름이 들어가도록 fname을 넣어줌
        if res: #이름바꾸고 ok를 누르면 실행되는 함수
            while True:
                self.ok=True
                for i in os.listdir(os.getcwd()): #현재 작업중인 디렉토리의 파일목록을 불러오도록 함.
                    print(i) #디버깅용
                    if i==text: #바꾼 이름과 기존 디렉토리에 있는 파일명과 비교하는것
                        text,res=QInputDialog.getText(self,"중복 오류!",
                                                      "바꿀 이름을 입력하세요.",QLineEdit.Normal, text)
                        if not res:
                            return
                        self.ok=False #바꿀이름을 넣으면 바로 바꾸지 말고 일단 false로 하고 다시 위로 올라감
                if self.ok:
                    break
            os.rename(fname,text) #while문을 벗어나게 되면 이름을 바꿔줌
            
    def rm(self):
        os.chdir(self.model.filePath(self.model.parent(self.index)))
        fname=self.model.fileName(self.index)
        try:
            if not self.model.isDir(self.index):
                os.unlink(fname)
                print(fname+'파일삭제')
            else:
                shutil.rmtree(fname)
                print(fname+'폴더삭제')
        except:
            print('에러발생')

app=QApplication([])
ex=main()
ex.show()
sys.exit(app.exec_())