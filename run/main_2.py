from MyLib import *
from Math import *

if __name__ == "__main__":
    # img = cv2.imread('27-04-2022-13-08-01.png')  # nguoc hand

    # img = cv2.imread('1.png')
    # img = cv2.imread('26-04-2022-23-10-41.png') # left hand
    # img = cv2.imread('27-04-2022-01-46-07.png') # left hand
    # img = cv2.imread('27-04-2022-01-46-07.png') # left hand

    # img = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\captured\\old\\13-05-2022-18-00-06.png')  # left hand
    img = cv2.imread('nam_tay.jpg')  # ban tay ngua
    # img = cv2.imread('13-05-2022-18-00-03.png')
    # img = cv2.imread('tay_up.jpg')  # ban tay ngua

    img = imutils.resize(img, height=720)
    mang_diem_moc, annotated_image, handType, image = TimDiemMoc(img)
    if mang_diem_moc[0][1] < mang_diem_moc[12][1]:
        print('Ảnh bị ngược')
        img = cv2.rotate(img, cv2.ROTATE_180)
        mang_diem_moc, annotated_image, handType, image = TimDiemMoc(img)
    # diem 38 39 50 49

    diem_so_38, diem_so_39, diem_so_50, diem_so_49 = TimDiemSo_38_39_49_50_tay_phai(mang_diem_moc[0], img)

    cv2.circle(img, diem_so_38, 2, (255, 0, 0), -1)
    cv2.putText(img, '38',
                diem_so_38, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.circle(img, diem_so_39, 2, (255, 0, 0), -1)
    cv2.putText(img, '39',
                diem_so_39, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.circle(img, diem_so_50, 2, (255, 0, 0), -1)
    cv2.putText(img, '50',
                diem_so_50, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.circle(img, diem_so_49, 2, (255, 0, 0), -1)
    cv2.putText(img, '49',
                diem_so_49, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.imshow('img', img)
    cv2.waitKey(0)

