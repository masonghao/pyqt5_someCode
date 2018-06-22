#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
最后一次编辑: masong 2018
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout,\
    QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon

class WinApp(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.initUI()

    # 定义主窗口组件
    def initUI(self):
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 209, 500, 309)
        self.setWindowTitle('Msong Box')
        self.setWindowIcon(QIcon('img/song.png'))  

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WinApp()
    sys.exit(app.exec_()) 