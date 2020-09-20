import sys, random
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QPainter,QColor,QFont,QPen,QBrush
from PyQt5.QtCore import Qt

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.a='NCS/EMG'
        self.setGeometry(300,100,800,800)
        self.setWindowTitle('NCS/EMG')
        self.show()

    def paintEvent(self,event): #점이나, 텍스트 색, 선색 등 변경시 #을 해제할것
        qp=QPainter()
        qp.begin(self)
        #self.drawText(event,qp)
        # self.drawPoints(qp)
        # self.drawRectangles(qp)
        # self.drawLines(qp)
        # self.drawBrushes(qp)
        qp.end()

    def drawText(self,event,qp):
        qp.setPen(QColor(168,34,3)) #펜의 색깔 지정, RGB값으로 R값이 가장 높으므로 붉은계열 색 나옴
        qp.setFont(QFont('gulim',10))
        qp.drawText(event.rect(),Qt.AlignHCenter,self.a)

    def drawPoints(self,qp): #바탕화면에 점찍어서 나옴
        qp.setPen(Qt.red)
        size = self.size()

        for i in range(1000):
            x=random.randint(0,size.width())
            y=random.randint(0,size.height())
            qp.drawPoint(x, y)

    def drawRectangles(self,qp):
        col=QColor()
        col.setNamedColor('#521E8D')
        qp.setPen(col)

        qp.setBrush(QColor(200,0,0))
        qp.drawRect(10,145,90,60)

        qp.setBrush(QColor(255,80,0,160))
        qp.drawRect(130,45,90,60)

        qp.setBrush(QColor(25,0,90,200))
        qp.drawRect(250,45,90,60)

    def drawLines(self,qp):
        pen=QPen(Qt.black,2,Qt.SolidLine)

        qp.setPen(pen)
        qp.drawLine(20,100,250,100)

        pen.setStyle(Qt.DashLine) #라인을 그릴때마다 펜 스타일 변경, 시작점과 끝점을 설정해줘야함
        qp.setPen(pen)
        qp.drawLine(20, 140, 250, 140)

        pen.setStyle(Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 180, 250, 180)

        pen.setStyle(Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(20, 220, 250, 220)

        pen.setStyle(Qt.DashDotDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 260, 250, 260)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        qp.setPen(pen)
        qp.drawLine(20, 300, 250, 300)

    def drawBrushes(self,qp):
        brush=QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawRect(10,15,90,60)

        brush.setStyle(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(130,15,90,60)

        brush.setStyle(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(250,15,90,60)

        brush.setStyle(Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawRect(10,105,90,60)

        brush.setStyle(Qt.Dense5Pattern)
        qp.setBrush(brush)
        qp.drawRect(130,105,90,60)

        brush.setStyle(Qt.Dense6Pattern)
        qp.setBrush(brush)
        qp.drawRect(250,105,90,60)

        brush.setStyle(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(10,195,90,60)

        brush.setStyle(Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawRect(130,195,90,60)

        brush.setStyle(Qt.Dense7Pattern)
        qp.setBrush(brush)
        qp.drawRect(250,195,90,60)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exam()
    sys.exit(app.exec_())

