import math
import mediapipe as mp

from Hand.function.MyLib import *
from Hand.function.Math import *

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
    # Do rong ngon tay tro
    mang_diem_rong_tay_tro = (dinh_ngon_tro, chan_ngon_tro, mang_diem_moc[6])
    rong_tay_tro_1, rong_tay_tro_2 = TimChieuRongNgonTay(mang_diem_rong_tay_tro, img, nguong)
    # Do rong ngon tay giua
    mang_diem_rong_tay_giua = (dinh_ngon_giua, chan_ngon_giua, mang_diem_moc[10])
    rong_tay_giua_1, rong_tay_giua_2 = TimChieuRongNgonTay(mang_diem_rong_tay_giua, img, nguong)
    # Do rong ngon tay ap ut
    mang_diem_rong_tay_ap_ut = (dinh_ngon_ap_ut, chan_ngon_ap_ut, mang_diem_moc[14])
    rong_tay_ap_ut_1, rong_tay_ap_ut_2 = TimChieuRongNgonTay(mang_diem_rong_tay_ap_ut, img, nguong)
    # Do rong ngon tay ut
    mang_diem_rong_tay_ut = (dinh_ngon_ut, chan_ngon_ut, mang_diem_moc[18])
    rong_tay_ut_1, rong_tay_ut_2 = TimChieuRongNgonTay(mang_diem_rong_tay_ut, img, nguong)
    # Tìm điểm 36
    mang_diem_36 = (dinh_ngon_tro, chan_ngon_tro, chan_ngon_tro)
    diem_36_A, diem_36_B = TimChieuRongNgonTay(mang_diem_36, img, nguong)
    kc1 = abs(diem_36_A[0] - mang_diem_moc[4][0])
    kc2 = abs(diem_36_B[0] - mang_diem_moc[4][0])
    diem_36 = diem_36_A if (kc1 < kc2) else diem_36_B
    # cv2.circle(img, diem_36, 2, (255, 0, 0), -1)
    # cv2.putText(img, '36',
    #             diem_36, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
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

    mang_ten = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 36, 37
    img_cp = img.copy()
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

    VeDuongThangDiQuaHaiDiem(img_cp, rong_tay_cai_1, rong_tay_cai_2)
    VeDuongThangDiQuaHaiDiem(img_cp, rong_tay_tro_1, rong_tay_tro_2)
    VeDuongThangDiQuaHaiDiem(img_cp, rong_tay_giua_1, rong_tay_giua_2)
    VeDuongThangDiQuaHaiDiem(img_cp, rong_tay_ap_ut_1, rong_tay_ap_ut_2)
    VeDuongThangDiQuaHaiDiem(img_cp, rong_tay_ut_1, rong_tay_ut_2)

    for i, moc in enumerate(diem_tren_tay_ngua):
        cv2.circle(img_cp, moc, 2, (255, 0, 0), -1)
        cv2.putText(img_cp, str(mang_ten[i]), moc, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    # cv2.imshow('KQ', img)
    # cv2.waitKey(0)

    return diem_tren_tay_ngua, img_cp


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

    img_cp = img.copy()
    mang_ten = 14, 15, 16, 17, 18, 19, 47, 48

    if handType == 'Right':
        mang = diem_so_14, diem_so_15, diem_so_16, diem_so_17, diem_so_18, diem_so_19, diem_so_47, diem_so_48
        for no_diem, diem in enumerate(mang):
            diem_tren_tay_up.append((diem[0], diem[1]))
    if handType == 'Left':
        mang = diem_so_14, diem_so_15, diem_so_16, diem_so_17, diem_so_18, diem_so_19, diem_so_47, diem_so_48
        for no_diem, diem in enumerate(mang):
            diem_tren_tay_up.append((diem[0], diem[1]))

    for i, moc in enumerate(diem_tren_tay_up):
        cv2.circle(img_cp, moc, 2, (255, 0, 0), -1)
        cv2.putText(img_cp, str(mang_ten[i]), moc, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    # cv2.imshow('KQ', img)
    # cv2.waitKey(0)

    return diem_tren_tay_up, img_cp


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
    mang_diem = mang_diem_moc[0], mang_diem_moc[1], mang_diem_moc[3]
    diem_so_12, diem_so_53, diem_so_54, diem_so_51, diem_so_52 = TimDiemSo_12_53_54_51_52(mang_diem, image,
                                                                                          nguong, handType)
    # diem 13
    mang_diem_moc_0_phay = (mang_diem_moc[0][0] + 10, mang_diem_moc[0][1])
    a0, b0, c0 = TimPhuongTrinhDuongThangBietHaiDiem(mang_diem_moc[0], mang_diem_moc_0_phay)
    a1, b1, c1 = TimPhuongTrinhDuongThangVuongGocVoiDuongThang(mang_diem_moc[0], mang_diem_moc_0_phay, diem_so_12)

    d0 = (a0, b0, c0)
    d1 = (a1, b1, c1)
    diem_so_13 = TimGiaoDiemHaiDuongThang(d0, d1)
    diem_nam_tay_phai_1 = []

    mang = diem_so_12, diem_so_13, diem_so_51, diem_so_52, diem_so_53, diem_so_54
    img_cp = img.copy()
    mang_ten = 12, 13, 51, 52, 53, 54

    for no_diem, diem in enumerate(mang):
        diem_nam_tay_phai_1.append((diem[0], diem[1]))

    for i, moc in enumerate(diem_nam_tay_phai_1):
        cv2.circle(img_cp, moc, 2, (255, 0, 0), -1)
        cv2.putText(img_cp, str(mang_ten[i]), moc, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    # cv2.imshow('annotated_image', annotated_image)
    # cv2.imshow('KQ', img_cp)
    # cv2.waitKey(0)
    return diem_nam_tay_phai_1, img_cp


def NamTayPhai2(img, nguong):
    # không cần lật ảnh
    mang_diem_moc, annotated_image, handtype, image = TimDiemMoc(img)
    if mang_diem_moc[0][1] < mang_diem_moc[12][1]:
        print('Ảnh bị ngược')
        img = cv2.rotate(img, cv2.ROTATE_180)
        mang_diem_moc, annotated_image, handtype, image = TimDiemMoc(img)
    handType = 'Right' if mang_diem_moc[0] <= mang_diem_moc[5] else 'Left'
    # diem 38 39 50 49
    mang_diem = mang_diem_moc[0], mang_diem_moc[6]
    diem_so_38, diem_so_39, diem_so_50, diem_so_49 = TimDiemSo_38_39_49_50_tay_phai(mang_diem, img, nguong,
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

    img_cp = img.copy()
    mang_ten = 38, 39, 49, 50

    mang = diem_so_38, diem_so_39, diem_so_49, diem_so_50
    for no_diem, diem in enumerate(mang):
        diem_nam_tay_phai_2.append((diem[0], diem[1]))

    for i, moc in enumerate(diem_nam_tay_phai_2):
        cv2.circle(img_cp, moc, 2, (255, 0, 0), -1)
        cv2.putText(img_cp, str(mang_ten[i]), moc, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    # cv2.imshow('annotated_image', annotated_image)
    # cv2.imshow('KQ', img_cp)
    # cv2.waitKey(0)

    return diem_nam_tay_phai_2, img_cp


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

    img_cp = img.copy()
    mang_ten = 45, 46

    if handType == 'Right':
        mang = diem_so_45, diem_so_46
        for no_diem, diem in enumerate(mang):
            diem_ngon_tro_phai.append((diem[0], diem[1]))
    if handType == 'Left':
        mang = diem_so_46, diem_so_45
        for no_diem, diem in enumerate(mang):
            diem_ngon_tro_phai.append((diem[0], diem[1]))

    for i, moc in enumerate(diem_ngon_tro_phai):
        cv2.circle(img_cp, moc, 2, (255, 0, 0), -1)
        cv2.putText(img_cp, str(mang_ten[i]), moc, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    # cv2.imshow('KQ', img)
    # cv2.waitKey(0)

    return diem_ngon_tro_phai, img_cp


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
    # Hai diem cao nhât dễ xác đinh sai truc
    # chi_so_diem_cao_nhat = mang_x.index(min(mang_x))
    # diem_cao_nhat = mang_diem_moc[chi_so_diem_cao_nhat]
    # diem_cao_nhi = mang_diem_moc[chi_so_diem_cao_nhat - 1]
    # print(chi_so_diem_cao_nhat)
    mang_diem = mang_diem_moc[0], mang_diem_moc[2], mang_diem_moc[4]

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

    img_cp = img.copy()
    mang_ten = 30, 31, 32, 33, 34, 35

    diem_mu_tay_phai_phai = []
    mang = diem_so_30, diem_so_31, diem_so_32, diem_so_33, diem_so_34, diem_so_35
    for no_diem, diem in enumerate(mang):
        diem_mu_tay_phai_phai.append((diem[0], diem[1]))

    for i, moc in enumerate(diem_mu_tay_phai_phai):
        cv2.circle(img_cp, moc, 2, (255, 0, 0), -1)
        cv2.putText(img_cp, str(mang_ten[i]), moc, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    # cv2.imshow('annotated_image''', annotated_image)
    # cv2.imshow('KQ', img_cp)
    # cv2.waitKey(0)

    return diem_mu_tay_phai_phai, img_cp


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
    img_cp = img.copy()
    mang_ten = 41, 42, 43, 44

    diem_hai_ngon_tay_phai = []
    if handType == 'Right':
        mang = diem_so_41, diem_so_42, diem_so_43, diem_so_44
        for no_diem, diem in enumerate(mang):
            diem_hai_ngon_tay_phai.append((diem[0], diem[1]))
    if handType == 'Left':
        mang = diem_so_44, diem_so_43, diem_so_42, diem_so_41
        for no_diem, diem in enumerate(mang):
            diem_hai_ngon_tay_phai.append((diem[0], diem[1]))

    for i, moc in enumerate(diem_hai_ngon_tay_phai):
        cv2.circle(img_cp, moc, 2, (255, 0, 0), -1)
        cv2.putText(img_cp, str(mang_ten[i]), moc, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    # cv2.imshow('KQ', img)
    # cv2.waitKey(0)

    return diem_hai_ngon_tay_phai, img_cp


def TimKhoangCachHaiDiemFloat(diem_A, diem_B):
    return math.sqrt(math.pow(diem_A[0] - diem_B[0], 2) + math.pow(diem_A[1] - diem_B[1], 2))


def TimCaoDo(diem_A, diem_B):
    return abs(diem_A[1] - diem_B[1])


def TimNgangDo(diem_A, diem_B):
    return abs(diem_A[0] - diem_B[0])


def TinhToanKhoangCach(mang_diem, mm_tren_pixel):
    mtp = mm_tren_pixel
    hs = 0.95
    mang_kich_thuoc = []

    # <====================> BAT DAU TAY PHAI <====================>
    # Dai ngon ut - 9 - 10
    D1_p = round(TimKhoangCachHaiDiemFloat(mang_diem[8], mang_diem[9]) * mtp * hs, 2)
    mang_kich_thuoc.append(D1_p)

    # Dai ngon ap ut - 7 - 8
    D2_p = round(TimKhoangCachHaiDiemFloat(mang_diem[6], mang_diem[7]) * mtp * hs, 2)
    mang_kich_thuoc.append(D2_p)

    # Dai ngon giua - 5 - 6
    D3_p = round(TimKhoangCachHaiDiemFloat(mang_diem[4], mang_diem[5]) * mtp * hs, 2)
    mang_kich_thuoc.append(D3_p)

    # Dai ngon tro - 3 - 4
    D4_p = round(TimKhoangCachHaiDiemFloat(mang_diem[2], mang_diem[3]) * mtp * hs, 2)
    mang_kich_thuoc.append(D4_p)

    # Dai ngon cai - 1 - 2
    D5_p = round(TimKhoangCachHaiDiemFloat(mang_diem[0], mang_diem[1]) * mtp * hs, 2)
    mang_kich_thuoc.append(D5_p)

    # Dai gan ban tay - 6 - 11
    D6_p = round(TimCaoDo(mang_diem[5], mang_diem[10]) * mtp * hs, 2)
    mang_kich_thuoc.append(D6_p)

    # Dai ban tay - 5 - 11
    D7_p = round(TimCaoDo(mang_diem[4], mang_diem[10]) * mtp * hs, 2)
    mang_kich_thuoc.append(D7_p)

    # Cheo gan ban tay - 36 - 37
    C1_p = round(TimKhoangCachHaiDiemFloat(mang_diem[21], mang_diem[22]) * mtp * hs, 2)
    mang_kich_thuoc.append(C1_p)

    # Rong ngon ut - 29 - 28
    R1_p = round(TimKhoangCachHaiDiemFloat(mang_diem[20], mang_diem[19]) * mtp * hs, 2)
    mang_kich_thuoc.append(R1_p)

    # Rong ngon ap ut - 27 - 26
    R2_p = round(TimKhoangCachHaiDiemFloat(mang_diem[18], mang_diem[17]) * mtp * hs, 2)
    mang_kich_thuoc.append(R2_p)

    # Rong ngon giua - 25 - 24
    R3_p = round(TimKhoangCachHaiDiemFloat(mang_diem[16], mang_diem[15]) * mtp * hs, 2)
    mang_kich_thuoc.append(R3_p)

    # Rong ngon tro - 23 -22
    R4_p = round(TimKhoangCachHaiDiemFloat(mang_diem[14], mang_diem[13]) * mtp * hs, 2)
    mang_kich_thuoc.append(R4_p)

    # Rong ngon cai - 21 -20
    R5_p = round(TimKhoangCachHaiDiemFloat(mang_diem[12], mang_diem[11]) * mtp * hs, 2)
    mang_kich_thuoc.append(R5_p)

    # Rong nam tay - 53 - 54 (b)
    R6_p = round(TimNgangDo(mang_diem[35], mang_diem[36]) * mtp * hs, 2)
    mang_kich_thuoc.append(R6_p)

    # Dai nam tay - 12 - 13
    D8_p = round(TimCaoDo(mang_diem[31], mang_diem[32]) * mtp * hs, 2)
    mang_kich_thuoc.append(D8_p)

    # Rong co tay - 51 - 52
    d_p = round(TimNgangDo(mang_diem[33], mang_diem[34]) * mtp * hs, 2)
    # mang_kich_thuoc.append(d_p)

    # Rong bon ngon - 14 - 15
    R7_p = round(TimKhoangCachHaiDiemFloat(mang_diem[23], mang_diem[24]) * mtp * hs, 2)
    mang_kich_thuoc.append(R7_p)

    # Rong gan ban tay - 16 - 17
    R8_p = round(TimKhoangCachHaiDiemFloat(mang_diem[25], mang_diem[26]) * mtp * hs, 2)
    mang_kich_thuoc.append(R8_p)

    # Rong ban tay - 18 - 19
    R9_p = round(TimKhoangCachHaiDiemFloat(mang_diem[27], mang_diem[28]) * mtp * hs, 2)
    mang_kich_thuoc.append(R9_p)

    # Day ngon cai - 47 - 48
    Da5_p = round(TimKhoangCachHaiDiemFloat(mang_diem[29], mang_diem[30]) * mtp * hs, 2)
    mang_kich_thuoc.append(Da5_p)

    # Day ngon tay ut - 43 - 44
    Da1_p = round(TimKhoangCachHaiDiemFloat(mang_diem[51], mang_diem[52]) * mtp * hs, 2)
    mang_kich_thuoc.append(Da1_p)

    # Day ngon ap ut - 41 - 42
    Da2_p = round(TimKhoangCachHaiDiemFloat(mang_diem[49], mang_diem[50]) * mtp * hs, 2)
    mang_kich_thuoc.append(Da2_p)

    # Day ngon giua - 30 - 31
    Da3_p = round(TimKhoangCachHaiDiemFloat(mang_diem[43], mang_diem[44]) * mtp * hs, 2)
    mang_kich_thuoc.append(Da3_p)

    # Day goc gap khop ban tay - 32 - 33
    Da7_p = round(TimKhoangCachHaiDiemFloat(mang_diem[45], mang_diem[46]) * mtp * hs, 2)
    mang_kich_thuoc.append(Da7_p)

    # Day ban tay - 34 - 35
    Da6_p = round(TimKhoangCachHaiDiemFloat(mang_diem[47], mang_diem[48]) * mtp * hs, 2)
    mang_kich_thuoc.append(Da6_p)

    # Day nam tay (a) - 38 - 39
    a_p = round(TimNgangDo(mang_diem[37], mang_diem[38]) * mtp * hs, 2)
    # mang_kich_thuoc.append(a_p)

    # Day co tay - 49 - 50
    c_p = round(TimNgangDo(mang_diem[39], mang_diem[40]) * mtp * hs, 2)
    # mang_kich_thuoc.append(c_p)

    # Day ngon tro - 45 - 46
    Da4_p = round(TimKhoangCachHaiDiemFloat(mang_diem[41], mang_diem[42]) * mtp * hs, 2)
    mang_kich_thuoc.append(Da4_p)

    # Vòng nắm tay
    # Công thức Ramanujan 1
    a1_p = R6_p / 2
    b1_p = a_p / 2
    V1_p = round(math.pi * (3 * (a1_p + b1_p) - math.sqrt((3 * a1_p + b1_p) * (a1_p + 3 * b1_p))), 2)
    mang_kich_thuoc.append(V1_p)

    # Vòng nắm tay
    # Công thức Ramanujan 1
    a2_p = d_p / 2
    b2_p = c_p / 2
    V2_p = round(math.pi * (3 * (a2_p + b2_p) - math.sqrt((3 * a2_p + b2_p) * (a2_p + 3 * b2_p))), 2)
    mang_kich_thuoc.append(V2_p)

    # <====================> HET TAY PHAI <====================>

    # <====================> BAT DAU TAY TRAI <====================>
    # Dai ngon ut - 9 - 10
    D1_t = round(TimKhoangCachHaiDiemFloat(mang_diem[61], mang_diem[62]) * mtp * hs, 2)
    mang_kich_thuoc.append(D1_t)

    # Dai ngon ap ut - 7 - 8
    D2_t = round(TimKhoangCachHaiDiemFloat(mang_diem[59], mang_diem[60]) * mtp * hs, 2)
    mang_kich_thuoc.append(D2_t)

    # Dai ngon giua - 5 - 6
    D3_t = round(TimKhoangCachHaiDiemFloat(mang_diem[57], mang_diem[58]) * mtp * hs, 2)
    mang_kich_thuoc.append(D3_t)

    # Dai ngon tro - 3 - 4
    D4_t = round(TimKhoangCachHaiDiemFloat(mang_diem[55], mang_diem[56]) * mtp * hs, 2)
    mang_kich_thuoc.append(D4_t)

    # Dai ngon cai - 1 - 2
    D5_t = round(TimKhoangCachHaiDiemFloat(mang_diem[53], mang_diem[54]) * mtp * hs, 2)
    mang_kich_thuoc.append(D5_t)

    # Dai gan ban tay - 6 - 11
    D6_t = round(TimCaoDo(mang_diem[58], mang_diem[63]) * mtp * hs, 2)
    mang_kich_thuoc.append(D6_t)

    # Dai ban tay - 5 - 11
    D7_t = round(TimCaoDo(mang_diem[57], mang_diem[63]) * mtp * hs, 2)
    mang_kich_thuoc.append(D7_t)

    # Cheo gan ban tay - 36 - 37
    C1_t = round(TimKhoangCachHaiDiemFloat(mang_diem[74], mang_diem[75]) * mtp * hs, 2)
    mang_kich_thuoc.append(C1_t)

    # Rong ngon ut - 29 - 28
    R1_t = round(TimKhoangCachHaiDiemFloat(mang_diem[73], mang_diem[72]) * mtp * hs, 2)
    mang_kich_thuoc.append(R1_t)

    # Rong ngon ap ut - 27 - 26
    R2_t = round(TimKhoangCachHaiDiemFloat(mang_diem[71], mang_diem[70]) * mtp * hs, 2)
    mang_kich_thuoc.append(R2_t)

    # Rong ngon giua - 25 - 24
    R3_t = round(TimKhoangCachHaiDiemFloat(mang_diem[69], mang_diem[68]) * mtp * hs, 2)
    mang_kich_thuoc.append(R3_t)

    # Rong ngon tro - 23 -22
    R4_t = round(TimKhoangCachHaiDiemFloat(mang_diem[67], mang_diem[66]) * mtp * hs, 2)
    mang_kich_thuoc.append(R4_t)

    # Rong ngon cai - 21 -20
    R5_t = round(TimKhoangCachHaiDiemFloat(mang_diem[65], mang_diem[64]) * mtp * hs, 2)
    mang_kich_thuoc.append(R5_t)

    # Rong nam tay - 53 - 54 (b)
    R6_t = round(TimNgangDo(mang_diem[88], mang_diem[89]) * mtp * hs, 2)
    mang_kich_thuoc.append(R6_t)

    # Dai nam tay - 12 - 13
    D8_t = round(TimCaoDo(mang_diem[84], mang_diem[85]) * mtp * hs, 2)
    mang_kich_thuoc.append(D8_t)

    # Rong co tay - 51 - 52 (d)
    d_t = round(TimNgangDo(mang_diem[86], mang_diem[87]) * mtp * hs, 2)
    # mang_kich_thuoc.append(d_t)

    # Rong bon ngon - 14 - 15
    R7_t = round(TimKhoangCachHaiDiemFloat(mang_diem[76], mang_diem[77]) * mtp * hs, 2)
    mang_kich_thuoc.append(R7_t)

    # Rong gan ban tay - 16 - 17
    R8_t = round(TimKhoangCachHaiDiemFloat(mang_diem[78], mang_diem[79]) * mtp * hs, 2)
    mang_kich_thuoc.append(R8_t)

    # Rong ban tay - 18 - 19
    R9_t = round(TimKhoangCachHaiDiemFloat(mang_diem[80], mang_diem[81]) * mtp * hs, 2)
    mang_kich_thuoc.append(R9_t)

    # Day ngon cai - 47 - 48
    Da5_t = round(TimKhoangCachHaiDiemFloat(mang_diem[82], mang_diem[83]) * mtp * hs, 2)
    mang_kich_thuoc.append(Da5_t)

    # Day ngon tay ut - 43 - 44
    Da1_t = round(TimKhoangCachHaiDiemFloat(mang_diem[104], mang_diem[105]) * mtp * hs, 2)
    mang_kich_thuoc.append(Da1_t)

    # Day ngon ap ut - 41 - 42
    Da2_t = round(TimKhoangCachHaiDiemFloat(mang_diem[102], mang_diem[103]) * mtp * hs, 2)
    mang_kich_thuoc.append(Da2_t)

    # Day ngon giua - 30 - 31
    Da3_t = round(TimKhoangCachHaiDiemFloat(mang_diem[96], mang_diem[97]) * mtp * hs, 2)
    mang_kich_thuoc.append(Da3_t)

    # Day goc gap khop ban tay - 32 - 33
    Da7_t = round(TimKhoangCachHaiDiemFloat(mang_diem[98], mang_diem[99]) * mtp * hs, 2)
    mang_kich_thuoc.append(Da7_t)

    # Day ban tay - 34 - 35
    Da6_t = round(TimKhoangCachHaiDiemFloat(mang_diem[100], mang_diem[101]) * mtp * hs, 2)
    mang_kich_thuoc.append(Da6_t)

    # Day nam tay (a) - 38 - 39
    a_t = round(TimNgangDo(mang_diem[90], mang_diem[91]) * mtp * hs, 2)
    # mang_kich_thuoc.append(a_t)

    # Day co tay - 49 - 50
    c_t = round(TimNgangDo(mang_diem[92], mang_diem[93]) * mtp * hs, 2)
    # mang_kich_thuoc.append(c_t)

    # Day ngon tro - 45 - 46
    Da4_t = round(TimKhoangCachHaiDiemFloat(mang_diem[94], mang_diem[95]) * mtp * hs, 2)
    mang_kich_thuoc.append(Da4_t)

    # Vòng nắm tay
    # Công thức Ramanujan 1
    a1_t = R6_t / 2
    b1_t = a_t / 2
    V1_t = round(math.pi * (3 * (a1_t + b1_t) - math.sqrt((3 * a1_t + b1_t) * (a1_t + 3 * b1_t))), 2)
    mang_kich_thuoc.append(V1_t)

    # Vòng nắm tay
    # Công thức Ramanujan 1
    a2_t = d_t / 2
    b2_t = c_t / 2
    V2_t = round(math.pi * (3 * (a2_t + b2_t) - math.sqrt((3 * a2_t + b2_t) * (a2_t + 3 * b2_t))), 2)
    mang_kich_thuoc.append(V2_t)
    # <====================> HET TAY TRAI <====================>

    return mang_kich_thuoc


""" =======================> Test <====================== """
img1 = cv2.imread(r'C:\Users\Nguyen Hai\PycharmProjects\pythonProject2\ImageHand\1.jpg')  # ban tay ngua
# img1 = cv2.imread('D:\\HUST\\LAB\DIR\\26-05-2022-14-30-26\\1.png')  # ban tay ngua


img1 = imutils.resize(img1, height=720)
# nguong_1 = self.cur_mang_nguong[0]
nguong_1 = 80
# nguong_1 = 24
diem_tren_tay_ngua, kq_img = NguaBanTayPhai(img1, nguong_1)
print(diem_tren_tay_ngua)
cv2.imshow('kq', kq_img)
cv2.waitKey(0)

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

# # img6 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\13.jpg')  # nguong 65
# img6 = cv2.imread(r'D:\HUST\LAB\DIR\31-05-2022-14-45-56\13.png') # nguong 102
# # img6 = cv2.imread(r'D:\HUST\LAB\DIR\01-06-2022-15-30-34\6.png') # nguong 23
#
# img6 = imutils.resize(img6, height=800)
# # nguong_2 = self.cur_mang_nguong[1]
# # nguong_6 = 28
# nguong_6 = 102
#
# diem_mu_tay_phai, img6_kq = MuTayPhai(img6, nguong_6)
# print(diem_mu_tay_phai)

# # img7 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\App\\handsample\\7.jpg')  # ban tay ngua
# # img7 = cv2.flip(img7, 1)
# img7 = cv2.imread('D:\\HUST\\LAB\DIR\\01-06-2022-15-30-34\\14.png')
# # img7 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\main\\test\\2ngon3.jpg')
# img7 = imutils.resize(img7, height=800)
# # nguong_2 = self.cur_mang_nguong[1]
# # nguong_7 = 90
# nguong_7 = 28
# diem_hai_ngon_tay_phai, img7_kq = HaiNgonTayPhai(img7, nguong_7)
# print(diem_hai_ngon_tay_phai)
# cv2.imshow('hai ngon tay', img7_kq)
# cv2.waitKeyEx(0)
