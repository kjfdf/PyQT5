import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QMessageBox,QMainWindow,QAction,QMenu,qApp,QHBoxLayout,QVBoxLayout,QApplication,
                             QGridLayout)
from PyQt5.QtCore import QCoreApplication

class Exam(QWidget):   #창으로 만들기
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        grid=QGridLayout() #창안에 작은 버튼으로 여러개 배열시키기
        self.setLayout(grid)

        names=['Rt median sensory','Lt median sensory','Rt median motor','Lt median motor',
               'Rt ulnar sensory','Lt ulnar sensory','Rt ulnar motor','Lt ulnar motor',
               'Rt sural sensory','Lt sural sensory','Rt tibial motor','Lt tibial motor',
               'Rt superficial peroneal sensory','Lt superficial peroneal sensory','Rt peroneal motor at EDB','Lt peroneal motor at EDB',
               'Rt peroneal motor at TA','Lt peroneal motor at TA','','',
               'Rt radial motor','Lt radial motor','Rt superficial radial sensory','Lt superficial radial sensory',
               'Rt medial antebrachial sensory','Lt medial antebrachial sensory','Rt lateral antebrachial sensory','Lt lateral antebrachial sensory',
               'Rt axillary motor','Lt axillary motor','','',
               'Rt musculocutaneous motor','Lt musculocutaneous motor','','',
               'Rt femoral motor','Lt femoral motor','Rt lateral femoral cutaneous','Lt lateral femoral cutaneous',
               'Rt saphenous sensory','Lt saphenous sensory','','',
               'Rt deep peroneal sensory','Lt deep peroneal sensory','','',
               'Rt medial plantar sensory','Lt medial plantar sensory','Rt lateral plantar sensory','Lt lateral plantar sensory']

        positions=[(i,j) for i in range(13) for j in range(4)] #i행, j열만큼으로 배열시킴

        for position, name in zip(positions,names):
            if name=='':
                continue
            button=QPushButton(name)
            grid.addWidget(button,*position)

        self.move(300,150)
        self.setWindowTitle('NCS/EMG')
        self.show()

if __name__== '__main__':
    app = QApplication(sys.argv)
    w = Exam()
    sys.exit(app.exec_())