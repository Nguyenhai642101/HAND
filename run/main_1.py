import cv2
import imutils

from MyLib import *
from Math import *

if __name__ == "__main__":
    # img = cv2.imread('27-04-2022-13-08-01.png')  # nguoc hand

    # img = cv2.imread('1.png')
    # img = cv2.imread('26-04-2022-23-10-41.png') # left hand
    # img = cv2.imread('27-04-2022-01-46-07.png') # left hand
    # img = cv2.imread('27-04-2022-01-46-07.png') # left hand

    # img = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\captured\\old\\13-05-2022-18-00-06.png')  # left hand
    img = cv2.imread('nam_tay_2.jpg')  # ban tay ngua
    # img = cv2.imread('13-05-2022-18-00-03.png')
    # img = cv2.imread('tay_up.jpg')  # ban tay ngua

    img = imutils.resize(img, height=720)
    mang_diem_moc, annotated_image, handType, image = TimDiemMoc(img)
    if mang_diem_moc[0][1] < mang_diem_moc[12][1]:
        print('Ảnh bị ngược')
        img = cv2.rotate(img, cv2.ROTATE_180)
        mang_diem_moc, annotated_image, handType, image = TimDiemMoc(img)
    # diem 12, 53, 54, 51, 52
    mang_diem_12 = mang_diem_moc[0]
    diem_so_12, diem_so_53, diem_so_54, diem_so_51, diem_so_52 = TimDiemSo_12_53_54_51_52(mang_diem_moc[0], image)

    cv2.circle(img, diem_so_12, 2, (255, 0, 0), -1)
    cv2.putText(img, '12',
                diem_so_12, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.circle(img, diem_so_53, 2, (255, 0, 0), -1)
    cv2.putText(img, '53',
                diem_so_53, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.circle(img, diem_so_54, 2, (255, 0, 0), -1)
    cv2.putText(img, '54',
                diem_so_54, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.circle(img, diem_so_51, 2, (255, 0, 0), -1)
    cv2.putText(img, '51',
                diem_so_51, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.circle(img, diem_so_52, 2, (255, 0, 0), -1)
    cv2.putText(img, '52',
                diem_so_52, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # diem 13
    mang_diem_moc_0_phay = (mang_diem_moc[0][0] + 10, mang_diem_moc[0][1])
    a0, b0, c0 = TimPhuongTrinhDuongThangBietHaiDiem(mang_diem_moc[0], mang_diem_moc_0_phay)
    a1, b1, c1 = TimPhuongTrinhDuongThangVuongGocVoiDuongThang(mang_diem_moc[0], mang_diem_moc_0_phay, diem_so_12)

    d0 = (a0, b0, c0)
    d1 = (a1, b1, c1)

    diem_so_13 = TimGiaoDiemHaiDuongThang(d0, d1)

    cv2.circle(img, diem_so_13, 2, (255, 0, 0), -1)
    cv2.putText(img, '13',
                diem_so_13, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.imwrite('img.png', annotated_image)
    cv2.imshow('img', img)

    cv2.waitKey(0)
