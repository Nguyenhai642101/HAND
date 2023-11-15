import numpy as np
import cv2 as cv

cap = cv.VideoCapture(1)
# cap.set()
# print(cap.get(cv.CAP_PROP_BRIGHTNESS))
# cap.set(60, cv.CAP_PROP_FPS)
# cap.set(50, cv.CAP_PROP_BRIGHTNESS)
# cap.set(cv.CAP_PROP_FOCUS, 20)
# cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)
# cap.set(cv.CAP_PROP_FRAME_WIDTH, 1920)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # print(cap.get(cv.CAP_PROP_FOCUS))
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

# import math
# import imutils
# import numpy as np
# import cv2
# import glob
#
# """
# # Camera Calibration with OpenCV
# """
#
#
# ################ FIND CHESSBOARD CORNERS - OBJECT POINTS AND IMAGE POINTS #############################
#
# # chessboardSize = (10, 7)
# # frameSize = (1920, 1080)
#
#
# def TimKhoangCachHaiDiemFloat(diem_A, diem_B):
#     return round(math.sqrt(math.pow(diem_A[0] - diem_B[0], 2) + math.pow(diem_A[1] - diem_B[1], 2)))
#
#
# def CalibCamera(folder, so_o_ngang, so_o_doc, frameSize):
#     chessboardSize = (so_o_ngang - 1, so_o_doc - 1)
#     # termination criteria
#     criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
#     # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
#     objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
#     objp[:, :2] = np.mgrid[0:chessboardSize[0], 0:chessboardSize[1]].T.reshape(-1, 2) * 10
#     axis = np.float32([[3, 0, 0], [0, 3, 0], [0, 0, -3]]).reshape(-1, 3) * 10
#     axisBoxes = 10 * np.float32([[0, 0, 0], [0, 3, 0], [3, 3, 0], [3, 0, 0],
#                                  [0, 0, -3], [0, 3, -3], [3, 3, -3], [3, 0, -3]])
#
#     # Arrays to store object points and image points from all the images.
#     objpoints = []  # 3d point in real world space
#     imgpoints = []  # 2d points in image plane.
#
#     # images = glob.glob('calibbantay\*.jpg')
#     # images = glob.glob('K:\PROJECT\PYQT5\DO_BAN_TAY\calib\obanco\*.jpg')
#     images = glob.glob('{}'.format(folder) + '\*.png')
#     print(len(images))
#     for image in images:
#         img = cv2.imread(image)
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         # Find the chess board corners
#         ret, corners = cv2.findChessboardCorners(gray, chessboardSize, None)
#         # If found, add object points, image points (after refining them)
#         if ret == True:
#             objpoints.append(objp)
#             corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
#             imgpoints.append(corners)
#
#             # # Draw and display the corners
#             # cv2.drawChessboardCorners(img, chessboardSize, corners2, ret)
#             # cv2.imshow('img', img)
#             # cv2.imwrite("corner.jpg", img)
#             # cv2.waitKey(1000)
#
#     ret, cameraMatrix, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, frameSize, None, None)
#
#     print(dist)
#     print(cameraMatrix)
#
#     # 1) undistort image
#     img1 = cv2.imread('{}'.format(folder) + '\{}.png'.format(1))
#
#     undst1 = cv2.undistort(img1, cameraMatrix, dist, None, cameraMatrix)
#
#     img2 = cv2.imread('{}'.format(folder) + '\{}.png'.format(2))
#
#     undst2 = cv2.undistort(img2, cameraMatrix, dist, None, cameraMatrix)
#
#     img3 = cv2.imread(r'D:\HUST\LAB\CALIB\NEW\30-05-2022-01-00-05\1.png')
#     undst3 = cv2.undistort(img3, cameraMatrix, dist, None, cameraMatrix)
#
#     diem = (480, 320)
#     kq = cv2.undistortPoints(diem, cameraMatrix, dist, None, cameraMatrix)
#     print(round(kq[0][0][0]))
#
#     # cv2.imwrite('test_undist.png', dst1)
#     cv2.imshow('test_undist_1', undst1)
#     cv2.imshow('test_undist_3', undst3)
#     cv2.waitKey(0)
#
#     # 2) Convert to grayscale
#     gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#     gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
#
#     # 3) Find the chessboard corners
#     ret1, corners1 = cv2.findChessboardCorners(gray1, chessboardSize, None)
#     ret2, corners2 = cv2.findChessboardCorners(gray2, chessboardSize, None)
#
#     # 4) If corners found:
#     if ret1 == True:
#         # a) draw corners
#         cv2.drawChessboardCorners(undst1, chessboardSize, corners1, ret1)
#         # b) define 4 source points src = np.float32([[,],[,],[,],[,]])
#         # Note: you could pick any four of the detected corners
#         # as long as those four corners define a rectangle
#         # One especially smart way to do this would be to use four well-chosen
#         # corners that were automatically detected during the undistortion steps
#         # We recommend using the automatic detection of corners in your code
#
#         nx = chessboardSize[0]
#         ny = chessboardSize[1]
#         # 4 góc bàn cờ
#         src = np.float32([corners1[0], corners1[nx - 1], corners1[-1], corners1[-nx]])
#
#         doc = TimKhoangCachHaiDiem(corners1[0][0], corners1[nx - 1][0])
#         print(doc)
#         ngang = TimKhoangCachHaiDiem(corners1[-1][0], corners1[-nx][0])
#         print(ngang)
#         # print(corners1[0], corners1[nx - 1])
#         # print(corners1[-1], corners1[-nx])
#
#     if ret2 == True:
#         # a) draw corners
#         cv2.drawChessboardCorners(undst2, chessboardSize, corners2, ret2)
#         # b) define 4 source points src = np.float32([[,],[,],[,],[,]])
#         # Note: you could pick any four of the detected corners
#         # as long as those four corners define a rectangle
#         # One especially smart way to do this would be to use four well-chosen
#         # corners that were automatically detected during the undistortion steps
#         # We recommend using the automatic detection of corners in your code
#
#         nx = chessboardSize[0]
#         ny = chessboardSize[1]
#         # 4 góc bàn cờ
#         src = np.float32([corners2[0], corners2[nx - 1], corners2[-1], corners2[-nx]])
#
#         doc = TimKhoangCachHaiDiem(corners2[0][0], corners2[nx - 1][0])
#         print(doc)
#         ngang = TimKhoangCachHaiDiem(corners2[-1][0], corners2[-nx][0])
#         print(ngang)
#         # print(corners2[0], corners2[nx - 1])
#         # print(corners2[-1], corners2[-nx])
#
#     cv2.imshow('undst1', undst1)
#     cv2.imshow('undst2', undst2)
#     cv2.waitKey(0)
#
#
# if __name__ == "__main__":
#     # folder = 'K:\PROJECT\PYQT5\DO_BAN_TAY\calib\obanco'
#     # folder = r'D:\HUST\LAB\CALIB\NEW\test'
#     folder = r'D:\HUST\LAB\CALIB\NEW\30-05-2022-00-57-04'
#
#     #
#     # so_o_ngang = 10
#     # so_o_doc = 7
#     frameSize = (960, 720)
#     # CalibCamera(folder, 11, 8, frameSize)
#     CalibCamera(folder, 7, 7, frameSize)
