from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, QCoreApplication
from PyQt5.QtWidgets import QLabel


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1009, 681)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.baton = QtWidgets.QPushButton(self.centralwidget)
        self.baton.setGeometry(QtCore.QRect(410, 560, 71, 31))
        self.baton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.baton.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                 "border: none")
        self.baton.setText("")
        self.baton.setObjectName("baton")
        self.kolbasa = QtWidgets.QPushButton(self.centralwidget)
        self.kolbasa.setGeometry(QtCore.QRect(550, 390, 41, 21))
        self.kolbasa.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kolbasa.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                   "border: none")
        self.kolbasa.setText("")
        self.kolbasa.setObjectName("kolbasa")
        self.tort = QtWidgets.QPushButton(self.centralwidget)
        self.tort.setGeometry(QtCore.QRect(610, 80, 41, 31))
        self.tort.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tort.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                "border: none")
        self.tort.setText("")
        self.tort.setObjectName("tort")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 90, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(810, 550, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(350, 420, 421, 131))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "border: none")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(470, 520, 301, 91))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "border: none")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(350, 120, 421, 251))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "border: none")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(350, 10, 251, 141))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "border: none")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(640, 10, 131, 141))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "border: none")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(350, 560, 61, 51))
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                         "border: none")
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(350, 350, 191, 81))
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                         "border: none")
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(590, 350, 181, 81))
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                         "border: none")
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 250, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 81, 81))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("photo_2023-05-1опр7_18имс-32-34.jpgе.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 140, 91, 91))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("photo_2023-05-роапрап18-32-34.jpgе.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 150, 101, 101))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("photo_2023-05-1опр7_1по8-32-34.jpgе.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(340, 10, 451, 611))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("photo_2023-05-17_18-25-48.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.wa = QtWidgets.QLabel(self.centralwidget)
        self.wa.setGeometry(QtCore.QRect(60, 320, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wa.setFont(font)
        self.wa.setObjectName("wa")
        self.ra = QtWidgets.QLabel(self.centralwidget)
        self.ra.setGeometry(QtCore.QRect(60, 320, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ra.setFont(font)
        self.ra.setObjectName("ra")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(370, 250, 261, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("\n"
                                   "background-color: rgb(158, 235, 199);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(370, 250, 281, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("\n"
                                   "\n"
                                   "background-color: rgb(243, 133, 144);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(170, 260, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 620, 61, 181))
        self.label_10.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
                                    "font: 6pt \"MS Shell Dlg 2\";\n"
                                    "border: none")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_5.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_6.raise_()
        self.tort.raise_()
        self.baton.raise_()
        self.kolbasa.raise_()
        self.label_10.raise_()
        self.wa.raise_()
        self.ra.raise_()
        self.pushButton_10.raise_()
        self.pushButton_12.raise_()
        self.pushButton_6.raise_()
        self.pushButton_9.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_5.raise_()
        self.pushButton_11.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1009, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.ra.hide()
        self.wa.hide()

        self.label_7.hide()
        self.label_8.hide()

        self.label_7.hidden = True
        self.label_8.hidden = True

        self.ra.hidden = True
        self.wa.hidden = True

        self.baton.clicked.connect(self.sh_ra)
        self.kolbasa.clicked.connect(self.sh_ra)
        self.tort.clicked.connect(self.sh_ra)
        self.pushButton_5.clicked.connect(self.sh_wa)
        self.pushButton_6.clicked.connect(self.sh_wa)
        self.pushButton_7.clicked.connect(self.sh_wa)
        self.pushButton_8.clicked.connect(self.sh_wa)
        self.pushButton_9.clicked.connect(self.sh_wa)
        self.pushButton_10.clicked.connect(self.sh_wa)
        self.pushButton_11.clicked.connect(self.sh_wa)
        self.pushButton_12.clicked.connect(self.sh_wa)
        self.pushButton.clicked.connect(self.agn)


    def agn(self):
        self.label_8.hide()
        self.label_8.hidden = True
        self.label_7.hide()
        self.label_7.hidden = True
        self.label_9.setText("3")
        self.label_10.setText('0')

    sch = 0

    def sh_ra(self, sch):
        self.ra.show()
        self.ra.hidden = False
        self.wa.hide()
        self.wa.hidden = True
        content = self.label_10.text()
        content = int(content)
        if content == 2:
            self.label_7.show()
            self.label_7.hidden = False

        else:
            content = int(content) + 1
            content = str(content)
            self.label_10.setText(content)
            if content == 3:
                self.label_7.show()
                self.label_7.hidden = False

    def sh_wa(self):
        self.wa.show()
        self.wa.hidden = False
        self.ra.hide()
        self.ra.hidden = True
        content = self.label_9.text()
        content = int(content)
        if content != 1:
            content = int(content) - 1
            content = str(content)
            self.label_9.setText(content)
            if content == 1:
                self.label_8.show()
                self.label_8.hidden = False
        else:
            self.label_8.show()
            self.label_8.hidden = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Найдите спрятанные предметы "))
        self.pushButton.setText(_translate("MainWindow", "Попробовать снова"))
        self.label.setText(_translate("MainWindow", "Осталось попыток: "))
        self.wa.setText(_translate("MainWindow", "Неправильно! Попробуйте еще раз!"))
        self.ra.setText(_translate("MainWindow", "Правильно! Продолжай в том же духе!"))
        self.label_7.setText(_translate("MainWindow", "           Вы выиграли!"))
        self.label_8.setText(_translate("MainWindow", "           Вы проиграли!"))
        self.label_9.setText(_translate("MainWindow", "3"))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"0", None))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
