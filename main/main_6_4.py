# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designermOVtlu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import pickle

import sys
import os

import pandas as pd
import openpyxl
import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Hand.function.TongHop import *
from Hand.gui.IntroductionUI import Ui_IntroductionWindow
from Hand.gui.CaptureUI import Ui_CaptureWindow
from Hand.gui.CalibCameraUI import Ui_CalibCameraWindow
from Hand.function.Calib import *


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

        self.calibCameraWindow = CalibCameraWindow()
        self.calibCameraWindow.setupUi(self.calibCameraWindow)

        self.thoatBT.clicked.connect(self.thoatBT_clicked)
        self.dangNhapBT.clicked.connect(self.dangNhapBT_clicked)

        # ===================> START CalibCameraWindow <========================#

        ################### 2.1 chonCamera action ######################
        self.calibCameraWindow.chonCamCB.currentTextChanged.connect(self.calibCameraWindow.chonCamCB_changed)
        ################### 2.1 chonKenhCB action ######################

        ################### 2.2 chonKenhCB action ######################
        self.calibCameraWindow.chonKenhCB.currentTextChanged.connect(self.calibCameraWindow.chonKenhCB_changed)
        ################### 2.2 chonKenhCB action ######################

        ################### 2.3 chon screen action ######################
        self.calibCameraWindow.smallScreenRB.toggled.connect(self.calibCameraWindow.smallScreenRB_toggled)
        self.calibCameraWindow.orginalScreenRB.toggled.connect(self.calibCameraWindow.fullScreenRB_toggled)
        ################### 2.3 chon screen action ######################

        ################### 2.4 thay doi do sang action ##################
        self.calibCameraWindow.BrightnessSlider.valueChanged[int].connect(
            self.calibCameraWindow.BrightnessSlider_valueChanged)
        self.calibCameraWindow.doSangDSB.valueChanged.connect(self.calibCameraWindow.doSangDSB_valueChanged)
        ################### 2.4 end thay doi do sang action ##############

        ################### 2.5 thay doi do tuong phan action #############
        self.calibCameraWindow.ContrastSlider.valueChanged[int].connect(
            self.calibCameraWindow.ContrastSlider_valueChanged)
        self.calibCameraWindow.doTuongPhanDSB.valueChanged.connect(self.calibCameraWindow.doTuongPhanDSB_valueChanged)
        ################### 2.5 end thay doi do tuong phan action ##########

        ################### 2.6 thay doi nguong action #############
        self.calibCameraWindow.FocusSlider.valueChanged[int].connect(self.calibCameraWindow.FocusSlider_valueChanged)
        self.calibCameraWindow.focusDSB.valueChanged.connect(self.calibCameraWindow.focusDSB_valueChanged)
        ################### 2.6 end thay doi nguong action ##########

        ################### 2.9 chon kich thuoc khung hinh ######################
        self.calibCameraWindow.choManHinhCB.currentTextChanged.connect(self.calibCameraWindow.choManHinhCB_changed)
        ################### 2.9 end chon kich thuoc khung hinh ######################

        ################### 2.10 chon dieu chinh khung hinh ######################
        self.calibCameraWindow.chonDieuHuongCB.currentTextChanged.connect(
            self.calibCameraWindow.chonDieuHuongCB_changed)
        ################### 2.10 end chon dieu chinh khung hinh ######################

        # Button
        ################### 2.12 chup button ######################
        self.calibCameraWindow.chupBT.clicked.connect(self.calibCameraWindow.chupBT_clicked)

        ################### 2.11 chon dieu chinh ô bàn cờ ######################
        self.calibCameraWindow.soONgangSB.valueChanged.connect(self.calibCameraWindow.soONgangSB_changed)
        self.calibCameraWindow.soODocSB.valueChanged.connect(self.calibCameraWindow.soODocSB_changed)
        self.calibCameraWindow.kichThuocOSB.valueChanged.connect(self.calibCameraWindow.kichThuocOSB_changed)

        ################### 2.11 end chon dieu chinh khung hinh ######################
        ################### 2.12 end chup button ######################

        self.calibCameraWindow.nextPage.clicked.connect(self.calibCameraWindow.nextPage_clicked)
        self.calibCameraWindow.calibBT.clicked.connect(self.calibCameraWindow.calibBT_clicked)
        self.calibCameraWindow.actionOpen.triggered.connect(self.calibCameraWindow.actionOpen_triggered)

        # ===================> END CalibCameraWindow <========================#

    def dangNhapBT_clicked(self):
        if self.calibCameraWindow.isVisible():
            self.calibCameraWindow.close()
            self.hide()
        else:
            self.calibCameraWindow.show()
            self.hide()
            # self.cameraRun()

    def thoatBT_clicked(self):
        # when click exitBT button , close all screen
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit Main Window?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCoreApplication.instance().quit()


class CalibCameraWindow(QMainWindow, Ui_CalibCameraWindow):
    def __init__(self):
        super(CalibCameraWindow, self).__init__()
        self.file_path_calib = None
        self.pickle_path = None
        self.dist = None
        self.cameraMatrix_calib = None
        self.dist_calib = None
        self.mm_tren_pixel_calib = None
        self.mydir_calib = None
        self.cur_dir_calib = None
        self.myRootPath_calib = "D:/HUST/LAB/CALIB/NEW"
        self.index_calib = 1
        self.frame_calib = None
        self.cap_calib = cv2.VideoCapture(0)
        self.cap_pix_calib = None
        self.mode_calib = 0
        self.screen_show_calib = 0
        self.contrast_adjuster_calib = 0
        self.brightness_adjuster_calib = 0
        self.cam_curr_index_calib = None
        self.cameraLogic_calib = -1
        self.man_hinh_number_calib = 0
        self.huong_number_calib = 0
        self.chanel_calib = 0
        self.ngang = 0
        self.doc = 0
        self.kichThuoc = 0
        self.setupUi(self)

        self.captureWindow = CaptureWindow()
        # self.captureWindow.huong_number = self.huong_number_calib
        # self.captureWindow.man_hinh_number = self.man_hinh_number_calib
        # self.captureWindow.chanel = self.chanel_calib
        # self.captureWindow.screen_show = self.screen_show_calib
        self.captureWindow.setupUi(self.captureWindow)

        # ===================> START CalibCameraWindow <========================#

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
        self.FocusSlider.valueChanged[int].connect(self.FocusSlider_valueChanged)
        self.focusDSB.valueChanged.connect(self.focusDSB_valueChanged)
        ################### 2.6 end thay doi nguong action ##########

        ################### 2.9 chon kich thuoc khung hinh ######################
        self.choManHinhCB.currentTextChanged.connect(self.choManHinhCB_changed)
        ################### 2.9 end chon kich thuoc khung hinh ######################

        ################### 2.10 chon dieu chinh khung hinh ######################
        self.chonDieuHuongCB.currentTextChanged.connect(self.chonDieuHuongCB_changed)
        ################### 2.10 end chon dieu chinh khung hinh ######################

        ################### 2.11 chon dieu chinh ô bàn cờ ######################
        self.soONgangSB.valueChanged.connect(self.soONgangSB_changed)
        self.soODocSB.valueChanged.connect(self.soODocSB_changed)
        self.kichThuocOSB.valueChanged.connect(self.kichThuocOSB_changed)
        ################### 2.11 end chon dieu chinh khung hinh ######################

        # Button
        ################### 2.12 chup button ######################
        self.chupBT.clicked.connect(self.chupBT_clicked)
        ################### 2.12 end chup button ######################

        self.nextPage.clicked.connect(self.nextPage_clicked)
        self.calibBT.clicked.connect(self.calibBT_clicked)
        self.actionOpen.triggered.connect(self.actionOpen_triggered)

        # ===================> END CalibCameraWindow <========================#

        # ===================> START CaptureWindow <========================#

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
        ################### 2.5 end thay doi
        # do tuong phan action #############

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
        self.captureWindow.actionOpen.triggered.connect(self.captureWindow_actionOpen_triggered)
        self.captureWindow.LuuBT.clicked.connect(self.captureWindow.LuuBT_clicked)
        # ===================> END CaptureWindow <========================#

    def captureWindow_actionOpen_triggered(self):
        self.captureWindow.hide()
        self.captureWindow.cameraLogic = -1
        self.captureWindow.cap.release()
        self.show()
        # self.cameraRun()

    def nextPage_clicked(self):
        if self.captureWindow.isVisible():
            self.captureWindow.close()
            self.hide()
            self.cameraLogic_calib = -1
            self.cap_calib.release()
        else:
            self.cameraLogic_calib = -1
            self.cap_calib.release()
            self.runUpdateCaptureWindow()
            self.captureWindow.show()
            self.hide()

    def runUpdateCaptureWindow(self):
        self.captureWindow.screen_show = self.screen_show_calib
        self.captureWindow.man_hinh_number = self.man_hinh_number_calib
        self.captureWindow.huong_number = self.huong_number_calib
        self.captureWindow.chanel = self.chanel_calib
        self.captureWindow.contrast_adjuster = self.contrast_adjuster_calib
        self.captureWindow.brightness_adjuster = self.brightness_adjuster_calib
        self.captureWindow.camera_matrix = self.cameraMatrix_calib
        self.captureWindow.dist = self.dist_calib
        self.captureWindow.mm_tren_pixel = self.mm_tren_pixel_calib
        self.captureWindow.path_data = self.file_path_calib

        ##################### update thong so ###########################
        self.captureWindow.doSangDSB.setValue(self.captureWindow.brightness_adjuster)
        self.captureWindow.doTuongPhanDSB.setValue(self.captureWindow.contrast_adjuster)
        self.captureWindow.BrightnessSlider.setSliderPosition(self.captureWindow.brightness_adjuster)
        self.captureWindow.ContrastSlider.setSliderPosition(self.captureWindow.contrast_adjuster)
        self.captureWindow.chonKenhCB.setCurrentIndex(self.captureWindow.chanel)
        self.captureWindow.choManHinhCB.setCurrentIndex(self.captureWindow.man_hinh_number)
        self.captureWindow.chonDieuHuongCB.setCurrentIndex(self.captureWindow.huong_number)

        if self.captureWindow.screen_show == 0:
            self.captureWindow.smallScreenRB.setChecked(True)
        else:
            self.captureWindow.orginalScreenRB.setChecked(True)
        ################################################################

    def chonCamCB_changed(self):
        chonCamText = self.chonCamCB.currentText()
        if chonCamText == "Tắt":
            self.cam_curr_index_calib = self.chonCamCB.currentIndex()
            self.cameraLogic_calib = -1
            print(chonCamText)
            # self.TestCameraRun()
            self.CameraRun()

        if chonCamText == "Camera 0":
            self.cam_curr_index_calib = self.chonCamCB.currentIndex()
            self.cameraLogic_calib = 0
            print(chonCamText)
            # self.TestCameraRun()
            self.CameraRun()
        if chonCamText == "Camera 1":
            self.cam_curr_index_calib = self.chonCamCB.currentIndex()
            self.cameraLogic_calib = 1
            print(chonCamText)
            # self.TestCameraRun()
            self.CameraRun()

        if chonCamText == "Camera 2":
            self.cam_curr_index_calib = self.chonCamCB.currentIndex()
            self.cameraLogic_calib = 2
            print(chonCamText)
            # self.TestCameraRun()
            self.CameraRun()

        if chonCamText == "Camera 3":
            self.cam_curr_index_calib = self.chonCamCB.currentIndex()
            self.cameraLogic_calib = 3
            print(chonCamText)
            # self.TestCameraRun()
            self.CameraRun()

    def chonKenhCB_changed(self):
        chonKenhText = self.chonKenhCB.currentText()
        if chonKenhText == "RGB":
            self.chanel_calib = 0
            # cv2.destroyAllWindows()
        if chonKenhText == "Grayscale":
            self.chanel_calib = 1
            # cv2.destroyAllWindows()

    def smallScreenRB_toggled(self):
        self.screen_show_calib = 0

    def fullScreenRB_toggled(self):
        self.screen_show_calib = 1

    def BrightnessSlider_valueChanged(self, value):
        self.brightness_adjuster_calib = int(value)
        self.doSangDSB.setValue(value)

    def doSangDSB_valueChanged(self, value):
        self.brightness_adjuster_calib = value
        self.BrightnessSlider.setValue(value)

    def ContrastSlider_valueChanged(self, value):
        self.contrast_adjuster_calib = int(value)
        self.doTuongPhanDSB.setValue(value)

    def doTuongPhanDSB_valueChanged(self, value):
        self.contrast_adjuster_calib = value
        self.ContrastSlider.setValue(value)

    def FocusSlider_valueChanged(self, value):
        self.focus_adjuster_calib = int(value)
        self.focusDSB.setValue(value)

    def focusDSB_valueChanged(self, value):
        self.focus_adjuster_calib = value
        self.FocusSlider.setValue(value)

    def soONgangSB_changed(self, value):
        self.ngang = value

    def soODocSB_changed(self, value):
        self.doc = value

    def kichThuocOSB_changed(self, value):
        self.kichThuoc = value

    def choManHinhCB_changed(self):
        choManHinhText = self.choManHinhCB.currentText()
        if choManHinhText == "Tự động":
            self.man_hinh_number_calib = 0
            cv2.destroyAllWindows()
        if choManHinhText == "2:3 (1080 x 720) ":
            self.man_hinh_number_calib = 1
            # print(choManHinhText)
            cv2.destroyAllWindows()
        if choManHinhText == "16:9 (960 x 540) ":
            self.man_hinh_number_calib = 2
            cv2.destroyAllWindows()
        if choManHinhText == "16:9 (640 x 360) ":
            self.man_hinh_number_calib = 3
            cv2.destroyAllWindows()
        if choManHinhText == "4:3 (960 x 720) ":
            self.man_hinh_number_calib = 4
            cv2.destroyAllWindows()
        if choManHinhText == "4:3 (640 x 480) ":
            self.man_hinh_number_calib = 5
            cv2.destroyAllWindows()

    def chonDieuHuongCB_changed(self):
        choDieuHuongText = self.chonDieuHuongCB.currentText()
        if choDieuHuongText == "Không":
            self.huong_number_calib = 0
            cv2.destroyAllWindows()
        if choDieuHuongText == "Lật":
            self.huong_number_calib = 1
            cv2.destroyAllWindows()
        if choDieuHuongText == "Đảo ngược":
            self.huong_number_calib = 2
            cv2.destroyAllWindows()
        if choDieuHuongText == "Xoay 90 độ sang trái":
            self.huong_number_calib = 3
            cv2.destroyAllWindows()
        if choDieuHuongText == "Xoay 90 độ sang phải":
            self.huong_number_calib = 4
            cv2.destroyAllWindows()

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
        if self.frame_calib is not None:
            if self.index_calib == 1:
                self.mydir_calib = self.myRootPath_calib + '/' + time.strftime("%d-%m-%Y-%H-%M-%S")
                os.mkdir(self.mydir_calib)
            # self.anhMauLB.setPixmap(QPixmap(u"../handsample/" + str(self.index + 1) + ".jpg"))
            if self.index_calib <= 10:
                self.SoLB.setText(str(self.index_calib))
                self.saveImage(self.index_calib)
                if self.index_calib == 10:
                    self.index_calib = 0
                    reply = QMessageBox.warning(self.centralwidget, 'Warning',
                                                "You must calib camera?", QMessageBox.Yes | QMessageBox.No,
                                                QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        self.cur_dir_calib = self.mydir_calib
                    # reset lại mang nguong va thu muc luu
                    # self.mydir_calib = self.myRootPath_calib + '/' + time.strftime("%d-%m-%Y-%H-%M-%S")
                    # os.mkdir(self.mydir_calib)
                self.index_calib = self.index_calib + 1

    def calibBT_clicked(self):
        # self.cur_dir_calib = r'D:\HUST\LAB\CALIB\NEW\30-05-2022-00-57-04'
        img = cv2.imread("{}/{}".format(self.cur_dir_calib, 1) + ".png")  # ban tay ngua
        if self.ngang == 0 or self.doc == 0 or self.kichThuoc == 0:
            QMessageBox.warning(self, "Warning", "You must fill out all ")
        else:
            # self.cameraMatrix, self.dist, self.mm_tren_pixel = CalibCamera(self.cur_dir_calib,
            #                                                                so_o_ngang=self.ngang,
            #                                                                so_o_doc=self.doc,
            #                                                                kichthuoc=self.kichThuoc,
            #                                                                frameSize=self.frame_calib.shape[:2])
            self.cameraMatrix_calib, self.dist_calib, self.mm_tren_pixel_calib = CalibCamera(folder=self.cur_dir_calib,
                                                                                             so_o_ngang=self.ngang,
                                                                                             so_o_doc=self.doc,
                                                                                             kichthuoc=self.kichThuoc,
                                                                                             frameSize=(img.shape[0],
                                                                                                        img.shape[1]))
            print(self.cameraMatrix_calib, self.dist_calib)
            reply = QMessageBox.question(self.centralwidget, 'Question',
                                         "Do you want save camera matrix?",
                                         QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.file_path_calib, _ = QFileDialog.getSaveFileName(self, "Save Camera Matrix", "",
                                                                      "P File(*.p);;All Files(*.*) ")
                if self.file_path_calib == "":
                    return
                print(self.file_path_calib)

                # data = {"camera_matrix": self.cameraMatrix,
                #         "dist_coeff": self.dist,
                #         "nx": self.ngang,
                #         "ny": self.doc,
                #         "kich thuoc o ban co": self.kichThuoc}
                # print(data)
                # Write JSON file
                # with open("sample.json", "w") as outfile:
                #     json.dump(data, outfile)
                dist_pickle = {}
                dist_pickle["camera_matrix"] = self.cameraMatrix_calib
                dist_pickle["dist_coeff"] = self.dist_calib
                dist_pickle["nx"] = self.ngang
                dist_pickle["ny"] = self.doc
                dist_pickle["kich thuoc o ban co"] = self.kichThuoc
                dist_pickle["gia tri 1 pixel"] = self.mm_tren_pixel_calib
                dist_pickle["screen show"] = self.screen_show_calib
                dist_pickle["man hinh"] = self.man_hinh_number_calib
                dist_pickle["huong"] = self.huong_number_calib
                dist_pickle["kenh"] = self.chanel_calib
                dist_pickle["contrast_adjuster"] = self.contrast_adjuster_calib
                dist_pickle["brightness_adjuster"] = self.brightness_adjuster_calib

                pickle.dump(dist_pickle, open(self.file_path_calib, "wb"))
                text = "camera matrix:\n" + \
                       "[{}, {}, {}]\n".format(self.cameraMatrix_calib[0][0], self.cameraMatrix_calib[0][1],
                                               self.cameraMatrix_calib[0][2]) + \
                       "[{}, {}, {}]\n".format(self.cameraMatrix_calib[1][0], self.cameraMatrix_calib[1][1],
                                               self.cameraMatrix_calib[1][2]) + \
                       "[{}, {}, {}]\n".format(self.cameraMatrix_calib[2][0], self.cameraMatrix_calib[2][1],
                                               self.cameraMatrix_calib[2][2]) + \
                       "dist_coeff:\n" + \
                       "[{}, {}, {},\n {}, {}]\n".format(self.dist_calib[0][0], self.dist_calib[0][1],
                                                         self.dist_calib[0][2],
                                                         self.dist_calib[0][3],
                                                         self.dist_calib[0][4]) + \
                       "nx: {}, ny: {}, kt(mm): {}\n".format(self.ngang, self.doc, self.kichThuoc) + \
                       "gia tri 1 pixel: {}".format(self.mm_tren_pixel_calib)

                self.KqLB.setText(text)

    def actionOpen_triggered(self):
        self.file_path_calib, _ = QFileDialog.getOpenFileName(self, "Select a file")
        print(self.file_path_calib)
        self.pickle_path = self.file_path_calib
        dist_pickle = pickle.load(open(self.pickle_path, "rb"))
        self.cameraMatrix_calib = dist_pickle["camera_matrix"]
        self.dist_calib = dist_pickle["dist_coeff"]
        self.ngang = dist_pickle["nx"]
        self.doc = dist_pickle["ny"]
        self.kichThuoc = dist_pickle["kich thuoc o ban co"]
        self.mm_tren_pixel_calib = dist_pickle["gia tri 1 pixel"]

        self.screen_show_calib = dist_pickle["screen show"]
        self.man_hinh_number_calib = dist_pickle["man hinh"]
        self.huong_number_calib = dist_pickle["huong"]
        self.chanel_calib = dist_pickle["kenh"]
        self.contrast_adjuster_calib = dist_pickle["contrast_adjuster"]
        self.brightness_adjuster_calib = dist_pickle["brightness_adjuster"]

        self.runUpdateCalibCameraWindow()

        text = "camera matrix:\n" + \
               "[{}, {}, {}]\n".format(self.cameraMatrix_calib[0][0], self.cameraMatrix_calib[0][1],
                                       self.cameraMatrix_calib[0][2]) + \
               "[{}, {}, {}]\n".format(self.cameraMatrix_calib[1][0], self.cameraMatrix_calib[1][1],
                                       self.cameraMatrix_calib[1][2]) + \
               "[{}, {}, {}]\n".format(self.cameraMatrix_calib[2][0], self.cameraMatrix_calib[2][1],
                                       self.cameraMatrix_calib[2][2]) + \
               "dist_coeff:\n" + \
               "[{}, {}, {},\n {}, {}]\n".format(self.dist_calib[0][0], self.dist_calib[0][1], self.dist_calib[0][2],
                                                 self.dist_calib[0][3],
                                                 self.dist_calib[0][4]) + \
               "nx: {}, ny: {}, kt(mm): {}\n".format(self.ngang, self.doc, self.kichThuoc) + \
               "gia tri 1 pixel: {}".format(self.mm_tren_pixel_calib)

        self.KqLB.setText(text)

    def runUpdateCalibCameraWindow(self):
        self.doSangDSB.setValue(self.brightness_adjuster_calib)
        self.doTuongPhanDSB.setValue(self.contrast_adjuster_calib)
        self.BrightnessSlider.setSliderPosition(self.brightness_adjuster_calib)
        self.ContrastSlider.setSliderPosition(self.contrast_adjuster_calib)
        self.chonKenhCB.setCurrentIndex(self.chanel_calib)
        self.choManHinhCB.setCurrentIndex(self.man_hinh_number_calib)
        self.chonDieuHuongCB.setCurrentIndex(self.huong_number_calib)

        if self.screen_show_calib == 0:
            self.smallScreenRB.setChecked(True)
        else:
            self.orginalScreenRB.setChecked(True)
        ################################################################

    def CameraRun(self):
        while self.cameraLogic_calib != -1:
            print('cameraLogic:' + str(self.cameraLogic_calib))
            # self.cap = cv2.VideoCapture(self.cameraLogic, cv2.CAP_DSHOW)
            # self.cap = cv2.VideoCapture(self.cameraLogic, cv2.CAP_MSMF)
            self.cap_calib = cv2.VideoCapture(self.cameraLogic_calib)
            # self.cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)
            # Using cv2.CAP_DSHOW removes the warning, but slows down my frame rate from 30fps to 7fps, on Windows
            # self.cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)  # turn the autofocus off
            # self.cap.set(cv2.CV_CAP_PROP_SETTINGS, 11)
            if not self.cap_calib.isOpened():
                QMessageBox.warning(self, "Warning", "Camera is not connected")
                break
            while self.cap_calib.isOpened():
                # self.anhMauLB.setPixmap(QPixmap(u"../handsample/" + str(self.index_calib) + ".jpg"))
                # Capture the video frame
                # by frame
                ret, self.frame_calib = self.cap_calib.read()
                if not ret:
                    print("Can't receive frame (stream end?). Exiting ...")
                    break
                self.frame_calib = self.ReturnFrameLan1(self.frame_calib, screen_show=self.screen_show_calib,
                                                        huong_number=self.huong_number_calib,
                                                        man_hinh_number=self.man_hinh_number_calib)
                self.frame_calib = self.ReturnFrameLan2(self.frame_calib, chanel=self.chanel_calib,
                                                        brightness_adjuster=self.brightness_adjuster_calib,
                                                        contrast_adjuster=self.contrast_adjuster_calib)
                if self.screen_show_calib == 0:
                    self.cap_pix_calib = convert_nparray_to_QPixmap(self.frame_calib)
                    self.cameraLB.setPixmap(self.cap_pix_calib)
                else:
                    self.frame_calib = imutils.resize(self.frame_calib, height=960)
                    cv2.imshow('Camera', self.frame_calib)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.cap_calib.release()
                    cv2.destroyAllWindows()
                    break
        self.cameraLB.clear()
        self.cap_calib.release()
        cv2.destroyAllWindows()

    def saveImage(self, index):
        cv2.imwrite("{}/{}".format(self.mydir_calib, index) + ".png", self.frame_calib)

    def closeEvent(self, event):
        # close with X button
        reply = QMessageBox.question(self.centralwidget, 'Question',
                                     "Are you sure to quit this Window?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.cameraLB.clear()
            self.cap_calib.release()
            cv2.destroyAllWindows()
            # QCoreApplication.instance().quit()
            # QCoreApplication.quit()
            # print('close')
            sys.exit()
            # event.accept()

        else:
            event.ignore()


class CaptureWindow(QMainWindow, Ui_CaptureWindow):
    def __init__(self):
        super(CaptureWindow, self).__init__()
        self.mang_kq_calib = []
        self.mang_ket_qua_hien_thoi = []
        self.mang_kich_thuoc = []
        self.camera_matrix = None
        self.dist = None
        self.mm_tren_pixel = 0
        self.mang_kq = []
        self.img_cur = None
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
        self.path_data = None
        self.setupUi(self)

        # ##################### update thong so ###########################
        # self.doSangDSB.setValue(self.brightness_adjuster)
        # self.doTuongPhanDSB.setValue(self.contrast_adjuster)
        # self.BrightnessSlider.setSliderPosition(self.brightness_adjuster)
        # self.ContrastSlider.setSliderPosition(self.contrast_adjuster)
        # self.chonKenhCB.setCurrentIndex(self.chanel)
        # self.choManHinhCB.setCurrentIndex(self.man_hinh_number)
        # self.chonDieuHuongCB.setCurrentIndex(self.huong_number)
        #
        # if self.screen_show == 0:
        #     self.smallScreenRB.setChecked(True)
        # else:
        #     self.orginalScreenRB.setChecked(True)

        ################################################################

        ################### 2.1 chonCamera action ######################
        self.chonCamCB.currentTextChanged.connect(self.chonCamCB_changed)
        ################### 2.1 chonKenhCB action ######################

        ################### 2.2 chonKenhCB action ######################
        # self.chonKenhCB.currentTextChanged.connect(self.chonKenhCB_changed)
        ################### 2.2 chonKenhCB action ######################

        ################### 2.3 chon screen action ######################
        # self.smallScreenRB.toggled.connect(self.smallScreenRB_toggled)
        # self.orginalScreenRB.toggled.connect(self.fullScreenRB_toggled)
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
        # self.choManHinhCB.currentTextChanged.connect(self.choManHinhCB_changed)
        ################### 2.9 end chon kich thuoc khung hinh ######################

        ################### 2.10 chon dieu chinh khung hinh ######################
        # self.chonDieuHuongCB.currentTextChanged.connect(self.chonDieuHuongCB_changed)
        ################### 2.10 end chon dieu chinh khung hinh ######################

        # Button
        ################### 2.12 chup button ######################
        self.chupBT.clicked.connect(self.chupBT_clicked)
        ################### 2.12 end chup button ######################
        # Button
        ################### 2.13 xemKQ button ######################
        self.XemKQBT.clicked.connect(self.XemKQBT_clicked)
        self.LuuBT.clicked.connect(self.LuuBT_clicked)
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
        if chonCamText == "Camera 2":
            self.cam_curr_index = self.chonCamCB.currentIndex()
            self.cameraLogic = 2
            print(chonCamText)
            # self.TestCameraRun()
            self.CameraRun()
        if chonCamText == "Camera 3":
            self.cam_curr_index = self.chonCamCB.currentIndex()
            self.cameraLogic = 3
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
        self.img_cur = self.frame
        if self.frame is not None:
            if self.index == 1:
                self.mang_ket_qua_hien_thoi = []
                self.mang_kich_thuoc = []
                self.mang_kq_calib = []
                self.mydir = self.myRootPath + '/' + time.strftime("%d-%m-%Y-%H-%M-%S")
                os.mkdir(self.mydir)
            # self.anhMauLB.setPixmap(QPixmap(u"../handsample/" + str(self.index + 1) + ".jpg"))
            if self.index <= 14:
                self.mang_nguong.append(self.nguong_adjuster)
                # self.myThread1 = threading.Thread(target=self.saveImage, args=(self.index,))
                # self.myThread1.start()
                self.SoLB.setText(str(self.index))
                status, mang_diem, img_kq = self.Function(self.img_cur, self.index, self.nguong_adjuster)

                # # # Test
                # status = True
                # mang_diem = [(431, 411), (354, 526), (356, 229), (291, 395), (266, 186), (237, 382),
                #              (174, 207), (181, 393), (75, 290), (123, 424), (213, 633), (398, 483),
                #              (356, 455), (336, 347), (295, 331), (271, 322), (225, 315), (204, 331),
                #              (159, 333)]

                if status == False:
                    reply = QMessageBox.warning(self.centralwidget, 'Warning',
                                                "No result?")
                    self.CameraRun()
                else:
                    self.mang_kq = self.mang_kq + mang_diem
                    self.saveImage(self.index)
                    if self.index == 14:
                        self.mang_ket_qua_hien_thoi = self.mang_kq
                        print("{}: {}".format(len(self.mang_ket_qua_hien_thoi), self.mang_ket_qua_hien_thoi))
                        self.index = 0
                        self.anhMauLB.setPixmap(QPixmap(u"../handsample/" + str(self.index + 1) + ".jpg"))
                        reply = QMessageBox.warning(self.centralwidget, 'Warning',
                                                    "You must save all files?", QMessageBox.Yes | QMessageBox.No,
                                                    QMessageBox.No)
                        if reply == QMessageBox.Yes:
                            self.cur_dir = self.mydir
                        self.cur_mang_nguong = self.mang_nguong
                        self.mang_nguong = []
                        self.mang_kq = []
                        # print(self.cur_mang_nguong)
                self.index = self.index + 1

    # ==================================================================================

    def XemKQBT_clicked_V5(self):
        # print(self.cur_mang_nguong)

        pickle_path = self.path_data
        dist_pickle = pickle.load(open(pickle_path, "rb"))
        self.camera_matrix = dist_pickle["camera_matrix"]
        self.dist = dist_pickle["dist_coeff"]
        self.mm_tren_pixel = dist_pickle["gia tri 1 pixel"]
        # self.mang_ket_qua_hien_thoi = [(419, 385), (355, 497), (353, 208), (291, 373), (261, 166), (237, 361),
        #                                (174, 189), (181, 373), (75, 271), (126, 404), (218, 609), (392, 455),
        #                                (350, 431), (336, 325), (294, 309), (268, 300), (222, 294), (203, 312),
        #                                (159, 314), (131, 362), (96, 376), (318, 383), (149, 615), (172, 403),
        #                                (350, 410), (136, 495), (356, 503), (113, 555), (347, 564), (92, 451),
        #                                (140, 446), (262, 275), (262, 562), (142, 719), (296, 719), (409, 404),
        #                                (142, 404), (407, 395), (188, 395), (345, 719), (216, 719), (302, 245),
        #                                (358, 241), (296, 183), (245, 181), (340, 371), (216, 371), (326, 464),
        #                                (178, 464), (351, 271), (318, 263), (346, 196), (214, 279), (23, 424), (94, 522),
        #                                (110, 227), (164, 392), (197, 187), (218, 382), (278, 212), (271, 390),
        #                                (366, 289), (327, 414), (246, 627), (51, 489), (91, 460), (126, 346), (169, 332),
        #                                (189, 318), (235, 313), (251, 327), (294, 329), (320, 373), (355, 384),
        #                                (144, 399), (321, 632), (320, 399), (143, 404), (351, 491), (134, 497),
        #                                (371, 549), (140, 555), (353, 440), (398, 450), (194, 254), (194, 540),
        #                                (304, 719), (153, 719), (58, 377), (325, 377), (80, 352), (303, 352), (125, 719),
        #                                (256, 719), (191, 249), (138, 249), (163, 192), (214, 184), (132, 368),
        #                                (254, 368), (162, 505), (300, 505), (163, 285), (196, 281), (271, 271),
        #                                (368, 350)]
        # self.camera_matrix = [[2.22193619e+03, 0.00000000e+00, 4.33098274e+02],
        #                       [0.00000000e+00, 2.32879163e+03, 1.75682388e+02],
        #                       [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]]
        #
        # self.mm_tren_pixel = 0.4232273154825574
        # self.dist = [[-4.56850084e-01, -1.59904221e+00, 6.14823738e-03, -3.54756064e-02,
        #               1.09590517e+02]]
        # file_name, _ = QFileDialog.getOpenFileName(self, "Select a file")
        # # pickle_path = self.path_data
        # pickle_path = file_name
        # dist_pickle = pickle.load(open(pickle_path, "rb"))
        # self.camera_matrix = dist_pickle["camera_matrix"]
        # self.dist = dist_pickle["dist_coeff"]
        # self.mm_tren_pixel = dist_pickle["gia tri 1 pixel"]
        print(self.mm_tren_pixel)

        self.mang_ket_qua_hien_thoi = [(431, 411), (354, 526), (356, 229), (291, 395), (266, 186), (237, 382),
                                       (174, 207), (181, 393), (75, 290), (123, 424), (213, 633), (398, 483),
                                       (356, 455), (336, 347), (295, 331), (271, 322), (225, 315), (204, 331),
                                       (159, 333), (130, 381), (95, 393), (317, 405), (142, 636), (161, 430),
                                       (344, 439), (129, 546), (348, 557), (117, 591), (340, 602), (81, 479),
                                       (127, 466), (172, 293), (172, 586), (109, 719), (259, 719), (355, 428),
                                       (111, 428), (346, 410), (124, 410), (269, 719), (149, 719), (231, 262),
                                       (286, 260), (350, 228), (303, 218), (383, 434), (265, 434), (376, 508),
                                       (231, 508), (376, 339), (342, 329), (279, 325), (238, 345), (74, 399),
                                       (133, 506), (153, 220), (208, 385), (243, 182), (263, 376), (327, 211),
                                       (316, 388), (421, 296), (370, 416), (282, 624), (96, 469), (138, 445),
                                       (168, 338), (211, 324), (233, 309), (278, 305), (295, 324), (338, 327),
                                       (369, 373), (402, 387), (187, 392), (353, 627), (341, 333), (165, 328),
                                       (370, 447), (156, 441), (384, 504), (165, 498), (385, 384), (430, 395),
                                       (255, 229), (255, 514), (354, 719), (197, 719), (130, 356), (380, 356),
                                       (137, 338), (355, 338), (196, 719), (333, 719), (234, 198), (178, 196),
                                       (244, 129), (291, 124), (218, 310), (355, 310), (235, 420), (392, 420),
                                       (173, 323), (208, 321), (272, 310), (305, 336)]

        mang_ket_qua_hien_thoi_new = np.array(self.mang_ket_qua_hien_thoi, dtype=np.float64)
        print(mang_ket_qua_hien_thoi_new)
        for no_point, point in enumerate(mang_ket_qua_hien_thoi_new):
            # point_calib = cv2.undistortPoints(point, self.camera_matrix, self.dist, None, self.camera_matrix)
            point_calib = cv2.undistortPoints(point, self.camera_matrix, self.dist, P=self.camera_matrix)
            print(point_calib)
            self.mang_kq_calib.append((point_calib[0][0][0], point_calib[0][0][1]))

        self.mang_kich_thuoc = TinhToanKhoangCach(self.mang_kq_calib, self.mm_tren_pixel)
        print(self.mang_kich_thuoc)
        self.progressBar.setValue(50)

        kt_1 = 'axb'

        # img1 = cv2.imread("{}/{}".format(self.cur_dir, 1) + ".png")
        #
        # kt_1 = '{}x{}'.format(img1.shape[0], img1.shape[1])

        self.data1 = {'Kích thước ảnh': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên điểm': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
                      'Vị trí': ['{}'.format(self.mang_ket_qua_hien_thoi[0]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[1]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[2]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[3]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[4]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[5]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[6]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[7]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[8]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[9])],
                      'Kích thước ảnh ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên điểm ': ['11', '20', '21', '22', '23', '24', '25', '26', '27', '28'],
                      'Vị trí ': ['{}'.format(self.mang_ket_qua_hien_thoi[10]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[11]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[12]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[13]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[14]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[15]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[16]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[17]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[18]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[19])],
                      'Kích thước ảnh  ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên điểm  ': ['29', '36', '37', '14', '15', '16', '17', '18', '19', '47'],
                      'Vị trí  ': ['{}'.format(self.mang_ket_qua_hien_thoi[20]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[21]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[22]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[23]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[24]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[25]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[26]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[27]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[28]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[29])],
                      'Kích thước ảnh   ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên điểm   ': ['48', '12', '13', '51', '52', '53', '54', '38', '39', '49'],
                      'Vị trí   ': ['{}'.format(self.mang_ket_qua_hien_thoi[30]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[31]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[32]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[33]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[34]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[35]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[36]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[37]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[38]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[39])],
                      'Kích thước ảnh    ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên điểm    ': ['50', '45', '46', '30', '31', '32', '33', '34', '35', '41'],
                      'Vị trí    ': ['{}'.format(self.mang_ket_qua_hien_thoi[40]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[41]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[42]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[43]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[44]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[45]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[46]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[47]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[48]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[49])],
                      'Kích thước ảnh     ': [kt_1, kt_1, kt_1],
                      'Tên điểm     ': ['42', '43', '44'],
                      'Vị trí     ': ['{}'.format(self.mang_ket_qua_hien_thoi[50]),
                                      '{}'.format(self.mang_ket_qua_hien_thoi[51]),
                                      '{}'.format(self.mang_ket_qua_hien_thoi[52])]
                      }
        self.data2 = {'Kích thước ảnh': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên điểm': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
                      'Vị trí': ['{}'.format(self.mang_ket_qua_hien_thoi[53]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[54]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[55]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[56]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[57]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[58]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[59]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[60]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[61]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[62])],
                      'Kích thước ảnh ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên điểm ': ['11', '20', '21', '22', '23', '24', '25', '26', '27', '28'],
                      'Vị trí ': ['{}'.format(self.mang_ket_qua_hien_thoi[63]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[64]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[65]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[66]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[67]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[68]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[69]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[70]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[71]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[72])],
                      'Kích thước ảnh  ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên điểm  ': ['29', '36', '37', '14', '15', '16', '17', '18', '19', '47'],
                      'Vị trí  ': ['{}'.format(self.mang_ket_qua_hien_thoi[73]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[74]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[75]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[76]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[77]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[78]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[79]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[80]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[81]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[82])],
                      'Kích thước ảnh   ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên điểm   ': ['48', '12', '13', '51', '52', '53', '54', '38', '39', '49'],
                      'Vị trí   ': ['{}'.format(self.mang_ket_qua_hien_thoi[83]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[84]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[85]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[86]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[87]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[88]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[89]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[90]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[91]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[92])],
                      'Kích thước ảnh    ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên điểm    ': ['50', '45', '46', '30', '31', '32', '33', '34', '35', '41'],
                      'Vị trí    ': ['{}'.format(self.mang_ket_qua_hien_thoi[93]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[94]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[95]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[96]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[97]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[98]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[99]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[100]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[101]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[102])],
                      'Kích thước ảnh     ': [kt_1, kt_1, kt_1],
                      'Tên điểm     ': ['42', '43', '44'],
                      'Vị trí     ': ['{}'.format(self.mang_ket_qua_hien_thoi[103]),
                                      '{}'.format(self.mang_ket_qua_hien_thoi[104]),
                                      '{}'.format(self.mang_ket_qua_hien_thoi[105])]
                      }
        self.data3 = {'Kích thước ảnh': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên kích thước': ['D1_p', 'D2_p', 'D3_p', 'D4_p', 'D5_p', 'D6_p', 'D7_p', 'C1_p', 'R1_p',
                                         'R2_p'],
                      'Giá trị (mm)': ['{}'.format(self.mang_kich_thuoc[0]),
                                       '{}'.format(self.mang_kich_thuoc[1]),
                                       '{}'.format(self.mang_kich_thuoc[2]),
                                       '{}'.format(self.mang_kich_thuoc[3]),
                                       '{}'.format(self.mang_kich_thuoc[4]),
                                       '{}'.format(self.mang_kich_thuoc[5]),
                                       '{}'.format(self.mang_kich_thuoc[6]),
                                       '{}'.format(self.mang_kich_thuoc[7]),
                                       '{}'.format(self.mang_kich_thuoc[8]),
                                       '{}'.format(self.mang_kich_thuoc[9])],
                      'Kích thước ảnh ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên kích thước ': ['R3_p', 'R4_p', 'R5_p', 'R6_p', 'D8_p', 'R7_p', 'R8_p', 'R9_p', 'Da5_p',
                                          'Da1_p'],
                      'Giá trị (mm) ': ['{}'.format(self.mang_kich_thuoc[10]),
                                        '{}'.format(self.mang_kich_thuoc[11]),
                                        '{}'.format(self.mang_kich_thuoc[12]),
                                        '{}'.format(self.mang_kich_thuoc[13]),
                                        '{}'.format(self.mang_kich_thuoc[14]),
                                        '{}'.format(self.mang_kich_thuoc[15]),
                                        '{}'.format(self.mang_kich_thuoc[16]),
                                        '{}'.format(self.mang_kich_thuoc[17]),
                                        '{}'.format(self.mang_kich_thuoc[18]),
                                        '{}'.format(self.mang_kich_thuoc[19])],
                      'Kích thước ảnh  ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên kích thước  ': ['Da2_p', 'Da3_p', 'Da7_p', 'Da6_p', 'Da4_p', 'V1_p', 'V2_p'],
                      'Giá trị (mm)  ': ['{}'.format(self.mang_kich_thuoc[20]),
                                         '{}'.format(self.mang_kich_thuoc[21]),
                                         '{}'.format(self.mang_kich_thuoc[22]),
                                         '{}'.format(self.mang_kich_thuoc[23]),
                                         '{}'.format(self.mang_kich_thuoc[24]),
                                         '{}'.format(self.mang_kich_thuoc[25]),
                                         '{}'.format(self.mang_kich_thuoc[26])],
                      }
        self.data4 = {'Kích thước ảnh': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên kích thước': ['D1_t', 'D2_t', 'D3_t', 'D4_t', 'D5_t', 'D6_t', 'D7_t', 'C1_t', 'R1_t',
                                         'R2_t'],
                      'Giá trị (mm) ': ['{}'.format(self.mang_kich_thuoc[27]),
                                        '{}'.format(self.mang_kich_thuoc[28]),
                                        '{}'.format(self.mang_kich_thuoc[29]),
                                        '{}'.format(self.mang_kich_thuoc[30]),
                                        '{}'.format(self.mang_kich_thuoc[31]),
                                        '{}'.format(self.mang_kich_thuoc[32]),
                                        '{}'.format(self.mang_kich_thuoc[33]),
                                        '{}'.format(self.mang_kich_thuoc[34]),
                                        '{}'.format(self.mang_kich_thuoc[35]),
                                        '{}'.format(self.mang_kich_thuoc[36])],
                      'Kích thước ảnh ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên kích thước ': ['R3_t', 'R4_t', 'R5_t', 'R6_t', 'D8_t', 'R7_t', 'R8_t', 'R9_t', 'Da5_t',
                                          'Da1_t'],
                      'Giá trị (mm)  ': ['{}'.format(self.mang_kich_thuoc[37]),
                                         '{}'.format(self.mang_kich_thuoc[38]),
                                         '{}'.format(self.mang_kich_thuoc[39]),
                                         '{}'.format(self.mang_kich_thuoc[40]),
                                         '{}'.format(self.mang_kich_thuoc[41]),
                                         '{}'.format(self.mang_kich_thuoc[42]),
                                         '{}'.format(self.mang_kich_thuoc[43]),
                                         '{}'.format(self.mang_kich_thuoc[44]),
                                         '{}'.format(self.mang_kich_thuoc[45]),
                                         '{}'.format(self.mang_kich_thuoc[46])],
                      'Kích thước ảnh  ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên kích thước  ': ['Da2_t', 'Da3_t', 'Da7_t', 'Da6_t', 'Da4_t', 'V1_t', 'V2_t'],
                      'Giá trị (mm)   ': ['{}'.format(self.mang_kich_thuoc[47]),
                                          '{}'.format(self.mang_kich_thuoc[48]),
                                          '{}'.format(self.mang_kich_thuoc[49]),
                                          '{}'.format(self.mang_kich_thuoc[50]),
                                          '{}'.format(self.mang_kich_thuoc[51]),
                                          '{}'.format(self.mang_kich_thuoc[52]),
                                          '{}'.format(self.mang_kich_thuoc[53])],
                      }

        self.progressBar.setValue(90)

        self.setData(self.bang_diem_tay_phai, self.data1)
        self.setData(self.bang_diem_tay_trai, self.data2)
        self.setData(self.bang_khoang_cach_tay_phai, self.data3)
        self.setData(self.bang_khoang_cach_tay_trai, self.data4)

        self.bang_diem_tay_phai.resizeColumnsToContents()
        self.bang_diem_tay_phai.resizeRowsToContents()
        self.bang_diem_tay_trai.resizeColumnsToContents()
        self.bang_diem_tay_trai.resizeRowsToContents()
        self.bang_khoang_cach_tay_phai.resizeColumnsToContents()
        self.bang_khoang_cach_tay_phai.resizeRowsToContents()
        self.bang_khoang_cach_tay_trai.resizeColumnsToContents()
        self.bang_khoang_cach_tay_trai.resizeRowsToContents()

        # set phan tram da xong
        self.progressBar.setValue(100)
        self.progressBar.setValue(0)

    # ==================================================================================
    # Test

    def XemKQBT_clicked(self):
        # print("{}: {}".format(len(self.mang_ket_qua_hien_thoi), self.mang_ket_qua_hien_thoi))
        # print(self.cur_mang_nguong)
        # pickle_path = self.path_data
        pickle_path = self.path_data
        dist_pickle = pickle.load(open(pickle_path, "rb"))
        self.camera_matrix = dist_pickle["camera_matrix"]
        self.dist = dist_pickle["dist_coeff"]
        self.mm_tren_pixel = dist_pickle["gia tri 1 pixel"]
        # print(self.mm_tren_pixel)
        # print(self.camera_matrix)
        # print(self.dist)

        mang_ket_qua_hien_thoi_new = np.array(self.mang_ket_qua_hien_thoi, dtype=np.float64)
        # print(mang_ket_qua_hien_thoi_new)
        for no_point, point in enumerate(mang_ket_qua_hien_thoi_new):
            # point_calib = cv2.undistortPoints(point, self.camera_matrix, self.dist, None, self.camera_matrix)
            point_calib = cv2.undistortPoints(point, self.camera_matrix, self.dist, P=self.camera_matrix)
            # print(point_calib)
            self.mang_kq_calib.append((point_calib[0][0][0], point_calib[0][0][1]))
        #
        # for no_point, point in enumerate(self.mang_ket_qua_hien_thoi):
        #     # point_calib = cv2.undistortPoints(point, self.camera_matrix, self.dist, None, self.camera_matrix)
        #     point_calib = cv2.undistortPoints(self.mang_ket_qua_hien_thoi[no_point], self.camera_matrix, self.dist,
        #                                       P=self.camera_matrix)
        #     print(point_calib)
        #     self.mang_kq_calib.append((point_calib[0][0][0], point_calib[0][0][1]))

        # print(self.camera_matrix)
        # print(self.dist)
        # print(self.camera_matrix)
        # print(mang_kq_calib)

        self.mang_kich_thuoc = TinhToanKhoangCach(self.mang_kq_calib, self.mm_tren_pixel)
        # print(self.mang_kich_thuoc)

        # for i, kq in enumerate(anh_chup):
        #     cv2.imwrite('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\result\\kq_img{}.png'.format(i), kq)
        img1 = cv2.imread("{}/{}".format(self.cur_dir, 1) + ".png")

        kt_1 = '{}x{}'.format(img1.shape[0], img1.shape[1])

        self.data1 = {'Kích thước ảnh': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên điểm': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
                      'Vị trí': ['{}'.format(self.mang_ket_qua_hien_thoi[0]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[1]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[2]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[3]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[4]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[5]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[6]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[7]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[8]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[9])],
                      'Kích thước ảnh ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên điểm ': ['11', '20', '21', '22', '23', '24', '25', '26', '27', '28'],
                      'Vị trí ': ['{}'.format(self.mang_ket_qua_hien_thoi[10]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[11]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[12]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[13]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[14]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[15]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[16]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[17]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[18]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[19])],
                      'Kích thước ảnh  ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên điểm  ': ['29', '36', '37', '14', '15', '16', '17', '18', '19', '47'],
                      'Vị trí  ': ['{}'.format(self.mang_ket_qua_hien_thoi[20]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[21]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[22]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[23]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[24]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[25]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[26]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[27]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[28]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[29])],
                      'Kích thước ảnh   ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên điểm   ': ['48', '12', '13', '51', '52', '53', '54', '38', '39', '49'],
                      'Vị trí   ': ['{}'.format(self.mang_ket_qua_hien_thoi[30]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[31]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[32]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[33]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[34]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[35]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[36]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[37]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[38]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[39])],
                      'Kích thước ảnh    ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên điểm    ': ['50', '45', '46', '30', '31', '32', '33', '34', '35', '41'],
                      'Vị trí    ': ['{}'.format(self.mang_ket_qua_hien_thoi[40]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[41]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[42]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[43]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[44]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[45]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[46]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[47]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[48]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[49])],
                      'Kích thước ảnh     ': [kt_1, kt_1, kt_1],
                      'Tên điểm     ': ['42', '43', '44'],
                      'Vị trí     ': ['{}'.format(self.mang_ket_qua_hien_thoi[50]),
                                      '{}'.format(self.mang_ket_qua_hien_thoi[51]),
                                      '{}'.format(self.mang_ket_qua_hien_thoi[52])]
                      }
        self.data2 = {'Kích thước ảnh': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên điểm': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
                      'Vị trí': ['{}'.format(self.mang_ket_qua_hien_thoi[53]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[54]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[55]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[56]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[57]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[58]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[59]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[60]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[61]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[62])],
                      'Kích thước ảnh ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên điểm ': ['11', '20', '21', '22', '23', '24', '25', '26', '27', '28'],
                      'Vị trí ': ['{}'.format(self.mang_ket_qua_hien_thoi[63]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[64]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[65]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[66]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[67]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[68]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[69]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[70]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[71]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[72])],
                      'Kích thước ảnh  ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên điểm  ': ['29', '36', '37', '14', '15', '16', '17', '18', '19', '47'],
                      'Vị trí  ': ['{}'.format(self.mang_ket_qua_hien_thoi[73]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[74]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[75]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[76]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[77]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[78]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[79]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[80]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[81]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[82])],
                      'Kích thước ảnh   ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên điểm   ': ['48', '12', '13', '51', '52', '53', '54', '38', '39', '49'],
                      'Vị trí   ': ['{}'.format(self.mang_ket_qua_hien_thoi[83]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[84]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[85]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[86]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[87]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[88]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[89]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[90]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[91]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[92])],
                      'Kích thước ảnh    ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên điểm    ': ['50', '45', '46', '30', '31', '32', '33', '34', '35', '41'],
                      'Vị trí    ': ['{}'.format(self.mang_ket_qua_hien_thoi[93]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[94]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[95]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[96]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[97]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[98]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[99]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[100]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[101]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[102])],
                      'Kích thước ảnh     ': [kt_1, kt_1, kt_1],
                      'Tên điểm     ': ['42', '43', '44'],
                      'Vị trí     ': ['{}'.format(self.mang_ket_qua_hien_thoi[103]),
                                      '{}'.format(self.mang_ket_qua_hien_thoi[104]),
                                      '{}'.format(self.mang_ket_qua_hien_thoi[105])]
                      }
        self.data3 = {'Kích thước ảnh': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên kích thước': ['D1_p', 'D2_p', 'D3_p', 'D4_p', 'D5_p', 'D6_p', 'D7_p', 'C1_p', 'R1_p',
                                         'R2_p'],
                      'Giá trị (mm)': ['{}'.format(self.mang_kich_thuoc[0]),
                                       '{}'.format(self.mang_kich_thuoc[1]),
                                       '{}'.format(self.mang_kich_thuoc[2]),
                                       '{}'.format(self.mang_kich_thuoc[3]),
                                       '{}'.format(self.mang_kich_thuoc[4]),
                                       '{}'.format(self.mang_kich_thuoc[5]),
                                       '{}'.format(self.mang_kich_thuoc[6]),
                                       '{}'.format(self.mang_kich_thuoc[7]),
                                       '{}'.format(self.mang_kich_thuoc[8]),
                                       '{}'.format(self.mang_kich_thuoc[9])],
                      'Kích thước ảnh ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên kích thước ': ['R3_p', 'R4_p', 'R5_p', 'R6_p', 'D8_p', 'R7_p', 'R8_p', 'R9_p', 'Da5_p',
                                          'Da1_p'],
                      'Giá trị (mm) ': ['{}'.format(self.mang_kich_thuoc[10]),
                                        '{}'.format(self.mang_kich_thuoc[11]),
                                        '{}'.format(self.mang_kich_thuoc[12]),
                                        '{}'.format(self.mang_kich_thuoc[13]),
                                        '{}'.format(self.mang_kich_thuoc[14]),
                                        '{}'.format(self.mang_kich_thuoc[15]),
                                        '{}'.format(self.mang_kich_thuoc[16]),
                                        '{}'.format(self.mang_kich_thuoc[17]),
                                        '{}'.format(self.mang_kich_thuoc[18]),
                                        '{}'.format(self.mang_kich_thuoc[19])],
                      'Kích thước ảnh  ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên kích thước  ': ['Da2_p', 'Da3_p', 'Da7_p', 'Da6_p', 'Da4_p', 'V1_p', 'V2_p'],
                      'Giá trị (mm)  ': ['{}'.format(self.mang_kich_thuoc[20]),
                                         '{}'.format(self.mang_kich_thuoc[21]),
                                         '{}'.format(self.mang_kich_thuoc[22]),
                                         '{}'.format(self.mang_kich_thuoc[23]),
                                         '{}'.format(self.mang_kich_thuoc[24]),
                                         '{}'.format(self.mang_kich_thuoc[25]),
                                         '{}'.format(self.mang_kich_thuoc[26])],
                      }
        self.data4 = {'Kích thước ảnh': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên kích thước': ['D1_t', 'D2_t', 'D3_t', 'D4_t', 'D5_t', 'D6_t', 'D7_t', 'C1_t', 'R1_t',
                                         'R2_t'],
                      'Giá trị (mm) ': ['{}'.format(self.mang_kich_thuoc[27]),
                                        '{}'.format(self.mang_kich_thuoc[28]),
                                        '{}'.format(self.mang_kich_thuoc[29]),
                                        '{}'.format(self.mang_kich_thuoc[30]),
                                        '{}'.format(self.mang_kich_thuoc[31]),
                                        '{}'.format(self.mang_kich_thuoc[32]),
                                        '{}'.format(self.mang_kich_thuoc[33]),
                                        '{}'.format(self.mang_kich_thuoc[34]),
                                        '{}'.format(self.mang_kich_thuoc[35]),
                                        '{}'.format(self.mang_kich_thuoc[36])],
                      'Kích thước ảnh ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên kích thước ': ['R3_t', 'R4_t', 'R5_t', 'R6_t', 'D8_t', 'R7_t', 'R8_t', 'R9_t', 'Da5_t',
                                          'Da1_t'],
                      'Giá trị (mm)  ': ['{}'.format(self.mang_kich_thuoc[37]),
                                         '{}'.format(self.mang_kich_thuoc[38]),
                                         '{}'.format(self.mang_kich_thuoc[39]),
                                         '{}'.format(self.mang_kich_thuoc[40]),
                                         '{}'.format(self.mang_kich_thuoc[41]),
                                         '{}'.format(self.mang_kich_thuoc[42]),
                                         '{}'.format(self.mang_kich_thuoc[43]),
                                         '{}'.format(self.mang_kich_thuoc[44]),
                                         '{}'.format(self.mang_kich_thuoc[45]),
                                         '{}'.format(self.mang_kich_thuoc[46])],
                      'Kích thước ảnh  ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên kích thước  ': ['Da2_t', 'Da3_t', 'Da7_t', 'Da6_t', 'Da4_t', 'V1_t', 'V2_t'],
                      'Giá trị (mm)   ': ['{}'.format(self.mang_kich_thuoc[47]),
                                          '{}'.format(self.mang_kich_thuoc[48]),
                                          '{}'.format(self.mang_kich_thuoc[49]),
                                          '{}'.format(self.mang_kich_thuoc[50]),
                                          '{}'.format(self.mang_kich_thuoc[51]),
                                          '{}'.format(self.mang_kich_thuoc[52]),
                                          '{}'.format(self.mang_kich_thuoc[53])],
                      }

        self.progressBar.setValue(90)

        self.setData(self.bang_diem_tay_phai, self.data1)
        self.setData(self.bang_diem_tay_trai, self.data2)
        self.setData(self.bang_khoang_cach_tay_phai, self.data3)
        self.setData(self.bang_khoang_cach_tay_trai, self.data4)

        self.bang_diem_tay_phai.resizeColumnsToContents()
        self.bang_diem_tay_phai.resizeRowsToContents()
        self.bang_diem_tay_trai.resizeColumnsToContents()
        self.bang_diem_tay_trai.resizeRowsToContents()
        self.bang_khoang_cach_tay_phai.resizeColumnsToContents()
        self.bang_khoang_cach_tay_phai.resizeRowsToContents()
        self.bang_khoang_cach_tay_trai.resizeColumnsToContents()
        self.bang_khoang_cach_tay_trai.resizeRowsToContents()

        # set phan tram da xong
        self.progressBar.setValue(100)
        self.progressBar.setValue(0)

    def XemKQBT_clicked_V3(self):
        # print(self.cur_mang_nguong)
        mang_kq_calib = []

        for no_point, point in enumerate(self.mang_ket_qua_hien_thoi):
            # point_calib = cv2.undistortPoints(point, self.camera_matrix, self.dist, None, self.camera_matrix)
            point_calib = cv2.undistortPoints(point, self.camera_matrix, self.dist, P=self.camera_matrix)
            mang_kq_calib.append((point_calib[0][0][0], point_calib[0][0][1]))

        # print(self.camera_matrix)
        # print(self.dist)
        # print(self.camera_matrix)
        # print(mang_kq_calib)

        self.mang_kich_thuoc = TinhToanKhoangCach(mang_kq_calib, self.mm_tren_pixel)
        print(self.mang_kich_thuoc)
        anh_chup = []
        for i in range(1, 15):
            img = cv2.imread("{}/{}".format(self.cur_dir, i) + ".png")  # ban tay ngua
            anh_chup.append(img)

        # set phan tram da xong
        self.progressBar.setValue(50)

        img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, img13, img14 = anh_chup
        # for i, kq in enumerate(anh_chup):
        #     cv2.imwrite('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\result\\kq_img{}.png'.format(i), kq)

        kt_1 = '{}x{}'.format(img1.shape[0], img1.shape[1])
        kt_2 = '{}x{}'.format(img2.shape[0], img2.shape[1])
        kt_3 = '{}x{}'.format(img3.shape[0], img3.shape[1])
        kt_4 = '{}x{}'.format(img4.shape[0], img4.shape[1])
        kt_5 = '{}x{}'.format(img5.shape[0], img5.shape[1])
        kt_6 = '{}x{}'.format(img6.shape[0], img6.shape[1])
        kt_7 = '{}x{}'.format(img7.shape[0], img7.shape[1])
        kt_8 = '{}x{}'.format(img8.shape[0], img8.shape[1])
        kt_9 = '{}x{}'.format(img9.shape[0], img9.shape[1])
        kt_10 = '{}x{}'.format(img10.shape[0], img10.shape[1])
        kt_11 = '{}x{}'.format(img11.shape[0], img11.shape[1])
        kt_12 = '{}x{}'.format(img12.shape[0], img12.shape[1])
        kt_13 = '{}x{}'.format(img13.shape[0], img13.shape[1])
        kt_14 = '{}x{}'.format(img14.shape[0], img14.shape[1])

        self.data1 = {'Kích thước ảnh': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên điểm': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
                      'Vị trí': ['{}'.format(self.mang_ket_qua_hien_thoi[0]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[1]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[2]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[3]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[4]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[5]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[6]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[7]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[8]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[9])],
                      'Kích thước ảnh ': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên điểm ': ['11', '20', '21', '22', '23', '24', '25', '26', '27', '28'],
                      'Vị trí ': ['{}'.format(self.mang_ket_qua_hien_thoi[10]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[11]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[12]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[13]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[14]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[15]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[16]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[17]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[18]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[19])],
                      'Kích thước ảnh  ': [kt_1, kt_1, kt_1, kt_2, kt_2, kt_2, kt_2, kt_2, kt_2, kt_2],
                      'Tên điểm  ': ['29', '36', '37', '14', '15', '16', '17', '18', '19', '47'],
                      'Vị trí  ': ['{}'.format(self.mang_ket_qua_hien_thoi[20]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[21]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[22]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[23]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[24]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[25]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[26]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[27]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[28]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[29])],
                      'Kích thước ảnh   ': [kt_2, kt_3, kt_3, kt_3, kt_3, kt_3, kt_3, kt_4, kt_4, kt_4],
                      'Tên điểm   ': ['48', '12', '13', '51', '52', '53', '54', '38', '39', '49'],
                      'Vị trí   ': ['{}'.format(self.mang_ket_qua_hien_thoi[30]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[31]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[32]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[33]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[34]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[35]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[36]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[37]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[38]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[39])],
                      'Kích thước ảnh    ': [kt_4, kt_5, kt_5, kt_6, kt_6, kt_6, kt_6, kt_6, kt_6, kt_7],
                      'Tên điểm    ': ['50', '45', '46', '30', '31', '32', '33', '34', '35', '41'],
                      'Vị trí    ': ['{}'.format(self.mang_ket_qua_hien_thoi[40]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[41]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[42]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[43]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[44]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[45]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[46]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[47]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[48]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[49])],
                      'Kích thước ảnh     ': [kt_7, kt_7, kt_7],
                      'Tên điểm     ': ['42', '43', '44'],
                      'Vị trí     ': ['{}'.format(self.mang_ket_qua_hien_thoi[50]),
                                      '{}'.format(self.mang_ket_qua_hien_thoi[51]),
                                      '{}'.format(self.mang_ket_qua_hien_thoi[52])]
                      }
        self.data2 = {'Kích thước ảnh': [kt_8, kt_8, kt_8, kt_8, kt_8, kt_8, kt_8, kt_8, kt_8, kt_8],
                      'Tên điểm': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
                      'Vị trí': ['{}'.format(self.mang_ket_qua_hien_thoi[53]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[54]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[55]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[56]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[57]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[58]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[59]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[60]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[61]),
                                 '{}'.format(self.mang_ket_qua_hien_thoi[62])],
                      'Kích thước ảnh ': [kt_8, kt_8, kt_8, kt_8, kt_8, kt_8, kt_8, kt_8, kt_8, kt_8],
                      'Tên điểm ': ['11', '20', '21', '22', '23', '24', '25', '26', '27', '28'],
                      'Vị trí ': ['{}'.format(self.mang_ket_qua_hien_thoi[63]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[64]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[65]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[66]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[67]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[68]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[69]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[70]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[71]),
                                  '{}'.format(self.mang_ket_qua_hien_thoi[72])],
                      'Kích thước ảnh  ': [kt_8, kt_8, kt_8, kt_9, kt_9, kt_9, kt_9, kt_9, kt_9, kt_9],
                      'Tên điểm  ': ['29', '36', '37', '14', '15', '16', '17', '18', '19', '47'],
                      'Vị trí  ': ['{}'.format(self.mang_ket_qua_hien_thoi[73]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[74]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[75]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[76]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[77]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[78]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[79]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[80]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[81]),
                                   '{}'.format(self.mang_ket_qua_hien_thoi[82])],
                      'Kích thước ảnh   ': [kt_9, kt_10, kt_10, kt_10, kt_10, kt_10, kt_10, kt_11, kt_11, kt_11],
                      'Tên điểm   ': ['48', '12', '13', '51', '52', '53', '54', '38', '39', '49'],
                      'Vị trí   ': ['{}'.format(self.mang_ket_qua_hien_thoi[83]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[84]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[85]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[86]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[87]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[88]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[89]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[90]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[91]),
                                    '{}'.format(self.mang_ket_qua_hien_thoi[92])],
                      'Kích thước ảnh    ': [kt_11, kt_12, kt_12, kt_13, kt_13, kt_13, kt_13, kt_13, kt_13, kt_14],
                      'Tên điểm    ': ['50', '45', '46', '30', '31', '32', '33', '34', '35', '41'],
                      'Vị trí    ': ['{}'.format(self.mang_ket_qua_hien_thoi[93]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[94]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[95]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[96]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[97]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[98]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[99]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[100]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[101]),
                                     '{}'.format(self.mang_ket_qua_hien_thoi[102])],
                      'Kích thước ảnh     ': [kt_14, kt_14, kt_14],
                      'Tên điểm     ': ['42', '43', '44'],
                      'Vị trí     ': ['{}'.format(self.mang_ket_qua_hien_thoi[103]),
                                      '{}'.format(self.mang_ket_qua_hien_thoi[104]),
                                      '{}'.format(self.mang_ket_qua_hien_thoi[105])]
                      }
        self.data3 = {'Kích thước ảnh': [kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1, kt_1],
                      'Tên kích thước': ['D1_p', 'D2_p', 'D3_p', 'D4_p', 'D5_p', 'D6_p', 'D7_p', 'C1_p', 'R1_p',
                                         'R2_p'],
                      'Giá trị (mm)': ['{}'.format(self.mang_kich_thuoc[0]),
                                       '{}'.format(self.mang_kich_thuoc[1]),
                                       '{}'.format(self.mang_kich_thuoc[2]),
                                       '{}'.format(self.mang_kich_thuoc[3]),
                                       '{}'.format(self.mang_kich_thuoc[4]),
                                       '{}'.format(self.mang_kich_thuoc[5]),
                                       '{}'.format(self.mang_kich_thuoc[6]),
                                       '{}'.format(self.mang_kich_thuoc[7]),
                                       '{}'.format(self.mang_kich_thuoc[8]),
                                       '{}'.format(self.mang_kich_thuoc[9])],
                      'Kích thước ảnh ': [kt_1, kt_1, kt_1, kt_3, kt_3, kt_3, kt_2, kt_2, kt_2, kt_2],
                      'Tên kích thước ': ['R3_p', 'R4_p', 'R5_p', 'b_p', 'D8_p', 'd_p', 'R7_p', 'R8_p', 'R9_p',
                                          'Da5_p'],
                      'Giá trị (mm) ': ['{}'.format(self.mang_kich_thuoc[10]),
                                        '{}'.format(self.mang_kich_thuoc[11]),
                                        '{}'.format(self.mang_kich_thuoc[12]),
                                        '{}'.format(self.mang_kich_thuoc[13]),
                                        '{}'.format(self.mang_kich_thuoc[14]),
                                        '{}'.format(self.mang_kich_thuoc[15]),
                                        '{}'.format(self.mang_kich_thuoc[16]),
                                        '{}'.format(self.mang_kich_thuoc[17]),
                                        '{}'.format(self.mang_kich_thuoc[18]),
                                        '{}'.format(self.mang_kich_thuoc[19])],
                      'Kích thước ảnh  ': [kt_7, kt_7, kt_6, kt_6, kt_6, kt_4, kt_4, kt_5],
                      'Tên kích thước  ': ['Da1_p', 'Da2_p', 'Da3_p', 'Da7_p', 'Da6_p', 'a_p', 'c_p', 'Da4_p'],
                      'Giá trị (mm)  ': ['{}'.format(self.mang_kich_thuoc[20]),
                                         '{}'.format(self.mang_kich_thuoc[21]),
                                         '{}'.format(self.mang_kich_thuoc[22]),
                                         '{}'.format(self.mang_kich_thuoc[23]),
                                         '{}'.format(self.mang_kich_thuoc[24]),
                                         '{}'.format(self.mang_kich_thuoc[25]),
                                         '{}'.format(self.mang_kich_thuoc[26]),
                                         '{}'.format(self.mang_kich_thuoc[27])],
                      }
        self.data4 = {'Kích thước ảnh': [kt_8, kt_8, kt_8, kt_8, kt_8, kt_8, kt_8, kt_8, kt_8, kt_8],
                      'Tên kích thước': ['D1_t', 'D2_t', 'D3_t', 'D4_t', 'D5_t', 'D6_t', 'D7_t', 'C1_t', 'R1_t',
                                         'R2_t'],
                      'Giá trị (mm) ': ['{}'.format(self.mang_kich_thuoc[28]),
                                        '{}'.format(self.mang_kich_thuoc[29]),
                                        '{}'.format(self.mang_kich_thuoc[30]),
                                        '{}'.format(self.mang_kich_thuoc[31]),
                                        '{}'.format(self.mang_kich_thuoc[32]),
                                        '{}'.format(self.mang_kich_thuoc[33]),
                                        '{}'.format(self.mang_kich_thuoc[34]),
                                        '{}'.format(self.mang_kich_thuoc[35]),
                                        '{}'.format(self.mang_kich_thuoc[36]),
                                        '{}'.format(self.mang_kich_thuoc[37])],
                      'Kích thước ảnh ': [kt_8, kt_8, kt_8, kt_10, kt_10, kt_10, kt_9, kt_9, kt_9, kt_9],
                      'Tên kích thước ': ['R3_t', 'R4_t', 'R5_t', 'b_t', 'D8_t', 'd_t', 'R7_t', 'R8_t', 'R9_t',
                                          'Da5_t'],
                      'Giá trị (mm)  ': ['{}'.format(self.mang_kich_thuoc[38]),
                                         '{}'.format(self.mang_kich_thuoc[39]),
                                         '{}'.format(self.mang_kich_thuoc[40]),
                                         '{}'.format(self.mang_kich_thuoc[41]),
                                         '{}'.format(self.mang_kich_thuoc[42]),
                                         '{}'.format(self.mang_kich_thuoc[43]),
                                         '{}'.format(self.mang_kich_thuoc[44]),
                                         '{}'.format(self.mang_kich_thuoc[45]),
                                         '{}'.format(self.mang_kich_thuoc[46]),
                                         '{}'.format(self.mang_kich_thuoc[47])],
                      'Kích thước ảnh  ': [kt_14, kt_14, kt_13, kt_13, kt_13, kt_11, kt_11, kt_12],
                      'Tên kích thước  ': ['Da1_t', 'Da2_t', 'Da3_t', 'Da7_t', 'Da6_t', 'a_t', 'c_t', 'Da4_t'],
                      'Giá trị (mm)   ': ['{}'.format(self.mang_kich_thuoc[48]),
                                          '{}'.format(self.mang_kich_thuoc[49]),
                                          '{}'.format(self.mang_kich_thuoc[50]),
                                          '{}'.format(self.mang_kich_thuoc[51]),
                                          '{}'.format(self.mang_kich_thuoc[52]),
                                          '{}'.format(self.mang_kich_thuoc[53]),
                                          '{}'.format(self.mang_kich_thuoc[54]),
                                          '{}'.format(self.mang_kich_thuoc[55])],
                      }

        self.progressBar.setValue(90)

        self.setData(self.bang_diem_tay_phai, self.data1)
        self.setData(self.bang_diem_tay_trai, self.data2)
        self.setData(self.bang_khoang_cach_tay_phai, self.data3)
        self.setData(self.bang_khoang_cach_tay_trai, self.data4)

        self.bang_diem_tay_phai.resizeColumnsToContents()
        self.bang_diem_tay_phai.resizeRowsToContents()
        self.bang_diem_tay_trai.resizeColumnsToContents()
        self.bang_diem_tay_trai.resizeRowsToContents()
        self.bang_khoang_cach_tay_phai.resizeColumnsToContents()
        self.bang_khoang_cach_tay_phai.resizeRowsToContents()
        self.bang_khoang_cach_tay_trai.resizeColumnsToContents()
        self.bang_khoang_cach_tay_trai.resizeRowsToContents()

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
                self.anhMauLB.setPixmap(QPixmap(u"../handsample1/" + str(self.index) + ".jpg"))
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

    def Function(self, img, index, nguong):
        status = False
        mang_diem = []
        img_kq = []
        if index == 1:
            try:
                mang_diem, img_kq = NguaBanTayPhai(img, nguong)
            except:
                print('Loi{}'.format(index))

            if len(mang_diem) != 0:
                status = True
                # print('diem_tren_tay_phai_ngua')
                # print(mang_diem)
                cv2.imshow('diem_tren_tay_phai_ngua', img_kq)
                cv2.waitKey(0)
            else:
                status = False
        if index == 2:
            try:
                mang_diem, img_kq = UpBanTayPhai(img, nguong)
            except:
                print('Loi{}'.format(index))

            if len(mang_diem) != 0:
                status = True
                # print('diem_tren_tay_phai_up')
                # print(mang_diem)
                cv2.imshow('diem_tren_tay_phai_up', img_kq)
                cv2.waitKey(0)
            else:
                status = False
        if index == 3:
            try:
                mang_diem, img_kq = NamTayPhai1(img, nguong)
            except:
                print('Loi{}'.format(index))

            if len(mang_diem) != 0:
                status = True
                # print('diem_nam_tay_phai_1')
                # print(mang_diem)
                cv2.imshow('diem_nam_tay_phai_1', img_kq)
                cv2.waitKey(0)
            else:
                status = False
        if index == 4:
            try:
                mang_diem, img_kq = NamTayPhai2(img, nguong)
            except:
                print('Loi{}'.format(index))

            if len(mang_diem) != 0:
                status = True
                # print('diem_nam_tay_phai_2')
                # print(mang_diem)
                cv2.imshow('diem_nam_tay_phai_2', img_kq)
                cv2.waitKey(0)
            else:
                status = False
        if index == 5:
            try:
                mang_diem, img_kq = NgonTroPhai(img, nguong)
            except:
                print('Loi{}'.format(index))

            if len(mang_diem) != 0:
                status = True
                # print('diem_ngon_tro_phai')
                # print(mang_diem)
                cv2.imshow('diem_ngon_tro_phai', img_kq)
                cv2.waitKey(0)
            else:
                status = False
        if index == 6:
            try:
                mang_diem, img_kq = MuTayPhai(img, nguong)
            except:
                print('Loi{}'.format(index))

            if len(mang_diem) != 0:
                status = True
                # print('diem_mu_tay_phai')
                # print(mang_diem)
                cv2.imshow('diem_mu_tay_phai', img_kq)
                cv2.waitKey(0)
            else:
                status = False
        if index == 7:
            try:
                mang_diem, img_kq = HaiNgonTayPhai(img, nguong)
            except:
                print('Loi{}'.format(index))

            if len(mang_diem) != 0:
                status = True
                # print('diem_hai_ngon_tay_phai')
                # print(mang_diem)
                cv2.imshow('diem_hai_ngon_tay_phai', img_kq)
                cv2.waitKey(0)
            else:
                status = False
        if index == 8:
            try:
                mang_diem, img_kq = NguaBanTayPhai(img, nguong)
            except:
                print('Loi{}'.format(index))

            if len(mang_diem) != 0:
                status = True
                # print('diem_tren_tay_ngua_trai')
                # print(mang_diem)
                cv2.imshow('diem_tren_tay_ngua_trai', img_kq)
                cv2.waitKey(0)
            else:
                status = False
        if index == 9:
            try:
                mang_diem, img_kq = UpBanTayPhai(img, nguong)
            except:
                print('Loi{}'.format(index))

            if len(mang_diem) != 0:
                status = True
                # print('diem_tren_tay_trai_up')
                # print(mang_diem)
                cv2.imshow('diem_tren_tay_trai_up', img_kq)
                cv2.waitKey(0)
            else:
                status = False
        if index == 10:
            try:
                mang_diem, img_kq = NamTayPhai1(img, nguong)
            except:
                print('Loi{}'.format(index))

            if len(mang_diem) != 0:
                status = True
                # print('diem_nam_tay_trai_1')
                # print(mang_diem)
                cv2.imshow('diem_nam_tay_trai_1', img_kq)
                cv2.waitKey(0)
            else:
                status = False
        if index == 11:
            try:
                mang_diem, img_kq = NamTayPhai2(img, nguong)
            except:
                print('Loi{}'.format(index))

            if len(mang_diem) != 0:
                status = True
                # print('diem_nam_tay_trai_2')
                # print(mang_diem)
                cv2.imshow('diem_nam_tay_trai_2', img_kq)
                cv2.waitKey(0)
            else:
                status = False
        if index == 12:
            try:
                mang_diem, img_kq = NgonTroPhai(img, nguong)
            except:
                print('Loi{}'.format(index))

            if len(mang_diem) != 0:
                status = True
                # print('diem_ngon_tro_trai')
                # print(mang_diem)
                cv2.imshow('diem_ngon_tro_trai', img_kq)
                cv2.waitKey(0)
            else:
                status = False
        if index == 13:
            try:
                mang_diem, img_kq = MuTayPhai(img, nguong)
            except:
                print('Loi{}'.format(index))

            if len(mang_diem) != 0:
                status = True
                # print('diem_mu_tay_trai')
                # print(mang_diem)
                cv2.imshow('diem_mu_tay_trai', img_kq)
                cv2.waitKey(0)
            else:
                status = False
        if index == 14:
            try:
                mang_diem, img_kq = HaiNgonTayPhai(img, nguong)
            except:
                print('Loi{}'.format(index))

            if len(mang_diem) != 0:
                status = True
                # print('diem_tren_tay_phai_up')
                # print(mang_diem)
                cv2.imshow('diem_tren_tay_phai_up', img_kq)
                cv2.waitKey(0)
            else:
                status = False
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
        return status, mang_diem, img_kq

    def TraVeDongCuoi(self):
        # sheets_names = pd.ExcelFile('du_lieu.xlsx').sheet_names ==> return: ['Page1']
        sheet = pd.read_excel('du_lieu.xlsx', sheet_name='Page1')
        L = pd.read_excel('du_lieu.xlsx',
                          sheet_name='Page1',
                          usecols='L')
        print(len(L), L)
        stt_cuoi = 0
        for col in L:
            while stt_cuoi < len(L):
                if pd.isna(L[col].values[stt_cuoi]):
                    break
                stt_cuoi = stt_cuoi + 1
        dong_cuoi = int(stt_cuoi - 1 + 2)
        return dong_cuoi

    def LuuBT_clicked(self):
        book = openpyxl.load_workbook('du_lieu.xlsx')
        sheet = book.active

        L = pd.read_excel('du_lieu.xlsx',
                          sheet_name='Page1',
                          usecols='L')
        # print(len(L), L)
        stt_cuoi = 0
        for col in L:
            while stt_cuoi < len(L):
                if pd.isna(L[col].values[stt_cuoi]):
                    break
                stt_cuoi = stt_cuoi + 1
        dong_cuoi = int(stt_cuoi - 1 + 2)

        # print(dong_cuoi)

        dong_tren = int(dong_cuoi + 1)
        dong_duoi = int(dong_tren + 1)

        # sheet['L{}'.format(dong_tren)] = 1.2
        # sheet['L{}'.format(dong_duoi)] = 3.4

        vi_tri_ten_1 = ''.join(['B', str(dong_tren)])
        sheet[vi_tri_ten_1] = str(self.nameTE.toPlainText())
        vi_tri_ten_2 = ''.join(['B', str(dong_duoi)])
        sheet[vi_tri_ten_2] = str(self.nameTE.toPlainText())

        vi_tri_D1_p = ''.join(['D', str(dong_tren)])
        vi_tri_D2_p = ''.join(['E', str(dong_tren)])
        vi_tri_D3_p = ''.join(['F', str(dong_tren)])
        vi_tri_D4_p = ''.join(['G', str(dong_tren)])
        vi_tri_D5_p = ''.join(['H', str(dong_tren)])
        vi_tri_D6_p = ''.join(['I', str(dong_tren)])
        vi_tri_D7_p = ''.join(['J', str(dong_tren)])
        vi_tri_D8_p = ''.join(['K', str(dong_tren)])
        vi_tri_R1_p = ''.join(['L', str(dong_tren)])
        vi_tri_R2_p = ''.join(['M', str(dong_tren)])
        vi_tri_R3_p = ''.join(['N', str(dong_tren)])
        vi_tri_R4_p = ''.join(['O', str(dong_tren)])
        vi_tri_R5_p = ''.join(['P', str(dong_tren)])
        vi_tri_R6_p = ''.join(['Q', str(dong_tren)])
        vi_tri_R7_p = ''.join(['R', str(dong_tren)])
        vi_tri_R8_p = ''.join(['S', str(dong_tren)])
        vi_tri_R9_p = ''.join(['T', str(dong_tren)])
        vi_tri_Da1_p = ''.join(['U', str(dong_tren)])
        vi_tri_Da2_p = ''.join(['V', str(dong_tren)])
        vi_tri_Da3_p = ''.join(['W', str(dong_tren)])
        vi_tri_Da4_p = ''.join(['X', str(dong_tren)])
        vi_tri_Da5_p = ''.join(['Y', str(dong_tren)])
        vi_tri_Da6_p = ''.join(['Z', str(dong_tren)])
        vi_tri_Da7_p = ''.join(['AA', str(dong_tren)])
        vi_tri_V1_p = ''.join(['AB', str(dong_tren)])
        vi_tri_V2_p = ''.join(['AC', str(dong_tren)])
        vi_tri_C1_p = ''.join(['AD', str(dong_tren)])

        vi_tri_D1_t = ''.join(['D', str(dong_duoi)])
        vi_tri_D2_t = ''.join(['E', str(dong_duoi)])
        vi_tri_D3_t = ''.join(['F', str(dong_duoi)])
        vi_tri_D4_t = ''.join(['G', str(dong_duoi)])
        vi_tri_D5_t = ''.join(['H', str(dong_duoi)])
        vi_tri_D6_t = ''.join(['I', str(dong_duoi)])
        vi_tri_D7_t = ''.join(['J', str(dong_duoi)])
        vi_tri_D8_t = ''.join(['K', str(dong_duoi)])
        vi_tri_R1_t = ''.join(['L', str(dong_duoi)])
        vi_tri_R2_t = ''.join(['M', str(dong_duoi)])
        vi_tri_R3_t = ''.join(['N', str(dong_duoi)])
        vi_tri_R4_t = ''.join(['O', str(dong_duoi)])
        vi_tri_R5_t = ''.join(['P', str(dong_duoi)])
        vi_tri_R6_t = ''.join(['Q', str(dong_duoi)])
        vi_tri_R7_t = ''.join(['R', str(dong_duoi)])
        vi_tri_R8_t = ''.join(['S', str(dong_duoi)])
        vi_tri_R9_t = ''.join(['T', str(dong_duoi)])
        vi_tri_Da1_t = ''.join(['U', str(dong_duoi)])
        vi_tri_Da2_t = ''.join(['V', str(dong_duoi)])
        vi_tri_Da3_t = ''.join(['W', str(dong_duoi)])
        vi_tri_Da4_t = ''.join(['X', str(dong_duoi)])
        vi_tri_Da5_t = ''.join(['Y', str(dong_duoi)])
        vi_tri_Da6_t = ''.join(['Z', str(dong_duoi)])
        vi_tri_Da7_t = ''.join(['AA', str(dong_duoi)])
        vi_tri_V1_t = ''.join(['AB', str(dong_duoi)])
        vi_tri_V2_t = ''.join(['AC', str(dong_duoi)])
        vi_tri_C1_t = ''.join(['AD', str(dong_duoi)])

        sheet[vi_tri_D1_p] = str(self.mang_kich_thuoc[0])
        sheet[vi_tri_D2_p] = str(self.mang_kich_thuoc[1])
        sheet[vi_tri_D3_p] = str(self.mang_kich_thuoc[2])
        sheet[vi_tri_D4_p] = str(self.mang_kich_thuoc[3])
        sheet[vi_tri_D5_p] = str(self.mang_kich_thuoc[4])
        sheet[vi_tri_D6_p] = str(self.mang_kich_thuoc[5])
        sheet[vi_tri_D7_p] = str(self.mang_kich_thuoc[6])
        sheet[vi_tri_D8_p] = str(self.mang_kich_thuoc[14])
        sheet[vi_tri_R1_p] = str(self.mang_kich_thuoc[8])
        sheet[vi_tri_R2_p] = str(self.mang_kich_thuoc[9])
        sheet[vi_tri_R3_p] = str(self.mang_kich_thuoc[10])
        sheet[vi_tri_R4_p] = str(self.mang_kich_thuoc[11])
        sheet[vi_tri_R5_p] = str(self.mang_kich_thuoc[12])
        sheet[vi_tri_R6_p] = str(self.mang_kich_thuoc[13])
        sheet[vi_tri_R7_p] = str(self.mang_kich_thuoc[15])
        sheet[vi_tri_R8_p] = str(self.mang_kich_thuoc[16])
        sheet[vi_tri_R9_p] = str(self.mang_kich_thuoc[17])
        sheet[vi_tri_Da1_p] = str(self.mang_kich_thuoc[19])
        sheet[vi_tri_Da2_p] = str(self.mang_kich_thuoc[20])
        sheet[vi_tri_Da3_p] = str(self.mang_kich_thuoc[21])
        sheet[vi_tri_Da4_p] = str(self.mang_kich_thuoc[24])
        sheet[vi_tri_Da5_p] = str(self.mang_kich_thuoc[18])
        sheet[vi_tri_Da6_p] = str(self.mang_kich_thuoc[23])
        sheet[vi_tri_Da7_p] = str(self.mang_kich_thuoc[22])
        sheet[vi_tri_V1_p] = str(self.mang_kich_thuoc[25])
        sheet[vi_tri_V2_p] = str(self.mang_kich_thuoc[26])
        sheet[vi_tri_C1_p] = str(self.mang_kich_thuoc[7])

        sheet[vi_tri_D1_t] = str(self.mang_kich_thuoc[27])
        sheet[vi_tri_D2_t] = str(self.mang_kich_thuoc[28])
        sheet[vi_tri_D3_t] = str(self.mang_kich_thuoc[29])
        sheet[vi_tri_D4_t] = str(self.mang_kich_thuoc[30])
        sheet[vi_tri_D5_t] = str(self.mang_kich_thuoc[31])
        sheet[vi_tri_D6_t] = str(self.mang_kich_thuoc[32])
        sheet[vi_tri_D7_t] = str(self.mang_kich_thuoc[33])
        sheet[vi_tri_D8_t] = str(self.mang_kich_thuoc[41])
        sheet[vi_tri_R1_t] = str(self.mang_kich_thuoc[35])
        sheet[vi_tri_R2_t] = str(self.mang_kich_thuoc[36])
        sheet[vi_tri_R3_t] = str(self.mang_kich_thuoc[37])
        sheet[vi_tri_R4_t] = str(self.mang_kich_thuoc[38])
        sheet[vi_tri_R5_t] = str(self.mang_kich_thuoc[39])
        sheet[vi_tri_R6_t] = str(self.mang_kich_thuoc[40])
        sheet[vi_tri_R7_t] = str(self.mang_kich_thuoc[42])
        sheet[vi_tri_R8_t] = str(self.mang_kich_thuoc[43])
        sheet[vi_tri_R9_t] = str(self.mang_kich_thuoc[44])
        sheet[vi_tri_Da1_t] = str(self.mang_kich_thuoc[46])
        sheet[vi_tri_Da2_t] = str(self.mang_kich_thuoc[47])
        sheet[vi_tri_Da3_t] = str(self.mang_kich_thuoc[48])
        sheet[vi_tri_Da4_t] = str(self.mang_kich_thuoc[51])
        sheet[vi_tri_Da5_t] = str(self.mang_kich_thuoc[45])
        sheet[vi_tri_Da6_t] = str(self.mang_kich_thuoc[50])
        sheet[vi_tri_Da7_t] = str(self.mang_kich_thuoc[49])
        sheet[vi_tri_V1_t] = str(self.mang_kich_thuoc[52])
        sheet[vi_tri_V2_t] = str(self.mang_kich_thuoc[53])
        sheet[vi_tri_C1_t] = str(self.mang_kich_thuoc[34])

        book.save('du_lieu.xlsx')

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
