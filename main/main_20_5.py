# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designermOVtlu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import threading
import time

import imutils
import numpy as np
import sys
import os
import cv2

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from App.run.MyLib import *
from App.run.Math import *
from App.run.TongHop import *
from App.gui.IntroductionUI import Ui_IntroductionWindow
from App.gui.CaptureUI import Ui_CaptureWindow


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


def change_brightness(input_img, value):
    """
    input: Anh mau RGB và do sang
    output: Anh RGB da thay doi do sang
    """
    hsv = cv2.cvtColor(input_img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v, value)
    final_hsv = cv2.merge((h, s, v))
    output_img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return output_img


def change_contrast(input_img, contrast=127):
    """
    input: Anh mau RGB và do tuong phan
    output: Anh RGB da thay doi do tuong phan
    """
    contrast = map(contrast, -50, 50, -127, 127)

    output_img = input_img.copy()
    if contrast != 0:
        f = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127 * (1 - f)
        output_img = cv2.addWeighted(input_img, alpha_c, input_img, 0, gamma_c)
    return output_img


def map(x, in_min, in_max, out_min, out_max):
    """
    de anh xa cac khoang in out
    """
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


class IntroductionWindow(QMainWindow, Ui_IntroductionWindow):
    def __init__(self):
        super(IntroductionWindow, self).__init__()
        self.setupUi(self)

        self.captureWindow = CaptureWindow()
        self.captureWindow.setupUi(self.captureWindow)

        self.thoatBT.clicked.connect(self.thoatBT_clicked)
        self.dangNhapBT.clicked.connect(self.dangNhapBT_clicked)

        self.captureWindow.chonCamCB.currentTextChanged.connect(self.captureWindow.chonCamCB_changed)

        self.captureWindow.tabWidget.setCurrentIndex(0)
        ################### 2.1 chonCamera action ######################
        self.captureWindow.chonCamCB.currentTextChanged.connect(self.captureWindow.chonCamCB_changed)
        ################### 2.1 chonKenhCB action ######################

        ################### 2.2 chonKenhCB action ######################
        self.captureWindow.chonKenhCB.currentTextChanged.connect(self.captureWindow.chonKenhCB_changed)
        ################### 2.2 chonKenhCB action ######################

        ################### 2.3 chon screen action ######################
        self.captureWindow.smallScreenRB.toggled.connect(self.captureWindow.smallScreenRB_toggled)
        self.captureWindow.orginalScreenRB.toggled.connect(self.captureWindow.fullScreenRB_toggled)
        ################### 2.3 chon screen action ######################

        ################### 2.4 thay doi do sang action ##################
        self.captureWindow.BrightnessSlider.valueChanged[int].connect(self.captureWindow.BrightnessSlider_valueChanged)
        self.captureWindow.doSangDSB.valueChanged.connect(self.captureWindow.doSangDSB_valueChanged)
        ################### 2.4 end thay doi do sang action ##############

        ################### 2.5 thay doi do tuong phan action #############
        self.captureWindow.ContrastSlider.valueChanged[int].connect(self.captureWindow.ContrastSlider_valueChanged)
        self.captureWindow.doTuongPhanDSB.valueChanged.connect(self.captureWindow.doTuongPhanDSB_valueChanged)
        ################### 2.5 end thay doi do tuong phan action #############

        ################### 2.6 thay doi nguong action #############
        self.captureWindow.nguongSlider.valueChanged[int].connect(self.captureWindow.nguongSlider_valueChanged)
        self.captureWindow.nguongDSB.valueChanged.connect(self.captureWindow.nguongDSB_valueChanged)
        ################### 2.6 end thay doi nguong action ##########

        ################### 2.7 chon hien duong bao #############
        self.captureWindow.hienduongbaoQRB.toggled.connect(self.captureWindow.hienduongbaoQRB_toggled)
        self.captureWindow.tatduongbaoQRB.toggled.connect(self.captureWindow.tatduongbaoQRB_toggled)
        ################### 2.7 end chon hien duong bao ##########

        ################### 2.8 chon tay #############
        self.captureWindow.tuDongQRB.toggled.connect(self.captureWindow.tuDongQRB_toggled)
        self.captureWindow.thuCongQRB.toggled.connect(self.captureWindow.thuCongQRB_toggled)
        ################### 2.8 end chon hien chon tay ##########

        ################### 2.9 chon kich thuoc khung hinh ######################
        self.captureWindow.choManHinhCB.currentTextChanged.connect(self.captureWindow.choManHinhCB_changed)
        ################### 2.9 end chon kich thuoc khung hinh ######################

        ################### 2.10 chon dieu chinh khung hinh ######################
        self.captureWindow.chonDieuHuongCB.currentTextChanged.connect(self.captureWindow.chonDieuHuongCB_changed)
        ################### 2.10 end chon dieu chinh khung hinh ######################

        # Button
        ################### 2.12 chup button ######################
        self.captureWindow.chupBT.clicked.connect(self.captureWindow.chupBT_clicked)
        ################### 2.12 end chup button ######################

        ################### 2.13 chup button ######################
        self.captureWindow.XemKQBT.clicked.connect(self.captureWindow.XemKQBT_clicked)
        ################### 2.13 end chup button ######################

    def dangNhapBT_clicked(self):
        if self.captureWindow.isVisible():
            self.captureWindow.close()
            self.hide()
        else:
            self.captureWindow.show()
            self.hide()
            # self.cameraRun()

    def thoatBT_clicked(self):
        # when click exitBT button , close all screen
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit Main Window?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCoreApplication.instance().quit()

    def closeEvent(self, event):
        # close with X button
        reply = QMessageBox.question(self.centralwidget, 'Message',
                                     "Are you sure to quit Window?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            # self.captureWindow.closeEvent(event)
            self.captureWindow.cap.release()
            cv2.destroyAllWindows()
            QCoreApplication.instance().quit()
            event.accept()
        else:
            event.ignore()


# toPlainText()
class CaptureWindow(QMainWindow, Ui_CaptureWindow):
    def __init__(self):
        super(CaptureWindow, self).__init__()
        self.data2 = None
        self.data1 = None
        self.cur_mang_nguong = []
        self.mang_nguong = []
        self.cur_dir = None
        self.myThread1 = None
        self.index = 1
        self.soLuong = 14
        self.myRootPath = "D:/HUST/LAB/DIR"
        self.mydir = None
        self.frame_out = None
        self.frame = None
        self.cap_pix = None
        self.cap = cv2.VideoCapture(0)
        self.mode = 0
        self.duong_bao_show = 0
        self.screen_show = 0
        self.nguong_adjuster = 65
        self.contrast_adjuster = 0
        self.brightness_adjuster = 0
        self.cam_curr_index = None
        self.cameraLogic = -1
        self.man_hinh_number = 0
        self.huong_number = 0
        self.chanel = 0
        self.setupUi(self)

        ################### 2.1 chonCamera action ######################
        self.chonCamCB.currentTextChanged.connect(self.chonCamCB_changed)
        ################### 2.1 chonKenhCB action ######################

        ################### 2.2 chonKenhCB action ######################
        self.chonKenhCB.currentTextChanged.connect(self.chonKenhCB_changed)
        ################### 2.2 chonKenhCB action ######################

        ################### 2.3 chon screen action ######################
        self.smallScreenRB.toggled.connect(self.smallScreenRB_toggled)
        self.orginalScreenRB.toggled.connect(self.fullScreenRB_toggled)
        ################### 2.3 chon screen action ######################

        ################### 2.4 thay doi do sang action ##################
        self.BrightnessSlider.valueChanged[int].connect(self.BrightnessSlider_valueChanged)
        self.doSangDSB.valueChanged.connect(self.doSangDSB_valueChanged)
        ################### 2.4 end thay doi do sang action ##############

        ################### 2.5 thay doi do tuong phan action #############
        self.ContrastSlider.valueChanged[int].connect(self.ContrastSlider_valueChanged)
        self.doTuongPhanDSB.valueChanged.connect(self.doTuongPhanDSB_valueChanged)
        ################### 2.5 end thay doi do tuong phan action ##########

        ################### 2.6 thay doi nguong action #############
        self.nguongSlider.valueChanged[int].connect(self.nguongSlider_valueChanged)
        self.nguongDSB.valueChanged.connect(self.nguongDSB_valueChanged)
        ################### 2.6 end thay doi nguong action ##########

        ################### 2.7 chon hien duong bao #############
        self.hienduongbaoQRB.toggled.connect(self.hienduongbaoQRB_toggled)
        self.tatduongbaoQRB.toggled.connect(self.tatduongbaoQRB_toggled)
        ################### 2.7 end chon hien duong bao ##########

        ################### 2.8 chon tay #############
        self.tuDongQRB.toggled.connect(self.tuDongQRB_toggled)
        self.thuCongQRB.toggled.connect(self.thuCongQRB_toggled)
        ################### 2.8 end chon hien chon tay ##########

        ################### 2.9 chon kich thuoc khung hinh ######################
        self.choManHinhCB.currentTextChanged.connect(self.choManHinhCB_changed)
        ################### 2.9 end chon kich thuoc khung hinh ######################

        ################### 2.10 chon dieu chinh khung hinh ######################
        self.chonDieuHuongCB.currentTextChanged.connect(self.chonDieuHuongCB_changed)
        ################### 2.10 end chon dieu chinh khung hinh ######################

        # Button
        ################### 2.12 chup button ######################
        self.chupBT.clicked.connect(self.chupBT_clicked)
        ################### 2.12 end chup button ######################
        # Button
        ################### 2.13 xemKQ button ######################
        self.XemKQBT.clicked.connect(self.XemKQBT_clicked)
        ################### 2.13 end chup button ######################

    def chonCamCB_changed(self):
        chonCamText = self.chonCamCB.currentText()
        if chonCamText == "Tắt":
            self.cam_curr_index = self.chonCamCB.currentIndex()
            self.cameraLogic = -1
            print(chonCamText)
            # self.TestCameraRun()
            self.CameraRun()

        if chonCamText == "Camera 0":
            self.cam_curr_index = self.chonCamCB.currentIndex()
            self.cameraLogic = 0
            print(chonCamText)
            # self.TestCameraRun()
            self.CameraRun()
        if chonCamText == "Camera 1":
            self.cam_curr_index = self.chonCamCB.currentIndex()
            self.cameraLogic = 1
            print(chonCamText)
            # self.TestCameraRun()
            self.CameraRun()

    def chonKenhCB_changed(self):
        chonKenhText = self.chonKenhCB.currentText()
        if chonKenhText == "RGB":
            self.chanel = 0
            # cv2.destroyAllWindows()
        if chonKenhText == "Grayscale":
            self.chanel = 1
            # cv2.destroyAllWindows()

    def smallScreenRB_toggled(self):
        self.screen_show = 0

    def fullScreenRB_toggled(self):
        self.screen_show = 1

    def BrightnessSlider_valueChanged(self, value):
        self.brightness_adjuster = int(value)
        self.doSangDSB.setValue(value)

    def doSangDSB_valueChanged(self, value):
        self.brightness_adjuster = value
        self.BrightnessSlider.setValue(value)

    def ContrastSlider_valueChanged(self, value):
        self.contrast_adjuster = int(value)
        self.doTuongPhanDSB.setValue(value)

    def doTuongPhanDSB_valueChanged(self, value):
        self.contrast_adjuster = value
        self.ContrastSlider.setValue(value)

    def nguongSlider_valueChanged(self, value):
        self.nguong_adjuster = int(value)
        self.nguongDSB.setValue(value)

    def nguongDSB_valueChanged(self, value):
        self.nguong_adjuster = value
        self.nguongSlider.setValue(value)

    def hienduongbaoQRB_toggled(self):
        self.duong_bao_show = 1

    def tatduongbaoQRB_toggled(self):
        self.duong_bao_show = 0

    def tuDongQRB_toggled(self):
        self.mode = 0

    def thuCongQRB_toggled(self):
        self.mode = 1

    def choManHinhCB_changed(self):
        choManHinhText = self.choManHinhCB.currentText()
        if choManHinhText == "Tự động":
            self.man_hinh_number = 0
            cv2.destroyAllWindows()
        if choManHinhText == "2:3 (1080 x 720) ":
            self.man_hinh_number = 1
            # print(choManHinhText)
            cv2.destroyAllWindows()
        if choManHinhText == "16:9 (960 x 540) ":
            self.man_hinh_number = 2
            cv2.destroyAllWindows()
        if choManHinhText == "16:9 (640 x 360) ":
            self.man_hinh_number = 3
            cv2.destroyAllWindows()
        if choManHinhText == "4:3 (960 x 720) ":
            self.man_hinh_number = 4
            cv2.destroyAllWindows()
        if choManHinhText == "4:3 (640 x 480) ":
            self.man_hinh_number = 5
            cv2.destroyAllWindows()

    def chonDieuHuongCB_changed(self):
        choDieuHuongText = self.chonDieuHuongCB.currentText()
        if choDieuHuongText == "Không":
            self.huong_number = 0
            cv2.destroyAllWindows()
        if choDieuHuongText == "Lật":
            self.huong_number = 1
            cv2.destroyAllWindows()
        if choDieuHuongText == "Đảo ngược":
            self.huong_number = 2
            cv2.destroyAllWindows()
        if choDieuHuongText == "Xoay 90 độ sang trái":
            self.huong_number = 3
            cv2.destroyAllWindows()
        if choDieuHuongText == "Xoay 90 độ sang phải":
            self.huong_number = 4
            cv2.destroyAllWindows()

    # def ReturnFrame(self, frame, screen_show, chanel,
    #                 duong_bao_show, mode, man_hinh_number, huong_number,
    #                 brightness_adjuster, contrast_adjuster, nguong_adjuster):
    def ReturnFrameLan1(self, frame, screen_show, huong_number, man_hinh_number):
        """
        Điều chỉnh đầu ra của frame
        """
        frame_copy = frame.copy()
        frame_out = []
        """
        Chọn kích thước và hướng của frame
        """
        if screen_show == 0:

            if man_hinh_number == 1:
                dim = (1080, 720)
                frame_out_man_hinh_number_1 = cv2.resize(frame_copy, dim)
                if huong_number == 1:
                    frame_out = cv2.flip(frame_out_man_hinh_number_1, 1)
                    frame_out = self.AutoScale(frame_out)
                if huong_number == 2:
                    frame_out = cv2.rotate(frame_out_man_hinh_number_1, cv2.ROTATE_180)
                    frame_out = self.AutoScale(frame_out)
                if huong_number == 3:
                    frame_out = cv2.rotate(frame_out_man_hinh_number_1, cv2.ROTATE_90_COUNTERCLOCKWISE)
                    frame_out = self.AutoScale(frame_out)
                if huong_number == 4:
                    frame_out = cv2.rotate(frame_out_man_hinh_number_1, cv2.ROTATE_90_CLOCKWISE)
                    frame_out = self.AutoScale(frame_out)
                if huong_number == 0:
                    frame_out = frame_out_man_hinh_number_1
                    # frame_out = self.AutoScale(frame_out)
            if man_hinh_number == 2:
                dim = (960, 540)
                frame_out_man_hinh_number_2 = cv2.resize(frame_copy, dim)
                if huong_number == 1:
                    frame_out = cv2.flip(frame_out_man_hinh_number_2, 1)
                    frame_out = self.AutoScale(frame_out)
                if huong_number == 2:
                    frame_out = cv2.rotate(frame_out_man_hinh_number_2, cv2.ROTATE_180)
                    frame_out = self.AutoScale(frame_out)
                if huong_number == 3:
                    frame_out = cv2.rotate(frame_out_man_hinh_number_2, cv2.ROTATE_90_COUNTERCLOCKWISE)
                    frame_out = self.AutoScale(frame_out)
                if huong_number == 4:
                    frame_out = cv2.rotate(frame_out_man_hinh_number_2, cv2.ROTATE_90_CLOCKWISE)
                    frame_out = self.AutoScale(frame_out)
                if huong_number == 0:
                    frame_out = frame_out_man_hinh_number_2
                    # frame_out = self.AutoScale(frame_out)
            if man_hinh_number == 3:
                dim = (640, 360)
                frame_out_man_hinh_number_3 = cv2.resize(frame_copy, dim)
                if huong_number == 1:
                    frame_out = cv2.flip(frame_out_man_hinh_number_3, 1)
                    frame_out = self.AutoScale(frame_out)
                if huong_number == 2:
                    frame_out = cv2.rotate(frame_out_man_hinh_number_3, cv2.ROTATE_180)
                    frame_out = self.AutoScale(frame_out)
                if huong_number == 3:
                    frame_out = cv2.rotate(frame_out_man_hinh_number_3, cv2.ROTATE_90_COUNTERCLOCKWISE)
                    frame_out = self.AutoScale(frame_out)
                if huong_number == 4:
                    frame_out = cv2.rotate(frame_out_man_hinh_number_3, cv2.ROTATE_90_CLOCKWISE)
                    frame_out = self.AutoScale(frame_out)
                if huong_number == 0:
                    frame_out = frame_out_man_hinh_number_3
                    # frame_out = self.AutoScale(frame_out)
            if man_hinh_number == 4:
                dim = (960, 720)
                frame_out_man_hinh_number_4 = cv2.resize(frame_copy, dim)
                if huong_number == 1:
                    frame_out = cv2.flip(frame_out_man_hinh_number_4, 1)
                    frame_out = self.AutoScale(frame_out)
                if huong_number == 2:
                    frame_out = cv2.rotate(frame_out_man_hinh_number_4, cv2.ROTATE_180)
                    frame_out = self.AutoScale(frame_out)
                if huong_number == 3:
                    frame_out = cv2.rotate(frame_out_man_hinh_number_4, cv2.ROTATE_90_COUNTERCLOCKWISE)
                    frame_out = self.AutoScale(frame_out)
                if huong_number == 4:
                    frame_out = cv2.rotate(frame_out_man_hinh_number_4, cv2.ROTATE_90_CLOCKWISE)
                    frame_out = self.AutoScale(frame_out)
                if huong_number == 0:
                    frame_out = frame_out_man_hinh_number_4
                    # frame_out = self.AutoScale(frame_out)
            if man_hinh_number == 5:
                dim = (640, 480)
                frame_out_man_hinh_number_5 = cv2.resize(frame_copy, dim)
                if huong_number == 1:
                    frame_out = cv2.flip(frame_out_man_hinh_number_5, 1)
                    frame_out = self.AutoScale(frame_out)
                if huong_number == 2:
                    frame_out = cv2.rotate(frame_out_man_hinh_number_5, cv2.ROTATE_180)
                    frame_out = self.AutoScale(frame_out)
                if huong_number == 3:
                    frame_out = cv2.rotate(frame_out_man_hinh_number_5, cv2.ROTATE_90_COUNTERCLOCKWISE)
                    frame_out = self.AutoScale(frame_out)
                if huong_number == 4:
                    frame_out = cv2.rotate(frame_out_man_hinh_number_5, cv2.ROTATE_90_CLOCKWISE)
                    frame_out = self.AutoScale(frame_out)
                if huong_number == 0:
                    frame_out = frame_out_man_hinh_number_5
                    # frame_out = self.AutoScale(frame_out)
            if man_hinh_number == 0:
                frame_out_man_hinh_number_0 = frame.copy()
                if frame.shape[0] / 720 < 1 or frame.shape[1] / 1080 < 1:
                    if frame.shape[0] / 720 >= frame.shape[1] / 1080:
                        scale_ratio = 720 / frame.shape[0]
                        width = int(frame.shape[1] * scale_ratio)
                        height = 720
                        dim = (width, height)
                        frame_out_man_hinh_number_0 = cv2.resize(frame, dim)
                    else:
                        scale_ratio = 1080 / frame.shape[1]
                        height = int(frame.shape[0] * scale_ratio)
                        width = 1080
                        dim = (width, height)
                        frame_out_man_hinh_number_0 = cv2.resize(frame, dim)
                if huong_number == 1:
                    frame_out = cv2.flip(frame_out_man_hinh_number_0, 1)
                    frame_out = self.AutoScale(frame_out)
                if huong_number == 2:
                    frame_out = cv2.rotate(frame_out_man_hinh_number_0, cv2.ROTATE_180)
                    frame_out = self.AutoScale(frame_out)
                if huong_number == 3:
                    frame_out = cv2.rotate(frame_out_man_hinh_number_0, cv2.ROTATE_90_COUNTERCLOCKWISE)
                    frame_out = self.AutoScale(frame_out)
                if huong_number == 4:
                    frame_out = cv2.rotate(frame_out_man_hinh_number_0, cv2.ROTATE_90_CLOCKWISE)
                    frame_out = self.AutoScale(frame_out)
                if huong_number == 0:
                    frame_out = frame_out_man_hinh_number_0
                    # frame_out = self.AutoScale(frame_out)
        else:
            frame_out = frame
            if huong_number == 1:
                frame_out = cv2.flip(frame, 1)
                frame_out = self.AutoScale(frame_out)
            if huong_number == 2:
                frame_out = cv2.rotate(frame, cv2.ROTATE_180)
                frame_out = self.AutoScale(frame_out)
            if huong_number == 3:
                frame_out = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
                frame_out = self.AutoScale(frame_out)
            if huong_number == 4:
                frame_out = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
                frame_out = self.AutoScale(frame_out)
            if huong_number == 0:
                frame_out = frame
                # frame_out = self.AutoScale(frame_out)
            """
            Chọn kiểu màn hình trong hay ngoài
            """
        return frame_out

    def ReturnFrameLan2(self, frame, chanel, brightness_adjuster, contrast_adjuster):
        """
        Chọn kênh màu và thay đổi độ sáng, độ tương phản
        """
        frame_out = []
        if chanel == 0:
            frame_out = frame
            frame_out = change_brightness(frame_out, brightness_adjuster)
            frame_out = change_brightness(frame_out, contrast_adjuster)
        if chanel == 1:
            frame_out = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return frame_out

    def ReturnFrameLan3(self, frame, duong_bao_show, nguong_adjuster):
        """
        Chọn hiện thị đường bao và thay đổi ngưỡng
        """
        frame_out = []

        if duong_bao_show == 1:
            frame_out = frame.copy()
            gray = cv2.cvtColor(frame_out, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (3, 3), 0)
            thresh = cv2.threshold(gray, nguong_adjuster, 255, cv2.THRESH_BINARY)[1]
            thresh = cv2.erode(thresh, None, iterations=2)
            thresh = cv2.dilate(thresh, None, iterations=2)
            # thres_adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            #                               cv2.THRESH_BINARY, 11, 2)
            # otsu_threshold, thresh_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
            # cnts = imutils.grab_contours(cnts)

            # try:
            #     if len(cnts) != 0:
            #         c = max(cnts, key=cv2.contourArea)
            #         for i in range(len(c)):
            #             cv2.drawContours(frame_out, [c], -1, (240, 0, 159), 2)
            # except:
            #     print('Non contour')

            if len(cnts) != 0:
                c = max(cnts, key=cv2.contourArea)
                cv2.drawContours(frame_out, [c], -1, (240, 0, 159), 2)

        if duong_bao_show == 0:
            frame_out = frame
        return frame, frame_out

    def AutoScale(self, frame):
        frame_auto_scale = frame.copy()
        if frame.shape[0] / 720 > 1 or frame.shape[1] / 1080 > 1:
            if frame.shape[0] / 720 >= frame.shape[1] / 1080:
                scale_ratio = 720 / frame.shape[0]
                width = int(frame.shape[1] * scale_ratio)
                height = 720
                dim = (width, height)
                frame_auto_scale = cv2.resize(frame, dim)
            else:
                scale_ratio = 1080 / frame.shape[1]
                height = int(frame.shape[0] * scale_ratio)
                width = 1080
                dim = (width, height)
                frame_auto_scale = cv2.resize(frame, dim)
        return frame_auto_scale

    def chupBT_clicked(self):
        if self.frame is not None:
            if self.mydir == None:
                self.mydir = self.myRootPath + '/' + time.strftime("%d-%m-%Y-%H-%M-%S")
                os.mkdir(self.mydir)
            self.anhMauLB.setPixmap(QPixmap(u"../handsample/" + str(self.index + 1) + ".jpg"))
            if self.index <= 14:
                self.mang_nguong.append(self.nguong_adjuster)
                # print(self.mang_nguong)
                self.myThread1 = threading.Thread(target=self.saveImage, args=(self.index,))
                self.myThread1.start()
                # self.myThread2 = threading.Thread(target=self.LayDiem, args=(self.index,))
                # self.myThread2.start()
                if self.index == 14:
                    self.index = 0
                    self.anhMauLB.setPixmap(QPixmap(u"../handsample/" + str(self.index + 1) + ".jpg"))
                    reply = QMessageBox.warning(self.centralwidget, 'Warning',
                                                "You must save all files?", QMessageBox.Yes | QMessageBox.No,
                                                QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        self.cur_dir = self.mydir
                        self.cur_mang_nguong = self.mang_nguong
                        # print(self.cur_mang_nguong)
                    # reset lại mang nguong va thu muc luu
                    self.mydir = self.myRootPath + '/' + time.strftime("%d-%m-%Y-%H-%M-%S")
                    self.mang_nguong = []
                    os.mkdir(self.mydir)
                    # print(self.cur_mang_nguong)
            self.index = self.index + 1

    # def XemKQBT_clicked(self):
    #     # print(self.cur_mang_nguong)
    #     # img1 = cv2.imread("{}/{}".format(self.cur_dir, 1) + ".png")  # ban tay ngua
    #     # # img1 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\1.jpg')  # ban tay ngua
    #     # img1 = imutils.resize(img1, height=800)
    #     # cv2.imshow('img', img1)
    #     # cv2.waitKey()
    #     print(self.cur_mang_nguong)
    #
    #     img1 = cv2.imread("{}/{}".format(self.cur_dir, 1) + ".png")  # ban tay ngua
    #     # img1 = imutils.resize(img1, height=800)
    #     # nguong_1 = self.cur_mang_nguong[0]
    #     nguong_1 = 65
    #     diem_tren_tay_phai_ngua, kq_img1 = NguaBanTayPhai(img1, nguong_1)
    #     # print('diem_tren_tay_phai_ngua')
    #     # print(diem_tren_tay_phai_ngua)
    #
    #     img2 = cv2.imread("{}/{}".format(self.cur_dir, 2) + ".png")  # ban tay ngua
    #     # img2 = imutils.resize(img2, height=800)
    #     # nguong_2 = self.cur_mang_nguong[1]
    #     nguong_2 = 65
    #     diem_tren_tay_phai_up, kq_img2 = UpBanTayPhai(img2, nguong_2)
    #
    #     anh_kq = kq_img1, kq_img2
    #     for i, kq in enumerate(anh_kq):
    #         cv2.imwrite('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\ViewResult\\kq_img{}.png'.format(i), kq)
    #
    # def XemKQBT_clicked_V1(self):
    #     print(self.cur_mang_nguong)
    #
    #     # img1 = cv2.imread("{}/{}".format(self.cur_dir, 1) + ".png")  # ban tay ngua
    #     img1 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\1.jpg')  # ban tay ngua
    #     img1 = imutils.resize(img1, height=800)
    #     # nguong_1 = self.cur_mang_nguong[0]
    #     nguong_1 = 65
    #     diem_tren_tay_phai_ngua, kq_img1 = NguaBanTayPhai(img1, nguong_1)
    #     # print('diem_tren_tay_phai_ngua')
    #     # print(diem_tren_tay_phai_ngua)
    #
    #     # set phan tram da xong
    #     self.progressBar.setValue(10)
    #
    #     # # img2 = cv2.imread("{}/{}".format(self.cur_dir, 2) + ".png")  # ban tay ngua
    #     img2 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\2.jpg')  # ban tay ngua
    #     img2 = imutils.resize(img2, height=800)
    #     # nguong_2 = self.cur_mang_nguong[1]
    #     nguong_2 = 65
    #     diem_tren_tay_phai_up, kq_img2 = UpBanTayPhai(img2, nguong_2)
    #     # print('diem_tren_tay_phai_up')
    #     # print(diem_tren_tay_phai_up)
    #
    #     # set phan tram da xong
    #     self.progressBar.setValue(20)
    #
    #     img3 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\3.jpg')  # ban tay ngua
    #     img3 = imutils.resize(img3, height=800)
    #     # nguong_2 = self.cur_mang_nguong[1]
    #     nguong_3 = 65
    #     diem_nam_tay_phai_1, kq_img3 = NamTayPhai1(img3, nguong_3)
    #     # print('diem_nam_tay_phai_1')
    #     # print(diem_nam_tay_phai_1)
    #
    #     #
    #     # set phan tram da xong
    #     self.progressBar.setValue(30)
    #
    #     img4 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\4.jpg')  # ban tay ngua
    #     img4 = imutils.resize(img4, height=800)
    #     # nguong_2 = self.cur_mang_nguong[1]
    #     nguong_4 = 65
    #     diem_nam_tay_phai_2, kq_img4 = NamTayPhai2(img4, nguong_4)
    #     # print('diem_nam_tay_phai_2')
    #     # print(diem_nam_tay_phai_2)
    #
    #     self.progressBar.setValue(40)
    #
    #     img5 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\5.jpg')  # ban tay ngua
    #     img5 = imutils.resize(img5, height=800)
    #     # nguong_2 = self.cur_mang_nguong[1]
    #     nguong_5 = 65
    #     diem_ngon_tro_phai, kq_img5 = NgonTroPhai(img5, nguong_5)
    #     # print('diem_ngon_tro_phai')
    #     # print(diem_ngon_tro_phai)
    #
    #     img6 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\6.jpg')  # ban tay ngua
    #     img6 = imutils.resize(img6, height=800)
    #     # nguong_2 = self.cur_mang_nguong[1]
    #     nguong_6 = 65
    #     diem_mu_tay_phai, kq_img6 = MuTayPhai(img6, nguong_6)
    #     print('diem_mu_tay_phai')
    #     print(diem_mu_tay_phai)
    #
    #     img7 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\main\\test\\2ngon4.jpg')
    #     img7 = imutils.resize(img7, height=800)
    #     # nguong_2 = self.cur_mang_nguong[1]
    #     # nguong_7 = 90
    #     nguong_7 = 90
    #     diem_hai_ngon_tay_phai, kq_img7 = HaiNgonTayPhai(img7, nguong_7)
    #     print('diem_hai_ngon_tay_phai')
    #     print(diem_hai_ngon_tay_phai)
    #
    #     self.progressBar.setValue(50)
    #
    #     # img1 = cv2.imread("{}/{}".format(self.mydir, 1) + ".png")  # ban tay ngua
    #     img8 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\8.jpg')  # ban tay ngua
    #     img8 = imutils.resize(img8, height=800)
    #     # nguong_1 = self.cur_mang_nguong[0]
    #     nguong_8 = 65
    #     diem_tren_tay_ngua_trai, kq_img8 = NguaBanTayPhai(img8, nguong_8)
    #     print('diem_tren_tay_ngua_trai')
    #     print(diem_tren_tay_ngua_trai)
    #     # set phan tram da xong
    #
    #     self.progressBar.setValue(60)
    #
    #     # # img2 = cv2.imread("{}/{}".format(self.mydir, 2) + ".png")  # ban tay ngua
    #     img9 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\9.jpg')  # ban tay ngua
    #     img9 = imutils.resize(img9, height=800)
    #     # nguong_2 = self.cur_mang_nguong[1]
    #     nguong_9 = 65
    #     diem_tren_tay_trai_up, kq_img9 = UpBanTayPhai(img9, nguong_9)
    #     print('diem_tren_tay_trai_up')
    #     print(diem_tren_tay_trai_up)
    #
    #     # set phan tram da xong
    #     self.progressBar.setValue(70)
    #
    #     img10 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\10.jpg')  # ban tay ngua
    #     img10 = imutils.resize(img10, height=800)
    #     # nguong_2 = self.cur_mang_nguong[1]
    #     nguong_10 = 65
    #     diem_nam_tay_trai_1, kq_img10 = NamTayPhai1(img10, nguong_10)
    #     print('diem_nam_tay_trai_1')
    #     print(diem_nam_tay_trai_1)
    #
    #     # set phan tram da xong
    #     self.progressBar.setValue(80)
    #
    #     img11 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\11.jpg')  # ban tay ngua
    #     img11 = imutils.resize(img11, height=800)
    #     # nguong_2 = self.cur_mang_nguong[1]
    #     nguong_11 = 65
    #     diem_nam_tay_trai_2, kq_img11 = NamTayPhai2(img11, nguong_11)
    #     print('diem_nam_tay_trai_2')
    #     print(diem_nam_tay_trai_2)
    #
    #     img12 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\12.jpg')  # ban tay ngua
    #     img12 = imutils.resize(img12, height=800)
    #     # nguong_2 = self.cur_mang_nguong[1]
    #     nguong_12 = 65
    #     diem_ngon_tro_trai, kq_img12 = NgonTroPhai(img12, nguong_12)
    #     print('diem_ngon_tro_trai')
    #     print(diem_ngon_tro_trai)
    #
    #     img13 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\13.jpg')  # ban tay ngua
    #     img13 = imutils.resize(img13, height=800)
    #     # nguong_2 = self.cur_mang_nguong[1]
    #     nguong_13 = 65
    #     diem_mu_tay_trai, kq_img13 = MuTayPhai(img13, nguong_13)
    #     print('diem_mu_tay_trai')
    #     print(diem_mu_tay_trai)
    #
    #     img14 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\main\\test\\2ngon3.jpg')
    #     img14 = imutils.resize(img14, height=800)
    #     # nguong_2 = self.cur_mang_nguong[1]
    #     # nguong_7 = 90
    #     nguong_14 = 90
    #     diem_hai_ngon_tay_trai, kq_img14 = HaiNgonTayPhai(img14, nguong_14)
    #     print('diem_hai_ngon_tay_trai')
    #     print(diem_hai_ngon_tay_trai)
    #
    #     # set phan tram da xong
    #     self.progressBar.setValue(90)
    #
    #     anh_kq = kq_img1, kq_img2, kq_img3, kq_img4, kq_img5, kq_img6, kq_img7, kq_img8, kq_img9, kq_img10, kq_img11, kq_img12, kq_img13, kq_img14
    #     for i, kq in enumerate(anh_kq):
    #         cv2.imwrite('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\result\\kq_img{}.png'.format(i), kq)
    #
    #     kt_1 = '{}x{}'.format(img1.shape[0], img1.shape[1])
    #     kt_2 = '{}x{}'.format(img2.shape[0], img2.shape[1])
    #     kt_3 = '{}x{}'.format(img3.shape[0], img3.shape[1])
    #     kt_4 = '{}x{}'.format(img4.shape[0], img4.shape[1])
    #     kt_5 = '{}x{}'.format(img5.shape[0], img5.shape[1])
    #     kt_6 = '{}x{}'.format(img6.shape[0], img6.shape[1])
    #     kt_7 = '{}x{}'.format(img7.shape[0], img7.shape[1])
    #
    #     self.data1 = {'Kích thước ảnh': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
    #                   'Tên điểm': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
    #                   'Vị trí': ['{}'.format(diem_tren_tay_phai_ngua[0]),
    #                              '{}'.format(diem_tren_tay_phai_ngua[1]),
    #                              '{}'.format(diem_tren_tay_phai_ngua[2]),
    #                              '{}'.format(diem_tren_tay_phai_ngua[3]),
    #                              '{}'.format(diem_tren_tay_phai_ngua[4]),
    #                              '{}'.format(diem_tren_tay_phai_ngua[5]),
    #                              '{}'.format(diem_tren_tay_phai_ngua[6]),
    #                              '{}'.format(diem_tren_tay_phai_ngua[7]),
    #                              '{}'.format(diem_tren_tay_phai_ngua[8]),
    #                              '{}'.format(diem_tren_tay_phai_ngua[9])],
    #                   'Kích thước ảnh ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
    #                   'Tên điểm ': ['11', '20', '21', '22', '23', '24', '25', '26', '27', '28'],
    #                   'Vị trí ': ['{}'.format(diem_tren_tay_phai_ngua[10]),
    #                               '{}'.format(diem_tren_tay_phai_ngua[11]),
    #                               '{}'.format(diem_tren_tay_phai_ngua[12]),
    #                               '{}'.format(diem_tren_tay_phai_ngua[13]),
    #                               '{}'.format(diem_tren_tay_phai_ngua[14]),
    #                               '{}'.format(diem_tren_tay_phai_ngua[15]),
    #                               '{}'.format(diem_tren_tay_phai_ngua[16]),
    #                               '{}'.format(diem_tren_tay_phai_ngua[17]),
    #                               '{}'.format(diem_tren_tay_phai_ngua[18]),
    #                               '{}'.format(diem_tren_tay_phai_ngua[19])],
    #                   'Kích thước ảnh  ': [kt_1, kt_1, kt_1, kt_2, kt_2, kt_2, kt_2, kt_2, kt_2, kt_2],
    #                   'Tên điểm  ': ['29', '36', '37', '15', '16', '17', '18', '19', '47', '48'],
    #                   'Vị trí  ': ['{}'.format(diem_tren_tay_phai_ngua[20]),
    #                                '{}'.format(diem_tren_tay_phai_ngua[21]),
    #                                '{}'.format(diem_tren_tay_phai_ngua[22]),
    #                                '{}'.format(diem_tren_tay_phai_up[0]),
    #                                '{}'.format(diem_tren_tay_phai_up[1]),
    #                                '{}'.format(diem_tren_tay_phai_up[2]),
    #                                '{}'.format(diem_tren_tay_phai_up[3]),
    #                                '{}'.format(diem_tren_tay_phai_up[4]),
    #                                '{}'.format(diem_tren_tay_phai_up[5]),
    #                                '{}'.format(diem_tren_tay_phai_up[6])],
    #                   'Kích thước ảnh   ': [kt_3, kt_3, kt_3, kt_3, kt_3, kt_3, kt_4, kt_4, kt_4, kt_4],
    #                   'Tên điểm   ': ['12', '13', '51', '52', '53', '54', '38', '39', '49', '50'],
    #                   'Vị trí   ': ['{}'.format(diem_nam_tay_phai_1[0]),
    #                                 '{}'.format(diem_nam_tay_phai_1[1]),
    #                                 '{}'.format(diem_nam_tay_phai_1[2]),
    #                                 '{}'.format(diem_nam_tay_phai_1[3]),
    #                                 '{}'.format(diem_nam_tay_phai_1[4]),
    #                                 '{}'.format(diem_nam_tay_phai_1[5]),
    #                                 '{}'.format(diem_nam_tay_phai_2[0]),
    #                                 '{}'.format(diem_nam_tay_phai_2[1]),
    #                                 '{}'.format(diem_nam_tay_phai_2[2]),
    #                                 '{}'.format(diem_nam_tay_phai_2[3])],
    #                   'Kích thước ảnh    ': [kt_5, kt_5, kt_6, kt_6, kt_6, kt_6, kt_6, kt_6, kt_7, kt_7],
    #                   'Tên điểm    ': ['45', '46', '30', '31', '32', '33', '34', '35', '41', '42'],
    #                   'Vị trí    ': ['{}'.format(diem_ngon_tro_phai[0]),
    #                                  '{}'.format(diem_ngon_tro_phai[1]),
    #                                  '{}'.format(diem_mu_tay_phai[0]),
    #                                  '{}'.format(diem_mu_tay_phai[1]),
    #                                  '{}'.format(diem_mu_tay_phai[2]),
    #                                  '{}'.format(diem_mu_tay_phai[3]),
    #                                  '{}'.format(diem_mu_tay_phai[4]),
    #                                  '{}'.format(diem_mu_tay_phai[5]),
    #                                  '{}'.format(diem_hai_ngon_tay_phai[0]),
    #                                  '{}'.format(diem_hai_ngon_tay_phai[1])],
    #                   'Kích thước ảnh     ': [kt_7, kt_7],
    #                   'Tên điểm     ': ['43', '44'],
    #                   'Vị trí     ': ['{}'.format(diem_hai_ngon_tay_phai[2]),
    #                                   '{}'.format(diem_hai_ngon_tay_phai[3])]
    #                   }
    #     self.data2 = {'Kích thước ảnh': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
    #                   'Tên điểm': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
    #                   'Vị trí': ['{}'.format(diem_tren_tay_ngua_trai[0]),
    #                              '{}'.format(diem_tren_tay_ngua_trai[1]),
    #                              '{}'.format(diem_tren_tay_ngua_trai[2]),
    #                              '{}'.format(diem_tren_tay_ngua_trai[3]),
    #                              '{}'.format(diem_tren_tay_ngua_trai[4]),
    #                              '{}'.format(diem_tren_tay_ngua_trai[5]),
    #                              '{}'.format(diem_tren_tay_ngua_trai[6]),
    #                              '{}'.format(diem_tren_tay_ngua_trai[7]),
    #                              '{}'.format(diem_tren_tay_ngua_trai[8]),
    #                              '{}'.format(diem_tren_tay_ngua_trai[9])],
    #                   'Kích thước ảnh ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
    #                   'Tên điểm ': ['11', '20', '21', '22', '23', '24', '25', '26', '27', '28'],
    #                   'Vị trí ': ['{}'.format(diem_tren_tay_ngua_trai[10]),
    #                               '{}'.format(diem_tren_tay_ngua_trai[11]),
    #                               '{}'.format(diem_tren_tay_ngua_trai[12]),
    #                               '{}'.format(diem_tren_tay_ngua_trai[13]),
    #                               '{}'.format(diem_tren_tay_ngua_trai[14]),
    #                               '{}'.format(diem_tren_tay_ngua_trai[15]),
    #                               '{}'.format(diem_tren_tay_ngua_trai[16]),
    #                               '{}'.format(diem_tren_tay_ngua_trai[17]),
    #                               '{}'.format(diem_tren_tay_ngua_trai[18]),
    #                               '{}'.format(diem_tren_tay_ngua_trai[19])],
    #                   'Kích thước ảnh  ': [kt_1, kt_1, kt_1, kt_2, kt_2, kt_2, kt_2, kt_2, kt_2, kt_2],
    #                   'Tên điểm  ': ['29', '36', '37', '15', '16', '17', '18', '19', '47', '48'],
    #                   'Vị trí  ': ['{}'.format(diem_tren_tay_ngua_trai[20]),
    #                                '{}'.format(diem_tren_tay_ngua_trai[21]),
    #                                '{}'.format(diem_tren_tay_ngua_trai[22]),
    #                                '{}'.format(diem_tren_tay_trai_up[0]),
    #                                '{}'.format(diem_tren_tay_trai_up[1]),
    #                                '{}'.format(diem_tren_tay_trai_up[2]),
    #                                '{}'.format(diem_tren_tay_trai_up[3]),
    #                                '{}'.format(diem_tren_tay_trai_up[4]),
    #                                '{}'.format(diem_tren_tay_trai_up[5]),
    #                                '{}'.format(diem_tren_tay_trai_up[6])],
    #                   'Kích thước ảnh   ': [kt_3, kt_3, kt_3, kt_3, kt_3, kt_3, kt_4, kt_4, kt_4, kt_4],
    #                   'Tên điểm   ': ['12', '13', '51', '52', '53', '54', '38', '39', '49', '50'],
    #                   'Vị trí   ': ['{}'.format(diem_nam_tay_trai_1[0]),
    #                                 '{}'.format(diem_nam_tay_trai_1[1]),
    #                                 '{}'.format(diem_nam_tay_trai_1[2]),
    #                                 '{}'.format(diem_nam_tay_trai_1[3]),
    #                                 '{}'.format(diem_nam_tay_trai_1[4]),
    #                                 '{}'.format(diem_nam_tay_trai_1[5]),
    #                                 '{}'.format(diem_nam_tay_trai_2[0]),
    #                                 '{}'.format(diem_nam_tay_trai_2[1]),
    #                                 '{}'.format(diem_nam_tay_trai_2[2]),
    #                                 '{}'.format(diem_nam_tay_trai_2[3])],
    #                   'Kích thước ảnh    ': [kt_5, kt_5, kt_6, kt_6, kt_6, kt_6, kt_6, kt_6, kt_7, kt_7],
    #                   'Tên điểm    ': ['45', '46', '30', '31', '32', '33', '34', '35', '41', '42'],
    #                   'Vị trí    ': ['{}'.format(diem_ngon_tro_trai[0]),
    #                                  '{}'.format(diem_ngon_tro_trai[1]),
    #                                  '{}'.format(diem_mu_tay_trai[0]),
    #                                  '{}'.format(diem_mu_tay_trai[1]),
    #                                  '{}'.format(diem_mu_tay_trai[2]),
    #                                  '{}'.format(diem_mu_tay_trai[3]),
    #                                  '{}'.format(diem_mu_tay_trai[4]),
    #                                  '{}'.format(diem_mu_tay_trai[5]),
    #                                  '{}'.format(diem_hai_ngon_tay_trai[0]),
    #                                  '{}'.format(diem_hai_ngon_tay_trai[1])],
    #                   'Kích thước ảnh     ': [kt_7, kt_7],
    #                   'Tên điểm     ': ['43', '44'],
    #                   'Vị trí     ': ['{}'.format(diem_hai_ngon_tay_trai[2]),
    #                                   '{}'.format(diem_hai_ngon_tay_trai[3])]
    #                   }
    #
    #     self.progressBar.setValue(90)
    #
    #     self.setData(self.bang_diem_tay_phai, self.data1)
    #     self.setData(self.bang_diem_tay_trai, self.data2)
    #
    #     self.bang_diem_tay_phai.resizeColumnsToContents()
    #     self.bang_diem_tay_phai.resizeRowsToContents()
    #     self.bang_diem_tay_trai.resizeColumnsToContents()
    #     self.bang_diem_tay_trai.resizeRowsToContents()
    #
    #     # set phan tram da xong
    #     self.progressBar.setValue(100)
    #     self.progressBar.setValue(0)

    def XemKQBT_clicked(self):
        print(self.cur_mang_nguong)
        # self.cur_mang_nguong = [28.0, 28.0, 28.0, 28.0, 22.0, 11.0, 11.0, 30.0, 30.0, 30.0, 15.0, 11.0, 11.0, 11.0]
        # self.cur_dir = "D:/HUST/LAB/DIR/27-05-2022-14-47-33"
        img1 = cv2.imread("{}/{}".format(self.cur_dir, 1) + ".png")  # ban tay ngua
        # img1 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\1.jpg')  # ban tay ngua
        # img1 = imutils.resize(img1, height=800)
        nguong_1 = int(self.cur_mang_nguong[0])
        print(nguong_1)
        # nguong_1 = 65
        diem_tren_tay_phai_ngua, kq_img1 = NguaBanTayPhai(img1, nguong_1)
        print('diem_tren_tay_phai_ngua')
        print(diem_tren_tay_phai_ngua)

        # set phan tram da xong
        self.progressBar.setValue(10)

        img2 = cv2.imread("{}/{}".format(self.cur_dir, 2) + ".png")  # ban tay ngua
        # img2 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\2.jpg')  # ban tay ngua
        # img2 = imutils.resize(img2, height=800)
        nguong_2 = int(self.cur_mang_nguong[1])
        # nguong_2 = 65
        diem_tren_tay_phai_up, kq_img2 = UpBanTayPhai(img2, nguong_2)
        print('diem_tren_tay_phai_up')
        print(diem_tren_tay_phai_up)

        # set phan tram da xong
        self.progressBar.setValue(20)

        img3 = cv2.imread("{}/{}".format(self.cur_dir, 3) + ".png")  # ban tay ngua
        # img3 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\3.jpg')  # ban tay ngua
        # img3 = imutils.resize(img3, height=800)
        nguong_3 = int(self.cur_mang_nguong[2])
        # nguong_3 = 65
        diem_nam_tay_phai_1, kq_img3 = NamTayPhai1(img3, nguong_3)
        print('diem_nam_tay_phai_1')
        print(diem_nam_tay_phai_1)

        #
        # set phan tram da xong
        self.progressBar.setValue(30)

        img4 = cv2.imread("{}/{}".format(self.cur_dir, 4) + ".png")  # ban tay ngua
        # img4 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\4.jpg')  # ban tay ngua
        # img4 = imutils.resize(img4, height=800)
        nguong_4 = int(self.cur_mang_nguong[3])
        # nguong_4 = 65
        diem_nam_tay_phai_2, kq_img4 = NamTayPhai2(img4, nguong_4)
        print('diem_nam_tay_phai_2')
        print(diem_nam_tay_phai_2)

        self.progressBar.setValue(40)

        img5 = cv2.imread("{}/{}".format(self.cur_dir, 5) + ".png")  # ban tay ngua
        # img5 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\5.jpg')  # ban tay ngua
        # img5 = imutils.resize(img5, height=800)
        nguong_5 = int(self.cur_mang_nguong[4])
        # nguong_5 = 65
        diem_ngon_tro_phai, kq_img5 = NgonTroPhai(img5, nguong_5)
        print('diem_ngon_tro_phai')
        print(diem_ngon_tro_phai)

        img6 = cv2.imread("{}/{}".format(self.cur_dir, 6) + ".png")  # ban tay ngua
        # img6 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\6.jpg')  # ban tay ngua
        # img6 = imutils.resize(img6, height=800)
        nguong_6 = int(self.cur_mang_nguong[5])
        # nguong_6 = 65
        diem_mu_tay_phai, kq_img6 = MuTayPhai(img6, nguong_6)
        print('diem_mu_tay_phai')
        print(diem_mu_tay_phai)

        img7 = cv2.imread("{}/{}".format(self.cur_dir, 7) + ".png")  # ban tay ngua
        # img7 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\main\\test\\2ngon4.jpg')
        # img7 = imutils.resize(img7, height=800)
        nguong_7 = int(self.cur_mang_nguong[6])
        # nguong_7 = 90
        diem_hai_ngon_tay_phai, kq_img7 = HaiNgonTayPhai(img7, nguong_7)
        print('diem_hai_ngon_tay_phai')
        print(diem_hai_ngon_tay_phai)

        self.progressBar.setValue(50)

        img8 = cv2.imread("{}/{}".format(self.cur_dir, 8) + ".png")  # ban tay ngua
        # img8 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\8.jpg')  # ban tay ngua
        # img8 = imutils.resize(img8, height=800)
        nguong_8 = int(self.cur_mang_nguong[7])
        # nguong_8 = 65
        diem_tren_tay_ngua_trai, kq_img8 = NguaBanTayPhai(img8, nguong_8)
        print('diem_tren_tay_ngua_trai')
        print(diem_tren_tay_ngua_trai)
        # set phan tram da xong

        self.progressBar.setValue(60)

        img9 = cv2.imread("{}/{}".format(self.cur_dir, 9) + ".png")  # ban tay ngua
        # img9 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\9.jpg')  # ban tay ngua
        # img9 = imutils.resize(img9, height=800)
        nguong_9 = int(self.cur_mang_nguong[8])
        # nguong_9 = 65
        diem_tren_tay_trai_up, kq_img9 = UpBanTayPhai(img9, nguong_9)
        print('diem_tren_tay_trai_up')
        print(diem_tren_tay_trai_up)

        # set phan tram da xong
        self.progressBar.setValue(70)

        img10 = cv2.imread("{}/{}".format(self.cur_dir, 10) + ".png")  # ban tay ngua
        # img10 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\10.jpg')  # ban tay ngua
        # img10 = imutils.resize(img10, height=800)
        nguong_10 = int(self.cur_mang_nguong[9])
        # nguong_10 = 65
        diem_nam_tay_trai_1, kq_img10 = NamTayPhai1(img10, nguong_10)
        print('diem_nam_tay_trai_1')
        print(diem_nam_tay_trai_1)

        # set phan tram da xong
        self.progressBar.setValue(80)

        img11 = cv2.imread("{}/{}".format(self.cur_dir, 11) + ".png")  # ban tay ngua
        # img11 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\11.jpg')  # ban tay ngua
        # img11 = imutils.resize(img11, height=800)
        nguong_11 = int(self.cur_mang_nguong[10])
        # nguong_11 = 65
        diem_nam_tay_trai_2, kq_img11 = NamTayPhai2(img11, nguong_11)
        print('diem_nam_tay_trai_2')
        print(diem_nam_tay_trai_2)

        img12 = cv2.imread("{}/{}".format(self.cur_dir, 12) + ".png")  # ban tay ngua
        # img12 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\12.jpg')  # ban tay ngua
        # img12 = imutils.resize(img12, height=800)
        nguong_12 = int(self.cur_mang_nguong[11])
        # nguong_12 = 65
        diem_ngon_tro_trai, kq_img12 = NgonTroPhai(img12, nguong_12)
        print('diem_ngon_tro_trai')
        print(diem_ngon_tro_trai)

        img13 = cv2.imread("{}/{}".format(self.cur_dir, 13) + ".png")  # ban tay ngua
        # img13 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\13.jpg')  # ban tay ngua
        # img13 = imutils.resize(img13, height=800)
        nguong_13 = int(self.cur_mang_nguong[12])
        # nguong_13 = 65
        diem_mu_tay_trai, kq_img13 = MuTayPhai(img13, nguong_13)
        print('diem_mu_tay_trai')
        print(diem_mu_tay_trai)

        img14 = cv2.imread("{}/{}".format(self.cur_dir, 14) + ".png")  # ban tay ngua
        # img14 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\main\\test\\2ngon3.jpg')
        # img14 = imutils.resize(img14, height=800)
        nguong_14 = int(self.cur_mang_nguong[13])
        # nguong_14 = 90
        diem_hai_ngon_tay_trai, kq_img14 = HaiNgonTayPhai(img14, nguong_14)
        print('diem_hai_ngon_tay_trai')
        print(diem_hai_ngon_tay_trai)

        # set phan tram da xong
        self.progressBar.setValue(90)

        anh_kq = kq_img1, kq_img2, kq_img3, kq_img4, kq_img5, kq_img6, kq_img7, kq_img8, kq_img9, kq_img10, kq_img11, kq_img12, kq_img13, kq_img14
        for i, kq in enumerate(anh_kq):
            cv2.imwrite('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\result\\kq_img{}.png'.format(i), kq)

        kt_1 = '{}x{}'.format(img1.shape[0], img1.shape[1])
        kt_2 = '{}x{}'.format(img2.shape[0], img2.shape[1])
        kt_3 = '{}x{}'.format(img3.shape[0], img3.shape[1])
        kt_4 = '{}x{}'.format(img4.shape[0], img4.shape[1])
        kt_5 = '{}x{}'.format(img5.shape[0], img5.shape[1])
        kt_6 = '{}x{}'.format(img6.shape[0], img6.shape[1])
        kt_7 = '{}x{}'.format(img7.shape[0], img7.shape[1])

        self.data1 = {'Kích thước ảnh': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên điểm': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
                      'Vị trí': ['{}'.format(diem_tren_tay_phai_ngua[0]),
                                 '{}'.format(diem_tren_tay_phai_ngua[1]),
                                 '{}'.format(diem_tren_tay_phai_ngua[2]),
                                 '{}'.format(diem_tren_tay_phai_ngua[3]),
                                 '{}'.format(diem_tren_tay_phai_ngua[4]),
                                 '{}'.format(diem_tren_tay_phai_ngua[5]),
                                 '{}'.format(diem_tren_tay_phai_ngua[6]),
                                 '{}'.format(diem_tren_tay_phai_ngua[7]),
                                 '{}'.format(diem_tren_tay_phai_ngua[8]),
                                 '{}'.format(diem_tren_tay_phai_ngua[9])],
                      'Kích thước ảnh ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên điểm ': ['11', '20', '21', '22', '23', '24', '25', '26', '27', '28'],
                      'Vị trí ': ['{}'.format(diem_tren_tay_phai_ngua[10]),
                                  '{}'.format(diem_tren_tay_phai_ngua[11]),
                                  '{}'.format(diem_tren_tay_phai_ngua[12]),
                                  '{}'.format(diem_tren_tay_phai_ngua[13]),
                                  '{}'.format(diem_tren_tay_phai_ngua[14]),
                                  '{}'.format(diem_tren_tay_phai_ngua[15]),
                                  '{}'.format(diem_tren_tay_phai_ngua[16]),
                                  '{}'.format(diem_tren_tay_phai_ngua[17]),
                                  '{}'.format(diem_tren_tay_phai_ngua[18]),
                                  '{}'.format(diem_tren_tay_phai_ngua[19])],
                      'Kích thước ảnh  ': [kt_1, kt_1, kt_1, kt_2, kt_2, kt_2, kt_2, kt_2, kt_2, kt_2],
                      'Tên điểm  ': ['29', '36', '37', '15', '16', '17', '18', '19', '47', '48'],
                      'Vị trí  ': ['{}'.format(diem_tren_tay_phai_ngua[20]),
                                   '{}'.format(diem_tren_tay_phai_ngua[21]),
                                   '{}'.format(diem_tren_tay_phai_ngua[22]),
                                   '{}'.format(diem_tren_tay_phai_up[0]),
                                   '{}'.format(diem_tren_tay_phai_up[1]),
                                   '{}'.format(diem_tren_tay_phai_up[2]),
                                   '{}'.format(diem_tren_tay_phai_up[3]),
                                   '{}'.format(diem_tren_tay_phai_up[4]),
                                   '{}'.format(diem_tren_tay_phai_up[5]),
                                   '{}'.format(diem_tren_tay_phai_up[6])],
                      'Kích thước ảnh   ': [kt_3, kt_3, kt_3, kt_3, kt_3, kt_3, kt_4, kt_4, kt_4, kt_4],
                      'Tên điểm   ': ['12', '13', '51', '52', '53', '54', '38', '39', '49', '50'],
                      'Vị trí   ': ['{}'.format(diem_nam_tay_phai_1[0]),
                                    '{}'.format(diem_nam_tay_phai_1[1]),
                                    '{}'.format(diem_nam_tay_phai_1[2]),
                                    '{}'.format(diem_nam_tay_phai_1[3]),
                                    '{}'.format(diem_nam_tay_phai_1[4]),
                                    '{}'.format(diem_nam_tay_phai_1[5]),
                                    '{}'.format(diem_nam_tay_phai_2[0]),
                                    '{}'.format(diem_nam_tay_phai_2[1]),
                                    '{}'.format(diem_nam_tay_phai_2[2]),
                                    '{}'.format(diem_nam_tay_phai_2[3])],
                      'Kích thước ảnh    ': [kt_5, kt_5, kt_6, kt_6, kt_6, kt_6, kt_6, kt_6, kt_7, kt_7],
                      'Tên điểm    ': ['45', '46', '30', '31', '32', '33', '34', '35', '41', '42'],
                      'Vị trí    ': ['{}'.format(diem_ngon_tro_phai[0]),
                                     '{}'.format(diem_ngon_tro_phai[1]),
                                     '{}'.format(diem_mu_tay_phai[0]),
                                     '{}'.format(diem_mu_tay_phai[1]),
                                     '{}'.format(diem_mu_tay_phai[2]),
                                     '{}'.format(diem_mu_tay_phai[3]),
                                     '{}'.format(diem_mu_tay_phai[4]),
                                     '{}'.format(diem_mu_tay_phai[5]),
                                     '{}'.format(diem_hai_ngon_tay_phai[0]),
                                     '{}'.format(diem_hai_ngon_tay_phai[1])],
                      'Kích thước ảnh     ': [kt_7, kt_7],
                      'Tên điểm     ': ['43', '44'],
                      'Vị trí     ': ['{}'.format(diem_hai_ngon_tay_phai[2]),
                                      '{}'.format(diem_hai_ngon_tay_phai[3])]
                      }
        self.data2 = {'Kích thước ảnh': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên điểm': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
                      'Vị trí': ['{}'.format(diem_tren_tay_ngua_trai[0]),
                                 '{}'.format(diem_tren_tay_ngua_trai[1]),
                                 '{}'.format(diem_tren_tay_ngua_trai[2]),
                                 '{}'.format(diem_tren_tay_ngua_trai[3]),
                                 '{}'.format(diem_tren_tay_ngua_trai[4]),
                                 '{}'.format(diem_tren_tay_ngua_trai[5]),
                                 '{}'.format(diem_tren_tay_ngua_trai[6]),
                                 '{}'.format(diem_tren_tay_ngua_trai[7]),
                                 '{}'.format(diem_tren_tay_ngua_trai[8]),
                                 '{}'.format(diem_tren_tay_ngua_trai[9])],
                      'Kích thước ảnh ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên điểm ': ['11', '20', '21', '22', '23', '24', '25', '26', '27', '28'],
                      'Vị trí ': ['{}'.format(diem_tren_tay_ngua_trai[10]),
                                  '{}'.format(diem_tren_tay_ngua_trai[11]),
                                  '{}'.format(diem_tren_tay_ngua_trai[12]),
                                  '{}'.format(diem_tren_tay_ngua_trai[13]),
                                  '{}'.format(diem_tren_tay_ngua_trai[14]),
                                  '{}'.format(diem_tren_tay_ngua_trai[15]),
                                  '{}'.format(diem_tren_tay_ngua_trai[16]),
                                  '{}'.format(diem_tren_tay_ngua_trai[17]),
                                  '{}'.format(diem_tren_tay_ngua_trai[18]),
                                  '{}'.format(diem_tren_tay_ngua_trai[19])],
                      'Kích thước ảnh  ': [kt_1, kt_1, kt_1, kt_2, kt_2, kt_2, kt_2, kt_2, kt_2, kt_2],
                      'Tên điểm  ': ['29', '36', '37', '15', '16', '17', '18', '19', '47', '48'],
                      'Vị trí  ': ['{}'.format(diem_tren_tay_ngua_trai[20]),
                                   '{}'.format(diem_tren_tay_ngua_trai[21]),
                                   '{}'.format(diem_tren_tay_ngua_trai[22]),
                                   '{}'.format(diem_tren_tay_trai_up[0]),
                                   '{}'.format(diem_tren_tay_trai_up[1]),
                                   '{}'.format(diem_tren_tay_trai_up[2]),
                                   '{}'.format(diem_tren_tay_trai_up[3]),
                                   '{}'.format(diem_tren_tay_trai_up[4]),
                                   '{}'.format(diem_tren_tay_trai_up[5]),
                                   '{}'.format(diem_tren_tay_trai_up[6])],
                      'Kích thước ảnh   ': [kt_3, kt_3, kt_3, kt_3, kt_3, kt_3, kt_4, kt_4, kt_4, kt_4],
                      'Tên điểm   ': ['12', '13', '51', '52', '53', '54', '38', '39', '49', '50'],
                      'Vị trí   ': ['{}'.format(diem_nam_tay_trai_1[0]),
                                    '{}'.format(diem_nam_tay_trai_1[1]),
                                    '{}'.format(diem_nam_tay_trai_1[2]),
                                    '{}'.format(diem_nam_tay_trai_1[3]),
                                    '{}'.format(diem_nam_tay_trai_1[4]),
                                    '{}'.format(diem_nam_tay_trai_1[5]),
                                    '{}'.format(diem_nam_tay_trai_2[0]),
                                    '{}'.format(diem_nam_tay_trai_2[1]),
                                    '{}'.format(diem_nam_tay_trai_2[2]),
                                    '{}'.format(diem_nam_tay_trai_2[3])],
                      'Kích thước ảnh    ': [kt_5, kt_5, kt_6, kt_6, kt_6, kt_6, kt_6, kt_6, kt_7, kt_7],
                      'Tên điểm    ': ['45', '46', '30', '31', '32', '33', '34', '35', '41', '42'],
                      'Vị trí    ': ['{}'.format(diem_ngon_tro_trai[0]),
                                     '{}'.format(diem_ngon_tro_trai[1]),
                                     '{}'.format(diem_mu_tay_trai[0]),
                                     '{}'.format(diem_mu_tay_trai[1]),
                                     '{}'.format(diem_mu_tay_trai[2]),
                                     '{}'.format(diem_mu_tay_trai[3]),
                                     '{}'.format(diem_mu_tay_trai[4]),
                                     '{}'.format(diem_mu_tay_trai[5]),
                                     '{}'.format(diem_hai_ngon_tay_trai[0]),
                                     '{}'.format(diem_hai_ngon_tay_trai[1])],
                      'Kích thước ảnh     ': [kt_7, kt_7],
                      'Tên điểm     ': ['43', '44'],
                      'Vị trí     ': ['{}'.format(diem_hai_ngon_tay_trai[2]),
                                      '{}'.format(diem_hai_ngon_tay_trai[3])]
                      }

        self.progressBar.setValue(90)

        self.setData(self.bang_diem_tay_phai, self.data1)
        self.setData(self.bang_diem_tay_trai, self.data2)

        self.bang_diem_tay_phai.resizeColumnsToContents()
        self.bang_diem_tay_phai.resizeRowsToContents()
        self.bang_diem_tay_trai.resizeColumnsToContents()
        self.bang_diem_tay_trai.resizeRowsToContents()

        # set phan tram da xong
        self.progressBar.setValue(100)
        self.progressBar.setValue(0)

    def setData(self, bang_diem, data):
        # horHeaders = []
        # for n, key in enumerate(sorted(data.keys())):
        #     horHeaders.append(key)
        #     for m, item in enumerate(data[key]):
        #         newitem = QTableWidgetItem(item)
        #         self.bang_diem.setItem(m, n, newitem)
        #
        # self.bang_diem.setHorizontalHeaderLabels(horHeaders)
        horHeaders = []
        for n, key in enumerate(data.keys()):
            horHeaders.append(key)
            for m, item in enumerate(data[key]):
                newitem = QTableWidgetItem(item)
                bang_diem.setItem(m, n, newitem)
        bang_diem.setHorizontalHeaderLabels(horHeaders)

    def countFile(self, dir_path):
        count = 0
        # Iterate directory
        for path in os.listdir(dir_path):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1
        print('File count:', count)
        return count

    def saveImage(self, index):
        cv2.imwrite("{}/{}".format(self.mydir, index) + ".png", self.frame)

    # def LayDiem(self, index):
    #     # img0 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\main\\test\\bantayngua.png')  # ban tay ngua
    #     # img0 = imutils.resize(img0, height=800)
    #     # diem_tren_tay_ngua = NguaBanTayPhai(img0, nguong)
    #
    #     img0 = cv2.imread("{}/{}".format(self.mydir, index) + ".png")  # ban tay ngua
    #     cv2.imshow('Anh', img0)
    #     cv2.waitKey()

    def CameraRun(self):
        while self.cameraLogic != -1:
            print('cameraLogic:' + str(self.cameraLogic))
            # self.cap = cv2.VideoCapture(self.cameraLogic, cv2.CAP_DSHOW)
            # self.cap = cv2.VideoCapture(self.cameraLogic, cv2.CAP_MSMF)
            self.cap = cv2.VideoCapture(self.cameraLogic)
            # self.cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)
            # Using cv2.CAP_DSHOW removes the warning, but slows down my frame rate from 30fps to 7fps, on Windows
            # self.cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)  # turn the autofocus off
            # self.cap.set(cv2.CV_CAP_PROP_SETTINGS, 11)
            if not self.cap.isOpened():
                QMessageBox.warning(self, "Warning", "Camera is not connected")
                break
            while self.cap.isOpened():
                # Capture the video frame
                # by frame
                ret, self.frame = self.cap.read()
                if not ret:
                    print("Can't receive frame (stream end?). Exiting ...")
                    break
                self.frame = self.ReturnFrameLan1(self.frame, screen_show=self.screen_show,
                                                  huong_number=self.huong_number,
                                                  man_hinh_number=self.man_hinh_number)
                self.frame = self.ReturnFrameLan2(self.frame, chanel=self.chanel,
                                                  brightness_adjuster=self.brightness_adjuster,
                                                  contrast_adjuster=self.contrast_adjuster)
                self.frame, self.frame_out = self.ReturnFrameLan3(self.frame, duong_bao_show=self.duong_bao_show,
                                                                  nguong_adjuster=self.nguong_adjuster)
                if self.screen_show == 0:
                    self.cap_pix = convert_nparray_to_QPixmap(self.frame_out)
                    self.cameraLB.setPixmap(self.cap_pix)
                else:
                    self.frame_out = imutils.resize(self.frame_out, height=960)
                    cv2.imshow('Video', self.frame_out)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.cap.release()
                    cv2.destroyAllWindows()
                    break
        self.cameraLB.clear()
        self.cap.release()
        cv2.destroyAllWindows()

    def CameraRun1(self):
        while self.cameraLogic != -1:
            print('cameraLogic:' + str(self.cameraLogic))
            # self.cap = cv2.VideoCapture(self.cameraLogic, cv2.CAP_DSHOW)
            # self.cap = cv2.VideoCapture(self.cameraLogic, cv2.CAP_MSMF)
            self.cap = cv2.VideoCapture(self.cameraLogic)
            # self.cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)
            # Using cv2.CAP_DSHOW removes the warning, but slows down my frame rate from 30fps to 7fps, on Windows
            if not self.cap.isOpened():
                QMessageBox.warning(self, "Warning", "Camera is not connected")
                break
            while self.cap.isOpened():
                # Capture the video frame
                # by frame
                ret, self.frame = self.cap.read()
                if not ret:
                    print("Can't receive frame (stream end?). Exiting ...")
                    break
                self.frame = self.ReturnFrameLan1(self.frame, screen_show=self.screen_show,
                                                  huong_number=self.huong_number,
                                                  man_hinh_number=self.man_hinh_number)
                self.frame = self.ReturnFrameLan2(self.frame, chanel=self.chanel,
                                                  brightness_adjuster=self.brightness_adjuster,
                                                  contrast_adjuster=self.contrast_adjuster)
                self.frame, self.frame_out = self.ReturnFrameLan3(self.frame, duong_bao_show=self.duong_bao_show,
                                                                  nguong_adjuster=self.nguong_adjuster)
                if self.screen_show == 0:
                    self.cap_pix = convert_nparray_to_QPixmap(self.frame_out)
                    self.cameraLB.setPixmap(self.cap_pix)
                else:
                    self.frame_out = imutils.resize(self.frame_out, height=960)
                    cv2.imshow('Video', self.frame_out)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.cap.release()
                    cv2.destroyAllWindows()
                    break
        self.cameraLB.clear()
        self.cap.release()
        cv2.destroyAllWindows()

    def TestCameraRun(self):
        self.cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
        if not self.cap.isOpened():
            print("Cannot open camera")
            exit()
        while True:
            # Capture frame-by-frame
            ret, self.frame = self.cap.read()
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            # Điều chỉnh đầu ra của frame
            frame_copy = self.frame.copy()
            # self.frame_out = []

            # Chọn kích thước và hướng của frame

            if self.screen_show == 0:
                if self.man_hinh_number == 1:
                    dim = (1080, 720)
                    frame_out_man_hinh_number_1 = cv2.resize(frame_copy, dim)
                    if self.huong_number == 1:
                        self.frame_out = cv2.flip(frame_out_man_hinh_number_1, 1)
                        self.frame_out = self.AutoScale(self.frame_out)
                    if self.huong_number == 2:
                        self.frame_out = cv2.rotate(frame_out_man_hinh_number_1, cv2.ROTATE_180)
                        self.frame_out = self.AutoScale(self.frame_out)
                    if self.huong_number == 3:
                        self.frame_out = cv2.rotate(frame_out_man_hinh_number_1, cv2.ROTATE_90_COUNTERCLOCKWISE)
                        self.frame_out = self.AutoScale(self.frame_out)
                    if self.huong_number == 4:
                        self.frame_out = cv2.rotate(frame_out_man_hinh_number_1, cv2.ROTATE_90_CLOCKWISE)
                        self.frame_out = self.AutoScale(self.frame_out)
                    if self.huong_number == 0:
                        self.frame_out = frame_out_man_hinh_number_1
                        # frame_out = self.AutoScale(frame_out)
                if self.man_hinh_number == 2:
                    dim = (960, 540)
                    frame_out_man_hinh_number_2 = cv2.resize(frame_copy, dim)
                    if self.huong_number == 1:
                        self.frame_out = cv2.flip(frame_out_man_hinh_number_2, 1)
                        self.frame_out = self.AutoScale(self.frame_out)
                    if self.huong_number == 2:
                        self.frame_out = cv2.rotate(frame_out_man_hinh_number_2, cv2.ROTATE_180)
                        self.frame_out = self.AutoScale(self.frame_out)
                    if self.huong_number == 3:
                        self.frame_out = cv2.rotate(frame_out_man_hinh_number_2, cv2.ROTATE_90_COUNTERCLOCKWISE)
                        self.frame_out = self.AutoScale(self.frame_out)
                    if self.huong_number == 4:
                        self.frame_out = cv2.rotate(frame_out_man_hinh_number_2, cv2.ROTATE_90_CLOCKWISE)
                        self.frame_out = self.AutoScale(self.frame_out)
                    if self.huong_number == 0:
                        self.frame_out = frame_out_man_hinh_number_2
                        # frame_out = self.AutoScale(frame_out)
                if self.man_hinh_number == 3:
                    dim = (640, 360)
                    frame_out_man_hinh_number_3 = cv2.resize(frame_copy, dim)
                    if self.huong_number == 1:
                        self.frame_out = cv2.flip(frame_out_man_hinh_number_3, 1)
                        self.frame_out = self.AutoScale(self.frame_out)
                    if self.huong_number == 2:
                        self.frame_out = cv2.rotate(frame_out_man_hinh_number_3, cv2.ROTATE_180)
                        self.frame_out = self.AutoScale(self.frame_out)
                    if self.huong_number == 3:
                        self.frame_out = cv2.rotate(frame_out_man_hinh_number_3, cv2.ROTATE_90_COUNTERCLOCKWISE)
                        self.frame_out = self.AutoScale(self.frame_out)
                    if self.huong_number == 4:
                        self.frame_out = cv2.rotate(frame_out_man_hinh_number_3, cv2.ROTATE_90_CLOCKWISE)
                        self.frame_out = self.AutoScale(self.frame_out)
                    if self.huong_number == 0:
                        self.frame_out = frame_out_man_hinh_number_3
                        # frame_out = self.AutoScale(frame_out)
                if self.man_hinh_number == 4:
                    dim = (960, 720)
                    frame_out_man_hinh_number_4 = cv2.resize(frame_copy, dim)
                    if self.huong_number == 1:
                        self.frame_out = cv2.flip(frame_out_man_hinh_number_4, 1)
                        self.frame_out = self.AutoScale(self.frame_out)
                    if self.huong_number == 2:
                        self.frame_out = cv2.rotate(frame_out_man_hinh_number_4, cv2.ROTATE_180)
                        self.frame_out = self.AutoScale(self.frame_out)
                    if self.huong_number == 3:
                        self.frame_out = cv2.rotate(frame_out_man_hinh_number_4, cv2.ROTATE_90_COUNTERCLOCKWISE)
                        self.frame_out = self.AutoScale(self.frame_out)
                    if self.huong_number == 4:
                        self.frame_out = cv2.rotate(frame_out_man_hinh_number_4, cv2.ROTATE_90_CLOCKWISE)
                        self.frame_out = self.AutoScale(self.frame_out)
                    if self.huong_number == 0:
                        self.frame_out = frame_out_man_hinh_number_4
                        # frame_out = self.AutoScale(frame_out)
                if self.man_hinh_number == 5:
                    dim = (640, 480)
                    frame_out_man_hinh_number_5 = cv2.resize(frame_copy, dim)
                    if self.huong_number == 1:
                        self.frame_out = cv2.flip(frame_out_man_hinh_number_5, 1)
                        self.frame_out = self.AutoScale(self.frame_out)
                    if self.huong_number == 2:
                        self.frame_out = cv2.rotate(frame_out_man_hinh_number_5, cv2.ROTATE_180)
                        self.frame_out = self.AutoScale(self.frame_out)
                    if self.huong_number == 3:
                        self.frame_out = cv2.rotate(frame_out_man_hinh_number_5, cv2.ROTATE_90_COUNTERCLOCKWISE)
                        self.frame_out = self.AutoScale(self.frame_out)
                    if self.huong_number == 4:
                        self.frame_out = cv2.rotate(frame_out_man_hinh_number_5, cv2.ROTATE_90_CLOCKWISE)
                        self.frame_out = self.AutoScale(self.frame_out)
                    if self.huong_number == 0:
                        self.frame_out = frame_out_man_hinh_number_5
                        # frame_out = self.AutoScale(frame_out)
                if self.man_hinh_number == 0:
                    frame_out_man_hinh_number_0 = self.frame.copy()
                    if self.frame.shape[0] / 720 < 1 or self.frame.shape[1] / 1080 < 1:
                        if self.frame.shape[0] / 720 >= self.frame.shape[1] / 1080:
                            scale_ratio = 720 / self.frame.shape[0]
                            width = int(self.frame.shape[1] * scale_ratio)
                            height = 720
                            dim = (width, height)
                            frame_out_man_hinh_number_0 = cv2.resize(self.frame, dim)
                        else:
                            scale_ratio = 1080 / self.frame.shape[1]
                            height = int(self.frame.shape[0] * scale_ratio)
                            width = 1080
                            dim = (width, height)
                            frame_out_man_hinh_number_0 = cv2.resize(self.frame, dim)
                    if self.huong_number == 1:
                        self.frame_out = cv2.flip(frame_out_man_hinh_number_0, 1)
                        self.frame_out = self.AutoScale(self.frame_out)
                    if self.huong_number == 2:
                        self.frame_out = cv2.rotate(frame_out_man_hinh_number_0, cv2.ROTATE_180)
                        self.frame_out = self.AutoScale(self.frame_out)
                    if self.huong_number == 3:
                        self.frame_out = cv2.rotate(frame_out_man_hinh_number_0, cv2.ROTATE_90_COUNTERCLOCKWISE)
                        self.frame_out = self.AutoScale(self.frame_out)
                    if self.huong_number == 4:
                        self.frame_out = cv2.rotate(frame_out_man_hinh_number_0, cv2.ROTATE_90_CLOCKWISE)
                        self.frame_out = self.AutoScale(self.frame_out)
                    if self.huong_number == 0:
                        self.frame_out = frame_out_man_hinh_number_0
                        # frame_out = self.AutoScale(frame_out)
            # else:
            #     frame_out = self.frame
            #     if self.huong_number == 1:
            #         self.frame_out = cv2.flip(self.frame, 1)
            #         self.frame_out = self.AutoScale(self.frame_out)
            #     if self.huong_number == 2:
            #         self.frame_out = cv2.rotate(self.frame, cv2.ROTATE_180)
            #         self.frame_out = self.AutoScale(self.frame_out)
            #     if self.huong_number == 3:
            #         self.frame_out = cv2.rotate(self.frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
            #         self.frame_out = self.AutoScale(self.frame_out)
            #     if self.huong_number == 4:
            #         self.frame_out = cv2.rotate(self.frame, cv2.ROTATE_90_CLOCKWISE)
            #         self.frame_out = self.AutoScale(self.frame_out)
            #     if self.huong_number == 0:
            #         self.frame_out = self.frame
            #         # frame_out = self.AutoScale(frame_out)
            #     """
            #     Chọn kiểu màn hình trong hay ngoài
            #     """
            # self.frame = self.ReturnFrameLan2(self.frame, chanel=self.chanel,
            #                                   brightness_adjuster=self.brightness_adjuster,
            #                                   contrast_adjuster=self.contrast_adjuster)
            # self.frame, self.frame_out = self.ReturnFrameLan3(self.frame, duong_bao_show=self.duong_bao_show,
            #                                                   nguong_adjuster=self.nguong_adjuster)
            print(self.frame_out.shape)

            if self.screen_show == 0:
                self.cap_pix = convert_nparray_to_QPixmap(self.frame_out)
                self.cameraLB.setPixmap(self.cap_pix)
            else:
                self.frame_out = imutils.resize(self.frame_out, height=960)
                cv2.imshow('Video', self.frame_out)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.cap.release()
                cv2.destroyAllWindows()
                break
            # # Our operations on the frame come here
            # gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            # # Display the resulting frame
            # cv2.imshow('frame', gray)
            # if cv2.waitKey(1) == ord('q'):
            #     break
        # When everything done, release the capture
        self.cap.release()
        cv2.destroyAllWindows()

    def closeEvent(self, event):
        # close with X button
        reply = QMessageBox.question(self.centralwidget, 'Question',
                                     "Are you sure to quit this Window?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.cameraLB.clear()
            self.cap.release()
            cv2.destroyAllWindows()
            # QCoreApplication.instance().quit()
            # QCoreApplication.quit()
            # print('close')
            sys.exit()
            # event.accept()

        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyle('Windows')
    # setStyle ['Breeze', 'Oxygen', 'QtCurve', 'Windows', 'Fusion']
    ui = IntroductionWindow()
    ui.show()
    sys.exit(app.exec_())
