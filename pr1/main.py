
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QLineEdit)
import wykres
import numpy as np

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
    #widgety
        #wykres
        Wykres = wykres.TestWindow()
        npoints = 1000000
        xdata = np.linspace(0., 10., npoints)
        Wykres.add_data(xdata, np.sin(xdata))
        Wykres.add_data(xdata, np.cos(xdata))
        Wykres.set_title("Simple example with %d curves of %d points " \
                     "(OpenGL Accelerated Series)" \
                     % (Wykres.ncurves, npoints))
        Wykres.setWindowTitle("Simple performance example")
        Wykres.show()
        Wykres.resize(500, 500)

        mapa = QPushButton("mapa")
        kompas = QPushButton("kompas")
        up = QPushButton("W")
        down = QPushButton("S")
        left = QPushButton("A")
        right = QPushButton("D")
        P1_disp = QLineEdit("P")
        P1_add = QPushButton()
        P1_sub = QPushButton()
        I1_disp = QLineEdit("I")
        I1_add = QPushButton()
        I1_sub = QPushButton()
        D1_disp = QLineEdit("D")
        D1_add = QPushButton()
        D1_sub = QPushButton()
        P2_disp = QLineEdit("P")
        P2_add = QPushButton()
        P2_sub = QPushButton()
        I2_disp = QLineEdit("I")
        I2_add = QPushButton()
        I2_sub = QPushButton()
        D2_disp = QLineEdit("D")
        D2_add = QPushButton()
        D2_sub = QPushButton()

    #P1
        P1 = QVBoxLayout()
        P1.addWidget(P1_add)
        P1.addWidget(P1_disp)
        P1.addWidget(P1_sub)

    #I1
        I1 = QVBoxLayout()
        I1.addWidget(I1_add)
        I1.addWidget(I1_disp)
        I1.addWidget(I1_sub)

    #D1
        D1 = QVBoxLayout()
        D1.addWidget(D1_add)
        D1.addWidget(D1_disp)
        D1.addWidget(D1_sub)

    # P2
        P2 = QVBoxLayout()
        P2.addWidget(P2_add)
        P2.addWidget(P2_disp)
        P2.addWidget(P2_sub)

    #I2
        I2 = QVBoxLayout()
        I2.addWidget(I2_add)
        I2.addWidget(I2_disp)
        I2.addWidget(I2_sub)

    #D2
        D2 = QVBoxLayout()
        D2.addWidget(D2_add)
        D2.addWidget(D2_disp)
        D2.addWidget(D2_sub)

    #strzalki
        strzalki_gora = QHBoxLayout()
        strzalki_gora.addSpacing(100)
        strzalki_gora.addWidget(up)
        strzalki_gora.addSpacing(100)

        strzalki_dol = QHBoxLayout()
        strzalki_dol.addWidget(left)
        strzalki_dol.addWidget(down)
        strzalki_dol.addWidget(right)

        strzalki = QVBoxLayout()
        strzalki.addLayout(strzalki_gora)
        strzalki.addLayout(strzalki_dol)

    #pidy
        pidy_gora = QHBoxLayout()
        pidy_gora.addLayout(P1)
        pidy_gora.addLayout(I1)
        pidy_gora.addLayout(D1)

        pidy_dol = QHBoxLayout()
        pidy_dol.addLayout(P2)
        pidy_dol.addLayout(I2)
        pidy_dol.addLayout(D2)

        pidy = QVBoxLayout()
        pidy.addLayout(pidy_gora)
        pidy.addLayout(pidy_dol)

    #gorna linia aplikacji
        hbox1 = QHBoxLayout()
        #hbox1.addStretch(1)
        hbox1.addWidget(Wykres)
        hbox1.addWidget(mapa)


    #dolna linia aplikacji
        hbox2 = QHBoxLayout()
        hbox2.addLayout(pidy)
        hbox2.addWidget(kompas)
        hbox2.addLayout(strzalki)

    #zlozenie gornej i dolnej linii aplikacji
        vbox = QVBoxLayout()
        #vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 500)
        self.setWindowTitle('Telemetria Romka')
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())