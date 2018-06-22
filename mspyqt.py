#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
最后一次编辑: January 2015
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolTip,\
    QMessageBox, QDesktopWidget, QAction, qApp, QTextEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class WinApp(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # 定义提示框富文本显示样式
        QToolTip.setFont(QFont('sansSerif', 10))

        self.initExitAction()
        self.initHelpAction()
        self.initUI()

    # 定义主窗口组件
    def initUI(self):
        # 主窗口显示
        self.statusBar().showMessage('Ready...')
        self.menubarshow()
        self.toolbarshow()

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        # 主窗口提示文字
        self.setToolTip('This is a <b>QWidget</b> widget.')

        self.setGeometry(300, 209, 500, 309)
        self.setWindowTitle('Msong Box')
        self.setWindowIcon(QIcon('img/song.png'))  

        self.show()

    # 定义工具栏
    def toolbarshow(self):
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(self.exitAction)
        toolbar.addAction(self.helpAction)

    # 定义菜单栏
    def menubarshow(self):
        menubar = self.menuBar()
        # 绑定退出选项的命令主体到指定菜单项

        fileMenu = menubar.addMenu('&文件')
        fileMenu.addAction(self.exitAction)

        helpMenu = menubar.addMenu('&帮助')
        helpMenu.addAction(self.helpAction)

    # 定义菜单栏退出选项的命令主体
    def initExitAction(self):
        self.exitAction = QAction(QIcon('img/song.png'), '&退出', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Exit application')
        self.exitAction.setToolTip('click it will close this app.')
        self.exitAction.triggered.connect(qApp.quit)

    # 定义菜单栏退出选项的命令主体
    def initHelpAction(self):
        self.helpAction = QAction(QIcon('img/help.png'), '&help', self)
        self.helpAction.setShortcut('Ctrl+H')
        self.helpAction.setStatusTip('show some of help.')
        self.helpAction.setToolTip('click it will show some of help.')
        self.helpAction.triggered.connect(qApp.quit)

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