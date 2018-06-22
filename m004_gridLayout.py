#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
最后一次编辑: masong 2018
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton,\
    QLabel, QLineEdit, QTextEdit
from PyQt5.QtGui import QIcon

class WinApp(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.initUI()
    # 定义主窗口组件
    def initUI(self):
        titlelab = QLabel('标题')
        authorlab = QLabel('作者')
        contenlab = QLabel('内容')

        titleinp = QLineEdit()
        authorinp = QLineEdit()
        conteninp = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(titlelab, 1, 0)
        grid.addWidget(titleinp, 1, 1)
        grid.addWidget(authorlab, 2, 0)
        grid.addWidget(authorinp, 2, 1)
        grid.addWidget(contenlab, 3, 0)
        grid.addWidget(conteninp, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 150, 500, 309)
        self.setWindowTitle('Testing')
        self.setWindowIcon(QIcon('song.png'))
        self.show()

    def initUI2(self):
        mGrid = QGridLayout()
        self.setLayout(mGrid)

        names = ['C', 'Bck', '', 'Close',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-', 
            '0', '.', '=', '+']

        position = [(i, j) for i in range(5) for j in range(4)]
        for position, name in zip(position, names):
            if name == '':
                continue
            button = QPushButton(name)
            mGrid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('Testing')
        self.setWindowIcon(QIcon('song.png'))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WinApp()
    sys.exit(app.exec_()) 