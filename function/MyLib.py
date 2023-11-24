from Hand.function.Math import *
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
mp_drawing_styles = mp.solutions.drawing_styles


# nguong = 65


# nguong = 90

def TimDiemMoc(image):
    """
    Hàm tìm điểm mốc bàn tay
    :param image: ảnh bàn tay
    :return: mảng điểm trên bàn tay
    """
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    # For static images:
    with mp_hands.Hands(
            static_image_mode=True,
            max_num_hands=1,
            min_detection_confidence=0.3) as hands:
        # image = imutils.resize(image, height=800)
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        # print('Handedness:', results.multi_handedness)
        for hand in results.multi_handedness:
            handType = hand.classification[0].label
            # print(handType)
        image_height, image_width, _ = image.shape
        annotated_image = image.copy()
        hand = results.multi_hand_landmarks[0]
        mp_drawing.draw_landmarks(
            annotated_image, hand, mp_hands.HAND_CONNECTIONS)

        mang_diem_moc = []
        for idx, landmark in enumerate(hand.landmark):
            mang_diem_moc.append((round(landmark.x * image_width), round(landmark.y * image_height)))

        for i, moc in enumerate(mang_diem_moc):
            cv2.circle(annotated_image, moc, 2, (255, 0, 0), -1)
            cv2.putText(annotated_image, str(i), moc, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

        return mang_diem_moc, annotated_image, handType, image

def ChupAnhTuCamera(camera_index=0):
    """
    Hàm cho phép chụp ảnh
    :param camera_index: loại camera
    :return: None
    """
    control = 0
    cap = cv2.VideoCapture(camera_index)
    cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)  # Tắt auto focus
    cap.set(cv2.CAP_PROP_FOCUS, 11)
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue
        if control == 0:
            image = cap.read()[1]
        if control == 1:
            image = cv2.flip(image, 1)
        if control == 2:
            image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        if control == 3:
            image = cv2.rotate(image, cv2.ROTATE_180)
        if control == 4:
            image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

        image_rs = imutils.resize(image, height=720)
        cv2.imshow('Camera', image_rs)

        if keyboard.is_pressed('o'):  # if key 'f' is pressed
            control = 0
        if keyboard.is_pressed('f'):  # if key 'f' is pressed
            control = 1
        if keyboard.is_pressed('r'):  # if key 'r' is pressed
            control = 2
        if keyboard.is_pressed('l'):  # if key 'l' is pressed
            control = 3
        if keyboard.is_pressed('s'):  # if key 's' is pressed
            control = 4
        if keyboard.is_pressed('c'):  # if key 'c' is pressed
            print('Capture !')
            cv2.imwrite('captured/' + time.strftime("%d-%m-%Y-%H-%M-%S") + '.png', image)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            cap.release()
            break





def PhatHienDiemKheNgonTay(mang_diem, handType, image, nguong):
    """
    Phát hiện khe ngón tay bằng cách crop các ảnh màu sau đó tìm đường bao
    :param mang_diem: mảng 4 điểm chứa vùng tối ở khe ngón tay
    :param handType: loại bàn tay
    :param image: ảnh đầu vào
    :param nguong: ngưỡng phân biệt đường bao
    :return: điểm khe ngón tay
    """
    """
    Crop lay vung chua khe tu mang 4 diem nhap vao A B C D
    """
    diem_A, diem_B, diem_C, diem_D = mang_diem
    x_max = max(diem_A[0], diem_B[0], diem_C[0], diem_D[0])
    y_max = max(diem_A[1], diem_B[1], diem_C[1], diem_D[1])
    x_min = min(diem_A[0], diem_B[0], diem_C[0], diem_D[0])
    y_min = min(diem_A[1], diem_B[1], diem_C[1], diem_D[1])
    local_coord_crop = [x_min, y_min]
    image_crop = image[y_min: y_max, x_min: x_max]

    """
    Sau khi da crop xong anh vung bao boi cac diem A B C D
    Tim diem chan dua vao đặc diem nam duoi cung và gan ngon cai nhat
    """

    hulls = []
    points_of_hull = []
    diem_day_tren_anh_crop = [0, 0]
    temp = 0

    """
    Tim duong bao và dùng convex hull dong goi cac duong bao ko lien mach 
    de sau do tim duong bao lon nhat
    """
    gray = cv2.cvtColor(image_crop, cv2.COLOR_BGR2GRAY)
    # thres = cv2.threshold(gray, nguong, 255, cv2.THRESH_BINARY_INV)[1]
    # edges = cv2.Canny(thres, 127, 200)
    #
    otsu_threshold, image_result = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU,
    )
    thres = cv2.threshold(gray, otsu_threshold, 255, cv2.THRESH_BINARY_INV)[1]
    # # print("Obtained threshold: ", otsu_threshold)
    edges = cv2.Canny(thres, 127, 200)

    contours_image_crop, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL,
                                                      cv2.CHAIN_APPROX_NONE)

    # thresh = cv2.threshold(gray, nguong, 255, cv2.THRESH_BINARY_INV)[1]
    # contours_image_crop, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    #                                                   cv2.CHAIN_APPROX_NONE)

    hull = []
    for cnt in contours_image_crop:
        hull = cv2.convexHull(cnt)
        hulls.append(hull)
    hull_max = max(hulls, key=cv2.contourArea)

    # cv2.drawContours(image_crop, [hull_max], 0, (0, 255, 0), 1)
    # cv2.imshow('a', image_crop)
    # cv2.waitKey(0)

    if len(contours_image_crop) == 0:
        print('Ko có nguong nao thich hơp')

    diem_moc_duoi_cung = np.max(hull_max, 0)
    # cv2.drawContours(image_crop, [hull], 0, (0, 255, 0), 1)
    # cv2.imshow('a', image_crop)
    # cv2.waitKey()
    """
    Chuyen các diem ve mot mang de xac dịnh diem chan ngón tro
    """

    for point_hull in hull_max:
        points_of_hull.append(point_hull[0])

    """
    Tim diem chan ngón tro với dieu kien nam thap nhat và xa nhat tưc la gan ngon tro nhat
    """

    for point_hull_no, point_hull in enumerate(points_of_hull):
        if point_hull[1] == diem_moc_duoi_cung[0][1]:
            temp = points_of_hull[point_hull_no][0]
            diem_day_tren_anh_crop[1] = diem_moc_duoi_cung[0][1]
            if handType == 'Right':
                if point_hull[0] > temp:
                    temp = points_of_hull[point_hull_no][0]
                diem_day_tren_anh_crop[0] = temp
            if handType == 'Left':
                if point_hull[0] < temp:
                    temp = points_of_hull[point_hull_no][0]
                diem_day_tren_anh_crop[0] = temp

    """
    Sau khi đã tìm được vị trí cua chân ngón trỏ trên anh crop
    Tiến hành xác định lại vị trí đó trên ảnh gốc
    """

    diem_nam_trong_khe = [0, 0]
    diem_nam_trong_khe[0] = local_coord_crop[0] + diem_day_tren_anh_crop[0]
    diem_nam_trong_khe[1] = local_coord_crop[1] + diem_day_tren_anh_crop[1]
    return diem_nam_trong_khe


def PhatHienDiemDinhNgonTay(mang_diem, image, nguong):
    """
    Crop anh dinh ngon tay tro dua vao hai diem 7 và 8
    Với:
    - tâm hcn là diem 8
    - chieu rong là do dai theo phuong y giưa 7 va 8
    - cao bang hai lan rong
    """
    diem_E, diem_F = mang_diem

    # diem E phai nam phia ben tren diem F.
    width = abs(diem_F[1] - diem_E[1])
    hight = 2 * width
    hafl_of_withd = int(width / 2)

    x_min = diem_E[0] - hafl_of_withd
    y_min = diem_E[1] - width
    x_max = x_min + width
    y_max = y_min + hight

    local_coord_crop = [x_min, y_min]
    image_crop = image[y_min: y_max, x_min: x_max]

    """
    Sau khi đã crop xong anh, tim dinh nam cao nhat và gan duong FG nhat 
    """
    hulls = []
    points_of_hull = []
    diem_dinh_tren_anh_crop = [0, 0]
    temp = 0
    mang_khoang_cach_den_duong_EF = []
    mang_so_thu_tu = []
    # Tim duong bao và dùng convex hull dong goi cac duong bao ko lien mach de sau do tim duong bao lon nhat
    gray = cv2.cvtColor(image_crop, cv2.COLOR_BGR2GRAY)

    thres = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                  cv2.THRESH_BINARY, 11, 2)
    thres1 = cv2.threshold(gray, nguong, 255, cv2.THRESH_BINARY)[1]
    edges = cv2.Canny(thres1, 127, 200)

    contours, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        hull = cv2.convexHull(cnt)
        hulls.append(hull)
    # print(len(hulls))

    # Tim duong bao hull lon nhat
    areas = [cv2.contourArea(c) for c in hulls]
    max_index = np.argmax(areas)
    hull = hulls[max_index]
    diem_moc_tren_cung = np.min(hull, 0)

    # Chuyen các diem ve mot mang de xac dịnh diem chan ngón tro
    for point_hull in hull:
        points_of_hull.append(point_hull[0])
    # Tim diem chan ngón tro với dieu kien nam thap nhat và xa nhat tưc la gan ngon tro nhat

    vecto_chi_phuong_EF = [diem_F[0] - diem_E[0], diem_F[1] - diem_E[1]]

    # chon diem gan duong thang 7-8 nhat
    for point_hull_no, point_hull in enumerate(points_of_hull):
        if point_hull[1] == diem_moc_tren_cung[0][1]:
            d = math.fabs(
                (point_hull[0] - diem_F[0]) * vecto_chi_phuong_EF[1] + (diem_F[1] - point_hull[1]) *
                vecto_chi_phuong_EF[0]) / math.sqrt(
                math.pow(vecto_chi_phuong_EF[0], 2) + math.pow(vecto_chi_phuong_EF[1], 2))

            mang_khoang_cach_den_duong_EF.append(d)
            mang_so_thu_tu.append(point_hull_no)

    diem_dinh_tren_anh_crop[1] = diem_moc_tren_cung[0][1]
    d_min = min(mang_khoang_cach_den_duong_EF)

    for d_no, d in enumerate(mang_khoang_cach_den_duong_EF):
        if d == d_min:
            idx = mang_so_thu_tu[d_no]
            diem_dinh_tren_anh_crop[0] = points_of_hull[idx][0]

    # cv2.drawContours(image_crop, [hull], 0, (0, 255, 0), 1)
    # cv2.circle(image_crop, diem_dinh_tren_anh_crop, 2, (0, 0, 255), -1)
    """
    Sau khi đã tìm được vị trí cua chân ngón trỏ trên anh crop
    Tiến hành xác định lại vị trí đó trên ảnh gốc
    """
    diem_dinh_tren_anh_goc = [0, 0]
    diem_dinh_tren_anh_goc[0] = local_coord_crop[0] + diem_dinh_tren_anh_crop[0]
    diem_dinh_tren_anh_goc[1] = local_coord_crop[1] + diem_dinh_tren_anh_crop[1]
    return diem_dinh_tren_anh_goc


def PhatHienDiemDinhNgonTayv1(mang_diem, image, nguong):
    """
    Crop anh dinh ngon tay tro dua vao hai diem 7 và 8
    Với:
    - tâm hcn là diem 8
    - chieu rong là do dai theo phuong y giưa 7 va 8
    - cao bang hai lan rong
    """
    diem_E, diem_F = mang_diem

    # diem E phai nam phia ben tren diem F.

    a, b, c = TimPhuongTrinhDuongThangBietHaiDiem(diem_E, diem_F)
    # He so goc k = -a/b
    alpha = 0
    if b != 0:
        k = -a / b
        alpha_rad = math.atan(k)  # rad
        alpha_deg = math.degrees(alpha_rad)  # deg
        if alpha_deg < 0:
            alpha = alpha_deg + 90
        if alpha_deg >= 0:
            alpha = alpha_deg - 90

    anh_xoay_lan_1, rot, h, w = rotationAngleInDegrees(image, alpha)

    diem_E_new = [0, 0]
    diem_E_new[0] = round(diem_E[0] * rot[0, 0] + diem_E[1] * rot[0, 1] + rot[0, 2])
    diem_E_new[1] = round(diem_E[0] * rot[1, 0] + diem_E[1] * rot[1, 1] + rot[1, 2])

    diem_F_new = [0, 0]
    diem_F_new[0] = round(diem_F[0] * rot[0, 0] + diem_F[1] * rot[0, 1] + rot[0, 2])
    diem_F_new[1] = round(diem_F[0] * rot[1, 0] + diem_F[1] * rot[1, 1] + rot[1, 2])

    width = abs(diem_F_new[1] - diem_E_new[1])
    hight = 2 * width
    hafl_of_withd = int(width / 2)

    x_min = diem_E_new[0] - hafl_of_withd
    y_min = diem_E_new[1] - width
    x_max = x_min + width
    y_max = y_min + hight

    local_coord_crop = [x_min, y_min]
    image_crop = anh_xoay_lan_1[y_min: y_max, x_min: x_max]

    """
    Sau khi đã crop xong anh, tim dinh nam cao nhat và gan duong FG nhat 
    """
    hulls = []
    points_of_hull = []
    diem_dinh_tren_anh_crop = [0, 0]
    temp = 0
    mang_khoang_cach_den_duong_EF = []
    mang_so_thu_tu = []
    nguong_new = nguong
    # Tim duong bao và dùng convex hull dong goi cac duong bao ko lien mach de sau do tim duong bao lon nhat
    gray = cv2.cvtColor(image_crop, cv2.COLOR_BGR2GRAY)

    # thres = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #                               cv2.THRESH_BINARY, 11, 2)
    thres1 = cv2.threshold(gray, nguong, 255, cv2.THRESH_BINARY)[1]
    edges = cv2.Canny(thres1, 127, 200)

    # otsu_threshold, image_result = cv2.threshold(
    #     gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU,
    # )
    # thres = cv2.threshold(gray, otsu_threshold, 255, cv2.THRESH_BINARY)[1]
    # # print("Obtained threshold: ", otsu_threshold)
    # edges = cv2.Canny(thres, 127, 200)

    contours, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    while len(contours) == 0 and nguong_new != 255:
        nguong_new = nguong_new + 5
        thres_tang = cv2.threshold(gray, nguong_new, 255, cv2.THRESH_BINARY)[1]
        edges = cv2.Canny(thres_tang, 127, 200)
        contours, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_NONE)

    nguong_new = nguong
    while len(contours) == 0 and nguong_new != 0:
        nguong_new = nguong_new - 5
        thres_tang = cv2.threshold(gray, nguong_new, 255, cv2.THRESH_BINARY)[1]
        edges = cv2.Canny(thres_tang, 127, 200)
        contours, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_NONE)

    if len(contours) == 0:
        print('Ko có nguong nao thich hơp')

    for cnt in contours:
        hull = cv2.convexHull(cnt)
        hulls.append(hull)
    # print(len(hulls))

    # Tim duong bao hull lon nhat
    areas = [cv2.contourArea(c) for c in hulls]
    max_index = np.argmax(areas)
    hull = hulls[max_index]
    diem_moc_tren_cung = np.min(hull, 0)

    # Chuyen các diem ve mot mang de xac dịnh diem chan ngón tro
    for point_hull in hull:
        points_of_hull.append(point_hull[0])
    # Tim diem chan ngón tro với dieu kien nam thap nhat và xa nhat tưc la gan ngon tro nhat

    vecto_chi_phuong_EF = [diem_F_new[0] - diem_E_new[0], diem_F_new[1] - diem_E_new[1]]

    # chon diem gan duong thang 7-8 nhat
    for point_hull_no, point_hull in enumerate(points_of_hull):
        if point_hull[1] == diem_moc_tren_cung[0][1]:
            d = math.fabs(
                (point_hull[0] - diem_F_new[0]) * vecto_chi_phuong_EF[1] + (diem_F_new[1] - point_hull[1]) *
                vecto_chi_phuong_EF[0]) / math.sqrt(
                math.pow(vecto_chi_phuong_EF[0], 2) + math.pow(vecto_chi_phuong_EF[1], 2))

            mang_khoang_cach_den_duong_EF.append(d)
            mang_so_thu_tu.append(point_hull_no)

    diem_dinh_tren_anh_crop[1] = diem_moc_tren_cung[0][1]
    d_min = min(mang_khoang_cach_den_duong_EF)

    for d_no, d in enumerate(mang_khoang_cach_den_duong_EF):
        if d == d_min:
            idx = mang_so_thu_tu[d_no]
            diem_dinh_tren_anh_crop[0] = points_of_hull[idx][0]

    # cv2.drawContours(image_crop, [hull], 0, (0, 255, 0), 1)
    # cv2.circle(image_crop, diem_dinh_tren_anh_crop, 2, (0, 0, 255), -1)
    """
    Sau khi đã tìm được vị trí cua chân ngón trỏ trên anh crop
    Tiến hành xác định lại vị trí đó trên ảnh gốc
    """

    diem_dinh_tren_anh_xoay_1 = [0, 0]
    diem_dinh_tren_anh_xoay_1[0] = local_coord_crop[0] + diem_dinh_tren_anh_crop[0]
    diem_dinh_tren_anh_xoay_1[1] = local_coord_crop[1] + diem_dinh_tren_anh_crop[1]

    anh_xoay_lan_2, rot2 = rotationAngleInDegreesBack(anh_xoay_lan_1, - alpha, h, w)

    diem_dinh_tren_anh_crop_back = [0, 0]
    diem_dinh_tren_anh_crop_back[0] = round(
        diem_dinh_tren_anh_xoay_1[0] * rot2[0, 0] + diem_dinh_tren_anh_xoay_1[1] * rot2[0, 1] + rot2[0, 2])
    diem_dinh_tren_anh_crop_back[1] = round(
        diem_dinh_tren_anh_xoay_1[0] * rot2[1, 0] + diem_dinh_tren_anh_xoay_1[1] * rot2[1, 1] + rot2[1, 2])

    return diem_dinh_tren_anh_crop_back


def PhatHienDiemChanNgonTay(mang_diem):
    # Tru ngon 3 va 4
    diem_dinh, diem_tren_truc, diem_khe = mang_diem
    a0, b0, c0 = TimPhuongTrinhDuongThangVuongGocVoiDuongThang(diem_dinh, diem_tren_truc, diem_khe)
    a1, b1, c1 = TimPhuongTrinhDuongThangBietHaiDiem(diem_dinh, diem_tren_truc)

    d0 = [a0, b0, c0]
    d1 = [a1, b1, c1]

    giao_diem = TimGiaoDiemHaiDuongThang(d0, d1)
    return giao_diem


def PhatHienDiemChanNgonTayv1(mang_diem):
    # Chi ngon 3 va 4
    diem_dinh, diem_tren_truc, diem_khe_trc, diem_khe_sau = mang_diem
    a0, b0, c0 = TimPhuongTrinhDuongThangBietHaiDiem(diem_khe_trc, diem_khe_sau)
    a1, b1, c1 = TimPhuongTrinhDuongThangBietHaiDiem(diem_dinh, diem_tren_truc)

    d0 = [a0, b0, c0]
    d1 = [a1, b1, c1]

    giao_diem = TimGiaoDiemHaiDuongThang(d0, d1)
    return giao_diem


def PhatHienDiemChanNgonTayUt(mang_diem):
    # Chi ngon ut
    diem_dinh, diem_tren_truc, diem_khe_thu_3, diem_khe_thu_4 = mang_diem
    a0, b0, c0 = TimPhuongTrinhDuongThangBietHaiDiem(diem_khe_thu_3, diem_khe_thu_4)
    a1, b1, c1 = TimPhuongTrinhDuongThangBietHaiDiem(diem_dinh, diem_tren_truc)

    d0 = [a0, b0, c0]
    d1 = [a1, b1, c1]

    giao_diem = TimGiaoDiemHaiDuongThang(d0, d1)
    return giao_diem


def TimChieuRongNgonTay(mang_diem, img, nguong):
    dinh_ngon_tro, chan_ngon_tro, mang_diem_moc_4 = mang_diem
    image = img.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(gray, nguong, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)
    # thres_adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #                               cv2.THRESH_BINARY, 11, 2)
    # otsu_threshold, thresh_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    # cnts = imutils.grab_contours(cnts)
    if len(cnts) != 0:
        c = max(cnts, key=cv2.contourArea)
        for i in range(len(c)):
            cv2.drawContours(image, [c], -1, (240, 0, 159), 2)
    # cv2.imshow('img', image)
    # cv2.waitKey()

    # VeDuongThangDiQuaHaiDiem(img, dinh_ngon_tro, chan_ngon_tro)
    a1, b1, c1 = TimPhuongTrinhDuongThangVuongGocVoiDuongThang(dinh_ngon_tro, chan_ngon_tro, mang_diem_moc_4)
    x = mang_diem_moc_4[0]
    while True:
        y = round((- c1 - a1 * x) / b1)
        (B, G, R) = image[y, x]
        if (B, G, R) == (240, 0, 159):
            rong_1 = (x, y)
            break
        else:
            x = x + 1

    x = mang_diem_moc_4[0]
    while True:
        y = round((- c1 - a1 * x) / b1)
        (B, G, R) = image[y, x]
        if (B, G, R) == (240, 0, 159):
            rong_2 = (x, y)
            break
        else:
            x = x - 1
    return rong_1, rong_2


def TimChieuRongNgonTayV1(mang_diem, img, nguong):
    dinh_ngon_tro, chan_ngon_tro, mang_diem_moc_4 = mang_diem
    image = img.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(gray, nguong, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)
    # thres_adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #                               cv2.THRESH_BINARY, 11, 2)
    # otsu_threshold, thresh_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    # cnts = imutils.grab_contours(cnts)
    contour = []
    if len(cnts) != 0:
        c = max(cnts, key=cv2.contourArea)
        for i in range(len(c)):
            cv2.drawContours(image, [c], -1, (240, 0, 159), 2)
            contour.append(c[i][0])

    # VeDuongThangDiQuaHaiDiem(img, dinh_ngon_tro, chan_ngon_tro)
    a1, b1, c1 = TimPhuongTrinhDuongThangVuongGocVoiDuongThang(dinh_ngon_tro, chan_ngon_tro, mang_diem_moc_4)
    d1 = a1, b1, c1
    mang_cac_diem_rong_1 = []
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            (B, G, R) = image[i, j]
            if (B, G, R) == (240, 0, 159):
                if j < mang_diem_moc_4[0]:
                    point = (j, i)
                    kc = TimKhoangCachTuDiemDenDuongThang(point, d1)
                    if kc <= 1:
                        mang_cac_diem_rong_1.append(point)
    mang_cac_diem_rong_1.sort(key=lambda a: a[0], reverse=True)
    rong_1 = mang_cac_diem_rong_1[0]

    mang_cac_diem_rong_2 = []
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            (B, G, R) = image[i, j]
            if (B, G, R) == (240, 0, 159):
                if j > mang_diem_moc_4[0]:
                    point = (j, i)
                    kc = TimKhoangCachTuDiemDenDuongThang(point, d1)
                    if kc <= 1:
                        mang_cac_diem_rong_2.append(point)
    mang_cac_diem_rong_2.sort(key=lambda a: a[0], reverse=False)
    rong_2 = mang_cac_diem_rong_2[0]

    # x = mang_diem_moc_4[0]
    # while True:
    #     y = round((- c1 - a1 * x) / b1)
    #     (B, G, R) = image[y, x]
    #     if (B, G, R) == (240, 0, 159):
    #         rong_1 = (x, y)
    #         break
    #     else:
    #         x = x + 1
    #
    # x = mang_diem_moc_4[0]
    # while True:
    #     y = round((- c1 - a1 * x) / b1)
    #     (B, G, R) = image[y, x]
    #     if (B, G, R) == (240, 0, 159):
    #         rong_2 = (x, y)
    #         break
    #     else:
    #         x = x - 1

    # mang_cac_diem_rong_1 = []
    # for point_no, point in enumerate(contour):
    #     if point[0] < mang_diem_moc_4[0]:
    #         kc = TimKhoangCachTuDiemDenDuongThang(point, d1)
    #         if kc <= 3:
    #             mang_cac_diem_rong_1.append(point)
    #
    # mang_cac_diem_rong_1.sort(key=lambda a: a[0], reverse=True)
    # rong_1 = mang_cac_diem_rong_1[0]
    #
    # mang_cac_diem_rong_2 = []
    # for point_no, point in enumerate(contour):
    #     if point[0] > mang_diem_moc_4[0]:
    #         kc = TimKhoangCachTuDiemDenDuongThang(point, d1)
    #         if kc <= 2:
    #             mang_cac_diem_rong_2.append(point)
    # print(mang_cac_diem_rong_2)
    # mang_cac_diem_rong_2.sort(key=lambda a: a[0], reverse=False)
    # rong_2 = mang_cac_diem_rong_2[0]
    return rong_1, rong_2


def TimDiemSo37(mang_diem, img, nguong):
    diem_37 = []
    mang_diem_moc_0, mang_diem_moc_17 = mang_diem
    image = img.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(gray, nguong, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)
    # thres_adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #                               cv2.THRESH_BINARY, 11, 2)
    # otsu_threshold, thresh_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    # cnts = imutils.grab_contours(cnts)

    contour = []

    try:
        if len(cnts) != 0:
            c = max(cnts, key=cv2.contourArea)
            for i in range(len(c)):
                cv2.drawContours(image, [c], -1, (240, 0, 159), 1)
                contour.append(c[i][0])
    except:
        print('Non contour')
    # print(c[1][0])
    # print(contour[0])
    # print(len(contour))
    hand_type = 'phai' if mang_diem_moc_17 <= mang_diem_moc_0 else 'trai'
    if hand_type == 'phai':
        kc = TimKhoangCachHaiDiem(mang_diem_moc_0, mang_diem_moc_17)
        for point_no, point in enumerate(contour):
            if point[0] < mang_diem_moc_0[0] and point[1] > mang_diem_moc_17[1]:
                kc_new = TimKhoangCachHaiDiem(point, mang_diem_moc_0)
                if kc_new < kc:
                    kc = kc_new
                    diem_37 = contour[point_no]
    if hand_type == 'trai':
        kc = TimKhoangCachHaiDiem(mang_diem_moc_0, mang_diem_moc_17)
        for point_no, point in enumerate(contour):
            if point[0] > mang_diem_moc_0[0] and point[1] > mang_diem_moc_17[1]:
                kc_new = TimKhoangCachHaiDiem(point, mang_diem_moc_0)
                if kc_new < kc:
                    kc = kc_new
                    diem_37 = contour[point_no]
    try:
        diem_37[1] == image.shape[1]
    except:
        print('Tay ban ko dung tu the hoac de qua thap')

    # cv2.imshow('boder', image)
    # cv2.waitKey(0)
    return diem_37


def TimDiemSo_12_53_54_51_52(mang_diem, img, nguong, handType):
    diem_so_53, diem_so_54, diem_so_51, diem_so_52 = [], [], [], []
    mang_diem_0, mang_diem_1, mang_diem_3 = mang_diem
    image = img.copy()
    h, w = image.shape[:2]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(gray, nguong, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)
    # thres_adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #                               cv2.THRESH_BINARY, 11, 2)
    # otsu_threshold, thresh_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    # cnts = imutils.grab_contours(cnts)

    contour = []
    contour_x = []
    contour_y = []
    try:
        if len(cnts) != 0:
            c = max(cnts, key=cv2.contourArea)
            for i in range(len(c)):
                cv2.drawContours(image, [c], -1, (240, 0, 159), 1)
                contour.append(c[i][0])
                contour_x.append(c[i][0][0])
                contour_y.append(c[i][0][1])

    except:
        print('Non contour')
    # cv2.imshow('img', image)
    # cv2.waitKey()
    chi_so_diem_12 = contour_y.index(min(contour_y))
    diem_so_12 = contour[chi_so_diem_12]

    contour_x_1 = contour_x
    if handType == 'Right':
        for point_no, point in enumerate(contour):
            if point[1] < mang_diem_3[1]:
                contour_x_1[point_no] = 0
            if point[1] > mang_diem_1[1]:
                contour_x_1[point_no] = 0

        chi_so_diem_53 = contour_x_1.index(max(contour_x_1))
        diem_so_53 = contour[chi_so_diem_53]

        x = diem_so_53[0]
        y = diem_so_53[1]
        while True:
            (B, G, R) = image[y, x]
            if (B, G, R) == (240, 0, 159) and abs(x - diem_so_53[0]) > 5:
                diem_so_54 = (x, y)
                break
            else:
                x = x - 1

        # OLD VERSION

        # chi_so_diem_54 = contour_x.index(min(contour_x))
        # diem_so_54 = contour[chi_so_diem_54]

        # contour_y_1 = contour_y.copy()
        # contour_y_2 = contour_y.copy()
        #
        # for point_no, point in enumerate(contour):
        #     if point[0] < mang_diem_0[0]:
        #         contour_y_1[point_no] = 0
        #     if point[0] > mang_diem_0[0]:
        #         contour_y_2[point_no] = 0
        #
        # chi_so_diem_51 = contour_y_1.index(max(contour_y_1))
        # diem_so_51 = contour[chi_so_diem_51]
        #
        # chi_so_diem_52 = contour_y_2.index(max(contour_y_2))
        # diem_so_52 = contour[chi_so_diem_52]
        x = 0
        y = h - 1
        while True:
            (B, G, R) = image[y, x]
            if (B, G, R) == (240, 0, 159):
                diem_so_51 = (x, y)
                break
            else:
                x = x + 1

        x = w - 1
        y = h - 1
        while True:
            (B, G, R) = image[y, x]
            if (B, G, R) == (240, 0, 159):
                diem_so_52 = (x, y)
                break
            else:
                x = x - 1
        # =========================================

    if handType == 'Left':
        for point_no, point in enumerate(contour):
            if point[1] < mang_diem_3[1]:
                contour_x_1[point_no] = w
            if point[1] > mang_diem_1[1]:
                contour_x_1[point_no] = w

        chi_so_diem_53 = contour_x_1.index(min(contour_x_1))
        diem_so_53 = contour[chi_so_diem_53]

        x = diem_so_53[0]
        y = diem_so_53[1]
        while True:
            (B, G, R) = image[y, x]
            if (B, G, R) == (240, 0, 159) and abs(x - diem_so_53[0]) > 5:
                diem_so_54 = (x, y)
                break
            else:
                x = x + 1

        # chi_so_diem_54 = contour_x.index(min(contour_x))
        # diem_so_54 = contour[chi_so_diem_54]

        # contour_y_1 = contour_y.copy()
        # contour_y_2 = contour_y.copy()
        #
        # for point_no, point in enumerate(contour):
        #     if point[0] < mang_diem_0[0]:
        #         contour_y_1[point_no] = 0
        #     if point[0] > mang_diem_0[0]:
        #         contour_y_2[point_no] = 0
        #
        # chi_so_diem_52 = contour_y_1.index(max(contour_y_1))
        # diem_so_52 = contour[chi_so_diem_52]
        #
        # chi_so_diem_51 = contour_y_2.index(max(contour_y_2))
        # diem_so_51 = contour[chi_so_diem_51]
        #
        x = 0
        y = h - 1
        while True:
            (B, G, R) = image[y, x]
            if (B, G, R) == (240, 0, 159):
                diem_so_52 = (x, y)
                break
            else:
                x = x + 1

        x = w - 1
        y = h - 1
        while True:
            (B, G, R) = image[y, x]
            if (B, G, R) == (240, 0, 159):
                diem_so_51 = (x, y)
                break
            else:
                x = x - 1

    return diem_so_12, diem_so_53, diem_so_54, diem_so_51, diem_so_52


def TimDiemSo_38_39_49_50_tay_phai(mang_diem, img, nguong, handType):
    mang_diem_0, mang_diem_6 = mang_diem
    image = img.copy()
    h, w = img.shape[:2]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(gray, nguong, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)
    # thres_adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #                               cv2.THRESH_BINARY, 11, 2)
    # otsu_threshold, thresh_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    # cnts = imutils.grab_contours(cnts)

    contour = []
    contour_x = []
    contour_y = []
    try:
        if len(cnts) != 0:
            c = max(cnts, key=cv2.contourArea)
            for i in range(len(c)):
                cv2.drawContours(image, [c], -1, (240, 0, 159), 1)
                contour.append(c[i][0])
                contour_x.append(c[i][0][0])
                contour_y.append(c[i][0][1])

    except:
        print('Non contour')
    # cv2.imshow('img', image)
    # cv2.waitKey()

    diem_so_38 = []
    diem_so_39 = []
    diem_so_50 = []
    diem_so_49 = []

    contour_x_1 = contour_x
    if handType == 'Right':
        for point_no, point in enumerate(contour):
            if point[1] < mang_diem_6[1]:
                contour_x_1[point_no] = 0
            if point[1] > mang_diem_0[1]:
                contour_x_1[point_no] = 0

        chi_so_diem_38 = contour_x_1.index(max(contour_x_1))
        diem_so_38 = contour[chi_so_diem_38]

        x = diem_so_38[0]
        y = diem_so_38[1]
        while True:
            (B, G, R) = image[y, x]
            if (B, G, R) == (240, 0, 159) and abs(x - diem_so_38[0]) > 3:
                diem_so_39 = (x, y)
                break
            else:
                x = x - 1

        x = 0
        y = h - 1
        while True:
            (B, G, R) = image[y, x]
            if (B, G, R) == (240, 0, 159):
                diem_so_50 = (x, y)
                break
            else:
                x = x + 1

        x = w - 1
        y = h - 1
        while True:
            (B, G, R) = image[y, x]
            if (B, G, R) == (240, 0, 159):
                diem_so_49 = (x, y)
                break
            else:
                x = x - 1

    if handType == 'Left':
        for point_no, point in enumerate(contour):
            if point[1] < mang_diem_6[1]:
                contour_x_1[point_no] = w
            if point[1] > mang_diem_0[1]:
                contour_x_1[point_no] = w

        chi_so_diem_38 = contour_x_1.index(min(contour_x_1))
        diem_so_38 = contour[chi_so_diem_38]

        x = diem_so_38[0]
        y = diem_so_38[1]
        while True:
            (B, G, R) = image[y, x]
            if (B, G, R) == (240, 0, 159) and abs(x - diem_so_38[0]) > 3:
                diem_so_39 = (x, y)
                break
            else:
                x = x + 1

        x = 0
        y = h - 1
        while True:
            (B, G, R) = image[y, x]
            if (B, G, R) == (240, 0, 159):
                diem_so_49 = (x, y)
                break
            else:
                x = x + 1

        x = w - 1
        y = h - 1
        while True:
            (B, G, R) = image[y, x]
            if (B, G, R) == (240, 0, 159):
                diem_so_50 = (x, y)
                break
            else:
                x = x - 1

    return diem_so_38, diem_so_39, diem_so_50, diem_so_49


def TimDiemSo_38_39_49_50(mang_diem, img, nguong):
    mang_diem_0 = mang_diem
    image = img.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(gray, nguong, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)
    # thres_adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #                               cv2.THRESH_BINARY, 11, 2)
    # otsu_threshold, thresh_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    # cnts = imutils.grab_contours(cnts)

    contour = []
    contour_x = []
    contour_y = []
    try:
        if len(cnts) != 0:
            c = max(cnts, key=cv2.contourArea)
            for i in range(len(c)):
                cv2.drawContours(image, [c], -1, (240, 0, 159), 1)
                contour.append(c[i][0])
                contour_x.append(c[i][0][0])
                contour_y.append(c[i][0][1])

    except:
        print('Non contour')
    # cv2.imshow('img', image)
    # cv2.waitKey()

    chi_so_diem_38 = contour_x.index(max(contour_x))
    diem_so_38 = contour[chi_so_diem_38]

    diem_so_39 = []
    for point_no, point in enumerate(contour):
        if point[1] == diem_so_38[1] and point[0] < mang_diem_0[0]:
            diem_so_39 = contour[point_no]

    contour_y_1 = contour_y.copy()
    contour_y_2 = contour_y.copy()

    for point_no, point in enumerate(contour):
        if point[0] < mang_diem_0[0]:
            contour_y_1[point_no] = 0
        if point[0] > mang_diem_0[0]:
            contour_y_2[point_no] = 0

    chi_so_diem_50 = contour_y_1.index(max(contour_y_1))
    diem_so_50 = contour[chi_so_diem_50]

    chi_so_diem_49 = contour_y_2.index(max(contour_y_2))
    diem_so_49 = contour[chi_so_diem_49]

    return diem_so_38, diem_so_39, diem_so_50, diem_so_49


def TimDiem_14_16_18(mang_diem, img, nguong):
    dinh_ngon_tro, chan_ngon_tro, mang_diem_moc_4, day_khe_thu_nhat = mang_diem
    image = img.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(gray, nguong, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)
    # thres_adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #                               cv2.THRESH_BINARY, 11, 2)
    # otsu_threshold, thresh_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    # cnts = imutils.grab_contours(cnts)

    contour = []
    contour_x = []
    contour_y = []
    try:
        if len(cnts) != 0:
            c = max(cnts, key=cv2.contourArea)
            for i in range(len(c)):
                cv2.drawContours(image, [c], -1, (240, 0, 159), 1)
                contour.append(c[i][0])
                contour_x.append(c[i][0][0])
                contour_y.append(c[i][0][1])

    except:
        print('Non contour')
    # cv2.imshow('img', image)
    # cv2.waitKey()

    # Tìm điểm 14 trung vói diem 36
    mang_diem_14 = (dinh_ngon_tro, chan_ngon_tro, chan_ngon_tro)
    diem_14_A, diem_14_B = TimChieuRongNgonTay(mang_diem_14, img, nguong)
    kc1 = abs(diem_14_A[0] - mang_diem_moc_4[0])
    kc2 = abs(diem_14_B[0] - mang_diem_moc_4[0])
    diem_so_14 = diem_14_A if (kc1 < kc2) else diem_14_B
    diem_so_16 = day_khe_thu_nhat

    a0, b0, c0 = TimPhuongTrinhDuongThangBietHaiDiem(diem_so_14, diem_so_16)
    diem_so_18 = []
    y = day_khe_thu_nhat[1]
    while True:
        x = round((- c0 - b0 * y) / a0)
        (B, G, R) = image[y, x]
        if (B, G, R) == (240, 0, 159):
            diem_so_18 = (x, y)
            break
        else:
            y = y + 1

    return diem_so_14, diem_so_16, diem_so_18


def TimDiem_15_17_19(mang_diem, img, handType, nguong):
    """
    Tim cac diem 15 17 19
    :param mang_diem: diem_so_6, diem_so_5, diem_so_14, diem_so_16, diem_so_18, chan_ngon_ut
    :param img: anh dau vao
    :param handType: loại bàn tay
    :param nguong: nguong phân biệt đường bao
    :return: mảng điểm 15 17 19

    Đã tối ưu 1 lần
    """

    diem_so_6, diem_so_5, diem_so_14, diem_so_16, diem_so_18, chan_ngon_ut = mang_diem
    image = img.copy()
    h, w = img.shape[:2]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(gray, nguong, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)
    # thres_adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #                               cv2.THRESH_BINARY, 11, 2)
    # otsu_threshold, thresh_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    # cnts = imutils.grab_contours(cnts)
    contour = []
    contour_x = []
    contour_y = []
    try:
        if len(cnts) != 0:
            c = max(cnts, key=cv2.contourArea)
            for i in range(len(c)):
                cv2.drawContours(image, [c], -1, (240, 0, 159), 1)
                contour.append(c[i][0])
                contour_x.append(c[i][0][0])
                contour_y.append(c[i][0][1])

    except:
        print('Non contour')
    # cv2.imshow('img', image)
    # cv2.waitKey()

    # Tim diem 17
    a0, b0, c0 = TimPhuongTrinhDuongThangVuongGocVoiDuongThang(diem_so_6, diem_so_5, diem_so_16)
    diem_so_17 = []
    if handType == 'Right':
        # x = diem_so_16[0]
        x = w - 1
        while True:
            y = round((- c0 - a0 * x) / b0)
            (B, G, R) = image[y, x]
            # if (B, G, R) == (240, 0, 159) and x > chan_ngon_ut[0]:
            if (B, G, R) == (240, 0, 159):
                diem_so_17 = (x, y)
                break
            else:
                x = x - 1
    if handType == 'Left':
        # x = diem_so_16[0]
        x = 0
        while True:
            y = round((- c0 - a0 * x) / b0)
            (B, G, R) = image[y, x]
            # if (B, G, R) == (240, 0, 159) and x < chan_ngon_ut[0]:
            if (B, G, R) == (240, 0, 159):
                diem_so_17 = (x, y)
                break
            else:
                x = x + 1

    # Tim diem 15
    a0, b0, c0 = TimPhuongTrinhDuongThangVuongGocVoiDuongThang(diem_so_6, diem_so_5, diem_so_14)
    diem_so_15 = []
    if handType == 'Right':
        # x = diem_so_14[0]
        x = w - 1
        while True:
            y = round((- c0 - a0 * x) / b0)
            (B, G, R) = image[y, x]
            # if (B, G, R) == (240, 0, 159) and x > chan_ngon_ut[0]:
            if (B, G, R) == (240, 0, 159):
                diem_so_15 = (x, y)
                break
            else:
                x = x - 1
    if handType == 'Left':
        # x = diem_so_14[0]
        x = 0
        while True:
            y = round((- c0 - a0 * x) / b0)
            (B, G, R) = image[y, x]
            # if (B, G, R) == (240, 0, 159) and x < chan_ngon_ut[0]:
            if (B, G, R) == (240, 0, 159):
                diem_so_15 = (x, y)
                break
            else:
                x = x + 1

    # Tim diem 19
    a0, b0, c0 = TimPhuongTrinhDuongThangVuongGocVoiDuongThang(diem_so_6, diem_so_5, diem_so_18)
    diem_so_19 = []
    if handType == 'Right':
        # x = diem_so_18[0]
        x = w - 1
        while True:
            y = round((- c0 - a0 * x) / b0)
            (B, G, R) = image[y, x]
            # if (B, G, R) == (240, 0, 159) and x > chan_ngon_ut[0]:
            if (B, G, R) == (240, 0, 159):
                diem_so_19 = (x, y)
                break
            else:
                x = x - 1
    if handType == 'Left':
        # x = diem_so_18[0]
        x = 0
        while True:
            y = round((- c0 - a0 * x) / b0)
            (B, G, R) = image[y, x]
            # if (B, G, R) == (240, 0, 159) and x < chan_ngon_ut[0]:
            if (B, G, R) == (240, 0, 159):
                diem_so_19 = (x, y)
                break
            else:
                x = x + 1

    return diem_so_17, diem_so_15, diem_so_19


def TimDiem_41_42_43_44_doanh(image, nguong):
    image1 = image.copy()
    (h, w, d) = image.shape
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(gray, nguong, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)
    # cv2.imshow('shf', thresh)
    # cv2.waitKey()
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    # cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv2.contourArea)
    point_db_tren = []
    point_db_duoi = []
    point_ch = []
    chon_2_diem = []
    chon_4_diem_db_tren = []
    chon_4_diem_db_duoi = []
    diem_giua = []
    chieu = False

    for i in range(len(c)):
        cv2.drawContours(image, [c], -1, (240, 0, 159), 2)
        if i == 0:
            point_db_tren.append((c[i][0][0], c[i][0][1]))
            point_ch.append(c[i][0][1])
        else:
            if not chieu:
                if c[i][0][1] < point_ch[0]:
                    chieu = True
                    point_db_duoi.append((c[i - 1][0][0], c[i - 1][0][1]))
            if chieu:
                if c[i][0][1] > point_ch[0]:
                    chieu = False
                    point_db_tren.append((c[i - 1][0][0], c[i - 1][0][1]))

            point_ch.append(c[i][0][1])
            point_ch.pop(0)

    vi_tri = np.where(point_db_tren == min(np.array(point_db_tren)[:, 1]))
    chon_2_diem.append(point_db_tren[vi_tri[0][0]])
    point_db_tren.pop(vi_tri[0][0])
    vi_tri = np.where(point_db_tren == min(np.array(point_db_tren)[:, 1]))
    chon_2_diem.append(point_db_tren[vi_tri[0][0]])
    point_db_tren.pop(vi_tri[0][0])
    if chon_2_diem[0][0] > chon_2_diem[1][0]:
        chon_2_diem.reverse()
    cv2.circle(image, chon_2_diem[0], 2, [250, 250, 25], -1)
    cv2.circle(image, chon_2_diem[1], 2, [250, 250, 25], -1)
    vi_tri = np.where(point_db_duoi == min(np.array(point_db_duoi)[:, 1]))
    chon_2_diem.append(point_db_duoi[vi_tri[0][0]])
    cv2.circle(image, chon_2_diem[2], 2, [0, 50, 250], -1)
    vi_tri = np.where(chon_2_diem == min(np.array(chon_2_diem)[:, 1]))
    if vi_tri[0][0] == 0:
        diem_giua = chon_2_diem[1]
    if vi_tri[0][0] == 1:
        diem_giua = chon_2_diem[0]
    cv2.line(image, (0, chon_2_diem[2][1]), (w, chon_2_diem[2][1]), (0, 0, 255))
    cv2.line(image, (0, diem_giua[1]), (w, diem_giua[1]), (0, 255, 0))

    ao = False

    for i_x in range(w):
        y = diem_giua[1] + (chon_2_diem[2][1] - diem_giua[1]) // 3
        (B, G, R) = image[y, i_x]
        if (B, G, R) == (240, 0, 159) and ao:
            # cv2.circle(image, (i_x, y), 1, [250, 250, 25], -1)
            chon_4_diem_db_tren.append((i_x, y))
            ao = False
        elif (B, G, R) != (240, 0, 159):
            ao = True
            image[y, i_x] = (0, 255, 0)
    print(chon_4_diem_db_tren)

    for i_x in range(w):
        y = diem_giua[1] + (chon_2_diem[2][1] - diem_giua[1]) * 2 // 3
        (B, G, R) = image[y, i_x]
        if (B, G, R) == (240, 0, 159) and ao:
            # cv2.circle(image, (i_x, y), 2, [250, 250, 25], -1)
            chon_4_diem_db_duoi.append((i_x, y))
            ao = False
        elif (B, G, R) != (240, 0, 159):
            ao = True
            image[y, i_x] = (0, 255, 0)
    print(chon_4_diem_db_duoi)

    cv2.circle(image, tim_trung_diem(chon_4_diem_db_tren[0], chon_4_diem_db_tren[1]), 2,
               [20, 50, 250], -1)
    cv2.circle(image, tim_trung_diem(chon_4_diem_db_duoi[0], chon_4_diem_db_duoi[1]), 2,
               [20, 50, 250], -1)
    cv2.circle(image, tim_trung_diem(chon_4_diem_db_tren[2], chon_4_diem_db_tren[3]), 2,
               [20, 50, 250], -1)
    cv2.circle(image, tim_trung_diem(chon_4_diem_db_duoi[2], chon_4_diem_db_duoi[3]), 2,
               [20, 50, 250], -1)

    # ngón út _____________________________________________________________________________________________________
    y1 = tim_trung_diem(chon_4_diem_db_tren[0], chon_4_diem_db_tren[1])[1]
    y2 = tim_trung_diem(chon_4_diem_db_duoi[0], chon_4_diem_db_duoi[1])[1]
    x1 = tim_trung_diem(chon_4_diem_db_tren[0], chon_4_diem_db_tren[1])[0]
    x2 = tim_trung_diem(chon_4_diem_db_duoi[0], chon_4_diem_db_duoi[1])[0]
    for i_y in range(y1, 0, -1):
        x = x1 - (x2 - x1) * (i_y - y1) // (y1 - y2)
        (B, G, R) = image[i_y, x]
        if (B, G, R) == (240, 0, 159):
            break
        image[i_y, x] = (0, 255, 0)

    for i_y in range(y1 + 1, h, 1):
        x = x1 - (x2 - x1) * (i_y - y1) // (y1 - y2)
        (B, G, R) = image[i_y, x]
        if (B, G, R) == (0, 255, 0):
            break
        image[i_y, x] = (0, 255, 0)

    #################### Đo chiều rộng ngón tay #######################
    mang_chieu_rong = []
    mang_vi_tri_chieu_rong = []

    for i_y in range(y1 + 1, y2, 1):
        x = x1 - (x2 - x1) * (i_y - y1) // (y1 - y2)
        b = x - (y1 - y2) * i_y // (x2 - x1)
        for i_x in range(x, 0, -1):
            y = (i_x - b) * (x2 - x1) // (y1 - y2)
            (B, G, R) = image[y, i_x]
            if (B, G, R) == (240, 0, 159):
                rong_1 = (i_x, y)
                break
            image[y, i_x] = (0, 255, 0)
        for i_x in range(x, w, 1):
            y = (i_x - b) * (x2 - x1) // (y1 - y2)
            (B, G, R) = image[y, i_x]
            if (B, G, R) == (240, 0, 159):
                rong_2 = (i_x, y)
                break
            image[y, i_x] = (0, 255, 0)
        chieu_rong = TimKhoangCachHaiDiem(rong_1, rong_2)
        mang_chieu_rong.append(chieu_rong)
        mang_vi_tri_chieu_rong.append((rong_1, rong_2))
    mang_chieu_rong = np.array(mang_chieu_rong)
    vi_tri = np.where(mang_chieu_rong == max(mang_chieu_rong))
    cv2.line(image, mang_vi_tri_chieu_rong[vi_tri[0][0]][0], mang_vi_tri_chieu_rong[vi_tri[0][0]][1],
             (0, 0, 255))
    cv2.line(image1, mang_vi_tri_chieu_rong[vi_tri[0][0]][0], mang_vi_tri_chieu_rong[vi_tri[0][0]][1],
             (0, 0, 255))
    cv2.putText(image1, str(max(mang_chieu_rong)),
                (mang_vi_tri_chieu_rong[vi_tri[0][0]][0][0], mang_vi_tri_chieu_rong[vi_tri[0][0]][0][1] - 5),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (255, 0, 0), 1)

    # ngón áp út _____________________________________________________________________________________________________
    y1 = tim_trung_diem(chon_4_diem_db_tren[2], chon_4_diem_db_tren[3])[1]
    y2 = tim_trung_diem(chon_4_diem_db_duoi[2], chon_4_diem_db_duoi[3])[1]
    x1 = tim_trung_diem(chon_4_diem_db_tren[2], chon_4_diem_db_tren[3])[0]
    x2 = tim_trung_diem(chon_4_diem_db_duoi[2], chon_4_diem_db_duoi[3])[0]
    for i_y in range(y1, 0, -1):
        x = x1 - (x2 - x1) * (i_y - y1) // (y1 - y2)
        (B, G, R) = image[i_y, x]
        if (B, G, R) == (240, 0, 159):
            break
        image[i_y, x] = (0, 255, 0)

    for i_y in range(y1 + 1, h, 1):
        x = x1 - (x2 - x1) * (i_y - y1) // (y1 - y2)
        (B, G, R) = image[i_y, x]
        if (B, G, R) == (0, 255, 0):
            break
        image[i_y, x] = (0, 255, 0)

    #################### Đo chiều rộng ngón tay #######################
    mang_chieu_rong = []
    mang_vi_tri_chieu_rong = []

    for i_y in range(y1 + 1, y2, 1):
        x = x1 - (x2 - x1) * (i_y - y1) // (y1 - y2)
        b = x - (y1 - y2) * i_y // (x2 - x1)
        for i_x in range(x, 0, -1):
            y = (i_x - b) * (x2 - x1) // (y1 - y2)
            (B, G, R) = image[y, i_x]
            if (B, G, R) == (240, 0, 159):
                rong_1 = (i_x, y)
                break
            image[y, i_x] = (0, 255, 0)
        for i_x in range(x, w, 1):
            y = (i_x - b) * (x2 - x1) // (y1 - y2)
            (B, G, R) = image[y, i_x]
            if (B, G, R) == (240, 0, 159):
                rong_2 = (i_x, y)
                break
            image[y, i_x] = (0, 255, 0)
        chieu_rong = TimKhoangCachHaiDiem(rong_1, rong_2)
        mang_chieu_rong.append(chieu_rong)
        mang_vi_tri_chieu_rong.append((rong_1, rong_2))
    mang_chieu_rong = np.array(mang_chieu_rong)
    vi_tri = np.where(mang_chieu_rong == max(mang_chieu_rong))
    cv2.line(image, mang_vi_tri_chieu_rong[vi_tri[0][0]][0], mang_vi_tri_chieu_rong[vi_tri[0][0]][1],
             (0, 0, 255))
    cv2.line(image1, mang_vi_tri_chieu_rong[vi_tri[0][0]][0], mang_vi_tri_chieu_rong[vi_tri[0][0]][1],
             (0, 0, 255))
    cv2.putText(image1, str(max(mang_chieu_rong)),
                (mang_vi_tri_chieu_rong[vi_tri[0][0]][0][0], mang_vi_tri_chieu_rong[vi_tri[0][0]][0][1] - 5),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (255, 0, 0), 1)
    cv2.imshow('img', image1)
    cv2.waitKey(0)


def TimDiem_41_42_43_44_dong(mang_diem, image, handType, nguong):
    mang_diem_moc_5, mang_diem_moc_4, mang_diem_moc_20 = mang_diem

    image_crop = []
    local_coord_crop = []
    if handType == 'Right':
        x_min = mang_diem_moc_4[0]
        y_min = mang_diem_moc_20[1]
        x_max = mang_diem_moc_20[0]
        y_max = mang_diem_moc_5[1]

        local_coord_crop = [x_min, y_min]
        image_crop = image[y_min: y_max, x_min: x_max]

    if handType == 'Left':
        x_min = mang_diem_moc_20[0]
        y_min = mang_diem_moc_20[1]
        x_max = mang_diem_moc_4[0]
        y_max = mang_diem_moc_5[1]

        local_coord_crop = [x_min, y_min]
        image_crop = image[y_min: y_max, x_min: x_max]

    hulls = []
    points_of_hull = []
    diem_day_tren_anh_crop = [0, 0]
    temp = 0

    """
    Tim duong bao và dùng convex hull dong goi cac duong bao ko lien mach 
    de sau do tim duong bao lon nhat
    """
    gray = cv2.cvtColor(image_crop, cv2.COLOR_BGR2GRAY)

    otsu_threshold, image_result = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU,
    )
    thres = cv2.threshold(gray, otsu_threshold, 255, cv2.THRESH_BINARY)[1]
    # print("Obtained threshold: ", otsu_threshold)
    edges = cv2.Canny(thres, 127, 200)

    contours, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)
    if len(contours) == 0:
        print('Ko có nguong nao thich hơp')

    dientich = 0
    max_contour = []
    for cnt_no, cnt in enumerate(contours):
        x, y, w, h = cv2.boundingRect(cnt)
        dientich_new = w * h
        if dientich_new > dientich:
            dientich = dientich_new
            max_contour = contours[cnt_no]

    points_of_max_contour_crop = []
    for point_cnt in max_contour:
        points_of_max_contour_crop.append(point_cnt[0])

    diem_day = []
    khe = 0
    for poit_no, point in enumerate(points_of_max_contour_crop):
        if point[1] > khe:
            khe = point[1]
            diem_day = point
    diem_day_tren_anh_goc = [0, 0]
    diem_day_tren_anh_goc[0] = local_coord_crop[0] + diem_day[0]
    diem_day_tren_anh_goc[1] = local_coord_crop[1] + diem_day[1]

    image1 = image.copy()
    gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, nguong, 255, cv2.THRESH_BINARY)[1]

    # thres_adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #                               cv2.THRESH_BINARY, 11, 2)
    # otsu_threshold, thresh_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    # cnts = imutils.grab_contours(cnts)
    contour = []
    contour_x = []
    contour_y = []
    try:
        if len(cnts) != 0:
            c = max(cnts, key=cv2.contourArea)
            for i in range(len(c)):
                cv2.drawContours(image1, [c], -1, (240, 0, 159), 2)
                contour.append(c[i][0])
                contour_x.append(c[i][0][0])
                contour_y.append(c[i][0][1])

    except:
        print('Non contour')
    h, w, c = image1.shape
    contour_y_1 = contour_y.copy()
    contour_y_2 = contour_y.copy()
    for point_no, point in enumerate(contour):
        if point[0] <= diem_day_tren_anh_goc[0]:
            contour_y_1[point_no] = h
        if point[0] > diem_day_tren_anh_goc[0]:
            contour_y_2[point_no] = h

    chi_so_diem_B = contour_y_1.index(min(contour_y_1))
    diem_B = contour[chi_so_diem_B]
    chi_so_diem_C = contour_y_2.index(min(contour_y_2))
    diem_C = contour[chi_so_diem_C]

    diem_thap_hon = diem_B if (diem_B[1] > diem_C[1]) else diem_C

    khoang_cach_duong_giong = round((diem_day_tren_anh_goc[1] - diem_thap_hon[1]) / 3)

    giong_1 = diem_day_tren_anh_goc[1] - khoang_cach_duong_giong

    giong_2 = diem_day_tren_anh_goc[1] - khoang_cach_duong_giong * 2

    VeDuongThangDiQuaHaiDiem(image1, (0, giong_1), (w, giong_1))
    VeDuongThangDiQuaHaiDiem(image1, (0, giong_2), (w, giong_2))

    mang_4_diem_tren = []
    mang_4_diem_tren_fn = []
    for point_no, point in enumerate(contour):
        if point[1] <= giong_2 + 2 and point[1] >= giong_2 - 2:
            mang_4_diem_tren.append(point)

    for point_mang_4_no, point_mang_4 in enumerate(mang_4_diem_tren):
        for index in range(point_mang_4_no + 1, len(mang_4_diem_tren)):
            if abs(mang_4_diem_tren[point_mang_4_no][0] - mang_4_diem_tren[index][0]) < 10:
                point_mang_4[0] = 0

    for point_mang_4_no, point_mang_4 in enumerate(mang_4_diem_tren):
        if point_mang_4[0] != 0:
            mang_4_diem_tren_fn.append(point_mang_4)

    mang_4_diem_duoi = []
    mang_4_diem_duoi_fn = []
    for point_no, point in enumerate(contour):
        if point[1] <= giong_1 + 2 and point[1] >= giong_1 - 2:
            mang_4_diem_duoi.append(point)

    for point_mang_4_no, point_mang_4 in enumerate(mang_4_diem_duoi):
        for index in range(point_mang_4_no + 1, len(mang_4_diem_duoi)):
            if abs(mang_4_diem_duoi[point_mang_4_no][0] - mang_4_diem_duoi[index][0]) < 10:
                point_mang_4[0] = 0

    for point_no, point in enumerate(mang_4_diem_duoi):
        if point[0] != 0:
            mang_4_diem_duoi_fn.append(point)

    # mang_4_diem_tren_fn.sort(key=takeFirst)
    # mang_4_diem_duoi_fn.sort(key=takeFirst)
    mang_4_diem_tren_fn.sort(key=lambda a: a[0])
    mang_4_diem_duoi_fn.sort(key=lambda a: a[0])

    trung_diem_t0_t1 = tim_trung_diem(mang_4_diem_tren_fn[0], mang_4_diem_tren_fn[1])
    trung_diem_d0_d1 = tim_trung_diem(mang_4_diem_duoi_fn[0], mang_4_diem_duoi_fn[1])
    VeDuongThangDiQuaHaiDiem(image1, trung_diem_t0_t1, trung_diem_d0_d1)

    trung_diem_t2_t3 = tim_trung_diem(mang_4_diem_tren_fn[2], mang_4_diem_tren_fn[3])
    trung_diem_d2_d3 = tim_trung_diem(mang_4_diem_duoi_fn[2], mang_4_diem_duoi_fn[3])
    VeDuongThangDiQuaHaiDiem(image1, trung_diem_t2_t3, trung_diem_d2_d3)

    a1, b1, c1 = TimPhuongTrinhDuongThangVuongGocVoiDuongThang(trung_diem_t0_t1, trung_diem_d0_d1, trung_diem_d0_d1)
    a2, b2, c2 = TimPhuongTrinhDuongThangVuongGocVoiDuongThang(trung_diem_t2_t3, trung_diem_d2_d3, trung_diem_d2_d3)
    d1 = a1, b1, c1
    d2 = a2, b2, c2

    mang_cac_diem_41 = []
    for point_no, point in enumerate(contour):
        if point[0] < trung_diem_d0_d1[0]:
            kc = TimKhoangCachTuDiemDenDuongThang(point, d1)
            if kc <= 2:
                mang_cac_diem_41.append(point)

    mang_cac_diem_41.sort(key=lambda a: a[0], reverse=True)
    diem_so_41 = mang_cac_diem_41[0]
    cv2.circle(image1, diem_so_41, 2, (255, 0, 0), -1)
    cv2.putText(image1, '41', diem_so_41, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    mang_cac_diem_42 = []
    for point_no, point in enumerate(contour):
        if point[0] > trung_diem_d0_d1[0]:
            kc = TimKhoangCachTuDiemDenDuongThang(point, d1)
            if kc <= 2:
                mang_cac_diem_42.append(point)

    mang_cac_diem_42.sort(key=lambda a: a[0], reverse=False)
    diem_so_42 = mang_cac_diem_42[0]
    cv2.circle(image1, diem_so_42, 2, (255, 0, 0), -1)
    cv2.putText(image1, '42', diem_so_42, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # VeDuongThangDiQuaHaiDiem(image1, diem_so_41, diem_so_42)

    mang_cac_diem_43 = []
    for point_no, point in enumerate(contour):
        if point[0] < trung_diem_d2_d3[0]:
            kc = TimKhoangCachTuDiemDenDuongThang(point, d2)
            if kc <= 2:
                mang_cac_diem_43.append(point)

    mang_cac_diem_43.sort(key=lambda a: a[0], reverse=True)
    diem_so_43 = mang_cac_diem_43[0]
    cv2.circle(image1, diem_so_43, 2, (255, 0, 0), -1)
    cv2.putText(image1, '43', diem_so_43, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    mang_cac_diem_44 = []
    for point_no, point in enumerate(contour):
        if point[0] > trung_diem_d2_d3[0]:
            kc = TimKhoangCachTuDiemDenDuongThang(point, d2)
            if kc <= 2:
                mang_cac_diem_44.append(point)

    mang_cac_diem_44.sort(key=lambda a: a[0], reverse=False)
    diem_so_44 = mang_cac_diem_44[0]
    cv2.circle(image1, diem_so_44, 2, (255, 0, 0), -1)
    cv2.putText(image1, '44', diem_so_44, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # VeDuongThangDiQuaHaiDiem(image1, diem_so_43, diem_so_44)
    # x = mang_diem_moc_4[0]
    # while True:
    #     y = round((- c1 - a1 * x) / b1)
    #     (B, G, R) = image[y, x]
    #     if (B, G, R) == (240, 0, 159):
    #         rong_2 = (x, y)
    #         break
    #     else:
    #         x = x - 1

    # print(len(mang_4_diem_duoi), mang_4_diem_duoi_fn)
    # print(len(mang_4_diem_tren), mang_4_diem_tren_fn)

    # for i, t in enumerate(mang_4_diem_tren_fn):
    #     cv2.circle(image1, t, 2, (255, 0, 0), -1)
    #     cv2.putText(image1, 't' + str(i), t, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    #
    # for i, d in enumerate(mang_4_diem_duoi_fn):
    #     cv2.circle(image1, d, 2, (255, 0, 0), -1)
    #     cv2.putText(image1, 'd' + str(i), d, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # cv2.circle(image1, diem_day_tren_anh_goc, 2, (255, 0, 0), -1)
    # cv2.putText(image, 'A', diem_day_tren_anh_goc, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    #
    # cv2.circle(image1, diem_B, 2, (255, 0, 0), -1)
    # cv2.putText(image1, 'B', diem_B, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    #
    # cv2.circle(image1, diem_C, 2, (255, 0, 0), -1)
    # cv2.putText(image1, 'C', diem_C, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    # cv2.drawContours(image1, [c], -1, (240, 0, 159), 2)
    # cv2.imshow('img', image1)
    # cv2.waitKey(0)

    return diem_so_41, diem_so_42, diem_so_43, diem_so_44


def TimDiem_41_42_43_44_dong_V1(mang_diem, image, handType, nguong):
    mang_diem_moc_5, mang_diem_moc_4, mang_diem_moc_20 = mang_diem

    image_crop = []
    local_coord_crop = []
    if handType == 'Right':
        x_min = mang_diem_moc_4[0]
        y_min = mang_diem_moc_20[1]
        x_max = mang_diem_moc_20[0]
        y_max = mang_diem_moc_5[1]

        local_coord_crop = [x_min, y_min]
        image_crop = image[y_min: y_max, x_min: x_max]

    if handType == 'Left':
        x_min = mang_diem_moc_20[0]
        y_min = mang_diem_moc_20[1]
        x_max = mang_diem_moc_4[0]
        y_max = mang_diem_moc_5[1]

        local_coord_crop = [x_min, y_min]
        image_crop = image[y_min: y_max, x_min: x_max]

    """
    Tim duong bao và dùng convex hull dong goi cac duong bao ko lien mach 
    de sau do tim duong bao lon nhat
    """
    gray = cv2.cvtColor(image_crop, cv2.COLOR_BGR2GRAY)

    # otsu_threshold, image_result = cv2.threshold(
    #     gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU,
    # )
    # thres = cv2.threshold(gray, otsu_threshold, 255, cv2.THRESH_BINARY)[1]
    # # print("Obtained threshold: ", otsu_threshold)
    # edges = cv2.Canny(thres, 127, 200)
    #
    # contours, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL,
    #                                        cv2.CHAIN_APPROX_NONE)
    thresh = cv2.threshold(gray, nguong, 255, cv2.THRESH_BINARY_INV)[1]
    contours_image_crop, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                                      cv2.CHAIN_APPROX_NONE)

    hulls = []
    hull = []
    for cnt in contours_image_crop:
        hull = cv2.convexHull(cnt)
        hulls.append(hull)
    hull = max(hulls, key=cv2.contourArea)

    # cv2.drawContours(image_crop, [hull], -1, (240, 0, 159), 1)

    points_of_max_contour_crop = []
    for point_cnt in hull:
        points_of_max_contour_crop.append(point_cnt[0])

    diem_day = []
    khe = 0
    for poit_no, point in enumerate(points_of_max_contour_crop):
        if point[1] > khe:
            khe = point[1]
            diem_day = point

    diem_day_tren_anh_goc = [0, 0]
    diem_day_tren_anh_goc[0] = local_coord_crop[0] + diem_day[0]
    diem_day_tren_anh_goc[1] = local_coord_crop[1] + diem_day[1]

    image1 = image.copy()
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    thresh1 = cv2.threshold(gray1, nguong, 255, cv2.THRESH_BINARY)[1]
    # thres_adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #                               cv2.THRESH_BINARY, 11, 2)
    # otsu_threshold, thresh_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cnts = cv2.findContours(thresh1.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    # cnts = imutils.grab_contours(cnts)
    contour = []
    contour_x = []
    contour_y = []
    try:
        if len(cnts) != 0:
            c = max(cnts, key=cv2.contourArea)
            for i in range(len(c)):
                cv2.drawContours(image1, [c], -1, (240, 0, 159), 2)
                contour.append(c[i][0])
                contour_x.append(c[i][0][0])
                contour_y.append(c[i][0][1])

    except:
        print('Non contour')
    h, w = image1.shape[:2]
    contour_y_1 = contour_y.copy()
    contour_y_2 = contour_y.copy()
    for point_no, point in enumerate(contour):
        if point[0] <= diem_day_tren_anh_goc[0]:
            contour_y_1[point_no] = h
        if point[0] > diem_day_tren_anh_goc[0]:
            contour_y_2[point_no] = h

    chi_so_diem_B = contour_y_1.index(min(contour_y_1))
    diem_B = contour[chi_so_diem_B]
    chi_so_diem_C = contour_y_2.index(min(contour_y_2))
    diem_C = contour[chi_so_diem_C]

    diem_thap_hon = diem_B if (diem_B[1] > diem_C[1]) else diem_C

    khoang_cach_duong_giong = round((diem_day_tren_anh_goc[1] - diem_thap_hon[1]) / 3)

    giong_1 = diem_day_tren_anh_goc[1] - khoang_cach_duong_giong

    giong_2 = diem_day_tren_anh_goc[1] - khoang_cach_duong_giong * 2

    mang_4_diem_tren = []
    y_tren = giong_2
    x_tren = 0
    x_truoc = 0
    while x_tren < w:
        (B, G, R) = image1[y_tren, x_tren]
        if (B, G, R) == (240, 0, 159) and abs(x_tren - x_truoc) >= 5:
            diem_tren = (x_tren, y_tren)
            mang_4_diem_tren.append(diem_tren)
            x_truoc = x_tren
        else:
            x_tren = x_tren + 1

    mang_4_diem_duoi = []
    y_duoi = giong_1
    x_duoi = 0
    x_truoc = 0
    while x_duoi < w:
        (B, G, R) = image1[y_duoi, x_duoi]
        if (B, G, R) == (240, 0, 159) and abs(x_duoi - x_truoc) >= 5:
            diem_duoi = (x_duoi, y_duoi)
            mang_4_diem_duoi.append(diem_duoi)
            x_truoc = x_duoi
        else:
            x_duoi = x_duoi + 1

    VeDuongThangDiQuaHaiDiem(image1, (0, giong_1), (w, giong_1))
    VeDuongThangDiQuaHaiDiem(image1, (0, giong_2), (w, giong_2))

    # print(mang_4_diem_tren)
    # print(len(mang_4_diem_tren))
    #
    # print(mang_4_diem_duoi)
    # print(len(mang_4_diem_duoi))

    trung_diem_t0_t1 = tim_trung_diem(mang_4_diem_tren[0], mang_4_diem_tren[1])
    trung_diem_d0_d1 = tim_trung_diem(mang_4_diem_duoi[0], mang_4_diem_duoi[1])

    trung_diem_t2_t3 = tim_trung_diem(mang_4_diem_tren[2], mang_4_diem_tren[3])
    trung_diem_d2_d3 = tim_trung_diem(mang_4_diem_duoi[2], mang_4_diem_duoi[3])

    # VeDuongThangDiQuaHaiDiem(image1, trung_diem_t0_t1, trung_diem_d0_d1)
    # VeDuongThangDiQuaHaiDiem(image1, trung_diem_t2_t3, trung_diem_d2_d3)

    a1, b1, c1 = TimPhuongTrinhDuongThangVuongGocVoiDuongThang(trung_diem_t0_t1, trung_diem_d0_d1, trung_diem_d0_d1)
    a2, b2, c2 = TimPhuongTrinhDuongThangVuongGocVoiDuongThang(trung_diem_t2_t3, trung_diem_d2_d3, trung_diem_d2_d3)
    d1 = a1, b1, c1
    d2 = a2, b2, c2

    """
    Tim diem 43, 44
    """
    diem_so_43 = []
    diem_so_44 = []
    x_43 = trung_diem_d0_d1[0]
    while True:
        y_43 = round((- c1 - a1 * x_43) / b1)
        (B, G, R) = image1[y_43, x_43]
        if (B, G, R) == (240, 0, 159) and abs(x_43 - trung_diem_d0_d1[0]) >= 3:
            diem_so_43 = (x_43, y_43)
            break
        else:
            x_43 = x_43 + 1

    x_44 = trung_diem_d0_d1[0]
    while True:
        y_44 = round((- c1 - a1 * x_44) / b1)
        (B, G, R) = image1[y_44, x_44]
        if (B, G, R) == (240, 0, 159) and abs(x_44 - trung_diem_d0_d1[0]) >= 3:
            diem_so_44 = (x_44, y_44)
            break
        else:
            x_44 = x_44 - 1
    """
    Tim diem 41, 42
    """
    diem_so_41 = []
    diem_so_42 = []
    x_41 = trung_diem_d2_d3[0]
    while True:
        y_41 = round((- c2 - a2 * x_41) / b2)
        (B, G, R) = image1[y_41, x_41]
        if (B, G, R) == (240, 0, 159) and abs(x_41 - trung_diem_d2_d3[0]) >= 3:
            diem_so_41 = (x_41, y_41)
            break
        else:
            x_41 = x_41 + 1

    x_42 = trung_diem_d2_d3[0]
    while True:
        y_42 = round((- c2 - a2 * x_42) / b2)
        (B, G, R) = image1[y_42, x_42]
        if (B, G, R) == (240, 0, 159) and abs(x_42 - trung_diem_d2_d3[0]) >= 3:
            diem_so_42 = (x_42, y_42)
            break
        else:
            x_42 = x_42 - 1

    cv2.circle(image1, diem_so_41, 2, (255, 0, 0), -1)
    cv2.putText(image1, '41',
                diem_so_41, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.circle(image1, diem_so_42, 2, (255, 0, 0), -1)
    cv2.putText(image1, '42',
                diem_so_42, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.circle(image1, diem_so_43, 2, (255, 0, 0), -1)
    cv2.putText(image1, '43',
                diem_so_43, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.circle(image1, diem_so_44, 2, (255, 0, 0), -1)
    cv2.putText(image1, '44',
                diem_so_44, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)

    cv2.circle(image1, diem_day_tren_anh_goc, 2, (255, 0, 0), -1)
    cv2.putText(image1, '0',
                diem_day_tren_anh_goc, cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 255), 1)
    # VeDuongThangDiQuaHaiDiem(image, diem_so_41, diem_so_42)
    # VeDuongThangDiQuaHaiDiem(image, diem_so_43, diem_so_44)
    # cv2.imshow('img1', image_crop)
    # cv2.imshow('img', image1)
    # cv2.waitKey(0)
    return diem_so_41, diem_so_42, diem_so_43, diem_so_44


def TimDiem_30_31_32_33_34_dong(mang_diem, img, handType, nguong):
    # điẻm so 6 ko ôn dinh, nen chọn diem so 4 là diem trên móng tay cái
    mang_diem_moc_0, mang_diem_moc_2, mang_diem_moc_4 = mang_diem
    image = img.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # gray = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(gray, nguong, 255, cv2.THRESH_BINARY)[1]
    # thresh = cv2.erode(thresh, None, iterations=2)
    # thresh = cv2.dilate(thresh, None, iterations=2)
    # thres_adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #                               cv2.THRESH_BINARY, 11, 2)
    # otsu_threshold, thresh_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    # cnts = imutils.grab_contours(cnts)

    contour = []
    contour_x = []
    contour_y = []
    try:
        if len(cnts) != 0:
            c = max(cnts, key=cv2.contourArea)
            for i in range(len(c)):
                cv2.drawContours(image, [c], -1, (240, 0, 159), 1)
                contour.append(c[i][0])
                contour_x.append(c[i][0][0])
                contour_y.append(c[i][0][1])

    except:
        print('Non contour')

    diem_so_30 = []
    diem_so_31 = []
    diem_so_32 = []
    diem_so_33 = []
    diem_so_34 = []
    diem_so_35 = []

    h, w = image.shape[:2]
    contour_x_1 = contour_x.copy()
    contour_x_2 = contour_x.copy()
    if handType == 'Right':
        for point_no, point in enumerate(contour):
            if point[1] <= mang_diem_moc_2[1]:
                contour_x_2[point_no] = w
            if point[1] > mang_diem_moc_0[1]:
                contour_x_2[point_no] = w

        chi_so_diem_35 = contour_x_2.index(min(contour_x_2))
        diem_so_35 = contour[chi_so_diem_35]

        # Tìm diểm 34

        y_34 = diem_so_35[1]
        x_34 = diem_so_35[0]
        while True:
            (B, G, R) = image[y_34, x_34]
            if (B, G, R) == (240, 0, 159) and abs(x_34 - diem_so_35[0]) >= 5:
                diem_so_34 = (x_34, y_34)
                break
            else:
                x_34 = x_34 + 1

        # Tìm diểm 32
        for point_no, point in enumerate(contour):
            if point[1] < mang_diem_moc_4[1]:
                contour_x_1[point_no] = 0
            if point[1] > mang_diem_moc_2[1]:
                contour_x_1[point_no] = 0

        chi_so_diem_32 = contour_x_1.index(max(contour_x_1))
        diem_so_32 = contour[chi_so_diem_32]

        # Tìm diểm 33
        y_33 = diem_so_32[1]
        x_33 = diem_so_32[0]
        while True:
            (B, G, R) = image[y_33, x_33]
            if (B, G, R) == (240, 0, 159) and abs(x_33 - diem_so_32[0]) >= 5:
                diem_so_33 = (x_33, y_33)
                break
            else:
                x_33 = x_33 - 1

        # Tìm diểm 30, 31

        # # a3, b3, c3 = TimPhuongTrinhDuongThangVuongGocVoiDuongThang(diem_cao_nhi, diem_cao_nhat, diem_cao_nhi)
        # # d3 = a3, b3, c3

        # Diem dinh ngon tay
        chi_so_diem_dinh = contour_y.index(min(contour_y))
        dinh_ngon_tay = contour[chi_so_diem_dinh]

        # Vẽ đuòng thảng ở độ cao 1/2 3/4 tính theo kc cao do tu diem so 4 toi dinh

        duong_tren = mang_diem_moc_4[1] - round(abs(mang_diem_moc_4[1] - dinh_ngon_tay[1]) * 3 / 4)
        duong_duoi = mang_diem_moc_4[1] - round(abs(mang_diem_moc_4[1] - dinh_ngon_tay[1]) * 1 / 2)

        mang_2_diem_tren = []
        y_tren = duong_tren
        x_tren = 0
        x_truoc = 0
        while x_tren < w:
            (B, G, R) = image[y_tren, x_tren]
            if (B, G, R) == (240, 0, 159) and abs(x_tren - x_truoc) >= 5:
                diem_tren = (x_tren, y_tren)
                mang_2_diem_tren.append(diem_tren)
                x_truoc = x_tren
            else:
                x_tren = x_tren + 1

        mang_2_diem_duoi = []
        y_duoi = duong_duoi
        x_duoi = 0
        x_truoc = 0
        while x_duoi < w:
            (B, G, R) = image[y_duoi, x_duoi]
            if (B, G, R) == (240, 0, 159) and abs(x_duoi - x_truoc) >= 5:
                diem_duoi = (x_duoi, y_duoi)
                mang_2_diem_duoi.append(diem_duoi)
                x_truoc = x_duoi
            else:
                x_duoi = x_duoi + 1

        # VeDuongThangDiQuaHaiDiem(image, (0, duong_duoi), (w, duong_duoi))
        # VeDuongThangDiQuaHaiDiem(image, (0, duong_tren), (w, duong_tren))
        trung_diem_tren = tim_trung_diem(mang_2_diem_tren[0], mang_2_diem_tren[1])
        trung_diem_duoi = tim_trung_diem(mang_2_diem_duoi[0], mang_2_diem_duoi[1])

        a1, b1, c1 = TimPhuongTrinhDuongThangVuongGocVoiDuongThang(trung_diem_tren, trung_diem_duoi, trung_diem_duoi)

        x_30 = trung_diem_duoi[0]
        while True:
            y_30 = round((- c1 - a1 * x_30) / b1)
            (B, G, R) = image[y_30, x_30]
            if (B, G, R) == (240, 0, 159) and abs(x_30 - trung_diem_duoi[0]) >= 3:
                diem_so_30 = (x_30, y_30)
                break
            else:
                x_30 = x_30 + 1

        x_31 = trung_diem_duoi[0]
        while True:
            y_31 = round((- c1 - a1 * x_31) / b1)
            (B, G, R) = image[y_31, x_31]
            if (B, G, R) == (240, 0, 159) and abs(x_31 - trung_diem_duoi[0]) >= 3:
                diem_so_31 = (x_31, y_31)
                break
            else:
                x_31 = x_31 - 1

    if handType == 'Left':
        for point_no, point in enumerate(contour):
            if point[1] <= mang_diem_moc_2[1]:
                contour_x_2[point_no] = 0
            if point[1] > mang_diem_moc_0[1]:
                contour_x_2[point_no] = 0

        chi_so_diem_35 = contour_x_2.index(max(contour_x_2))
        diem_so_35 = contour[chi_so_diem_35]

        # Tìm diểm 34

        y_34 = diem_so_35[1]
        x_34 = diem_so_35[0]
        while True:
            (B, G, R) = image[y_34, x_34]
            if (B, G, R) == (240, 0, 159) and abs(x_34 - diem_so_35[0]) >= 5:
                diem_so_34 = (x_34, y_34)
                break
            else:
                x_34 = x_34 - 1

        # Tìm diểm 32
        for point_no, point in enumerate(contour):
            if point[1] < mang_diem_moc_4[1]:
                contour_x_1[point_no] = w
            if point[1] > mang_diem_moc_2[1]:
                contour_x_1[point_no] = w

        chi_so_diem_32 = contour_x_1.index(min(contour_x_1))
        diem_so_32 = contour[chi_so_diem_32]

        # Tìm diểm 33
        y_33 = diem_so_32[1]
        x_33 = diem_so_32[0]
        while True:
            (B, G, R) = image[y_33, x_33]
            if (B, G, R) == (240, 0, 159) and abs(x_33 - diem_so_32[0]) >= 5:
                diem_so_33 = (x_33, y_33)
                break
            else:
                x_33 = x_33 + 1

        # Tìm diểm 30, 31

        # # a3, b3, c3 = TimPhuongTrinhDuongThangVuongGocVoiDuongThang(diem_cao_nhi, diem_cao_nhat, diem_cao_nhi)
        # # d3 = a3, b3, c3

        # Diem dinh ngon tay
        chi_so_diem_dinh = contour_y.index(min(contour_y))
        dinh_ngon_tay = contour[chi_so_diem_dinh]

        # Vẽ duong thang ở độ cao 1/2 3/4 tính theo kc cao do tu diem so 4 toi dinh

        duong_tren = mang_diem_moc_4[1] - round(abs(mang_diem_moc_4[1] - dinh_ngon_tay[1]) * 3 / 4)
        duong_duoi = mang_diem_moc_4[1] - round(abs(mang_diem_moc_4[1] - dinh_ngon_tay[1]) * 1 / 2)

        mang_2_diem_tren = []
        y_tren = duong_tren
        x_tren = 0
        x_truoc = 0
        while x_tren < w:
            (B, G, R) = image[y_tren, x_tren]
            if (B, G, R) == (240, 0, 159) and abs(x_tren - x_truoc) >= 5:
                diem_tren = (x_tren, y_tren)
                mang_2_diem_tren.append(diem_tren)
                x_truoc = x_tren
            else:
                x_tren = x_tren + 1

        mang_2_diem_duoi = []
        y_duoi = duong_duoi
        x_duoi = 0
        x_truoc = 0
        while x_duoi < w:
            (B, G, R) = image[y_duoi, x_duoi]
            if (B, G, R) == (240, 0, 159) and abs(x_duoi - x_truoc) >= 5:
                diem_duoi = (x_duoi, y_duoi)
                mang_2_diem_duoi.append(diem_duoi)
                x_truoc = x_duoi
            else:
                x_duoi = x_duoi + 1

        # VeDuongThangDiQuaHaiDiem(image, (0, duong_duoi), (w, duong_duoi))
        # VeDuongThangDiQuaHaiDiem(image, (0, duong_tren), (w, duong_tren))
        trung_diem_tren = tim_trung_diem(mang_2_diem_tren[0], mang_2_diem_tren[1])
        trung_diem_duoi = tim_trung_diem(mang_2_diem_duoi[0], mang_2_diem_duoi[1])

        a1, b1, c1 = TimPhuongTrinhDuongThangVuongGocVoiDuongThang(trung_diem_tren, trung_diem_duoi, trung_diem_duoi)

        x_30 = trung_diem_duoi[0]
        while True:
            y_30 = round((- c1 - a1 * x_30) / b1)
            (B, G, R) = image[y_30, x_30]
            if (B, G, R) == (240, 0, 159) and abs(x_30 - trung_diem_duoi[0]) >= 3:
                diem_so_30 = (x_30, y_30)
                break
            else:
                x_30 = x_30 - 1

        x_31 = trung_diem_duoi[0]
        while True:
            y_31 = round((- c1 - a1 * x_31) / b1)
            (B, G, R) = image[y_31, x_31]
            if (B, G, R) == (240, 0, 159) and abs(x_31 - trung_diem_duoi[0]) >= 3:
                diem_so_31 = (x_31, y_31)
                break
            else:
                x_31 = x_31 + 1

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
    # cv2.imshow('img', image)
    # cv2.waitKey(0)

    return diem_so_30, diem_so_31, diem_so_32, diem_so_33, diem_so_34, diem_so_35
