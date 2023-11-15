# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_nguongbfahuH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1351, 960)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 20, 291, 161))
        self.ngongDSB = QDoubleSpinBox(self.groupBox)
        self.ngongDSB.setObjectName(u"ngongDSB")
        self.ngongDSB.setGeometry(QRect(220, 100, 62, 22))
        self.ngongDSB.setDecimals(0)
        self.ngongDSB.setMaximum(255.000000000000000)
        self.ngongDSB.setSingleStep(1.000000000000000)
        self.ngongDSB.setStepType(QAbstractSpinBox.DefaultStepType)
        self.ngongDSB.setValue(0.000000000000000)
        self.nguongSL = QSlider(self.groupBox)
        self.nguongSL.setObjectName(u"nguongSL")
        self.nguongSL.setGeometry(QRect(30, 100, 160, 22))
        self.nguongSL.setMaximum(255)
        self.nguongSL.setValue(0)
        self.nguongSL.setOrientation(Qt.Horizontal)
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(30, 50, 95, 20))
        self.anhLB = QLabel(self.centralwidget)
        self.anhLB.setObjectName(u"anhLB")
        self.anhLB.setGeometry(QRect(190, 240, 960, 640))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(460, 60, 701, 31))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1200, 60, 93, 28))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1351, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"L\u1ef1a ch\u1ecdn", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"L\u1ea5y ng\u01b0\u1ee1ng", None))
        self.anhLB.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Xem \u1ea3nh", None))
    # retranslateUi

