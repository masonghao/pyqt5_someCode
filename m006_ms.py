#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
最后一次编辑: Masong 2018-06-22
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSignal, QObject

class Communicate(object):
    closeApp = pyqtSignal()
    
    def __init__(self):
        pass

class Msapp(QMainWindow):
    """docstring for Msapp"""
    def __init__(self):
        QMainWindow.__init__(self)
        self.main()
        
    def main(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 150, 500, 309)
        self.setWindowTitle("msh app.")
        self.show()

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WinApp()
    sys.exit(app.exec_()) 