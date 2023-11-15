from MyLib import *
from Math import *

if __name__ == "__main__":
    # img = cv2.imread('27-04-2022-13-08-01.png')  # nguoc hand

    # img = cv2.imread('1.png')
    # img = cv2.imread('26-04-2022-23-10-41.png') # left hand
    # img = cv2.imread('27-04-2022-01-46-07.png') # left hand
    # img = cv2.imread('27-04-2022-01-46-07.png') # left hand

    # img = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\captured\\old\\13-05-2022-18-00-06.png')  # left hand
    img = cv2.imread('ngon_tro.jpg')  # ban tay ngua
    # img = cv2.imread('captured/17-05-2022-17-03-17.png')
    # img = cv2.imread('tay_up.jpg')  # ban tay ngua

    img = imutils.resize(img, height=720)
    mang_diem_moc, annotated_image, handType, image = TimDiemMoc(img)
    if mang_diem_moc[0][1] < mang_diem_moc[12][1]:
        print('Ảnh bị ngược')
        img = cv2.rotate(img, cv2.ROTATE_180)
        mang_diem_moc, annotated_image, handType, image = TimDiemMoc(img)
    # # diem 38 39 50 49
    mang_diem_moc_ngon_tro = mang_diem_moc[5], mang_diem_moc[7], mang_diem_moc[6]
    rong_1, rong_2 = TimChieuRongNgonTay(mang_diem_moc_ngon_tro, img)
    print(rong_1, rong_2)

    VeDuongThangDiQuaHaiDiem(img, rong_1, rong_2)

    cv2.circle(img, rong_1, 2, (255, 0, 0), -1)
    cv2.putText(img, 'R1',
                rong_1, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.circle(img, rong_2, 2, (255, 0, 0), -1)
    cv2.putText(img, 'R2',
                rong_2, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # cv2.circle(img, diem_so_50, 2, (255, 0, 0), -1)
    # cv2.putText(img, '50',
    #             diem_so_50, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    #
    # cv2.circle(img, diem_so_49, 2, (255, 0, 0), -1)
    # cv2.putText(img, '49',
    #             diem_so_49, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    #
    # cv2.circle(img, mang_diem_moc[0], 2, (255, 0, 0), -1)
    # cv2.putText(img, '0',
    #             mang_diem_moc[0], cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.imshow('img', img)
    cv2.waitKey(0)
