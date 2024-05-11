import sys
from PyQt5 import QtWidgets as qtw
from CalculatorGUI import Ui_MainWindow

class Uygulama(qtw.QMainWindow):
    sayi=None
    sayi2=False
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.sifir.clicked.connect(self.basmak)
        self.ui.bir.clicked.connect(self.basmak)    
        self.ui.iki.clicked.connect(self.basmak)
        self.ui.uc.clicked.connect(self.basmak)
        self.ui.dort.clicked.connect(self.basmak)
        self.ui.bes.clicked.connect(self.basmak)
        self.ui.alti.clicked.connect(self.basmak)
        self.ui.yedi.clicked.connect(self.basmak)
        self.ui.sekiz.clicked.connect(self.basmak)
        self.ui.dokuz.clicked.connect(self.basmak)
        self.ui.esittir.clicked.connect(self.hesapla)
        self.ui.carpma.clicked.connect(self.matematik)
        self.ui.bolme.clicked.connect(self.matematik)
        self.ui.cikarma.clicked.connect(self.matematik)
        self.ui.toplama.clicked.connect(self.matematik)
        self.ui.isaretdegis.clicked.connect(self.isaret)
        self.ui.gerial.clicked.connect(self.geri)
        self.ui.yuzde.clicked.connect(self.yuzde)
        self.ui.temizle.clicked.connect(self.temiz)
        self.ui.virgul.clicked.connect(self.ondalik)

        self.ui.toplama.setCheckable(True)
        self.ui.cikarma.setCheckable(True)
        self.ui.carpma.setCheckable(True)
        self.ui.bolme.setCheckable(True)
        self.ui.esittir.setCheckable(True)


    def basmak(self):
        buton=self.sender()
        if((self.sayi2) and (self.ui.esittir.isChecked())):
            self.ui.sonuc.setText(format(float(buton.text()),'.15g'))
            self.sayi2=True
            self.ui.esittir.setChecked(False)
        elif ((self.ui.toplama.isChecked() or self.ui.cikarma.isChecked() or self.ui.carpma.isChecked() or self.ui.bolme.isChecked()) and (not self.sayi2)):
            self.ui.sonuc.setText(format(float(buton.text()),'.15g'))
            self.sayi2=True
        else:
            if(("." in self.ui.sonuc.text() and buton.text()=="0")):
                self.ui.sonuc.setText(format(float(self.ui.sonuc.text()+ buton.text())))
            else:
                self.ui.sonuc.setText(format(float(self.ui.sonuc.text()+ buton.text()),".15g"))

    def ondalik(self):
        if "." not in self.ui.sonuc.text():
            self.ui.sonuc.setText(self.ui.sonuc.text()+ ".")

    def isaret(self):
        deger=float(self.ui.sonuc.text())*-1
        self.ui.sonuc.setText(format(deger,".15g"))

    def yuzde(self):
        deger=float(self.ui.sonuc.text())*0.01
        self.ui.sonuc.setText(format(deger,".15g"))

    def temiz(Self):
        Self.sayi=0
        Self.sayi2=False
        Self.ui.sonuc.setText("0")
        Self.ui.toplama.setChecked(False)
        Self.ui.cikarma.setChecked(False)
        Self.ui.bolme.setChecked(False)
        Self.ui.carpma.setChecked(False)
        Self.ui.esittir.setChecked(False)

    def matematik(self):
        buton=self.sender()
        self.sayi=float(self.ui.sonuc.text())
        buton.setChecked(True)
        if buton.text() == 'x':
            self.ui.sonuc.setText('x')
        elif buton.text()=="÷":
            self.ui.sonuc.setText("÷")
        elif buton.text()=="+":
            self.ui.sonuc.setText("+")
        elif buton.text()=="-":
            self.ui.sonuc.setText("-")

    def hesapla(self):
        self.sayi2=float(self.ui.sonuc.text())
        if self.ui.toplama.isChecked():
            yenideger=round((self.sayi+self.sayi2))
            self.ui.sonuc.setText(format(yenideger))
            self.ui.toplama.setChecked(False)
        elif self.ui.cikarma.isChecked():
            yenideger=round((self.sayi-self.sayi2),2)
            self.ui.sonuc.setText(format(yenideger))
            self.ui.cikarma.setChecked(False)
        elif self.ui.carpma.isChecked():
            yenideger=round((self.sayi*self.sayi2),2)
            self.ui.sonuc.setText(format(yenideger))
            self.ui.carpma.setChecked(False)
        elif self.ui.bolme.isChecked():
            yenideger=round((self.sayi/self.sayi2),2)
            self.ui.sonuc.setText(format(yenideger))
            self.ui.bolme.setChecked(False)

        self.sayi=yenideger
        self.ui.esittir.setChecked(True)

    def geri(self):
        text = self.ui.sonuc.text()
        self.ui.sonuc.setText(text[:-1])

def app():
    app=qtw.QApplication(sys.argv)
    win=Uygulama()
    win.show()
    sys.exit(app.exec_())
app()