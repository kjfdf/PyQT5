import sys
from PyQt5.QtWidgets import (QWidget, QComboBox,QLabel, QApplication, QVBoxLayout)
from PyQt5.QtCore import QDate


class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self): #C-radi, plexo등 아래로 나오게 추가
        self.lbl=QLabel("C-radi",self)
        combo=QComboBox(self)
        combo.addItem("brachial plexo")
        combo.addItem("LS plexo")
        combo.addItem("LS-radi")
        combo.addItem("MND")
        combo.addItem("myopathy")
        combo.addItem("ulnar neuropathy")
        combo.addItem("radial neuropathy")
        combo.addItem("peroneal neuropathy")

        combo.move(10,10)
        self.lbl.move(10,40)

        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300,100,800,800)
        self.setWindowTitle("NCS/EMG")
        self.show()

    def onActivated(self,text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Exam()
    sys.exit(app.exec_())