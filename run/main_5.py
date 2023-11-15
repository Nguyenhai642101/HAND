from MyLib import *
from Math import *

# if __name__ == "__main__":
#     # img = cv2.imread('27-04-2022-13-08-01.png')  # nguoc hand
#
#     # img = cv2.imread('1.png')
#     # img = cv2.imread('26-04-2022-23-10-41.png') # left hand
#     # img = cv2.imread('27-04-2022-01-46-07.png') # left hand
#     # img = cv2.imread('27-04-2022-01-46-07.png') # left hand
#
#     # img = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\captured\\old\\13-05-2022-18-00-06.png')  # left hand
#     # img = cv2.imread('my2.jpg')  # ban tay ngua
#     img = cv2.imread('2ngon2.jpg')  # ban tay ngua
#     # img = cv2.imread('2ngon.jpg')  # ban tay ngua
#     #
#     # img = cv2.imread('captured/17-05-2022-17-03-17.png')
#     # img = cv2.imread('tay_up.jpg')  # ban tay ngua
#
#     img = imutils.resize(img, height=720)
#     mang_diem_moc, annotated_image, handType, image = TimDiemMoc(img)
#     if mang_diem_moc[0][1] < mang_diem_moc[12][1]:
#         print('Ảnh bị ngược')
#         img = cv2.rotate(img, cv2.ROTATE_180)
#         mang_diem_moc, annotated_image, handType, image = TimDiemMoc(img)
#
#     handType = 'Left' if mang_diem_moc[17] <= mang_diem_moc[3] else 'Right'
#
#     mang_diem = mang_diem_moc[5], mang_diem_moc[6], mang_diem_moc[20]
#     diem_so_41, diem_so_42, diem_so_43, diem_so_44 = TimDiem_41_42_43_44_dong(mang_diem, img, handType)
#
#     # # diem 41 42 43 44
#
#     cv2.circle(img, diem_so_41, 2, (255, 0, 0), -1)
#     cv2.putText(img, '41',
#                 diem_so_41, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
#
#     cv2.circle(img, diem_so_42, 2, (255, 0, 0), -1)
#     cv2.putText(img, '42',
#                 diem_so_42, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
#
#     cv2.circle(img, diem_so_43, 2, (255, 0, 0), -1)
#     cv2.putText(img, '43',
#                 diem_so_43, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
#
#     cv2.circle(img, diem_so_44, 2, (255, 0, 0), -1)
#     cv2.putText(img, '44',
#                 diem_so_44, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
#
#     VeDuongThangDiQuaHaiDiem(image, diem_so_41, diem_so_42)
#     VeDuongThangDiQuaHaiDiem(image, diem_so_43, diem_so_44)
#
#
#     cv2.imshow('img', image)
#     cv2.waitKey(0)

if __name__ == "__main__":

    # img = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\captured\\old\\13-05-2022-18-00-06.png')  # left hand
    # img = cv2.imread('my2.jpg')  # ban tay ngua
    img = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\main\\test\\2ngon2.jpg')  # ban tay ngua
    # img = cv2.imread('2ngon.jpg')  # ban tay ngua
    #
    # img = cv2.imread('captured/17-05-2022-17-03-17.png')
    # img = cv2.imread('tay_up.jpg')  # ban tay ngua

    img = imutils.resize(img, height=720)
    mang_diem_moc, annotated_image, handType, image = TimDiemMoc(img)
    if mang_diem_moc[0][1] < mang_diem_moc[12][1]:
        print('Ảnh bị ngược')
        img = cv2.rotate(img, cv2.ROTATE_180)
        mang_diem_moc, annotated_image, handType, image = TimDiemMoc(img)

    handType = 'Left' if mang_diem_moc[17] <= mang_diem_moc[3] else 'Right'

    mang_diem = mang_diem_moc[5], mang_diem_moc[6], mang_diem_moc[20]
    kq = TimDiem_41_42_43_44_dong_V1(mang_diem, img, handType, nguong=90)
    diem_so_41, diem_so_42, diem_so_43, diem_so_44 = kq
# # diem 41 42 43 44

    cv2.circle(img, diem_so_41, 2, (255, 0, 0), -1)
    cv2.putText(img, '41',
                diem_so_41, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.circle(img, diem_so_42, 2, (255, 0, 0), -1)
    cv2.putText(img, '42',
                diem_so_42, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.circle(img, diem_so_43, 2, (255, 0, 0), -1)
    cv2.putText(img, '43',
                diem_so_43, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.circle(img, diem_so_44, 2, (255, 0, 0), -1)
    cv2.putText(img, '44',
                diem_so_44, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    VeDuongThangDiQuaHaiDiem(image, diem_so_41, diem_so_42)
    VeDuongThangDiQuaHaiDiem(image, diem_so_43, diem_so_44)

    cv2.imshow('img', image)
    cv2.waitKey(0)
