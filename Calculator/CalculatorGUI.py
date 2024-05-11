from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(386, 459)
        MainWindow.setMinimumSize(QtCore.QSize(386, 459))
        MainWindow.setMaximumSize(QtCore.QSize(386, 459))
        font = QtGui.QFont()
        font.setPointSize(6)
        MainWindow.setFont(font)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sonuc = QtWidgets.QLabel(self.centralwidget)
        self.sonuc.setGeometry(QtCore.QRect(0, 10, 381, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(32)
        self.sonuc.setFont(font)
        self.sonuc.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sonuc.setObjectName("sonuc")
        self.isaretdegis = QtWidgets.QPushButton(self.centralwidget)
        self.isaretdegis.setGeometry(QtCore.QRect(4, 380, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.isaretdegis.setFont(font)
        self.isaretdegis.setObjectName("isaretdegis")
        self.sifir = QtWidgets.QPushButton(self.centralwidget)
        self.sifir.setGeometry(QtCore.QRect(99, 380, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.sifir.setFont(font)
        self.sifir.setObjectName("sifir")
        self.esittir = QtWidgets.QPushButton(self.centralwidget)
        self.esittir.setGeometry(QtCore.QRect(289, 381, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.esittir.setFont(font)
        self.esittir.setStyleSheet("background-color: rgb(0, 232, 0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.esittir.setObjectName("esittir")
        self.virgul = QtWidgets.QPushButton(self.centralwidget)
        self.virgul.setGeometry(QtCore.QRect(194, 380, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.virgul.setFont(font)
        self.virgul.setObjectName("virgul")
        self.yuzde = QtWidgets.QPushButton(self.centralwidget)
        self.yuzde.setGeometry(QtCore.QRect(99, 100, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.yuzde.setFont(font)
        self.yuzde.setStyleSheet("color: rgb(0, 177, 0);")
        self.yuzde.setObjectName("yuzde")
        self.gerial = QtWidgets.QPushButton(self.centralwidget)
        self.gerial.setGeometry(QtCore.QRect(289, 100, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.gerial.setFont(font)
        self.gerial.setStyleSheet("color: rgb(34, 109, 28)")
        self.gerial.setObjectName("gerial")
        self.bolme = QtWidgets.QPushButton(self.centralwidget)
        self.bolme.setGeometry(QtCore.QRect(194, 100, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.bolme.setFont(font)
        self.bolme.setStyleSheet("color: rgb(0, 177, 0);")
        self.bolme.setObjectName("bolme")
        self.temizle = QtWidgets.QPushButton(self.centralwidget)
        self.temizle.setGeometry(QtCore.QRect(4, 100, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.temizle.setFont(font)
        self.temizle.setStyleSheet("color: rgb(227, 0, 0);\n"
"")
        self.temizle.setObjectName("temizle")
        self.sekiz = QtWidgets.QPushButton(self.centralwidget)
        self.sekiz.setGeometry(QtCore.QRect(99, 170, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.sekiz.setFont(font)
        self.sekiz.setObjectName("sekiz")
        self.carpma = QtWidgets.QPushButton(self.centralwidget)
        self.carpma.setGeometry(QtCore.QRect(289, 170, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.carpma.setFont(font)
        self.carpma.setStyleSheet("color: rgb(0, 177, 0);")
        self.carpma.setObjectName("carpma")
        self.dokuz = QtWidgets.QPushButton(self.centralwidget)
        self.dokuz.setGeometry(QtCore.QRect(194, 170, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.dokuz.setFont(font)
        self.dokuz.setObjectName("dokuz")
        self.yedi = QtWidgets.QPushButton(self.centralwidget)
        self.yedi.setGeometry(QtCore.QRect(4, 170, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.yedi.setFont(font)
        self.yedi.setObjectName("yedi")
        self.bes = QtWidgets.QPushButton(self.centralwidget)
        self.bes.setGeometry(QtCore.QRect(99, 240, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.bes.setFont(font)
        self.bes.setObjectName("bes")
        self.cikarma = QtWidgets.QPushButton(self.centralwidget)
        self.cikarma.setGeometry(QtCore.QRect(289, 240, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(30)
        self.cikarma.setFont(font)
        self.cikarma.setStyleSheet("color: rgb(0, 177, 0);")
        self.cikarma.setObjectName("cikarma")
        self.alti = QtWidgets.QPushButton(self.centralwidget)
        self.alti.setGeometry(QtCore.QRect(194, 240, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.alti.setFont(font)
        self.alti.setObjectName("alti")
        self.dort = QtWidgets.QPushButton(self.centralwidget)
        self.dort.setGeometry(QtCore.QRect(4, 240, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.dort.setFont(font)
        self.dort.setObjectName("dort")
        self.iki = QtWidgets.QPushButton(self.centralwidget)
        self.iki.setGeometry(QtCore.QRect(99, 310, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.iki.setFont(font)
        self.iki.setObjectName("iki")
        self.toplama = QtWidgets.QPushButton(self.centralwidget)
        self.toplama.setGeometry(QtCore.QRect(289, 310, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.toplama.setFont(font)
        self.toplama.setStyleSheet("color: rgb(0, 177, 0);")
        self.toplama.setObjectName("toplama")
        self.uc = QtWidgets.QPushButton(self.centralwidget)
        self.uc.setGeometry(QtCore.QRect(194, 310, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.uc.setFont(font)
        self.uc.setObjectName("uc")
        self.bir = QtWidgets.QPushButton(self.centralwidget)
        self.bir.setGeometry(QtCore.QRect(4, 310, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.bir.setFont(font)
        self.bir.setObjectName("bir")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hesap Makinesi"))
        self.sonuc.setText(_translate("MainWindow", "0"))
        self.isaretdegis.setText(_translate("MainWindow", "+/-"))
        self.sifir.setText(_translate("MainWindow", "0"))
        self.esittir.setText(_translate("MainWindow", "="))
        self.virgul.setText(_translate("MainWindow", "."))
        self.yuzde.setText(_translate("MainWindow", "%"))
        self.gerial.setText(_translate("MainWindow", "←"))
        self.bolme.setText(_translate("MainWindow", "÷"))
        self.temizle.setText(_translate("MainWindow", "C"))
        self.sekiz.setText(_translate("MainWindow", "8"))
        self.carpma.setText(_translate("MainWindow", "x"))
        self.dokuz.setText(_translate("MainWindow", "9"))
        self.yedi.setText(_translate("MainWindow", "7"))
        self.bes.setText(_translate("MainWindow", "5"))
        self.cikarma.setText(_translate("MainWindow", "-"))
        self.alti.setText(_translate("MainWindow", "6"))
        self.dort.setText(_translate("MainWindow", "4"))
        self.iki.setText(_translate("MainWindow", "2"))
        self.toplama.setText(_translate("MainWindow", "+"))
        self.uc.setText(_translate("MainWindow", "3"))
        self.bir.setText(_translate("MainWindow", "1"))
