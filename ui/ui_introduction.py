# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'introductionWqNfpe.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1907, 1080)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.backGroundLB = QLabel(self.centralwidget)
        self.backGroundLB.setObjectName(u"backGroundLB")
        self.backGroundLB.setGeometry(QRect(0, 0, 1920, 1080))
        self.backGroundLB.setStyleSheet(u"")
        self.backGroundLB.setPixmap(QPixmap(u"../App/images/bk.png"))
        self.backGroundLB.setAlignment(Qt.AlignCenter)
        self.dangNhapBT = QPushButton(self.centralwidget)
        self.dangNhapBT.setObjectName(u"dangNhapBT")
        self.dangNhapBT.setGeometry(QRect(1640, 70, 140, 40))
        font = QFont()
        font.setPointSize(10)
        self.dangNhapBT.setFont(font)
        self.dangNhapBT.setStyleSheet(u"color: white;\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"")
        self.thoatBT = QPushButton(self.centralwidget)
        self.thoatBT.setObjectName(u"thoatBT")
        self.thoatBT.setGeometry(QRect(1640, 120, 140, 40))
        self.thoatBT.setFont(font)
        self.thoatBT.setStyleSheet(u"color: white;\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(1129, 59, 331, 161))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1907, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
        self.backGroundLB.setText("")
        self.dangNhapBT.setText(QCoreApplication.translate("MainWindow", u"\u0110\u0102NG NH\u1eacP", None))
        self.thoatBT.setText(QCoreApplication.translate("MainWindow", u"THO\u00c1T", None))
    # retranslateUi

