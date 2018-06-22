#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
最后一次编辑: Masong 2018-06-22
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton,\
    QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class WinApp(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.initUI()

    # 定义主窗口组件
    def initUI(self):
        QToolTip.setFont(QFont('sansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget.')

        btn = QPushButton('Button', self)
        btn.setToolTip('thi is a <b>QPushButton</b> nothing to do.')
        btn.resize(btn.sizeHint())
        btn.move(320,260)

        qbtn = QPushButton('quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.setToolTip('clicked to quit the window.')
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(400, 260)

        # self.setGeometry(500, 380, 200, 200)
        self.resize(500,309)
        self.center()
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('img/song.png'))  

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 点击系统自带的关闭窗口时触发确认询问
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',\
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WinApp()
    sys.exit(app.exec_()) 