# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mail.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 41, 31))
        self.label.setObjectName("label")
        self.txtTo = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTo.setGeometry(QtCore.QRect(70, 30, 681, 31))
        self.txtTo.setObjectName("txtTo")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 41, 31))
        self.label_2.setObjectName("label_2")
        self.txtTitle = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTitle.setGeometry(QtCore.QRect(70, 70, 681, 31))
        self.txtTitle.setObjectName("txtTitle")
        self.txtAtt = QtWidgets.QLineEdit(self.centralwidget)
        self.txtAtt.setGeometry(QtCore.QRect(80, 110, 681, 31))
        self.txtAtt.setObjectName("txtAtt")
        self.btnAtt = QtWidgets.QPushButton(self.centralwidget)
        self.btnAtt.setGeometry(QtCore.QRect(0, 110, 75, 23))
        self.btnAtt.setObjectName("btnAtt")
        self.txtCont = QtWidgets.QTextEdit(self.centralwidget)
        self.txtCont.setGeometry(QtCore.QRect(10, 150, 751, 361))
        self.txtCont.setObjectName("txtCont")
        self.btnReset = QtWidgets.QPushButton(self.centralwidget)
        self.btnReset.setGeometry(QtCore.QRect(10, 530, 75, 23))
        self.btnReset.setObjectName("btnReset")
        self.btnSend = QtWidgets.QPushButton(self.centralwidget)
        self.btnSend.setGeometry(QtCore.QRect(690, 530, 75, 23))
        self.btnSend.setObjectName("btnSend")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "메일전송"))
        self.label.setText(_translate("MainWindow", "받는이"))
        self.label_2.setText(_translate("MainWindow", "제목"))
        self.btnAtt.setText(_translate("MainWindow", "파일첨부"))
        self.btnReset.setText(_translate("MainWindow", "초기화"))
        self.btnSend.setText(_translate("MainWindow", "전송"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
