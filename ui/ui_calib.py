# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calibWnnZFi.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CalibCameraWindow(object):
    def setupUi(self, CalibCameraWindow):
        if not CalibCameraWindow.objectName():
            CalibCameraWindow.setObjectName(u"CalibCameraWindow")
        CalibCameraWindow.resize(1920, 1080)
        self.actionOpen = QAction(CalibCameraWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.centralwidget = QWidget(CalibCameraWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(20, 370, 411, 121))
        self.layoutWidget_5 = QWidget(self.groupBox_5)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(30, 30, 341, 31))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.chonCameraLB_2 = QLabel(self.layoutWidget_5)
        self.chonCameraLB_2.setObjectName(u"chonCameraLB_2")

        self.horizontalLayout_10.addWidget(self.chonCameraLB_2)

        self.choManHinhCB = QComboBox(self.layoutWidget_5)
        self.choManHinhCB.addItem("")
        self.choManHinhCB.addItem("")
        self.choManHinhCB.addItem("")
        self.choManHinhCB.addItem("")
        self.choManHinhCB.addItem("")
        self.choManHinhCB.addItem("")
        self.choManHinhCB.setObjectName(u"choManHinhCB")

        self.horizontalLayout_10.addWidget(self.choManHinhCB)

        self.layoutWidget_9 = QWidget(self.groupBox_5)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(30, 70, 341, 31))
        self.horizontalLayout_11 = QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.chonCameraLB_3 = QLabel(self.layoutWidget_9)
        self.chonCameraLB_3.setObjectName(u"chonCameraLB_3")

        self.horizontalLayout_11.addWidget(self.chonCameraLB_3)

        self.chonDieuHuongCB = QComboBox(self.layoutWidget_9)
        self.chonDieuHuongCB.addItem("")
        self.chonDieuHuongCB.addItem("")
        self.chonDieuHuongCB.addItem("")
        self.chonDieuHuongCB.addItem("")
        self.chonDieuHuongCB.addItem("")
        self.chonDieuHuongCB.setObjectName(u"chonDieuHuongCB")

        self.horizontalLayout_11.addWidget(self.chonDieuHuongCB)

        self.cameraOptionGB = QGroupBox(self.centralwidget)
        self.cameraOptionGB.setObjectName(u"cameraOptionGB")
        self.cameraOptionGB.setGeometry(QRect(20, 30, 411, 311))
        self.verticalLayoutWidget_4 = QWidget(self.cameraOptionGB)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 50, 381, 241))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.chonCameraLB_4 = QLabel(self.verticalLayoutWidget_4)
        self.chonCameraLB_4.setObjectName(u"chonCameraLB_4")

        self.gridLayout_3.addWidget(self.chonCameraLB_4, 0, 0, 1, 1)

        self.chonCamCB = QComboBox(self.verticalLayoutWidget_4)
        self.chonCamCB.addItem("")
        self.chonCamCB.addItem("")
        self.chonCamCB.addItem("")
        self.chonCamCB.addItem("")
        self.chonCamCB.addItem("")
        self.chonCamCB.setObjectName(u"chonCamCB")

        self.gridLayout_3.addWidget(self.chonCamCB, 0, 1, 1, 1)

        self.chonKenhLB_2 = QLabel(self.verticalLayoutWidget_4)
        self.chonKenhLB_2.setObjectName(u"chonKenhLB_2")

        self.gridLayout_3.addWidget(self.chonKenhLB_2, 1, 0, 1, 1)

        self.chonKenhCB = QComboBox(self.verticalLayoutWidget_4)
        self.chonKenhCB.addItem("")
        self.chonKenhCB.addItem("")
        self.chonKenhCB.setObjectName(u"chonKenhCB")

        self.gridLayout_3.addWidget(self.chonKenhCB, 1, 1, 1, 1)


        self.horizontalLayout_13.addLayout(self.gridLayout_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.smallScreenRB = QRadioButton(self.verticalLayoutWidget_4)
        self.smallScreenRB.setObjectName(u"smallScreenRB")
        self.smallScreenRB.setChecked(True)

        self.gridLayout_4.addWidget(self.smallScreenRB, 1, 0, 1, 1)

        self.orginalScreenRB = QRadioButton(self.verticalLayoutWidget_4)
        self.orginalScreenRB.setObjectName(u"orginalScreenRB")

        self.gridLayout_4.addWidget(self.orginalScreenRB, 2, 0, 1, 1)


        self.horizontalLayout_13.addLayout(self.gridLayout_4)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_13)


        self.verticalLayout_7.addLayout(self.horizontalLayout_12)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.doSangLB_3 = QLabel(self.verticalLayoutWidget_4)
        self.doSangLB_3.setObjectName(u"doSangLB_3")
        self.doSangLB_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.doSangLB_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.BrightnessSlider = QSlider(self.verticalLayoutWidget_4)
        self.BrightnessSlider.setObjectName(u"BrightnessSlider")
        self.BrightnessSlider.setMinimum(-50)
        self.BrightnessSlider.setMaximum(50)
        self.BrightnessSlider.setSliderPosition(0)
        self.BrightnessSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.BrightnessSlider)

        self.doSangDSB = QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.doSangDSB.setObjectName(u"doSangDSB")
        self.doSangDSB.setDecimals(0)
        self.doSangDSB.setMinimum(-50.000000000000000)
        self.doSangDSB.setMaximum(50.000000000000000)
        self.doSangDSB.setValue(0.000000000000000)

        self.horizontalLayout_2.addWidget(self.doSangDSB)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.doSangLB_4 = QLabel(self.verticalLayoutWidget_4)
        self.doSangLB_4.setObjectName(u"doSangLB_4")
        self.doSangLB_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.doSangLB_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ContrastSlider = QSlider(self.verticalLayoutWidget_4)
        self.ContrastSlider.setObjectName(u"ContrastSlider")
        self.ContrastSlider.setMinimum(-50)
        self.ContrastSlider.setMaximum(50)
        self.ContrastSlider.setSliderPosition(0)
        self.ContrastSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.ContrastSlider)

        self.doTuongPhanDSB = QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.doTuongPhanDSB.setObjectName(u"doTuongPhanDSB")
        self.doTuongPhanDSB.setDecimals(0)
        self.doTuongPhanDSB.setMinimum(-50.000000000000000)
        self.doTuongPhanDSB.setMaximum(50.000000000000000)
        self.doTuongPhanDSB.setValue(0.000000000000000)

        self.horizontalLayout_5.addWidget(self.doTuongPhanDSB)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.verticalLayout_7.addLayout(self.verticalLayout_2)

        self.doSangLB_5 = QLabel(self.verticalLayoutWidget_4)
        self.doSangLB_5.setObjectName(u"doSangLB_5")
        self.doSangLB_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.doSangLB_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.FocusSlider = QSlider(self.verticalLayoutWidget_4)
        self.FocusSlider.setObjectName(u"FocusSlider")
        self.FocusSlider.setMinimum(-50)
        self.FocusSlider.setMaximum(50)
        self.FocusSlider.setSliderPosition(0)
        self.FocusSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.FocusSlider)

        self.focusDSB = QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.focusDSB.setObjectName(u"focusDSB")
        self.focusDSB.setDecimals(0)
        self.focusDSB.setMinimum(-50.000000000000000)
        self.focusDSB.setMaximum(50.000000000000000)
        self.focusDSB.setValue(0.000000000000000)

        self.horizontalLayout_6.addWidget(self.focusDSB)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.groupBox_6 = QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(449, 30, 1381, 840))
        self.anhMauLB = QLabel(self.groupBox_6)
        self.anhMauLB.setObjectName(u"anhMauLB")
        self.anhMauLB.setGeometry(QRect(1120, 30, 240, 320))
        self.anhMauLB.setScaledContents(True)
        self.label_3 = QLabel(self.groupBox_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(1210, 360, 55, 16))
        self.cameraLB = QLabel(self.groupBox_6)
        self.cameraLB.setObjectName(u"cameraLB")
        self.cameraLB.setGeometry(QRect(20, 30, 1080, 720))
        self.cameraLB.setScaledContents(False)
        self.cameraLB.setAlignment(Qt.AlignCenter)
        self.noteLB = QLabel(self.groupBox_6)
        self.noteLB.setObjectName(u"noteLB")
        self.noteLB.setGeometry(QRect(20, 760, 1340, 61))
        self.SoLB = QLabel(self.groupBox_6)
        self.SoLB.setObjectName(u"SoLB")
        self.SoLB.setGeometry(QRect(1120, 430, 240, 320))
        font = QFont()
        font.setPointSize(64)
        self.SoLB.setFont(font)
        self.SoLB.setScaledContents(True)
        self.SoLB.setAlignment(Qt.AlignCenter)
        self.nextPage = QPushButton(self.centralwidget)
        self.nextPage.setObjectName(u"nextPage")
        self.nextPage.setGeometry(QRect(1650, 920, 120, 30))
        self.groupBox_7 = QGroupBox(self.centralwidget)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(20, 520, 411, 201))
        self.chonCameraLB_9 = QLabel(self.groupBox_7)
        self.chonCameraLB_9.setObjectName(u"chonCameraLB_9")
        self.chonCameraLB_9.setGeometry(QRect(17, 110, 111, 71))
        self.SoLB_3 = QLabel(self.groupBox_7)
        self.SoLB_3.setObjectName(u"SoLB_3")
        self.SoLB_3.setGeometry(QRect(20, 730, 381, 181))
        self.SoLB_3.setScaledContents(True)
        self.chonCameraLB_8 = QLabel(self.groupBox_7)
        self.chonCameraLB_8.setObjectName(u"chonCameraLB_8")
        self.chonCameraLB_8.setGeometry(QRect(17, 90, 50, 16))
        self.chonCameraLB_7 = QLabel(self.groupBox_7)
        self.chonCameraLB_7.setObjectName(u"chonCameraLB_7")
        self.chonCameraLB_7.setGeometry(QRect(17, 43, 65, 16))
        self.soONgangSB = QSpinBox(self.groupBox_7)
        self.soONgangSB.setObjectName(u"soONgangSB")
        self.soONgangSB.setGeometry(QRect(250, 30, 121, 31))
        self.soODocSB = QSpinBox(self.groupBox_7)
        self.soODocSB.setObjectName(u"soODocSB")
        self.soODocSB.setGeometry(QRect(250, 80, 121, 31))
        self.kichThuocOSB = QSpinBox(self.groupBox_7)
        self.kichThuocOSB.setObjectName(u"kichThuocOSB")
        self.kichThuocOSB.setGeometry(QRect(250, 130, 121, 31))
        self.kichThuocOSB.setMaximum(100)
        self.chupBT = QPushButton(self.centralwidget)
        self.chupBT.setObjectName(u"chupBT")
        self.chupBT.setGeometry(QRect(1500, 920, 120, 30))
        self.KqLB = QLabel(self.centralwidget)
        self.KqLB.setObjectName(u"KqLB")
        self.KqLB.setGeometry(QRect(20, 740, 411, 251))
        self.KqLB.setScaledContents(True)
        self.resetBT = QPushButton(self.centralwidget)
        self.resetBT.setObjectName(u"resetBT")
        self.resetBT.setGeometry(QRect(1350, 920, 120, 30))
        self.calibBT = QPushButton(self.centralwidget)
        self.calibBT.setObjectName(u"calibBT")
        self.calibBT.setGeometry(QRect(1200, 920, 120, 30))
        CalibCameraWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CalibCameraWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuOpen = QMenu(self.menubar)
        self.menuOpen.setObjectName(u"menuOpen")
        self.menuQuit = QMenu(self.menubar)
        self.menuQuit.setObjectName(u"menuQuit")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        CalibCameraWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CalibCameraWindow)
        self.statusbar.setObjectName(u"statusbar")
        CalibCameraWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOpen.menuAction())
        self.menubar.addAction(self.menuQuit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuOpen.addAction(self.actionOpen)

        self.retranslateUi(CalibCameraWindow)

        QMetaObject.connectSlotsByName(CalibCameraWindow)
    # setupUi

    def retranslateUi(self, CalibCameraWindow):
        CalibCameraWindow.setWindowTitle(QCoreApplication.translate("CalibCameraWindow", u"CalibWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("CalibCameraWindow", u"Open file", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("CalibCameraWindow", u"Ch\u1ecdn m\u00e0n h\u00ecnh", None))
        self.chonCameraLB_2.setText(QCoreApplication.translate("CalibCameraWindow", u"Ch\u1ecdn m\u00e0n h\u00ecnh", None))
        self.choManHinhCB.setItemText(0, QCoreApplication.translate("CalibCameraWindow", u"T\u1ef1 \u0111\u1ed9ng", None))
        self.choManHinhCB.setItemText(1, QCoreApplication.translate("CalibCameraWindow", u"2:3 (1080 x 720) ", None))
        self.choManHinhCB.setItemText(2, QCoreApplication.translate("CalibCameraWindow", u"16:9 (960 x 540) ", None))
        self.choManHinhCB.setItemText(3, QCoreApplication.translate("CalibCameraWindow", u"16:9 (640 x 360) ", None))
        self.choManHinhCB.setItemText(4, QCoreApplication.translate("CalibCameraWindow", u"4:3 (960 x 720) ", None))
        self.choManHinhCB.setItemText(5, QCoreApplication.translate("CalibCameraWindow", u"4:3 (640 x 480) ", None))

        self.chonCameraLB_3.setText(QCoreApplication.translate("CalibCameraWindow", u"\u0110i\u1ec1u ch\u1ec9nh h\u01b0\u1edbng", None))
        self.chonDieuHuongCB.setItemText(0, QCoreApplication.translate("CalibCameraWindow", u"Kh\u00f4ng", None))
        self.chonDieuHuongCB.setItemText(1, QCoreApplication.translate("CalibCameraWindow", u"L\u1eadt", None))
        self.chonDieuHuongCB.setItemText(2, QCoreApplication.translate("CalibCameraWindow", u"\u0110\u1ea3o ng\u01b0\u1ee3c", None))
        self.chonDieuHuongCB.setItemText(3, QCoreApplication.translate("CalibCameraWindow", u"Xoay 90 \u0111\u1ed9 sang tr\u00e1i", None))
        self.chonDieuHuongCB.setItemText(4, QCoreApplication.translate("CalibCameraWindow", u"Xoay 90 \u0111\u1ed9 sang ph\u1ea3i", None))

        self.cameraOptionGB.setTitle(QCoreApplication.translate("CalibCameraWindow", u"Ch\u1ecdn Camera", None))
        self.chonCameraLB_4.setText(QCoreApplication.translate("CalibCameraWindow", u"Ch\u1ecdn camera:", None))
        self.chonCamCB.setItemText(0, QCoreApplication.translate("CalibCameraWindow", u"T\u1eaft", None))
        self.chonCamCB.setItemText(1, QCoreApplication.translate("CalibCameraWindow", u"Camera 0", None))
        self.chonCamCB.setItemText(2, QCoreApplication.translate("CalibCameraWindow", u"Camera 1", None))
        self.chonCamCB.setItemText(3, QCoreApplication.translate("CalibCameraWindow", u"Camera 2", None))
        self.chonCamCB.setItemText(4, QCoreApplication.translate("CalibCameraWindow", u"Camera 3", None))

        self.chonKenhLB_2.setText(QCoreApplication.translate("CalibCameraWindow", u"Ch\u1ecdn k\u00eanh:", None))
        self.chonKenhCB.setItemText(0, QCoreApplication.translate("CalibCameraWindow", u"RGB", None))
        self.chonKenhCB.setItemText(1, QCoreApplication.translate("CalibCameraWindow", u"Grayscale", None))

        self.smallScreenRB.setText(QCoreApplication.translate("CalibCameraWindow", u"M\u00e0n h\u00ecnh nh\u1ecf", None))
        self.orginalScreenRB.setText(QCoreApplication.translate("CalibCameraWindow", u"M\u00e0n h\u00ecnh g\u1ed1c", None))
        self.doSangLB_3.setText(QCoreApplication.translate("CalibCameraWindow", u"\u0110\u1ed9 s\u00e1ng", None))
        self.doSangLB_4.setText(QCoreApplication.translate("CalibCameraWindow", u"\u0110\u1ed9 t\u01b0\u01a1ng ph\u1ea3n", None))
        self.doSangLB_5.setText(QCoreApplication.translate("CalibCameraWindow", u"Focus", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("CalibCameraWindow", u"Camera", None))
        self.anhMauLB.setText("")
        self.label_3.setText("")
        self.cameraLB.setText("")
        self.noteLB.setText("")
        self.SoLB.setText("")
        self.nextPage.setText(QCoreApplication.translate("CalibCameraWindow", u"Next", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("CalibCameraWindow", u"K\u00edch th\u01b0\u1edbc \u00f4 b\u00e0n c\u1edd", None))
        self.chonCameraLB_9.setText(QCoreApplication.translate("CalibCameraWindow", u"K\u00edch th\u01b0\u1edbc \u00f4 (mm)", None))
        self.SoLB_3.setText(QCoreApplication.translate("CalibCameraWindow", u"K\u00edch th\u01b0\u1edbc \u00f4 (mm)", None))
        self.chonCameraLB_8.setText(QCoreApplication.translate("CalibCameraWindow", u"S\u1ed1 \u00f4 d\u1ecdc", None))
        self.chonCameraLB_7.setText(QCoreApplication.translate("CalibCameraWindow", u"S\u1ed1 \u00f4 ngang", None))
        self.chupBT.setText(QCoreApplication.translate("CalibCameraWindow", u"Ch\u1ee5p", None))
        self.KqLB.setText("")
        self.resetBT.setText(QCoreApplication.translate("CalibCameraWindow", u"Reset", None))
        self.calibBT.setText(QCoreApplication.translate("CalibCameraWindow", u"Calib", None))
        self.menuFile.setTitle(QCoreApplication.translate("CalibCameraWindow", u"File", None))
        self.menuOpen.setTitle(QCoreApplication.translate("CalibCameraWindow", u"Open", None))
        self.menuQuit.setTitle(QCoreApplication.translate("CalibCameraWindow", u"Exit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("CalibCameraWindow", u"Help", None))
    # retranslateUi

