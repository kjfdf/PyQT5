import sys
from PyQt5.QtWidgets import (QWidget,QLabel,QLineEdit,
                             QTextEdit,QGridLayout,QApplication)

class Exam(QWidget):   #창으로 만들기
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        title=QLabel('Title')  #Title, author, review옆에 빈칸 넣기
        author=QLabel('Author')
        review=QLabel('Review')

        titleEdit=QLineEdit()
        authorEdit=QLineEdit()
        reviewEdit=QLineEdit()

        grid=QGridLayout()
        grid.setSpacing(10) #label과 edit사이의 공간, title/author/review사이의 공간 10

        grid.addWidget(title,1,0)
        grid.addWidget(titleEdit,1,1)

        grid.addWidget(author,2,0)
        grid.addWidget(authorEdit,2,1)

        grid.addWidget(review,3,0)
        grid.addWidget(reviewEdit,3,1,5,2) #칸에 쓸수있는 문자의 줄수가 3줄인데 5줄로 만듦,

        self.setLayout(grid)

        self.setGeometry(300, 100, 1200, 900)  # 창크기 조절, 가로 400, 세로 500, 왼쪽에서
        self.setWindowTitle('NCS/EMG판독기')  # 창 제목 붙이기
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Exam()
    sys.exit(app.exec_())