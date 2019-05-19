#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we position two push
buttons in the bottom-right corner
of the window.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        wykres = QPushButton("wykres")
        mapa = QPushButton("mapa")
        pidy_dol = QPushButton("pidy_dol")
        kompas = QPushButton("kompas")
        up = QPushButton("W")
        down = QPushButton("S")
        left = QPushButton("A")
        right = QPushButton("D")
        P1 = QPushButton("P")
        I1 = QPushButton("I")
        D1 = QPushButton("D")
        P2 = QPushButton("P")
        I2 = QPushButton("I")
        D2 = QPushButton("D")

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

        pidy_gora = QHBoxLayout()
        pidy_gora.addWidget(P1)
        pidy_gora.addWidget(I1)
        pidy_gora.addWidget(D1)

        pidy_dol = QHBoxLayout()
        pidy_dol.addWidget(P2)
        pidy_dol.addWidget(I2)
        pidy_dol.addWidget(D2)

        pidy = QVBoxLayout()
        pidy.addLayout(pidy_gora)
        pidy.addLayout(pidy_dol)

    #gorna linia aplikacji
        hbox1 = QHBoxLayout()
        #hbox1.addStretch(1)
        hbox1.addWidget(wykres)
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

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Telemetria Romka')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())