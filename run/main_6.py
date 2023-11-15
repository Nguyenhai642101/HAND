from MyLib import *
from Math import *

if __name__ == "__main__":
    # img = cv2.imread('27-04-2022-13-08-01.png')  # nguoc hand

    # img = cv2.imread('1.png')
    # img = cv2.imread('26-04-2022-23-10-41.png') # left hand
    # img = cv2.imread('27-04-2022-01-46-07.png') # left hand
    # img = cv2.imread('27-04-2022-01-46-07.png') # left hand

    # img = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\captured\\old\\13-05-2022-18-00-06.png')  # left hand
    # img = cv2.imread('my2.jpg')  # ban tay ngua
    img = cv2.imread('chitay.jpg')  # ban tay ngua
    # img = cv2.imread('2ngon.jpg')  # ban tay ngua
    #
    # img = cv2.imread('captured/17-05-2022-17-03-17.png')
    img = cv2.flip(img, 1)
    img = imutils.resize(img, height=720)
    mang_diem_moc, annotated_image, handType, image = TimDiemMoc(img)
    if mang_diem_moc[0][1] < mang_diem_moc[12][1]:
        print('Ảnh bị ngược')
        img = cv2.rotate(img, cv2.ROTATE_180)
        mang_diem_moc, annotated_image, handType, image = TimDiemMoc(img)

    handType = 'Left' if mang_diem_moc[0] >= mang_diem_moc[1] else 'Right'
    print(handType)

    mang_diem = mang_diem_moc[0], mang_diem_moc[3], mang_diem_moc[7], mang_diem_moc[8]
    # diem_so_41, diem_so_42, diem_so_43, diem_so_44 =
    #
    # # # diem 41 42 43 44
    #
    # cv2.circle(img, diem_so_41, 2, (255, 0, 0), -1)
    # cv2.putText(img, '41',
    #             diem_so_41, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    #
    # cv2.circle(img, diem_so_42, 2, (255, 0, 0), -1)
    # cv2.putText(img, '42',
    #             diem_so_42, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    #
    # cv2.circle(img, diem_so_43, 2, (255, 0, 0), -1)
    # cv2.putText(img, '43',
    #             diem_so_43, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    #
    # cv2.circle(img, diem_so_44, 2, (255, 0, 0), -1)
    # cv2.putText(img, '44',
    #             diem_so_44, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    #
    # VeDuongThangDiQuaHaiDiem(image, diem_so_41, diem_so_42)
    # VeDuongThangDiQuaHaiDiem(image, diem_so_43, diem_so_44)

    diem_so_30, diem_so_31, \
    diem_so_32, diem_so_33, \
    diem_so_34, diem_so_35 = TimDiem_30_31_32_33_34_dong(mang_diem, img, handType)

    cv2.circle(image, diem_so_30, 2, (255, 0, 0), -1)
    cv2.putText(image, '30', diem_so_30, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.circle(image, diem_so_31, 2, (255, 0, 0), -1)
    cv2.putText(image, '31', diem_so_31, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.circle(image, diem_so_32, 2, (255, 0, 0), -1)
    cv2.putText(image, '32', diem_so_32, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.circle(image, diem_so_33, 2, (255, 0, 0), -1)
    cv2.putText(image, '33', diem_so_33, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.circle(image, diem_so_34, 2, (255, 0, 0), -1)
    cv2.putText(image, '34', diem_so_34, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.circle(image, diem_so_35, 2, (255, 0, 0), -1)
    cv2.putText(image, '35', diem_so_35, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    VeDuongThangDiQuaHaiDiem(image, diem_so_30, diem_so_31)
    VeDuongThangDiQuaHaiDiem(image, diem_so_32, diem_so_33)
    VeDuongThangDiQuaHaiDiem(image, diem_so_34, diem_so_35)

    cv2.imshow('img', img)
    # cv2.imshow('annotated_image', annotated_image)

    cv2.waitKey(0)
