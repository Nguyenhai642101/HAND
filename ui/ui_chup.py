# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chupdmBEwN.ui'
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
        MainWindow.resize(1859, 1080)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1920, 1080))
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tab_nhap_thong_tin = QWidget()
        self.tab_nhap_thong_tin.setObjectName(u"tab_nhap_thong_tin")
        self.groupBox = QGroupBox(self.tab_nhap_thong_tin)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(100, 170, 800, 500))
        self.groupBox.setToolTipDuration(-1)
        self.groupBox.setFlat(False)
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 50, 180, 240))
        self.label_5.setScaledContents(True)
        self.chonAnhBT = QPushButton(self.groupBox)
        self.chonAnhBT.setObjectName(u"chonAnhBT")
        self.chonAnhBT.setGeometry(QRect(80, 320, 91, 31))
        self.birthdayTE = QTextEdit(self.groupBox)
        self.birthdayTE.setObjectName(u"birthdayTE")
        self.birthdayTE.setGeometry(QRect(338, 117, 422, 37))
        font = QFont()
        font.setPointSize(12)
        self.birthdayTE.setFont(font)
        self.nameTE = QTextEdit(self.groupBox)
        self.nameTE.setObjectName(u"nameTE")
        self.nameTE.setGeometry(QRect(338, 51, 422, 37))
        self.nameTE.setFont(font)
        self.addressTE = QTextEdit(self.groupBox)
        self.addressTE.setObjectName(u"addressTE")
        self.addressTE.setGeometry(QRect(338, 183, 422, 37))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.addressTE.sizePolicy().hasHeightForWidth())
        self.addressTE.setSizePolicy(sizePolicy1)
        self.addressTE.setFont(font)
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(271, 117, 60, 16))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(271, 51, 27, 16))
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(271, 183, 44, 16))
        self.groupBox_2 = QGroupBox(self.tab_nhap_thong_tin)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(1020, 170, 800, 500))
        self.groupBox_2.setToolTipDuration(-1)
        self.groupBox_2.setFlat(False)
        self.Tab_diem_va_ket_qua = QTabWidget(self.groupBox_2)
        self.Tab_diem_va_ket_qua.setObjectName(u"Tab_diem_va_ket_qua")
        self.Tab_diem_va_ket_qua.setGeometry(QRect(10, 30, 780, 460))
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.bang_diem_tay_phai = QTableWidget(self.tab_1)
        if (self.bang_diem_tay_phai.columnCount() < 18):
            self.bang_diem_tay_phai.setColumnCount(18)
        __qtablewidgetitem = QTableWidgetItem()
        self.bang_diem_tay_phai.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.bang_diem_tay_phai.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.bang_diem_tay_phai.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.bang_diem_tay_phai.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.bang_diem_tay_phai.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.bang_diem_tay_phai.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.bang_diem_tay_phai.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.bang_diem_tay_phai.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.bang_diem_tay_phai.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.bang_diem_tay_phai.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.bang_diem_tay_phai.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.bang_diem_tay_phai.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.bang_diem_tay_phai.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.bang_diem_tay_phai.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.bang_diem_tay_phai.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.bang_diem_tay_phai.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.bang_diem_tay_phai.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.bang_diem_tay_phai.setHorizontalHeaderItem(17, __qtablewidgetitem17)
        if (self.bang_diem_tay_phai.rowCount() < 10):
            self.bang_diem_tay_phai.setRowCount(10)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.bang_diem_tay_phai.setVerticalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.bang_diem_tay_phai.setVerticalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.bang_diem_tay_phai.setVerticalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.bang_diem_tay_phai.setVerticalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.bang_diem_tay_phai.setVerticalHeaderItem(4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.bang_diem_tay_phai.setVerticalHeaderItem(5, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.bang_diem_tay_phai.setVerticalHeaderItem(6, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.bang_diem_tay_phai.setVerticalHeaderItem(7, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.bang_diem_tay_phai.setVerticalHeaderItem(8, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.bang_diem_tay_phai.setVerticalHeaderItem(9, __qtablewidgetitem27)
        self.bang_diem_tay_phai.setObjectName(u"bang_diem_tay_phai")
        self.bang_diem_tay_phai.setGeometry(QRect(10, 10, 750, 420))
        self.bang_diem_tay_phai.setAutoFillBackground(False)
        self.bang_diem_tay_phai.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Tab_diem_va_ket_qua.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.bang_diem_tay_trai = QTableWidget(self.tab_2)
        if (self.bang_diem_tay_trai.columnCount() < 18):
            self.bang_diem_tay_trai.setColumnCount(18)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.bang_diem_tay_trai.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.bang_diem_tay_trai.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.bang_diem_tay_trai.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.bang_diem_tay_trai.setHorizontalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.bang_diem_tay_trai.setHorizontalHeaderItem(4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.bang_diem_tay_trai.setHorizontalHeaderItem(5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.bang_diem_tay_trai.setHorizontalHeaderItem(6, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.bang_diem_tay_trai.setHorizontalHeaderItem(7, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.bang_diem_tay_trai.setHorizontalHeaderItem(8, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.bang_diem_tay_trai.setHorizontalHeaderItem(9, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.bang_diem_tay_trai.setHorizontalHeaderItem(10, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.bang_diem_tay_trai.setHorizontalHeaderItem(11, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.bang_diem_tay_trai.setHorizontalHeaderItem(12, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.bang_diem_tay_trai.setHorizontalHeaderItem(13, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.bang_diem_tay_trai.setHorizontalHeaderItem(14, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.bang_diem_tay_trai.setHorizontalHeaderItem(15, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.bang_diem_tay_trai.setHorizontalHeaderItem(16, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.bang_diem_tay_trai.setHorizontalHeaderItem(17, __qtablewidgetitem45)
        if (self.bang_diem_tay_trai.rowCount() < 10):
            self.bang_diem_tay_trai.setRowCount(10)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.bang_diem_tay_trai.setVerticalHeaderItem(0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.bang_diem_tay_trai.setVerticalHeaderItem(1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.bang_diem_tay_trai.setVerticalHeaderItem(2, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.bang_diem_tay_trai.setVerticalHeaderItem(3, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.bang_diem_tay_trai.setVerticalHeaderItem(4, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.bang_diem_tay_trai.setVerticalHeaderItem(5, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.bang_diem_tay_trai.setVerticalHeaderItem(6, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.bang_diem_tay_trai.setVerticalHeaderItem(7, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.bang_diem_tay_trai.setVerticalHeaderItem(8, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.bang_diem_tay_trai.setVerticalHeaderItem(9, __qtablewidgetitem55)
        self.bang_diem_tay_trai.setObjectName(u"bang_diem_tay_trai")
        self.bang_diem_tay_trai.setGeometry(QRect(10, 10, 750, 420))
        self.bang_diem_tay_trai.setAutoFillBackground(False)
        self.bang_diem_tay_trai.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Tab_diem_va_ket_qua.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.bang_khoang_cach_tay_phai = QTableWidget(self.tab_3)
        if (self.bang_khoang_cach_tay_phai.columnCount() < 12):
            self.bang_khoang_cach_tay_phai.setColumnCount(12)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.bang_khoang_cach_tay_phai.setHorizontalHeaderItem(0, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.bang_khoang_cach_tay_phai.setHorizontalHeaderItem(1, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.bang_khoang_cach_tay_phai.setHorizontalHeaderItem(2, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.bang_khoang_cach_tay_phai.setHorizontalHeaderItem(3, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.bang_khoang_cach_tay_phai.setHorizontalHeaderItem(4, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.bang_khoang_cach_tay_phai.setHorizontalHeaderItem(5, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.bang_khoang_cach_tay_phai.setHorizontalHeaderItem(6, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.bang_khoang_cach_tay_phai.setHorizontalHeaderItem(7, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.bang_khoang_cach_tay_phai.setHorizontalHeaderItem(8, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.bang_khoang_cach_tay_phai.setHorizontalHeaderItem(9, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.bang_khoang_cach_tay_phai.setHorizontalHeaderItem(10, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.bang_khoang_cach_tay_phai.setHorizontalHeaderItem(11, __qtablewidgetitem67)
        if (self.bang_khoang_cach_tay_phai.rowCount() < 10):
            self.bang_khoang_cach_tay_phai.setRowCount(10)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.bang_khoang_cach_tay_phai.setVerticalHeaderItem(0, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.bang_khoang_cach_tay_phai.setVerticalHeaderItem(1, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.bang_khoang_cach_tay_phai.setVerticalHeaderItem(2, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.bang_khoang_cach_tay_phai.setVerticalHeaderItem(3, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.bang_khoang_cach_tay_phai.setVerticalHeaderItem(4, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.bang_khoang_cach_tay_phai.setVerticalHeaderItem(5, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.bang_khoang_cach_tay_phai.setVerticalHeaderItem(6, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.bang_khoang_cach_tay_phai.setVerticalHeaderItem(7, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.bang_khoang_cach_tay_phai.setVerticalHeaderItem(8, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.bang_khoang_cach_tay_phai.setVerticalHeaderItem(9, __qtablewidgetitem77)
        self.bang_khoang_cach_tay_phai.setObjectName(u"bang_khoang_cach_tay_phai")
        self.bang_khoang_cach_tay_phai.setGeometry(QRect(10, 10, 750, 420))
        self.bang_khoang_cach_tay_phai.setAutoFillBackground(False)
        self.bang_khoang_cach_tay_phai.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Tab_diem_va_ket_qua.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.bang_khoang_cach_tay_trai = QTableWidget(self.tab_4)
        if (self.bang_khoang_cach_tay_trai.columnCount() < 12):
            self.bang_khoang_cach_tay_trai.setColumnCount(12)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.bang_khoang_cach_tay_trai.setHorizontalHeaderItem(0, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.bang_khoang_cach_tay_trai.setHorizontalHeaderItem(1, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.bang_khoang_cach_tay_trai.setHorizontalHeaderItem(2, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.bang_khoang_cach_tay_trai.setHorizontalHeaderItem(3, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.bang_khoang_cach_tay_trai.setHorizontalHeaderItem(4, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.bang_khoang_cach_tay_trai.setHorizontalHeaderItem(5, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.bang_khoang_cach_tay_trai.setHorizontalHeaderItem(6, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.bang_khoang_cach_tay_trai.setHorizontalHeaderItem(7, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.bang_khoang_cach_tay_trai.setHorizontalHeaderItem(8, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.bang_khoang_cach_tay_trai.setHorizontalHeaderItem(9, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.bang_khoang_cach_tay_trai.setHorizontalHeaderItem(10, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.bang_khoang_cach_tay_trai.setHorizontalHeaderItem(11, __qtablewidgetitem89)
        if (self.bang_khoang_cach_tay_trai.rowCount() < 10):
            self.bang_khoang_cach_tay_trai.setRowCount(10)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.bang_khoang_cach_tay_trai.setVerticalHeaderItem(0, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.bang_khoang_cach_tay_trai.setVerticalHeaderItem(1, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.bang_khoang_cach_tay_trai.setVerticalHeaderItem(2, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.bang_khoang_cach_tay_trai.setVerticalHeaderItem(3, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.bang_khoang_cach_tay_trai.setVerticalHeaderItem(4, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.bang_khoang_cach_tay_trai.setVerticalHeaderItem(5, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.bang_khoang_cach_tay_trai.setVerticalHeaderItem(6, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.bang_khoang_cach_tay_trai.setVerticalHeaderItem(7, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.bang_khoang_cach_tay_trai.setVerticalHeaderItem(8, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.bang_khoang_cach_tay_trai.setVerticalHeaderItem(9, __qtablewidgetitem99)
        self.bang_khoang_cach_tay_trai.setObjectName(u"bang_khoang_cach_tay_trai")
        self.bang_khoang_cach_tay_trai.setGeometry(QRect(10, 10, 750, 420))
        self.bang_khoang_cach_tay_trai.setAutoFillBackground(False)
        self.bang_khoang_cach_tay_trai.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Tab_diem_va_ket_qua.addTab(self.tab_4, "")
        self.XemKQBT = QPushButton(self.tab_nhap_thong_tin)
        self.XemKQBT.setObjectName(u"XemKQBT")
        self.XemKQBT.setGeometry(QRect(1500, 920, 120, 30))
        self.LuuBT = QPushButton(self.tab_nhap_thong_tin)
        self.LuuBT.setObjectName(u"LuuBT")
        self.LuuBT.setGeometry(QRect(1650, 920, 120, 30))
        self.tabTruocBT_2 = QPushButton(self.tab_nhap_thong_tin)
        self.tabTruocBT_2.setObjectName(u"tabTruocBT_2")
        self.tabTruocBT_2.setGeometry(QRect(150, 920, 120, 30))
        self.tabSauBT_2 = QPushButton(self.tab_nhap_thong_tin)
        self.tabSauBT_2.setObjectName(u"tabSauBT_2")
        self.tabSauBT_2.setGeometry(QRect(300, 920, 120, 30))
        self.label = QLabel(self.tab_nhap_thong_tin)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(768, 51, 362, 48))
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.xoaBT = QPushButton(self.tab_nhap_thong_tin)
        self.xoaBT.setObjectName(u"xoaBT")
        self.xoaBT.setGeometry(QRect(1350, 920, 120, 30))
        self.progressBar = QProgressBar(self.tab_nhap_thong_tin)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(1580, 690, 211, 20))
        self.progressBar.setValue(0)
        self.label_2 = QLabel(self.tab_nhap_thong_tin)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(1494, 690, 71, 20))
        self.tabWidget.addTab(self.tab_nhap_thong_tin, "")
        self.label.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.XemKQBT.raise_()
        self.LuuBT.raise_()
        self.tabTruocBT_2.raise_()
        self.tabSauBT_2.raise_()
        self.xoaBT.raise_()
        self.progressBar.raise_()
        self.label_2.raise_()
        self.tab_chup_anh = QWidget()
        self.tab_chup_anh.setObjectName(u"tab_chup_anh")
        self.groupBox_3 = QGroupBox(self.tab_chup_anh)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 310, 411, 111))
        self.layoutWidget = QWidget(self.groupBox_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 60, 381, 31))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.nguongSlider = QSlider(self.layoutWidget)
        self.nguongSlider.setObjectName(u"nguongSlider")
        self.nguongSlider.setMinimum(0)
        self.nguongSlider.setMaximum(255)
        self.nguongSlider.setValue(65)
        self.nguongSlider.setSliderPosition(65)
        self.nguongSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.nguongSlider)

        self.nguongDSB = QDoubleSpinBox(self.layoutWidget)
        self.nguongDSB.setObjectName(u"nguongDSB")
        self.nguongDSB.setDecimals(0)
        self.nguongDSB.setMinimum(0.000000000000000)
        self.nguongDSB.setMaximum(254.000000000000000)
        self.nguongDSB.setValue(65.000000000000000)

        self.horizontalLayout_6.addWidget(self.nguongDSB)

        self.doSangLB_3 = QLabel(self.groupBox_3)
        self.doSangLB_3.setObjectName(u"doSangLB_3")
        self.doSangLB_3.setGeometry(QRect(10, 30, 377, 16))
        self.doSangLB_3.setAlignment(Qt.AlignCenter)
        self.cameraOptionGB = QGroupBox(self.tab_chup_anh)
        self.cameraOptionGB.setObjectName(u"cameraOptionGB")
        self.cameraOptionGB.setGeometry(QRect(20, 30, 411, 261))
        self.verticalLayoutWidget_3 = QWidget(self.cameraOptionGB)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 50, 381, 191))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.chonCameraLB = QLabel(self.verticalLayoutWidget_3)
        self.chonCameraLB.setObjectName(u"chonCameraLB")

        self.gridLayout.addWidget(self.chonCameraLB, 0, 0, 1, 1)

        self.chonCamCB = QComboBox(self.verticalLayoutWidget_3)
        self.chonCamCB.addItem("")
        self.chonCamCB.addItem("")
        self.chonCamCB.addItem("")
        self.chonCamCB.addItem("")
        self.chonCamCB.addItem("")
        self.chonCamCB.setObjectName(u"chonCamCB")

        self.gridLayout.addWidget(self.chonCamCB, 0, 1, 1, 1)

        self.chonKenhLB = QLabel(self.verticalLayoutWidget_3)
        self.chonKenhLB.setObjectName(u"chonKenhLB")

        self.gridLayout.addWidget(self.chonKenhLB, 1, 0, 1, 1)

        self.chonKenhCB = QComboBox(self.verticalLayoutWidget_3)
        self.chonKenhCB.addItem("")
        self.chonKenhCB.addItem("")
        self.chonKenhCB.setObjectName(u"chonKenhCB")

        self.gridLayout.addWidget(self.chonKenhCB, 1, 1, 1, 1)


        self.horizontalLayout_8.addLayout(self.gridLayout)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.smallScreenRB = QRadioButton(self.verticalLayoutWidget_3)
        self.smallScreenRB.setObjectName(u"smallScreenRB")
        self.smallScreenRB.setChecked(True)

        self.gridLayout_2.addWidget(self.smallScreenRB, 1, 0, 1, 1)

        self.orginalScreenRB = QRadioButton(self.verticalLayoutWidget_3)
        self.orginalScreenRB.setObjectName(u"orginalScreenRB")

        self.gridLayout_2.addWidget(self.orginalScreenRB, 2, 0, 1, 1)


        self.horizontalLayout_8.addLayout(self.gridLayout_2)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.doSangLB = QLabel(self.verticalLayoutWidget_3)
        self.doSangLB.setObjectName(u"doSangLB")
        self.doSangLB.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.doSangLB)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.BrightnessSlider = QSlider(self.verticalLayoutWidget_3)
        self.BrightnessSlider.setObjectName(u"BrightnessSlider")
        self.BrightnessSlider.setMinimum(-50)
        self.BrightnessSlider.setMaximum(50)
        self.BrightnessSlider.setSliderPosition(0)
        self.BrightnessSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.BrightnessSlider)

        self.doSangDSB = QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.doSangDSB.setObjectName(u"doSangDSB")
        self.doSangDSB.setDecimals(0)
        self.doSangDSB.setMinimum(-50.000000000000000)
        self.doSangDSB.setMaximum(50.000000000000000)
        self.doSangDSB.setValue(0.000000000000000)

        self.horizontalLayout.addWidget(self.doSangDSB)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.doSangLB_2 = QLabel(self.verticalLayoutWidget_3)
        self.doSangLB_2.setObjectName(u"doSangLB_2")
        self.doSangLB_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.doSangLB_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.ContrastSlider = QSlider(self.verticalLayoutWidget_3)
        self.ContrastSlider.setObjectName(u"ContrastSlider")
        self.ContrastSlider.setMinimum(-50)
        self.ContrastSlider.setMaximum(50)
        self.ContrastSlider.setSliderPosition(0)
        self.ContrastSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.ContrastSlider)

        self.doTuongPhanDSB = QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.doTuongPhanDSB.setObjectName(u"doTuongPhanDSB")
        self.doTuongPhanDSB.setDecimals(0)
        self.doTuongPhanDSB.setMinimum(-50.000000000000000)
        self.doTuongPhanDSB.setMaximum(50.000000000000000)
        self.doTuongPhanDSB.setValue(0.000000000000000)

        self.horizontalLayout_4.addWidget(self.doTuongPhanDSB)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.groupBox_4 = QGroupBox(self.tab_chup_anh)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(20, 450, 411, 121))
        self.layoutWidget_2 = QWidget(self.groupBox_4)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(30, 40, 341, 61))
        self.gridLayout_3 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.hienduongbaoQRB = QRadioButton(self.layoutWidget_2)
        self.hienduongbaoQRB.setObjectName(u"hienduongbaoQRB")

        self.gridLayout_3.addWidget(self.hienduongbaoQRB, 2, 0, 1, 1)

        self.tatduongbaoQRB = QRadioButton(self.layoutWidget_2)
        self.tatduongbaoQRB.setObjectName(u"tatduongbaoQRB")
        self.tatduongbaoQRB.setChecked(True)

        self.gridLayout_3.addWidget(self.tatduongbaoQRB, 1, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.tab_chup_anh)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(20, 600, 411, 121))
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

        self.xemKetQuaBT = QPushButton(self.tab_chup_anh)
        self.xemKetQuaBT.setObjectName(u"xemKetQuaBT")
        self.xemKetQuaBT.setGeometry(QRect(1500, 920, 120, 30))
        self.tabSauBT = QPushButton(self.tab_chup_anh)
        self.tabSauBT.setObjectName(u"tabSauBT")
        self.tabSauBT.setGeometry(QRect(300, 920, 120, 30))
        self.chupBT = QPushButton(self.tab_chup_anh)
        self.chupBT.setObjectName(u"chupBT")
        self.chupBT.setGeometry(QRect(1650, 920, 120, 30))
        self.tabTruocBT = QPushButton(self.tab_chup_anh)
        self.tabTruocBT.setObjectName(u"tabTruocBT")
        self.tabTruocBT.setGeometry(QRect(150, 920, 120, 30))
        self.groupBox_6 = QGroupBox(self.tab_chup_anh)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(449, 30, 1381, 840))
        self.anhMauLB = QLabel(self.groupBox_6)
        self.anhMauLB.setObjectName(u"anhMauLB")
        self.anhMauLB.setGeometry(QRect(1120, 30, 240, 320))
        self.anhMauLB.setPixmap(QPixmap(u"../handsample/1.jpg"))
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
        font2 = QFont()
        font2.setPointSize(64)
        self.SoLB.setFont(font2)
        self.SoLB.setScaledContents(True)
        self.SoLB.setAlignment(Qt.AlignCenter)
        self.groupBox_7 = QGroupBox(self.tab_chup_anh)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(20, 750, 411, 121))
        self.layoutWidget_8 = QWidget(self.groupBox_7)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(30, 40, 341, 61))
        self.gridLayout_9 = QGridLayout(self.layoutWidget_8)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.tuDongQRB = QRadioButton(self.layoutWidget_8)
        self.tuDongQRB.setObjectName(u"tuDongQRB")
        self.tuDongQRB.setChecked(True)

        self.gridLayout_9.addWidget(self.tuDongQRB, 1, 0, 1, 1)

        self.thuCongQRB = QRadioButton(self.layoutWidget_8)
        self.thuCongQRB.setObjectName(u"thuCongQRB")

        self.gridLayout_9.addWidget(self.thuCongQRB, 2, 0, 1, 1)

        self.luiBT = QPushButton(self.tab_chup_anh)
        self.luiBT.setObjectName(u"luiBT")
        self.luiBT.setGeometry(QRect(1050, 920, 120, 30))
        self.tienBT = QPushButton(self.tab_chup_anh)
        self.tienBT.setObjectName(u"tienBT")
        self.tienBT.setGeometry(QRect(1200, 920, 120, 30))
        self.resetBT = QPushButton(self.tab_chup_anh)
        self.resetBT.setObjectName(u"resetBT")
        self.resetBT.setGeometry(QRect(1350, 920, 120, 30))
        self.tabWidget.addTab(self.tab_chup_anh, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1859, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuCalibration = QMenu(self.menubar)
        self.menuCalibration.setObjectName(u"menuCalibration")
        self.menuQuit = QMenu(self.menubar)
        self.menuQuit.setObjectName(u"menuQuit")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCalibration.menuAction())
        self.menubar.addAction(self.menuQuit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuCalibration.addAction(self.actionOpen)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.Tab_diem_va_ket_qua.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open CalibWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Th\u00f4ng tin", None))
        self.label_5.setText("")
        self.chonAnhBT.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn \u1ea3nh", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y sinh:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"T\u00ean:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ecba ch\u1ec9:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"K\u1ebft qu\u1ea3", None))
        ___qtablewidgetitem = self.bang_diem_tay_phai.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"K\u00edch th\u01b0\u1edbc \u1ea3nh", None));
        ___qtablewidgetitem1 = self.bang_diem_tay_phai.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"T\u00ean \u0111i\u1ec3m", None));
        ___qtablewidgetitem2 = self.bang_diem_tay_phai.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"V\u1ecb tr\u00ed", None));
        ___qtablewidgetitem3 = self.bang_diem_tay_phai.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"K\u00edch th\u01b0\u1edbc \u1ea3nh", None));
        ___qtablewidgetitem4 = self.bang_diem_tay_phai.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"T\u00ean \u0111i\u1ec3m", None));
        ___qtablewidgetitem5 = self.bang_diem_tay_phai.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"V\u1ecb tr\u00ed", None));
        ___qtablewidgetitem6 = self.bang_diem_tay_phai.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"K\u00edch th\u01b0\u1edbc \u1ea3nh", None));
        ___qtablewidgetitem7 = self.bang_diem_tay_phai.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"T\u00ean \u0111i\u1ec3m", None));
        ___qtablewidgetitem8 = self.bang_diem_tay_phai.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"V\u1ecb tr\u00ed", None));
        ___qtablewidgetitem9 = self.bang_diem_tay_phai.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"K\u00edch th\u01b0\u1edbc \u1ea3nh", None));
        ___qtablewidgetitem10 = self.bang_diem_tay_phai.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"T\u00ean \u0111i\u1ec3m", None));
        ___qtablewidgetitem11 = self.bang_diem_tay_phai.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"V\u1ecb tr\u00ed", None));
        ___qtablewidgetitem12 = self.bang_diem_tay_phai.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"K\u00edch th\u01b0\u1edbc \u1ea3nh", None));
        ___qtablewidgetitem13 = self.bang_diem_tay_phai.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"T\u00ean \u0111i\u1ec3m", None));
        ___qtablewidgetitem14 = self.bang_diem_tay_phai.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"V\u1ecb tr\u00ed", None));
        ___qtablewidgetitem15 = self.bang_diem_tay_phai.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"K\u00edch th\u01b0\u1edbc \u1ea3nh", None));
        ___qtablewidgetitem16 = self.bang_diem_tay_phai.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"T\u00ean \u0111i\u1ec3m", None));
        ___qtablewidgetitem17 = self.bang_diem_tay_phai.horizontalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"V\u1ecb tr\u00ed", None));
        ___qtablewidgetitem18 = self.bang_diem_tay_phai.verticalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem19 = self.bang_diem_tay_phai.verticalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem20 = self.bang_diem_tay_phai.verticalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem21 = self.bang_diem_tay_phai.verticalHeaderItem(3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem22 = self.bang_diem_tay_phai.verticalHeaderItem(4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem23 = self.bang_diem_tay_phai.verticalHeaderItem(5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem24 = self.bang_diem_tay_phai.verticalHeaderItem(6)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem25 = self.bang_diem_tay_phai.verticalHeaderItem(7)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem26 = self.bang_diem_tay_phai.verticalHeaderItem(8)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem27 = self.bang_diem_tay_phai.verticalHeaderItem(9)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"10", None));
        self.Tab_diem_va_ket_qua.setTabText(self.Tab_diem_va_ket_qua.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"V\u1ecb tr\u00ed c\u00e1c \u0111i\u1ec3m tay ph\u1ea3i", None))
        ___qtablewidgetitem28 = self.bang_diem_tay_trai.horizontalHeaderItem(0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"K\u00edch th\u01b0\u1edbc \u1ea3nh", None));
        ___qtablewidgetitem29 = self.bang_diem_tay_trai.horizontalHeaderItem(1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"T\u00ean \u0111i\u1ec3m", None));
        ___qtablewidgetitem30 = self.bang_diem_tay_trai.horizontalHeaderItem(2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"V\u1ecb tr\u00ed", None));
        ___qtablewidgetitem31 = self.bang_diem_tay_trai.horizontalHeaderItem(3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"K\u00edch th\u01b0\u1edbc \u1ea3nh", None));
        ___qtablewidgetitem32 = self.bang_diem_tay_trai.horizontalHeaderItem(4)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"T\u00ean \u0111i\u1ec3m", None));
        ___qtablewidgetitem33 = self.bang_diem_tay_trai.horizontalHeaderItem(5)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"V\u1ecb tr\u00ed", None));
        ___qtablewidgetitem34 = self.bang_diem_tay_trai.horizontalHeaderItem(6)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"K\u00edch th\u01b0\u1edbc \u1ea3nh", None));
        ___qtablewidgetitem35 = self.bang_diem_tay_trai.horizontalHeaderItem(7)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"T\u00ean \u0111i\u1ec3m", None));
        ___qtablewidgetitem36 = self.bang_diem_tay_trai.horizontalHeaderItem(8)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"V\u1ecb tr\u00ed", None));
        ___qtablewidgetitem37 = self.bang_diem_tay_trai.horizontalHeaderItem(9)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"K\u00edch th\u01b0\u1edbc \u1ea3nh", None));
        ___qtablewidgetitem38 = self.bang_diem_tay_trai.horizontalHeaderItem(10)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"T\u00ean \u0111i\u1ec3m", None));
        ___qtablewidgetitem39 = self.bang_diem_tay_trai.horizontalHeaderItem(11)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"V\u1ecb tr\u00ed", None));
        ___qtablewidgetitem40 = self.bang_diem_tay_trai.horizontalHeaderItem(12)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"K\u00edch th\u01b0\u1edbc \u1ea3nh", None));
        ___qtablewidgetitem41 = self.bang_diem_tay_trai.horizontalHeaderItem(13)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"T\u00ean \u0111i\u1ec3m", None));
        ___qtablewidgetitem42 = self.bang_diem_tay_trai.horizontalHeaderItem(14)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"V\u1ecb tr\u00ed", None));
        ___qtablewidgetitem43 = self.bang_diem_tay_trai.horizontalHeaderItem(15)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"K\u00edch th\u01b0\u1edbc \u1ea3nh", None));
        ___qtablewidgetitem44 = self.bang_diem_tay_trai.horizontalHeaderItem(16)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"T\u00ean \u0111i\u1ec3m", None));
        ___qtablewidgetitem45 = self.bang_diem_tay_trai.horizontalHeaderItem(17)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"V\u1ecb tr\u00ed", None));
        ___qtablewidgetitem46 = self.bang_diem_tay_trai.verticalHeaderItem(0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem47 = self.bang_diem_tay_trai.verticalHeaderItem(1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem48 = self.bang_diem_tay_trai.verticalHeaderItem(2)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem49 = self.bang_diem_tay_trai.verticalHeaderItem(3)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem50 = self.bang_diem_tay_trai.verticalHeaderItem(4)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem51 = self.bang_diem_tay_trai.verticalHeaderItem(5)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem52 = self.bang_diem_tay_trai.verticalHeaderItem(6)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem53 = self.bang_diem_tay_trai.verticalHeaderItem(7)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem54 = self.bang_diem_tay_trai.verticalHeaderItem(8)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem55 = self.bang_diem_tay_trai.verticalHeaderItem(9)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"10", None));
        self.Tab_diem_va_ket_qua.setTabText(self.Tab_diem_va_ket_qua.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"V\u1ecb tr\u00ed c\u00e1c \u0111i\u1ec3m tay tr\u00e1i", None))
        ___qtablewidgetitem56 = self.bang_khoang_cach_tay_phai.horizontalHeaderItem(0)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"K\u00edch th\u01b0\u1edbc \u1ea3nh", None));
        ___qtablewidgetitem57 = self.bang_khoang_cach_tay_phai.horizontalHeaderItem(1)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"T\u00ean", None));
        ___qtablewidgetitem58 = self.bang_khoang_cach_tay_phai.horizontalHeaderItem(2)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"Kho\u1ea3ng c\u00e1ch", None));
        ___qtablewidgetitem59 = self.bang_khoang_cach_tay_phai.horizontalHeaderItem(3)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"K\u00edch th\u01b0\u1edbc \u1ea3nh", None));
        ___qtablewidgetitem60 = self.bang_khoang_cach_tay_phai.horizontalHeaderItem(4)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"T\u00ean", None));
        ___qtablewidgetitem61 = self.bang_khoang_cach_tay_phai.horizontalHeaderItem(5)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"Kho\u1ea3ng c\u00e1ch", None));
        ___qtablewidgetitem62 = self.bang_khoang_cach_tay_phai.horizontalHeaderItem(6)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"K\u00edch th\u01b0\u1edbc \u1ea3nh", None));
        ___qtablewidgetitem63 = self.bang_khoang_cach_tay_phai.horizontalHeaderItem(7)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"T\u00ean", None));
        ___qtablewidgetitem64 = self.bang_khoang_cach_tay_phai.horizontalHeaderItem(8)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"Kho\u1ea3ng c\u00e1ch", None));
        ___qtablewidgetitem65 = self.bang_khoang_cach_tay_phai.horizontalHeaderItem(9)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"K\u00edch th\u01b0\u1edbc \u1ea3nh", None));
        ___qtablewidgetitem66 = self.bang_khoang_cach_tay_phai.horizontalHeaderItem(10)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"T\u00ean", None));
        ___qtablewidgetitem67 = self.bang_khoang_cach_tay_phai.horizontalHeaderItem(11)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"Kho\u1ea3ng c\u00e1ch", None));
        ___qtablewidgetitem68 = self.bang_khoang_cach_tay_phai.verticalHeaderItem(0)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem69 = self.bang_khoang_cach_tay_phai.verticalHeaderItem(1)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem70 = self.bang_khoang_cach_tay_phai.verticalHeaderItem(2)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem71 = self.bang_khoang_cach_tay_phai.verticalHeaderItem(3)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem72 = self.bang_khoang_cach_tay_phai.verticalHeaderItem(4)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem73 = self.bang_khoang_cach_tay_phai.verticalHeaderItem(5)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem74 = self.bang_khoang_cach_tay_phai.verticalHeaderItem(6)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem75 = self.bang_khoang_cach_tay_phai.verticalHeaderItem(7)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem76 = self.bang_khoang_cach_tay_phai.verticalHeaderItem(8)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem77 = self.bang_khoang_cach_tay_phai.verticalHeaderItem(9)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"10", None));
        self.Tab_diem_va_ket_qua.setTabText(self.Tab_diem_va_ket_qua.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Kho\u1ea3ng c\u00e1ch thu\u1ed9c tay ph\u1ea3i", None))
        ___qtablewidgetitem78 = self.bang_khoang_cach_tay_trai.horizontalHeaderItem(0)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"K\u00edch th\u01b0\u1edbc \u1ea3nh", None));
        ___qtablewidgetitem79 = self.bang_khoang_cach_tay_trai.horizontalHeaderItem(1)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"T\u00ean", None));
        ___qtablewidgetitem80 = self.bang_khoang_cach_tay_trai.horizontalHeaderItem(2)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"Kho\u1ea3ng c\u00e1ch", None));
        ___qtablewidgetitem81 = self.bang_khoang_cach_tay_trai.horizontalHeaderItem(3)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"K\u00edch th\u01b0\u1edbc \u1ea3nh", None));
        ___qtablewidgetitem82 = self.bang_khoang_cach_tay_trai.horizontalHeaderItem(4)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"T\u00ean", None));
        ___qtablewidgetitem83 = self.bang_khoang_cach_tay_trai.horizontalHeaderItem(5)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"Kho\u1ea3ng c\u00e1ch", None));
        ___qtablewidgetitem84 = self.bang_khoang_cach_tay_trai.horizontalHeaderItem(6)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"K\u00edch th\u01b0\u1edbc \u1ea3nh", None));
        ___qtablewidgetitem85 = self.bang_khoang_cach_tay_trai.horizontalHeaderItem(7)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"T\u00ean", None));
        ___qtablewidgetitem86 = self.bang_khoang_cach_tay_trai.horizontalHeaderItem(8)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"Kho\u1ea3ng c\u00e1ch", None));
        ___qtablewidgetitem87 = self.bang_khoang_cach_tay_trai.horizontalHeaderItem(9)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"K\u00edch th\u01b0\u1edbc \u1ea3nh", None));
        ___qtablewidgetitem88 = self.bang_khoang_cach_tay_trai.horizontalHeaderItem(10)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"T\u00ean", None));
        ___qtablewidgetitem89 = self.bang_khoang_cach_tay_trai.horizontalHeaderItem(11)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"Kho\u1ea3ng c\u00e1ch", None));
        ___qtablewidgetitem90 = self.bang_khoang_cach_tay_trai.verticalHeaderItem(0)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem91 = self.bang_khoang_cach_tay_trai.verticalHeaderItem(1)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem92 = self.bang_khoang_cach_tay_trai.verticalHeaderItem(2)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem93 = self.bang_khoang_cach_tay_trai.verticalHeaderItem(3)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem94 = self.bang_khoang_cach_tay_trai.verticalHeaderItem(4)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem95 = self.bang_khoang_cach_tay_trai.verticalHeaderItem(5)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem96 = self.bang_khoang_cach_tay_trai.verticalHeaderItem(6)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem97 = self.bang_khoang_cach_tay_trai.verticalHeaderItem(7)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem98 = self.bang_khoang_cach_tay_trai.verticalHeaderItem(8)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem99 = self.bang_khoang_cach_tay_trai.verticalHeaderItem(9)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"10", None));
        self.Tab_diem_va_ket_qua.setTabText(self.Tab_diem_va_ket_qua.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Kho\u1ea3ng c\u00e1ch thu\u1ed9c tay tr\u00e1i", None))
        self.XemKQBT.setText(QCoreApplication.translate("MainWindow", u"Xem KQ", None))
        self.LuuBT.setText(QCoreApplication.translate("MainWindow", u"L\u01b0u ", None))
        self.tabTruocBT_2.setText(QCoreApplication.translate("MainWindow", u"Tab tr\u01b0\u1edbc", None))
        self.tabSauBT_2.setText(QCoreApplication.translate("MainWindow", u"Tab sau", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"NH\u1eacP TH\u00d4NG TIN", None))
        self.xoaBT.setText(QCoreApplication.translate("MainWindow", u"Xo\u00e1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Processing", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_nhap_thong_tin), QCoreApplication.translate("MainWindow", u"Nh\u1eadp th\u00f4ng tin", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0110i\u1ec1u ch\u1ec9nh ng\u01b0\u1ee1ng", None))
        self.doSangLB_3.setText(QCoreApplication.translate("MainWindow", u"Ng\u01b0\u1ee1ng t\u00e1ch n\u1ec1n", None))
        self.cameraOptionGB.setTitle(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn Camera", None))
        self.chonCameraLB.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn camera:", None))
        self.chonCamCB.setItemText(0, QCoreApplication.translate("MainWindow", u"T\u1eaft", None))
        self.chonCamCB.setItemText(1, QCoreApplication.translate("MainWindow", u"Camera 0", None))
        self.chonCamCB.setItemText(2, QCoreApplication.translate("MainWindow", u"Camera 1", None))
        self.chonCamCB.setItemText(3, QCoreApplication.translate("MainWindow", u"Camera 2", None))
        self.chonCamCB.setItemText(4, QCoreApplication.translate("MainWindow", u"Camera 3", None))

        self.chonKenhLB.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn k\u00eanh:", None))
        self.chonKenhCB.setItemText(0, QCoreApplication.translate("MainWindow", u"RGB", None))
        self.chonKenhCB.setItemText(1, QCoreApplication.translate("MainWindow", u"Grayscale", None))

        self.smallScreenRB.setText(QCoreApplication.translate("MainWindow", u"M\u00e0n h\u00ecnh nh\u1ecf", None))
        self.orginalScreenRB.setText(QCoreApplication.translate("MainWindow", u"M\u00e0n h\u00ecnh g\u1ed1c", None))
        self.doSangLB.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ed9 s\u00e1ng", None))
        self.doSangLB_2.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ed9 t\u01b0\u01a1ng ph\u1ea3n", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Tu\u1ef3 ch\u1ecdn", None))
        self.hienduongbaoQRB.setText(QCoreApplication.translate("MainWindow", u"Hi\u1ec7n \u0111\u01b0\u1eddng bao", None))
        self.tatduongbaoQRB.setText(QCoreApplication.translate("MainWindow", u"T\u1eaft \u0111\u01b0\u1eddng bao", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn m\u00e0n h\u00ecnh", None))
        self.chonCameraLB_2.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn m\u00e0n h\u00ecnh", None))
        self.choManHinhCB.setItemText(0, QCoreApplication.translate("MainWindow", u"T\u1ef1 \u0111\u1ed9ng", None))
        self.choManHinhCB.setItemText(1, QCoreApplication.translate("MainWindow", u"2:3 (1080 x 720) ", None))
        self.choManHinhCB.setItemText(2, QCoreApplication.translate("MainWindow", u"16:9 (960 x 540) ", None))
        self.choManHinhCB.setItemText(3, QCoreApplication.translate("MainWindow", u"16:9 (640 x 360) ", None))
        self.choManHinhCB.setItemText(4, QCoreApplication.translate("MainWindow", u"4:3 (960 x 720) ", None))
        self.choManHinhCB.setItemText(5, QCoreApplication.translate("MainWindow", u"4:3 (640 x 480) ", None))

        self.chonCameraLB_3.setText(QCoreApplication.translate("MainWindow", u"\u0110i\u1ec1u ch\u1ec9nh h\u01b0\u1edbng", None))
        self.chonDieuHuongCB.setItemText(0, QCoreApplication.translate("MainWindow", u"Kh\u00f4ng", None))
        self.chonDieuHuongCB.setItemText(1, QCoreApplication.translate("MainWindow", u"L\u1eadt", None))
        self.chonDieuHuongCB.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0110\u1ea3o ng\u01b0\u1ee3c", None))
        self.chonDieuHuongCB.setItemText(3, QCoreApplication.translate("MainWindow", u"Xoay 90 \u0111\u1ed9 sang tr\u00e1i", None))
        self.chonDieuHuongCB.setItemText(4, QCoreApplication.translate("MainWindow", u"Xoay 90 \u0111\u1ed9 sang ph\u1ea3i", None))

        self.xemKetQuaBT.setText(QCoreApplication.translate("MainWindow", u"Xem \u1ea3nh k\u1ebft qu\u1ea3", None))
        self.tabSauBT.setText(QCoreApplication.translate("MainWindow", u"Tab sau", None))
        self.chupBT.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ee5p", None))
        self.tabTruocBT.setText(QCoreApplication.translate("MainWindow", u"Tab tr\u01b0\u1edbc", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.anhMauLB.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u1ea2nh m\u1eabu", None))
        self.cameraLB.setText("")
        self.noteLB.setText("")
        self.SoLB.setText("")
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn ch\u1ebf \u0111\u1ed9 ch\u1ee5p", None))
        self.tuDongQRB.setText(QCoreApplication.translate("MainWindow", u"T\u1ef1 \u0111\u1ed9ng", None))
        self.thuCongQRB.setText(QCoreApplication.translate("MainWindow", u"Th\u1ee7 c\u00f4ng", None))
        self.luiBT.setText(QCoreApplication.translate("MainWindow", u"L\u00f9i", None))
        self.tienBT.setText(QCoreApplication.translate("MainWindow", u"Ti\u1ebfn", None))
        self.resetBT.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_chup_anh), QCoreApplication.translate("MainWindow", u"Ch\u1ee5p \u1ea3nh", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuCalibration.setTitle(QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.menuQuit.setTitle(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

