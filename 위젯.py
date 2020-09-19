import sys
from PyQt5.QtWidgets import QWidget,QCheckBox,QApplication
from PyQt5.QtCore import Qt

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb=QCheckBox('Show title',self)
        cb.move(20,20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 100, 900, 900)
        self.setWindowTitle('NCS/EMG')
        self.show()

    def changeTitle(self,state): # Show title옆에 체크하면 title나오고 체크 없애면 타이틀 안나오게 만듦
        if state==Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exam()
    sys.exit(app.exec_())