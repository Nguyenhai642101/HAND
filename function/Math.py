import math
import time

import keyboard
import mediapipe as mp
import cv2
import imutils
import numpy as np


def tim_trung_diem(d1, d2):
    x_td = (d1[0] + d2[0]) // 2
    y_td = (d1[1] + d2[1]) // 2
    d_td = (x_td, y_td)

    return d_td


def giao_diem(d1, d2, m1, m2):
    y1 = d1[1]
    y2 = d2[1]
    x1 = d1[0]
    x2 = d2[0]
    if (x2 - x1) != 0:
        a1 = (y2 - y1) / (x2 - x1)
        b1 = y1 - (y2 - y1) * x1 / (x2 - x1)
    x3 = m1[0]
    x4 = m2[0]
    y3 = m1[1]
    y4 = m2[1]
    if (x4 - x3) != 0:
        a2 = (y4 - y3) / (x4 - x3)
        b2 = y3 - (y4 - y3) * x3 / (x4 - x3)
    if (x2 - x1) != 0 and (x4 - x3) != 0:
        x = (b2 - b1) / (a1 - a2)
        y = a1 * x + b1
    if (x2 - x1) == 0:
        x = x1
        y = a2 * x + b2
    if (x4 - x3) == 0:
        x = x3
        y = a1 * x + b1

    return round(x), round(y)


def ve_dt_dung(d1, d2, image, image1):
    for i_y in range(d1[1], 0, -1):
        x = (i_y - d1[1]) * (d2[0] - d1[0]) // (d2[1] - d1[1]) + d1[0]
        (B, G, R) = image1[i_y, x]
        if (B, G, R) == (240, 0, 159):
            p_tren = (x, i_y)
            break
        image[i_y, x] = (0, 255, 0)

    return p_tren


def ve_dt_vuong_voi_dt_dung(d1, d2, diem_di_qua, image, image1, w):
    b = diem_di_qua[1] + ((d2[0] - d1[0]) * diem_di_qua[0]) // (d2[1] - d1[1])
    for i_x in range(diem_di_qua[0], 0, -1):
        y = (-(d2[0] - d1[0]) * i_x) // (d2[1] - d1[1]) + b
        (B, G, R) = image1[y, i_x]
        if (B, G, R) == (240, 0, 159):
            rong_1 = (i_x, y)
            break
        image[y, i_x] = (0, 255, 0)
    for i_x in range(diem_di_qua[0], w, 1):
        y = (-(d2[0] - d1[0]) * i_x) // (d2[1] - d1[1]) + b
        (B, G, R) = image1[y, i_x]
        if (B, G, R) == (240, 0, 159):
            rong_2 = (i_x, y)
            break
        image[y, i_x] = (0, 255, 0)

    return rong_1, rong_2


def TimPhuongTrinhDuongThangVuongGocVoiDuongThang(diem_A, diem_B, diem_C):
    xA = diem_A[0]
    xB = diem_B[0]
    xC = diem_C[0]
    yA = diem_A[1]
    yB = diem_B[1]
    yC = diem_C[1]

    # vector phap tuyen n
    n = (xA - xB, yA - yB)

    # duong thang vuong goc ax + by +c = 0
    a = n[0]
    b = n[1]
    c = - a * xC - b * yC

    return a, b, c


def TimPhuongTrinhDuongThangBietHaiDiem(diem_A, diem_B):
    xA = diem_A[0]
    xB = diem_B[0]
    yA = diem_A[1]
    yB = diem_B[1]

    # vector chỉ phuong u = (a,b)
    u = (xA - xB, yA - yB)
    # vector phap tuyen n = (-b,a)
    n = (yB - yA, xA - xB)

    # duong thang vuong goc ax + by +c = 0
    a = n[0]
    b = n[1]
    c = - a * xA - b * yA

    return a, b, c


def TimGiaoDiemHaiDuongThang(d1, d2):
    a1 = d1[0]
    b1 = d1[1]
    c1 = d1[2]
    a2 = d2[0]
    b2 = d2[1]
    c2 = d2[2]
    x, y = 0, 0
    try:
        if (a2 * b1 - b2 * a1) == 0:
            print('Ko tim duoc giao diem')
        else:
            if (a1 == b2 and a1 == 0):
                y = int(-c1 / b1)
                x = int(-c2 / a2)
            else:
                if (a2 == b1 and a2 == 0):
                    x = int(-c1 / a1)
                    y = int(-c2 / b2)
                else:
                    y = (a1 * c2 - a2 * c1) / (a2 * b1 - b2 * a1)
                    x = (b1 * c2 - b2 * c1) / (a1 * b2 - b1 * a2)
                    # x = (-c1 - b1 * y) / a1
        y = int(y)
        x = int(x)
    except:
        print('Khong the tim thay giao diem')
    return x, y


def VeDuongThangDiQuaHaiDiem(img, diem_A, diem_B):
    cv2.line(img, diem_A, diem_B, color=(0, 255, 0), thickness=1)


def rotationAngleInDegrees(image, angleInDegrees):
    h, w = image.shape[:2]
    img_c = (w / 2, h / 2)

    rot = cv2.getRotationMatrix2D(img_c, angleInDegrees, 1)
    # print(rot)
    rad = math.radians(angleInDegrees)
    sin = math.sin(rad)
    cos = math.cos(rad)
    b_w = int((h * abs(sin)) + (w * abs(cos)))
    b_h = int((h * abs(cos)) + (w * abs(sin)))

    rot[0, 2] += ((b_w / 2) - img_c[0])
    rot[1, 2] += ((b_h / 2) - img_c[1])

    outImg = cv2.warpAffine(image, rot, (b_w, b_h), flags=cv2.INTER_LINEAR)
    return outImg, rot, h, w


def rotationAngleInDegreesV1(image, angleInDegrees):
    h, w = image.shape[:2]
    img_c = (w / 2, h / 2)

    rot = cv2.getRotationMatrix2D(img_c, angleInDegrees, 1)
    outImg = cv2.warpAffine(image, rot, (h, w), flags=cv2.INTER_LINEAR)
    return outImg, rot


def rotationAngleInDegreesV2(image, angleInDegrees):
    h, w = image.shape[:2]
    img_c = (w / 2, h / 2)

    rot = cv2.getRotationMatrix2D(img_c, angleInDegrees, 1)
    # print(rot)
    rad = math.radians(angleInDegrees)
    sin = math.sin(rad)
    cos = math.cos(rad)
    b_w = int((h * abs(sin)) + (w * abs(cos)))
    b_h = int((h * abs(cos)) + (w * abs(sin)))

    rot[0, 2] += ((b_w / 2) - img_c[0])
    rot[1, 2] += ((b_h / 2) - img_c[1])

    outImg = cv2.warpAffine(image, rot, (b_w, b_h), flags=cv2.INTER_LINEAR)
    return outImg, rot, h, w


def rotationAngleInDegreesBack(image, angleInDegrees, h, w):
    hh, ww = image.shape[:2]
    img_c = (ww / 2, hh / 2)

    rot = cv2.getRotationMatrix2D(img_c, angleInDegrees, 1)
    # print(rot)
    rad = math.radians(angleInDegrees)
    sin = math.sin(rad)
    cos = math.cos(rad)
    b_w = int((h * abs(sin)) + (w * abs(cos)))
    b_h = int((h * abs(cos)) + (w * abs(sin)))

    rot[0, 2] -= ((b_w / 2) - w / 2)
    rot[1, 2] -= ((b_h / 2) - h / 2)

    outImg = cv2.warpAffine(image, rot, (w, h), flags=cv2.INTER_LINEAR)
    return outImg, rot


def TimKhoangCachHaiDiem(diem_A, diem_B):
    return round(math.sqrt(math.pow(diem_A[0] - diem_B[0], 2) + math.pow(diem_A[1] - diem_B[1], 2)))


def TimKhoangCachTuDiemDenDuongThang(diem, d):
    u, v = diem
    a, b, c = d
    return round(abs(a * u + b * v + c) / (math.sqrt(a ** 2 + b ** 2)))
