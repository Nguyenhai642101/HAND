# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_nguongbfahuH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os

def convert_nparray_to_QPixmap(img):
    """
    input: Anh mau RGB hoac anh xam
    output: Tao mot doi tuong QPixmax de hien thi bang cach chuyen du lieu anh sang mot doi tuong QImage
    print("{0} {1} {2}".format(img.shape[0], img.shape[1], img.ndim, ))
    """
    if img.ndim == 2:
        w, h = img.shape
        # Convert resulting image to pixmap
        qimg = QImage(img.data, h, w, h, QImage.Format_Grayscale8)
        qpixmap = QPixmap(qimg)
        return qpixmap
    if img.ndim == 3:
        w, h, ch = img.shape
        # Convert resulting image to pixmap
        qimg = QImage(img.data, h, w, 3 * h, QImage.Format_RGB888).rgbSwapped()
        qpixmap = QPixmap(qimg)
        # print(qpixmap.size())
        return qpixmap


class Ui_MainWindow(object):
    def __init__(self):
        self.img = None

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1400, 960)
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
        self.anhLB.setAlignment(Qt.AlignCenter)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(460, 60, 701, 31))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1200, 60, 93, 28))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1400, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.radioButton.toggled.connect(self.radioButton_toggled)

        self.nguongSL.valueChanged[int].connect(self.nguongSL_valueChanged)
        self.ngongDSB.valueChanged.connect(self.ngongDSB_valueChanged)
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"L\u1ef1a ch\u1ecdn", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"L\u1ea5y ng\u01b0\u1ee1ng", None))
        self.anhLB.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Xem \u1ea3nh", None))

    # setupUi
    # setupUi
    def pushButton_clicked(self):
        filepath = self.textEdit.toPlainText()
        # print(filepath)
        # img = cv2.imread(r'{}'.format(filepath))
        self.image = cv2.imread(r'{}'.format(str(filepath)))
        # cv2.imshow('a', self.img)
        # cv2.waitKey(0)
        self.img = self.image.copy()
        if self.img.shape[0] / 640 > 1 or self.img.shape[1] / 960 > 1:
            if self.img.shape[0] / 640 >= self.img.shape[1] / 960:
                scale_ratio = 640 / self.img.shape[0]
                width = int(self.img.shape[1] * scale_ratio)
                height = 640
                dim = (width, height)
                self.img = cv2.resize(self.img, dim)
            else:
                scale_ratio = 960 / self.img.shape[1]
                height = int(self.img.shape[0] * scale_ratio)
                width = 960
                dim = (width, height)
                self.img = cv2.resize(self.img, dim)
            # if self.mode:
            #     gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            #     thresh = cv2.threshold(gray, self.nguong, 255, cv2.THRESH_BINARY)[1]
            #     cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
            #
            #     if len(cnts) != 0:
            #         c = max(cnts, key=cv2.contourArea)
            #         for i in range(len(c)):
            #             cv2.drawContours(self.img, [c], -1, (240, 0, 159), 1)
            #     self.anhLB.setPixmap(convert_nparray_to_QPixmap(self.img))

        self.anhLB.setPixmap(convert_nparray_to_QPixmap(self.img))
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    def radioButton_toggled(self):
        self.mode = True

    def nguongSL_valueChanged(self, value):
        self.nguong = int(value)
        self.ngongDSB.setValue(value)
        cv2.destroyAllWindows()
        image = self.img.copy()
        if self.mode:
            gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            thresh = cv2.threshold(gray, self.nguong, 255, cv2.THRESH_BINARY)[1]
            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

            if len(cnts) != 0:
                c = max(cnts, key=cv2.contourArea)
                for i in range(len(c)):
                    cv2.drawContours(image, [c], -1, (240, 0, 159), 1)
        self.anhLB.setPixmap(convert_nparray_to_QPixmap(image))

    def ngongDSB_valueChanged(self, value):
        self.nguong = int(value)
        self.nguongSL.setValue(value)
        cv2.destroyAllWindows()
        image = self.img.copy()
        if self.mode:
            gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            thresh = cv2.threshold(gray, self.nguong, 255, cv2.THRESH_BINARY)[1]
            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

            if len(cnts) != 0:
                c = max(cnts, key=cv2.contourArea)
                for i in range(len(c)):
                    cv2.drawContours(image, [c], -1, (240, 0, 159), 1)
        self.anhLB.setPixmap(convert_nparray_to_QPixmap(image))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
