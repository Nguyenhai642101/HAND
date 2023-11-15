from App.run.MyLib import *
from App.run.Math import *

import imutils


def NguaBanTayPhai(img, nguong):
    """
    Phát hiện các điểm trên bàn tay ngửa
    :param img: Ảnh đầu vào
    :param nguong: Ngưỡng để phân biệt đường bao
    :return: Mảng các điểm nằm trên bàn tay ngửa
    """
    # không cần lật ảnh
    mang_diem_moc, annotated_image, handType, image = TimDiemMoc(img)
    if mang_diem_moc[0][1] < mang_diem_moc[12][1]:
        print('Ảnh bị ngược')
        img = cv2.rotate(img, cv2.ROTATE_180)
        mang_diem_moc, annotated_image, hand_type, image = TimDiemMoc(img)
    handType = 'Right' if mang_diem_moc[17] <= mang_diem_moc[0] else 'Left'
    # Khe thu nhat =======================================================
    mang_diem_chua_khe_thu_nhat = [mang_diem_moc[1], mang_diem_moc[3], mang_diem_moc[5], mang_diem_moc[6]]
    day_khe_thu_nhat = PhatHienDiemKheNgonTay(mang_diem_chua_khe_thu_nhat, handType, img, nguong)
    # Khe thu hai =======================================================
    mang_diem_chua_khe_thu_hai = [mang_diem_moc[5], mang_diem_moc[6], mang_diem_moc[9], mang_diem_moc[10]]
    day_khe_thu_hai = PhatHienDiemKheNgonTay(mang_diem_chua_khe_thu_hai, handType, img, nguong)
    # Khe thu ba =======================================================
    mang_diem_chua_khe_thu_ba = [mang_diem_moc[9], mang_diem_moc[10], mang_diem_moc[13], mang_diem_moc[14]]
    day_khe_thu_ba = PhatHienDiemKheNgonTay(mang_diem_chua_khe_thu_ba, handType, img, nguong)
    # Khe thu tu =======================================================
    mang_diem_chua_khe_thu_tu = [mang_diem_moc[13], mang_diem_moc[14], mang_diem_moc[17], mang_diem_moc[18]]
    day_khe_thu_tu = PhatHienDiemKheNgonTay(mang_diem_chua_khe_thu_tu, handType, img, nguong)
    # Dinh ngon cai =======================================================
    mang_diem_chua_dinh_ngon_cai = [mang_diem_moc[4], mang_diem_moc[3]]
    dinh_ngon_cai = PhatHienDiemDinhNgonTayv1(mang_diem_chua_dinh_ngon_cai, img, nguong)
    # Dinh ngon tro =======================================================
    mang_diem_chua_dinh_ngon_tro = [mang_diem_moc[8], mang_diem_moc[7]]
    dinh_ngon_tro = PhatHienDiemDinhNgonTayv1(mang_diem_chua_dinh_ngon_tro, img, nguong)
    # Dinh ngon giua =======================================================
    mang_diem_chua_dinh_ngon_giua = [mang_diem_moc[12], mang_diem_moc[11]]
    dinh_ngon_giua = PhatHienDiemDinhNgonTayv1(mang_diem_chua_dinh_ngon_giua, img, nguong)
    # Dinh ngon ap ut =======================================================
    mang_diem_chua_dinh_ngon_ap_ut = [mang_diem_moc[16], mang_diem_moc[15]]
    dinh_ngon_ap_ut = PhatHienDiemDinhNgonTayv1(mang_diem_chua_dinh_ngon_ap_ut, img, nguong)
    # Dinh ngon ut =======================================================
    mang_diem_chua_dinh_ngon_ut = [mang_diem_moc[20], mang_diem_moc[19]]
    dinh_ngon_ut = PhatHienDiemDinhNgonTayv1(mang_diem_chua_dinh_ngon_ut, img, nguong)
    # Chan ngon cai =======================================================
    mang_diem_chua_chan_ngon_cai = [dinh_ngon_cai, mang_diem_moc[2], day_khe_thu_nhat]
    chan_ngon_cai = PhatHienDiemChanNgonTay(mang_diem_chua_chan_ngon_cai)
    # Chan ngon tro =======================================================
    mang_diem_chua_chan_ngon_tro = [dinh_ngon_tro, mang_diem_moc[6], day_khe_thu_hai]
    chan_ngon_tro = PhatHienDiemChanNgonTay(mang_diem_chua_chan_ngon_tro)
    # Chan ngon giua =======================================================
    mang_diem_chua_chan_ngon_giua = [dinh_ngon_giua, mang_diem_moc[10], day_khe_thu_ba, day_khe_thu_hai]
    chan_ngon_giua = PhatHienDiemChanNgonTayv1(mang_diem_chua_chan_ngon_giua)
    # Chan ngon ap ut =======================================================
    mang_diem_chua_chan_ngon_ap_ut = [dinh_ngon_ap_ut, mang_diem_moc[14], day_khe_thu_tu, day_khe_thu_ba]
    chan_ngon_ap_ut = PhatHienDiemChanNgonTayv1(mang_diem_chua_chan_ngon_ap_ut)
    # Chan ngon ut =======================================================
    mang_diem_chua_chan_ngon_ut = [dinh_ngon_ut, mang_diem_moc[18], day_khe_thu_ba, day_khe_thu_tu]
    chan_ngon_ut = PhatHienDiemChanNgonTayUt(mang_diem_chua_chan_ngon_ut)
    # Diem 11 (diem 0 trong mang moc) ========================================
    # Do do rong ngon tay
    # Do rong ngon tay cai
    mang_diem_rong_tay_cai = (dinh_ngon_cai, chan_ngon_cai, mang_diem_moc[3])
    rong_tay_cai_1, rong_tay_cai_2 = TimChieuRongNgonTay(mang_diem_rong_tay_cai, img, nguong)
    VeDuongThangDiQuaHaiDiem(img, rong_tay_cai_1, rong_tay_cai_2)
    # Do rong ngon tay tro
    mang_diem_rong_tay_tro = (dinh_ngon_tro, chan_ngon_tro, mang_diem_moc[6])
    rong_tay_tro_1, rong_tay_tro_2 = TimChieuRongNgonTay(mang_diem_rong_tay_tro, img, nguong)
    VeDuongThangDiQuaHaiDiem(img, rong_tay_tro_1, rong_tay_tro_2)
    # Do rong ngon tay giua
    mang_diem_rong_tay_giua = (dinh_ngon_giua, chan_ngon_giua, mang_diem_moc[10])
    rong_tay_giua_1, rong_tay_giua_2 = TimChieuRongNgonTay(mang_diem_rong_tay_giua, img, nguong)
    VeDuongThangDiQuaHaiDiem(img, rong_tay_giua_1, rong_tay_giua_2)
    # Do rong ngon tay ap ut
    mang_diem_rong_tay_ap_ut = (dinh_ngon_ap_ut, chan_ngon_ap_ut, mang_diem_moc[14])
    rong_tay_ap_ut_1, rong_tay_ap_ut_2 = TimChieuRongNgonTay(mang_diem_rong_tay_ap_ut, img, nguong)
    VeDuongThangDiQuaHaiDiem(img, rong_tay_ap_ut_1, rong_tay_ap_ut_2)
    # Do rong ngon tay ut
    mang_diem_rong_tay_ut = (dinh_ngon_ut, chan_ngon_ut, mang_diem_moc[18])
    rong_tay_ut_1, rong_tay_ut_2 = TimChieuRongNgonTay(mang_diem_rong_tay_ut, img, nguong)
    VeDuongThangDiQuaHaiDiem(img, rong_tay_ut_1, rong_tay_ut_2)
    # Tìm điểm 36
    mang_diem_36 = (dinh_ngon_tro, chan_ngon_tro, chan_ngon_tro)
    diem_36_A, diem_36_B = TimChieuRongNgonTay(mang_diem_36, img, nguong)
    kc1 = abs(diem_36_A[0] - mang_diem_moc[4][0])
    kc2 = abs(diem_36_B[0] - mang_diem_moc[4][0])
    diem_36 = diem_36_A if (kc1 < kc2) else diem_36_B
    cv2.circle(img, diem_36, 2, (255, 0, 0), -1)
    cv2.putText(img, '36',
                diem_36, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    # Tìm điểm 37
    mang_diem_37 = (mang_diem_moc[0], mang_diem_moc[17])
    diem_37 = TimDiemSo37(mang_diem_37, img, nguong)
    diem_tren_tay_ngua = []
    mang = []
    diem_so_1 = dinh_ngon_cai
    diem_so_3 = dinh_ngon_tro
    diem_so_5 = dinh_ngon_giua
    diem_so_7 = dinh_ngon_ap_ut
    diem_so_9 = dinh_ngon_ut
    diem_so_2 = chan_ngon_cai
    diem_so_4 = chan_ngon_tro
    diem_so_6 = chan_ngon_giua
    diem_so_8 = chan_ngon_ap_ut
    diem_so_10 = chan_ngon_ut
    diem_so_11 = mang_diem_moc[0]
    diem_so_20 = rong_tay_cai_1
    diem_so_21 = rong_tay_cai_2
    diem_so_22 = rong_tay_tro_1
    diem_so_23 = rong_tay_tro_2
    diem_so_24 = rong_tay_giua_1
    diem_so_25 = rong_tay_giua_2
    diem_so_26 = rong_tay_ap_ut_1
    diem_so_27 = rong_tay_ap_ut_2
    diem_so_28 = rong_tay_ut_1
    diem_so_29 = rong_tay_ut_2
    diem_so_36 = diem_36
    diem_so_37 = diem_37
    if handType == 'Right':
        mang = diem_so_1, diem_so_2, diem_so_3, diem_so_4, diem_so_5, diem_so_6, \
               diem_so_7, diem_so_8, diem_so_9, diem_so_10, diem_so_11, diem_so_20, \
               diem_so_21, diem_so_22, diem_so_23, diem_so_24, diem_so_25, diem_so_26, \
               diem_so_27, diem_so_28, diem_so_29, diem_so_36, diem_so_37
        for no_diem, diem in enumerate(mang):
            diem_tren_tay_ngua.append((diem[0], diem[1]))
    if handType == 'Left':
        mang = diem_so_1, diem_so_2, diem_so_3, diem_so_4, diem_so_5, diem_so_6, \
               diem_so_7, diem_so_8, diem_so_9, diem_so_10, diem_so_11, diem_so_21, \
               diem_so_20, diem_so_23, diem_so_22, diem_so_25, diem_so_24, diem_so_27, \
               diem_so_26, diem_so_29, diem_so_28, diem_so_36, diem_so_37
        for no_diem, diem in enumerate(mang):
            diem_tren_tay_ngua.append((diem[0], diem[1]))

    mang_ten = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 36, 37
    for i, moc in enumerate(diem_tren_tay_ngua):
        cv2.circle(img, moc, 2, (255, 0, 0), -1)
        cv2.putText(img, str(mang_ten[i]), moc, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    cv2.imshow('KQ', img)
    cv2.waitKey(0)

    return diem_tren_tay_ngua, img


def UpBanTayPhai(img, nguong):
    """
    Tìm các điểm nằm trên bàn tay phải khi đang úp
    :param img: Ảnh đầu vào
    :param nguong: ngưỡng phân biệt màu
    :return: Mảng các điểm trên bàn tay úp
    """
    # không cần lật ảnh
    mang_diem_moc, annotated_image, handtype, image = TimDiemMoc(img)
    if mang_diem_moc[0][1] < mang_diem_moc[12][1]:
        print('Ảnh bị ngược')
        img = cv2.rotate(img, cv2.ROTATE_180)
        mang_diem_moc, annotated_image, handtype, image = TimDiemMoc(img)

    handType = 'Left' if mang_diem_moc[17] <= mang_diem_moc[4] else 'Right'
    # print(handType)
    # Khe thu nhat =======================================================
    mang_diem_chua_khe_thu_nhat = [mang_diem_moc[1], mang_diem_moc[3], mang_diem_moc[5], mang_diem_moc[6]]

    day_khe_thu_nhat = PhatHienDiemKheNgonTay(mang_diem_chua_khe_thu_nhat, handType, img, nguong)
    # Khe thu hai =======================================================
    mang_diem_chua_khe_thu_hai = [mang_diem_moc[5], mang_diem_moc[6], mang_diem_moc[9], mang_diem_moc[10]]

    day_khe_thu_hai = PhatHienDiemKheNgonTay(mang_diem_chua_khe_thu_hai, handType, img, nguong)

    # Khe thu ba =======================================================
    mang_diem_chua_khe_thu_ba = [mang_diem_moc[9], mang_diem_moc[10], mang_diem_moc[13], mang_diem_moc[14]]

    day_khe_thu_ba = PhatHienDiemKheNgonTay(mang_diem_chua_khe_thu_ba, handType, img, nguong)

    # Dinh ngon cai =======================================================
    mang_diem_chua_dinh_ngon_cai = [mang_diem_moc[4], mang_diem_moc[3]]
    dinh_ngon_cai = PhatHienDiemDinhNgonTayv1(mang_diem_chua_dinh_ngon_cai, img, nguong)

    # Chan ngon cai =======================================================
    mang_diem_chua_chan_ngon_cai = [dinh_ngon_cai, mang_diem_moc[2], day_khe_thu_nhat]
    chan_ngon_cai = PhatHienDiemChanNgonTay(mang_diem_chua_chan_ngon_cai)

    mang_diem_moc_ngon_cai = dinh_ngon_cai, chan_ngon_cai, mang_diem_moc[3]
    rong_1, rong_2 = TimChieuRongNgonTay(mang_diem_moc_ngon_cai, img, nguong)

    # Dinh ngon giua =======================================================
    mang_diem_chua_dinh_ngon_giua = [mang_diem_moc[12], mang_diem_moc[11]]
    dinh_ngon_giua = PhatHienDiemDinhNgonTayv1(mang_diem_chua_dinh_ngon_giua, img, nguong)

    # Chan ngon giua =======================================================
    mang_diem_chua_chan_ngon_giua = [dinh_ngon_giua, mang_diem_moc[10], day_khe_thu_ba, day_khe_thu_hai]
    chan_ngon_giua = PhatHienDiemChanNgonTayv1(mang_diem_chua_chan_ngon_giua)

    # Dinh ngon tro =======================================================
    mang_diem_chua_dinh_ngon_tro = [mang_diem_moc[8], mang_diem_moc[7]]
    dinh_ngon_tro = PhatHienDiemDinhNgonTayv1(mang_diem_chua_dinh_ngon_tro, img, nguong)

    # Chan ngon tro =======================================================
    mang_diem_chua_chan_ngon_tro = [dinh_ngon_tro, mang_diem_moc[6], day_khe_thu_hai]
    chan_ngon_tro = PhatHienDiemChanNgonTay(mang_diem_chua_chan_ngon_tro)

    # Khe thu tu =======================================================
    mang_diem_chua_khe_thu_tu = [mang_diem_moc[13], mang_diem_moc[14], mang_diem_moc[17], mang_diem_moc[18]]
    day_khe_thu_tu = PhatHienDiemKheNgonTay(mang_diem_chua_khe_thu_tu, handType, img, nguong)

    # Dinh ngon ut =======================================================
    mang_diem_chua_dinh_ngon_ut = [mang_diem_moc[20], mang_diem_moc[19]]
    dinh_ngon_ut = PhatHienDiemDinhNgonTayv1(mang_diem_chua_dinh_ngon_ut, img, nguong)

    # Chan ngon ut =======================================================
    mang_diem_chua_chan_ngon_ut = [dinh_ngon_ut, mang_diem_moc[18], day_khe_thu_ba, day_khe_thu_tu]
    chan_ngon_ut = PhatHienDiemChanNgonTayUt(mang_diem_chua_chan_ngon_ut)

    mang_diem_14_16_18 = dinh_ngon_tro, chan_ngon_tro, mang_diem_moc[4], day_khe_thu_nhat
    diem_so_14, diem_so_16, diem_so_18 = TimDiem_14_16_18(mang_diem_14_16_18, img, nguong)

    # diem_so_11 = mang_diem_moc[0]
    diem_so_6 = chan_ngon_giua
    diem_so_5 = dinh_ngon_giua
    mang_diem_moc_15_17_19 = diem_so_6, diem_so_5, diem_so_14, diem_so_16, diem_so_18, chan_ngon_ut

    diem_so_17, diem_so_15, diem_so_19 = TimDiem_15_17_19(mang_diem_moc_15_17_19, img, handType, nguong)

    diem_tren_tay_up = []
    diem_so_48 = rong_1
    diem_so_47 = rong_2

    if handType == 'Right':
        mang = diem_so_14, diem_so_15, diem_so_16, diem_so_17, diem_so_18, diem_so_19, diem_so_47, diem_so_48
        for no_diem, diem in enumerate(mang):
            diem_tren_tay_up.append((diem[0], diem[1]))
    if handType == 'Left':
        mang = diem_so_14, diem_so_15, diem_so_16, diem_so_17, diem_so_18, diem_so_19, diem_so_47, diem_so_48
        for no_diem, diem in enumerate(mang):
            diem_tren_tay_up.append((diem[0], diem[1]))

    mang_ten = 14, 15, 16, 17, 18, 19, 47, 48
    for i, moc in enumerate(diem_tren_tay_up):
        cv2.circle(img, moc, 2, (255, 0, 0), -1)
        cv2.putText(img, str(mang_ten[i]), moc, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    # cv2.imshow('KQ', img)
    # cv2.waitKey(0)

    return diem_tren_tay_up, img


def NamTayPhai1(img, nguong):
    """
    Tìm các điểm trên ảnh nắm tay phải 1
    :param img: Ảnh đầu vào
    :param nguong: Ngưỡng phân biệt đường bao
    :return: Mảng các điểm trên nắm bàn tay phải 1
    """
    # không cần lật ảnh
    mang_diem_moc, annotated_image, handtype, image = TimDiemMoc(img)
    if mang_diem_moc[0][1] < mang_diem_moc[12][1]:
        print('Ảnh bị ngược')
        img = cv2.rotate(img, cv2.ROTATE_180)
        mang_diem_moc, annotated_image, handtype, image = TimDiemMoc(img)

    handType = 'Right' if mang_diem_moc[17] <= mang_diem_moc[0] else 'Left'
    # diem 12, 53, 54, 51, 52
    diem_so_12, diem_so_53, diem_so_54, diem_so_51, diem_so_52 = TimDiemSo_12_53_54_51_52(mang_diem_moc[0], image,
                                                                                          nguong)
    # diem 13
    mang_diem_moc_0_phay = (mang_diem_moc[0][0] + 10, mang_diem_moc[0][1])
    a0, b0, c0 = TimPhuongTrinhDuongThangBietHaiDiem(mang_diem_moc[0], mang_diem_moc_0_phay)
    a1, b1, c1 = TimPhuongTrinhDuongThangVuongGocVoiDuongThang(mang_diem_moc[0], mang_diem_moc_0_phay, diem_so_12)

    d0 = (a0, b0, c0)
    d1 = (a1, b1, c1)
    diem_so_13 = TimGiaoDiemHaiDuongThang(d0, d1)
    diem_nam_tay_phai_1 = []

    if handType == 'Right':
        mang = diem_so_12, diem_so_13, diem_so_51, diem_so_52, diem_so_53, diem_so_54,
        for no_diem, diem in enumerate(mang):
            diem_nam_tay_phai_1.append((diem[0], diem[1]))

    if handType == 'Left':
        mang = diem_so_12, diem_so_13, diem_so_52, diem_so_51, diem_so_54, diem_so_53,
        for no_diem, diem in enumerate(mang):
            diem_nam_tay_phai_1.append((diem[0], diem[1]))

    mang_ten = 12, 13, 51, 52, 53, 54
    for i, moc in enumerate(diem_nam_tay_phai_1):
        cv2.circle(img, moc, 2, (255, 0, 0), -1)
        cv2.putText(img, str(mang_ten[i]), moc, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    # cv2.imshow('KQ', img)
    # cv2.waitKey(0)
    return diem_nam_tay_phai_1, img


def NamTayPhai2(img, nguong):
    # không cần lật ảnh
    mang_diem_moc, annotated_image, handtype, image = TimDiemMoc(img)
    if mang_diem_moc[0][1] < mang_diem_moc[12][1]:
        print('Ảnh bị ngược')
        img = cv2.rotate(img, cv2.ROTATE_180)
        mang_diem_moc, annotated_image, handtype, image = TimDiemMoc(img)
    handType = 'Right' if mang_diem_moc[0] <= mang_diem_moc[5] else 'Left'
    # diem 38 39 50 49
    diem_so_38, diem_so_39, diem_so_50, diem_so_49 = TimDiemSo_38_39_49_50_tay_phai(mang_diem_moc[0], img, nguong,
                                                                                    handType)
    # cv2.circle(img, diem_so_38, 2, (255, 0, 0), -1)
    # cv2.putText(img, '38',
    #             diem_so_38, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    #
    # cv2.circle(img, diem_so_39, 2, (255, 0, 0), -1)
    # cv2.putText(img, '39',
    #             diem_so_39, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    #
    # cv2.circle(img, diem_so_50, 2, (255, 0, 0), -1)
    # cv2.putText(img, '50',
    #             diem_so_50, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    #
    # cv2.circle(img, diem_so_49, 2, (255, 0, 0), -1)
    # cv2.putText(img, '49',
    #             diem_so_49, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    #
    # cv2.imshow('img', img)
    # cv2.waitKey(0)
    diem_nam_tay_phai_2 = []

    if handType == 'Right':
        mang = diem_so_38, diem_so_39, diem_so_49, diem_so_50
        for no_diem, diem in enumerate(mang):
            diem_nam_tay_phai_2.append((diem[0], diem[1]))
    if handType == 'Left':
        mang = diem_so_38, diem_so_39, diem_so_49, diem_so_50
        for no_diem, diem in enumerate(mang):
            diem_nam_tay_phai_2.append((diem[0], diem[1]))

    mang_ten = 38, 39, 49, 50
    for i, moc in enumerate(diem_nam_tay_phai_2):
        cv2.circle(img, moc, 2, (255, 0, 0), -1)
        cv2.putText(img, str(mang_ten[i]), moc, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    cv2.imshow('KQ', img)
    cv2.waitKey(0)

    return diem_nam_tay_phai_2, img


def NgonTroPhai(img, nguong):
    # không cần lật ảnh
    img = imutils.resize(img, height=720)
    mang_diem_moc, annotated_image, handtype, image = TimDiemMoc(img)
    if mang_diem_moc[0][1] < mang_diem_moc[12][1]:
        print('Ảnh bị ngược')
        img = cv2.rotate(img, cv2.ROTATE_180)
        mang_diem_moc, annotated_image, handtype, image = TimDiemMoc(img)
    # # diem 38 39 50 49
    handType = 'Right' if mang_diem_moc[0] <= mang_diem_moc[5] else 'Left'
    mang_diem_moc_ngon_tro = mang_diem_moc[5], mang_diem_moc[7], mang_diem_moc[6]
    diem_so_46, diem_so_45 = TimChieuRongNgonTay(mang_diem_moc_ngon_tro, img, nguong)
    # print(diem_so_46, diem_so_45)
    #
    # VeDuongThangDiQuaHaiDiem(img, diem_so_46, diem_so_45)
    #
    # cv2.circle(img, diem_so_46, 2, (255, 0, 0), -1)
    # cv2.putText(img, 'R1',
    #             diem_so_46, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    #
    # cv2.circle(img, diem_so_45, 2, (255, 0, 0), -1)
    # cv2.putText(img, 'R2',
    #             diem_so_45, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    #
    # cv2.imshow('img', img)
    # cv2.waitKey(0)
    diem_ngon_tro_phai = []
    if handType == 'Right':
        mang = diem_so_45, diem_so_46
        for no_diem, diem in enumerate(mang):
            diem_ngon_tro_phai.append((diem[0], diem[1]))
    if handType == 'Left':
        mang = diem_so_46, diem_so_45
        for no_diem, diem in enumerate(mang):
            diem_ngon_tro_phai.append((diem[0], diem[1]))

    mang_ten = 45, 46
    for i, moc in enumerate(diem_ngon_tro_phai):
        cv2.circle(img, moc, 2, (255, 0, 0), -1)
        cv2.putText(img, str(mang_ten[i]), moc, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    # cv2.imshow('KQ', img)
    # cv2.waitKey(0)

    return diem_ngon_tro_phai, img


def MuTayPhai(img, nguong):
    # không cần lật ảnh
    mang_diem_moc, annotated_image, handtype, image = TimDiemMoc(img)
    if mang_diem_moc[0][1] < mang_diem_moc[12][1]:
        print('Ảnh bị ngược')
        img = cv2.rotate(img, cv2.ROTATE_180)
        mang_diem_moc, annotated_image, handtype, image = TimDiemMoc(img)

    handType = 'Right' if mang_diem_moc[0] >= mang_diem_moc[1] else 'Left'
    print(handType)
    # cv2.imwrite('mutayphai.png', annotated_image)
    mang_x = []
    for i, diem in enumerate(mang_diem_moc):
        mang_x.append(diem[1])
    chi_so_diem_cao_nhat = mang_x.index(min(mang_x))
    diem_cao_nhat = mang_diem_moc[chi_so_diem_cao_nhat]
    diem_cao_nhi = mang_diem_moc[chi_so_diem_cao_nhat - 1]
    print(chi_so_diem_cao_nhat)
    mang_diem = mang_diem_moc[0], mang_diem_moc[3], diem_cao_nhi, diem_cao_nhat

    diem_so_30, diem_so_31, \
    diem_so_32, diem_so_33, \
    diem_so_34, diem_so_35 = TimDiem_30_31_32_33_34_dong(mang_diem, img, handType, nguong)

    # cv2.circle(image, diem_so_30, 2, (255, 0, 0), -1)
    # cv2.putText(image, '30', diem_so_30, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    #
    # cv2.circle(image, diem_so_31, 2, (255, 0, 0), -1)
    # cv2.putText(image, '31', diem_so_31, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    #
    # cv2.circle(image, diem_so_32, 2, (255, 0, 0), -1)
    # cv2.putText(image, '32', diem_so_32, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    #
    # cv2.circle(image, diem_so_33, 2, (255, 0, 0), -1)
    # cv2.putText(image, '33', diem_so_33, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    #
    # cv2.circle(image, diem_so_34, 2, (255, 0, 0), -1)
    # cv2.putText(image, '34', diem_so_34, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    #
    # cv2.circle(image, diem_so_35, 2, (255, 0, 0), -1)
    # cv2.putText(image, '35', diem_so_35, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    #
    # VeDuongThangDiQuaHaiDiem(image, diem_so_30, diem_so_31)
    # VeDuongThangDiQuaHaiDiem(image, diem_so_32, diem_so_33)
    # VeDuongThangDiQuaHaiDiem(image, diem_so_34, diem_so_35)
    #
    # cv2.imshow('img', img)
    # # cv2.imshow('annotated_image', annotated_image)
    #
    # cv2.waitKey(0)

    diem_mu_tay_phai_phai = []
    mang = diem_so_30, diem_so_31, diem_so_32, diem_so_33, diem_so_34, diem_so_35
    for no_diem, diem in enumerate(mang):
        diem_mu_tay_phai_phai.append((diem[0], diem[1]))

    mang_ten = 30, 31, 32, 33, 34, 35
    for i, moc in enumerate(diem_mu_tay_phai_phai):
        cv2.circle(img, moc, 2, (255, 0, 0), -1)
        cv2.putText(img, str(mang_ten[i]), moc, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    cv2.imshow('KQ', img)
    cv2.waitKey(0)

    return diem_mu_tay_phai_phai, img


def HaiNgonTayPhai(img, nguong):
    # không cần lật ảnh
    mang_diem_moc, annotated_image, handtype, image = TimDiemMoc(img)
    if mang_diem_moc[0][1] < mang_diem_moc[12][1]:
        print('Ảnh bị ngược')
        img = cv2.rotate(img, cv2.ROTATE_180)
        mang_diem_moc, annotated_image, handtype, image = TimDiemMoc(img)

    handType = 'Left' if mang_diem_moc[0] <= mang_diem_moc[3] else 'Right'
    print(handType)
    mang_diem = mang_diem_moc[5], mang_diem_moc[6], mang_diem_moc[20]
    diem_so_41, diem_so_42, diem_so_43, diem_so_44 = TimDiem_41_42_43_44_dong_V1(mang_diem, img, handType, nguong)
    # diem 41 42 43 44

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
    #
    # cv2.imshow('img', image)
    # cv2.waitKey(0)

    diem_hai_ngon_tay_phai = []
    if handType == 'Right':
        mang = diem_so_41, diem_so_42, diem_so_43, diem_so_44
        for no_diem, diem in enumerate(mang):
            diem_hai_ngon_tay_phai.append((diem[0], diem[1]))
    if handType == 'Left':
        mang = diem_so_44, diem_so_43, diem_so_42, diem_so_41
        for no_diem, diem in enumerate(mang):
            diem_hai_ngon_tay_phai.append((diem[0], diem[1]))

    mang_ten = 41, 42, 43, 44
    for i, moc in enumerate(diem_hai_ngon_tay_phai):
        cv2.circle(img, moc, 2, (255, 0, 0), -1)
        cv2.putText(img, str(mang_ten[i]), moc, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    cv2.imshow('KQ', img)
    cv2.waitKey(0)

    return diem_hai_ngon_tay_phai, img


""" =======================> Test <====================== """
# img1 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\8.jpg')  # ban tay ngua
# # img1 = cv2.imread('D:\\HUST\\LAB\DIR\\26-05-2022-14-30-26\\1.png')  # ban tay ngua
#
#
# img1 = imutils.resize(img1, height=800)
# # nguong_1 = self.cur_mang_nguong[0]
# nguong_1 = 65
# # nguong_1 = 24
# diem_tren_tay_ngua, kq_img = NguaBanTayPhai(img1, nguong_1)
# print(diem_tren_tay_ngua)
#
# img2 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\9.jpg')  # ban tay ngua

# img2 = cv2.imread("D:/HUST/LAB/DIR/27-05-2022-14-47-33/2.png")
# img2 = imutils.resize(img2, height=800)
# # nguong_2 = self.cur_mang_nguong[1]
# nguong_2 = 28
# # nguong_2 = 65
# diem_tren_tay_up = UpBanTayPhai(img2, nguong_2)
# print(diem_tren_tay_up)

# img3 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\10.jpg')  # ban tay ngua
# img3 = imutils.resize(img3, height=800)
# # nguong_2 = self.cur_mang_nguong[1]
# nguong_3 = 65
# diem_nam_tay_phai_1 = NamTayPhai1(img3, nguong_3)
# print(diem_nam_tay_phai_1)

# img4 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\4.jpg')  # ban tay ngua
# img4 = imutils.resize(img4, height=800)
# # nguong_2 = self.cur_mang_nguong[1]
# nguong_4 = 65
# diem_nam_tay_phai_2, img4_kq = NamTayPhai2(img4, nguong_4)
# print(diem_nam_tay_phai_2)
#
# img5 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\12.jpg')  # ban tay ngua
# img5 = imutils.resize(img5, height=800)
# # nguong_2 = self.cur_mang_nguong[1]
# nguong_5 = 65
# diem_ngon_tro_phai, img5_kq = NgonTroPhai(img5, nguong_5)
# print(diem_ngon_tro_phai)

# img6 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\13.jpg')  # ban tay ngua
# img6 = imutils.resize(img6, height=800)
# # nguong_2 = self.cur_mang_nguong[1]
# nguong_6 = 65
# diem_mu_tay_phai, img6_kq = MuTayPhai(img6, nguong_6)
# print(diem_mu_tay_phai)

# img7 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\7.jpg')  # ban tay ngua
# img7 = cv2.flip(img7, 1)
# img7 = cv2.imread('D:\\HUST\\LAB\DIR\\27-05-2022-17-54-03\\7.png')
# img7 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\main\\test\\2ngon3.jpg')
# img7 = imutils.resize(img7, height=800)
# # nguong_2 = self.cur_mang_nguong[1]
# nguong_7 = 90
# # nguong_7 = 28
# diem_hai_ngon_tay_phai, img7_kq = HaiNgonTayPhai(img7, nguong_7)
# print(diem_hai_ngon_tay_phai)
