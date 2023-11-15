from MyLib import *
from Math import *

if __name__ == "__main__":
    # img = cv2.imread('27-04-2022-13-08-01.png')  # nguoc hand
    # img = cv2.imread('1.png')
    # img = cv2.imread('26-04-2022-23-10-41.png') # left hand
    # img = cv2.imread('27-04-2022-01-46-07.png') # left hand
    # img = cv2.imread('27-04-2022-01-46-07.png') # left hand

    # img = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\captured\\old\\13-05-2022-18-00-06.png')  # left hand
    # img = cv2.imread('tay_up.jpg')  # ban tay ngua
    # img = cv2.imread('captured/17-05-2022-17-03-17.png')
    img = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\main\\test\\tay_up.jpg')  # ban tay ngua

    nguong = 65
    img = imutils.resize(img, height=720)
    mang_diem_moc, annotated_image, handType, image = TimDiemMoc(img)
    if mang_diem_moc[0][1] < mang_diem_moc[12][1]:
        print('Ảnh bị ngược')
        img = cv2.rotate(img, cv2.ROTATE_180)
        mang_diem_moc, annotated_image, handType, image = TimDiemMoc(img)

    handType = 'Left' if mang_diem_moc[17] <= mang_diem_moc[4] else 'Right'
    print(handType)
    cv2.circle(img, mang_diem_moc[0], 2, (255, 0, 0), -1)
    cv2.putText(img, '11',
                mang_diem_moc[0], cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    # Khe thu nhat =======================================================
    mang_diem_chua_khe_thu_nhat = [mang_diem_moc[1], mang_diem_moc[3], mang_diem_moc[5], mang_diem_moc[6]]

    day_khe_thu_nhat = PhatHienDiemKheNgonTay(mang_diem_chua_khe_thu_nhat, handType, img, nguong)
    # Khe thu hai =======================================================
    mang_diem_chua_khe_thu_hai = [mang_diem_moc[5], mang_diem_moc[6], mang_diem_moc[9], mang_diem_moc[10]]

    day_khe_thu_hai = PhatHienDiemKheNgonTay(mang_diem_chua_khe_thu_hai, handType, img, nguong)

    cv2.circle(img, day_khe_thu_hai, 2, (255, 0, 0), -1)
    cv2.putText(img, 'B',
                day_khe_thu_hai, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # Khe thu ba =======================================================
    mang_diem_chua_khe_thu_ba = [mang_diem_moc[9], mang_diem_moc[10], mang_diem_moc[13], mang_diem_moc[14]]

    day_khe_thu_ba = PhatHienDiemKheNgonTay(mang_diem_chua_khe_thu_ba, handType, img, nguong)

    cv2.circle(img, day_khe_thu_ba, 2, (255, 0, 0), -1)
    cv2.putText(img, 'C',
                day_khe_thu_ba, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # Dinh ngon cai =======================================================
    mang_diem_chua_dinh_ngon_cai = [mang_diem_moc[4], mang_diem_moc[3]]
    dinh_ngon_cai = PhatHienDiemDinhNgonTayv1(mang_diem_chua_dinh_ngon_cai, img, nguong)

    # cv2.circle(img, dinh_ngon_cai, 2, (255, 0, 0), -1)
    # cv2.putText(img, '1',
    #             dinh_ngon_cai, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # Chan ngon cai =======================================================
    mang_diem_chua_chan_ngon_cai = [dinh_ngon_cai, mang_diem_moc[2], day_khe_thu_nhat]
    chan_ngon_cai = PhatHienDiemChanNgonTay(mang_diem_chua_chan_ngon_cai)

    # cv2.circle(img, chan_ngon_cai, 2, (255, 0, 0), -1)
    # cv2.putText(img, '2',
    #             chan_ngon_cai, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    mang_diem_moc_ngon_cai = dinh_ngon_cai, chan_ngon_cai, mang_diem_moc[3]
    rong_1, rong_2 = TimChieuRongNgonTay(mang_diem_moc_ngon_cai, img, nguong)

    VeDuongThangDiQuaHaiDiem(img, rong_1, rong_2)

    cv2.circle(img, rong_1, 2, (255, 0, 0), -1)
    cv2.putText(img, 'R1',
                rong_1, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.circle(img, rong_2, 2, (255, 0, 0), -1)
    cv2.putText(img, 'R2',
                rong_2, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # Dinh ngon giua =======================================================
    mang_diem_chua_dinh_ngon_giua = [mang_diem_moc[12], mang_diem_moc[11]]
    dinh_ngon_giua = PhatHienDiemDinhNgonTayv1(mang_diem_chua_dinh_ngon_giua, img, nguong)

    cv2.circle(img, dinh_ngon_giua, 2, (255, 0, 0), -1)
    cv2.putText(img, '5',
                dinh_ngon_giua, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    
    # Chan ngon giua =======================================================
    mang_diem_chua_chan_ngon_giua = [dinh_ngon_giua, mang_diem_moc[10], day_khe_thu_ba, day_khe_thu_hai]
    chan_ngon_giua = PhatHienDiemChanNgonTayv1(mang_diem_chua_chan_ngon_giua)

    cv2.circle(img, chan_ngon_giua, 2, (255, 0, 0), -1)
    cv2.putText(img, '6',
                chan_ngon_giua, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # Dinh ngon tro =======================================================
    mang_diem_chua_dinh_ngon_tro = [mang_diem_moc[8], mang_diem_moc[7]]
    dinh_ngon_tro = PhatHienDiemDinhNgonTayv1(mang_diem_chua_dinh_ngon_tro, img, nguong)

    cv2.circle(img, dinh_ngon_tro, 2, (255, 0, 0), -1)
    cv2.putText(img, '3',
                dinh_ngon_tro, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # Chan ngon tro =======================================================
    mang_diem_chua_chan_ngon_tro = [dinh_ngon_tro, mang_diem_moc[6], day_khe_thu_hai]
    chan_ngon_tro = PhatHienDiemChanNgonTay(mang_diem_chua_chan_ngon_tro)

    cv2.circle(img, chan_ngon_tro, 2, (255, 0, 0), -1)
    cv2.putText(img, '4',
                chan_ngon_tro, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    # Khe thu tu =======================================================
    mang_diem_chua_khe_thu_tu = [mang_diem_moc[13], mang_diem_moc[14], mang_diem_moc[17], mang_diem_moc[18]]
    day_khe_thu_tu = PhatHienDiemKheNgonTay(mang_diem_chua_khe_thu_tu, handType, img, nguong)

    # Dinh ngon ut =======================================================
    mang_diem_chua_dinh_ngon_ut = [mang_diem_moc[20], mang_diem_moc[19]]
    dinh_ngon_ut = PhatHienDiemDinhNgonTayv1(mang_diem_chua_dinh_ngon_ut, img, nguong)

    # Chan ngon ut =======================================================
    mang_diem_chua_chan_ngon_ut = [dinh_ngon_ut, mang_diem_moc[18], day_khe_thu_tu]
    chan_ngon_ut = PhatHienDiemChanNgonTay(mang_diem_chua_chan_ngon_ut)

    # cv2.circle(img, chan_ngon_ut, 2, (255, 0, 0), -1)
    # cv2.putText(img, '10',
    #             chan_ngon_ut, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    mang_diem_14_16_18 = dinh_ngon_tro, chan_ngon_tro, mang_diem_moc[4], day_khe_thu_nhat
    diem_so_14, diem_so_16, diem_so_18 = TimDiem_14_16_18(mang_diem_14_16_18, img, nguong)

    cv2.circle(img, diem_so_14, 2, (255, 0, 0), -1)
    cv2.putText(img, '14',
                diem_so_14, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.circle(img, diem_so_16, 2, (255, 0, 0), -1)
    cv2.putText(img, '16',
                diem_so_16, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.circle(img, diem_so_18, 2, (255, 0, 0), -1)
    cv2.putText(img, '18',
                diem_so_18, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    diem_so_11 = mang_diem_moc[0]
    diem_so_6 = chan_ngon_giua

    mang_diem_moc_15_17_19 = diem_so_6, diem_so_11, diem_so_14, diem_so_16, diem_so_18, chan_ngon_ut

    diem_so_17, diem_so_15, diem_so_19 = TimDiem_15_17_19(mang_diem_moc_15_17_19, img, handType, nguong)

    cv2.circle(img, diem_so_17, 2, (255, 0, 0), -1)
    cv2.putText(img, '17',
                diem_so_17, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)


    cv2.circle(img, diem_so_15, 2, (255, 0, 0), -1)
    cv2.putText(img, '15',
                diem_so_15, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.circle(img, diem_so_19, 2, (255, 0, 0), -1)
    cv2.putText(img, '19',
                diem_so_19, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    VeDuongThangDiQuaHaiDiem(img, diem_so_14, diem_so_15)
    VeDuongThangDiQuaHaiDiem(img, diem_so_16, diem_so_17)
    VeDuongThangDiQuaHaiDiem(img, diem_so_18, diem_so_19)

    cv2.imshow('img', img)
    cv2.waitKey(0)
