#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
最后一次编辑: Masong 2018-06-22
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QSlider,\
    QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class WinApp(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.initUI()

    # 定义主窗口组件
    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.statusBar()
        self.setGeometry(300, 150, 500, 309)
        self.setWindowTitle('M005 testing.')
        self.setWindowIcon(QIcon('img/song.png'))
        self.show()

    def eventSender(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text()+' was is sender.')

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WinApp()
    sys.exit(app.exec_()) 