import imutils

from MyLib import *
from Math import *

if __name__ == "__main__":
    # img = cv2.imread('27-04-2022-13-08-01.png')  # nguoc hand

    # img = cv2.imread('1.png')
    # img = cv2.imread('26-04-2022-23-10-41.png') # left hand
    # img = cv2.imread('27-04-2022-0117-05-2022-16-29-12.png-46-07.png') # left hand
    # img = cv2.imread('captured\\17-05-2022-16-36-01.png') # left hand

    # img = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\captured\\old\\13-05-2022-18-00-06.png')  # left hand
    img0 = cv2.imread('K:\\PROJECT\\PYQT5\\DO_BAN_TAY\\main\\test\\bantayngua.png')  # ban tay ngua
    # img = cv2.imread('13-05-2022-18-00-03.png')
    # img = cv2.imread('tay_up.jpg')  # ban tay ngua

    img0 = imutils.resize(img0, height=800)

    # img = cv2.imread('27-04-2022-01-46-06.png')  # right hand

    # img = cv2.imread('25-04-2022-14-20-55.png')  # right hand
    # img = cv2.imread('27-04-2022-16-37-13.png')  # right hand
    # img = cv2.imread('27-04-2022-16-37-36.png')  # right hand

    mang_diem_moc, annotated_image, handType, image = TimDiemMoc(img0)
    if mang_diem_moc[0][1] < mang_diem_moc[12][1]:
        print('Ảnh bị ngược')
        img0 = cv2.rotate(img0, cv2.ROTATE_180)
        mang_diem_moc, annotated_image, hand_type, image = TimDiemMoc(img0)

    handType = 'Right' if mang_diem_moc[17] <= mang_diem_moc[0] else 'Left'
    img = img0.copy()

    # Khe thu nhat =======================================================
    mang_diem_chua_khe_thu_nhat = [mang_diem_moc[1], mang_diem_moc[3], mang_diem_moc[5], mang_diem_moc[6]]

    day_khe_thu_nhat = PhatHienDiemKheNgonTay(mang_diem_chua_khe_thu_nhat, handType, img, nguong)

    # cv2.circle(img, day_khe_thu_nhat, 2, (255, 0, 0), -1)
    # cv2.putText(img, 'A',
    #             day_khe_thu_nhat, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # Khe thu hai =======================================================
    mang_diem_chua_khe_thu_hai = [mang_diem_moc[5], mang_diem_moc[6], mang_diem_moc[9], mang_diem_moc[10]]

    day_khe_thu_hai = PhatHienDiemKheNgonTay(mang_diem_chua_khe_thu_hai, handType, img, nguong)

    # cv2.circle(img, day_khe_thu_hai, 2, (255, 0, 0), -1)
    # cv2.putText(img, 'B',
    #             day_khe_thu_hai, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # Khe thu ba =======================================================
    mang_diem_chua_khe_thu_ba = [mang_diem_moc[9], mang_diem_moc[10], mang_diem_moc[13], mang_diem_moc[14]]

    day_khe_thu_ba = PhatHienDiemKheNgonTay(mang_diem_chua_khe_thu_ba, handType, img, nguong)

    # cv2.circle(img, day_khe_thu_ba, 2, (255, 0, 0), -1)
    # cv2.putText(img, 'C',
    #             day_khe_thu_ba, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # Khe thu tu =======================================================
    mang_diem_chua_khe_thu_tu = [mang_diem_moc[13], mang_diem_moc[14], mang_diem_moc[17], mang_diem_moc[18]]
    day_khe_thu_tu = PhatHienDiemKheNgonTay(mang_diem_chua_khe_thu_tu, handType, img, nguong)

    # cv2.circle(img, day_khe_thu_tu, 2, (255, 0, 0), -1)
    # cv2.putText(img, 'D',
    #             day_khe_thu_tu, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # Dinh ngon cai =======================================================
    mang_diem_chua_dinh_ngon_cai = [mang_diem_moc[4], mang_diem_moc[3]]
    dinh_ngon_cai = PhatHienDiemDinhNgonTayv1(mang_diem_chua_dinh_ngon_cai, img, nguong)

    cv2.circle(img0, dinh_ngon_cai, 2, (255, 0, 0), -1)
    cv2.putText(img0, '1',
                dinh_ngon_cai, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # Dinh ngon tro =======================================================
    mang_diem_chua_dinh_ngon_tro = [mang_diem_moc[8], mang_diem_moc[7]]
    dinh_ngon_tro = PhatHienDiemDinhNgonTayv1(mang_diem_chua_dinh_ngon_tro, img, nguong)

    cv2.circle(img0, dinh_ngon_tro, 2, (255, 0, 0), -1)
    cv2.putText(img0, '3',
                dinh_ngon_tro, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # Dinh ngon giua =======================================================
    mang_diem_chua_dinh_ngon_giua = [mang_diem_moc[12], mang_diem_moc[11]]
    dinh_ngon_giua = PhatHienDiemDinhNgonTayv1(mang_diem_chua_dinh_ngon_giua, img, nguong)

    cv2.circle(img0, dinh_ngon_giua, 2, (255, 0, 0), -1)
    cv2.putText(img0, '5',
                dinh_ngon_giua, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # Dinh ngon ap ut =======================================================
    mang_diem_chua_dinh_ngon_ap_ut = [mang_diem_moc[16], mang_diem_moc[15]]
    dinh_ngon_ap_ut = PhatHienDiemDinhNgonTayv1(mang_diem_chua_dinh_ngon_ap_ut, img, nguong)

    cv2.circle(img0, dinh_ngon_ap_ut, 2, (255, 0, 0), -1)
    cv2.putText(img0, '7',
                dinh_ngon_ap_ut, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # Dinh ngon ut =======================================================
    mang_diem_chua_dinh_ngon_ut = [mang_diem_moc[20], mang_diem_moc[19]]
    dinh_ngon_ut = PhatHienDiemDinhNgonTayv1(mang_diem_chua_dinh_ngon_ut, img, nguong)

    cv2.circle(img0, dinh_ngon_ut, 2, (255, 0, 0), -1)
    cv2.putText(img0, '9',
                dinh_ngon_ut, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # Chan ngon cai =======================================================
    mang_diem_chua_chan_ngon_cai = [dinh_ngon_cai, mang_diem_moc[2], day_khe_thu_nhat]
    chan_ngon_cai = PhatHienDiemChanNgonTay(mang_diem_chua_chan_ngon_cai)

    cv2.circle(img0, chan_ngon_cai, 2, (255, 0, 0), -1)
    cv2.putText(img0, '2',
                chan_ngon_cai, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # Chan ngon tro =======================================================
    mang_diem_chua_chan_ngon_tro = [dinh_ngon_tro, mang_diem_moc[6], day_khe_thu_hai]
    chan_ngon_tro = PhatHienDiemChanNgonTay(mang_diem_chua_chan_ngon_tro)

    cv2.circle(img0, chan_ngon_tro, 2, (255, 0, 0), -1)
    cv2.putText(img0, '4',
                chan_ngon_tro, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # Chan ngon giua =======================================================
    mang_diem_chua_chan_ngon_giua = [dinh_ngon_giua, mang_diem_moc[10], day_khe_thu_ba, day_khe_thu_hai]
    chan_ngon_giua = PhatHienDiemChanNgonTayv1(mang_diem_chua_chan_ngon_giua)

    cv2.circle(img0, chan_ngon_giua, 2, (255, 0, 0), -1)
    cv2.putText(img0, '6',
                chan_ngon_giua, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # Chan ngon ap ut =======================================================
    mang_diem_chua_chan_ngon_ap_ut = [dinh_ngon_ap_ut, mang_diem_moc[14], day_khe_thu_tu, day_khe_thu_ba]
    chan_ngon_ap_ut = PhatHienDiemChanNgonTayv1(mang_diem_chua_chan_ngon_ap_ut)

    cv2.circle(img0, chan_ngon_ap_ut, 2, (255, 0, 0), -1)
    cv2.putText(img0, '8',
                chan_ngon_ap_ut, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # Chan ngon ut =======================================================
    mang_diem_chua_chan_ngon_ut = [dinh_ngon_ut, mang_diem_moc[18], day_khe_thu_tu]
    chan_ngon_ut = PhatHienDiemChanNgonTay(mang_diem_chua_chan_ngon_ut)

    cv2.circle(img0, chan_ngon_ut, 2, (255, 0, 0), -1)
    cv2.putText(img0, '10',
                chan_ngon_ut, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # Diem 11 (diem 0 trong mang moc) ========================================
    cv2.circle(img0, mang_diem_moc[0], 2, (255, 0, 0), -1)
    cv2.putText(img0, '11',
                mang_diem_moc[0], cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # Do do rong ngon tay
    #
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
    rong_tay_ut_1, rong_tay_ut_2 = TimChieuRongNgonTayV1(mang_diem_rong_tay_ut, img, nguong)
    # cv2.circle(img, rong_1, 2, (255, 0, 0), -1)
    # cv2.putText(img, 'R1',
    #             rong_1, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    # cv2.circle(img, rong_2, 2, (255, 0, 0), -1)
    # cv2.putText(img, 'R2',
    #             rong_2, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # Tìm điểm 36
    mang_diem_36 = (dinh_ngon_tro, chan_ngon_tro, chan_ngon_tro)
    diem_36_A, diem_36_B = TimChieuRongNgonTay(mang_diem_36, img, nguong)
    kc1 = abs(diem_36_A[0] - mang_diem_moc[4][0])
    kc2 = abs(diem_36_B[0] - mang_diem_moc[4][0])
    diem_36 = diem_36_A if (kc1 < kc2) else diem_36_B
    cv2.circle(img0, diem_36, 2, (255, 0, 0), -1)
    cv2.putText(img0, '36',
                diem_36, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # Tìm điểm 37
    mang_diem_37 = (mang_diem_moc[0], mang_diem_moc[17])
    diem_37 = TimDiemSo37(mang_diem_37, img0)
    # print(diem_37)
    cv2.circle(img0, diem_37, 2, (255, 0, 0), -1)
    cv2.putText(img0, '37',
                diem_37, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    VeDuongThangDiQuaHaiDiem(img0, rong_tay_cai_1, rong_tay_cai_2)
    VeDuongThangDiQuaHaiDiem(img0, rong_tay_tro_1, rong_tay_tro_2)
    VeDuongThangDiQuaHaiDiem(img0, rong_tay_giua_1, rong_tay_giua_2)
    VeDuongThangDiQuaHaiDiem(img0, rong_tay_ap_ut_1, rong_tay_ap_ut_2)
    VeDuongThangDiQuaHaiDiem(img0, rong_tay_ut_1, rong_tay_ut_2)

    # cv2.imwrite('KqHien1.png', img0)
    # cv2.imwrite('annotated_image.png', annotated_image)

    cv2.imshow('Anh image', img0)
    # cv2.imshow('Anh crop', dinh_ngon_tro_image_crop)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
