#!/usr/bin/env python2

#TODO
# -visualizations
# -find cable function
# -add calibration photos for new camera
# -add calibration photos for cable

# TODO left off making sure the cable/aruco present flags are set correctly.

import sys,os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'support'))
import cv2
from cv2 import aruco
import numpy as np
import glob
import math
import os
import atexit

import pose_models

class Camera:
    def __init__(self,path_to_cal_images):
        atexit.register(self.shutdown)
        self.path_to_cal_photos = path_to_cal_images
        self.cap = cv2.VideoCapture(self.__find_dev_path())
        self.aruco_dict = aruco.Dictionary_get(aruco.DICT_ARUCO_ORIGINAL)
        self.aruco_params = aruco.DetectorParameters_create()
        self.pose_model = pose_models.CameraGroundTruth()
        self.__calibrate_cam()
        self.__calibrate_cable()

    def find_ground_truth(self,undistort=True,illustrations=False):
        self.cable_pos, self.cable_ang = None,None
        self.aruco_present,self.cable_present = False,False
        ret, self.frame = self.cap.read()
        if undistort:
            self.frame = cv2.undistort(self.frame, self.mtx, self.dist, None, self.newcameramtx)
        self.__find_aruco()
        if self.aruco_present:
            self.__aruco_transform()
            self.__find_cable()
        if illustrations:
            self.__show_ground_truth()
        return self.cable_pos,self.cable_ang

    def __find_aruco(self):
        """Finds the aruco marker in self.frame, and sets some parameters."""
        gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        self.corners, self.ids, rejectedImgPoints = aruco.detectMarkers(gray, self.aruco_dict, parameters=self.aruco_params)
        if not self.corners:
            self.aruco_present = False
            return
        self.aruco_present = True
        center = np.average(np.array(self.corners[0][0]), axis=0)
        self.aruco_center = [round(center[0]),round(center[1])]
        self.aruc_bot_left_pt,self.aruco_bot_right_pt = self.corners[0][0][0],self.corners[0][0][1]

    def __aruco_transform(self):
        """Rotate the image to align with aruco and cable coordinates. This greatly simplifies things.
        An alternative might be to analytically figure it out. In that case this desmos might be nice to look at.
        https://www.desmos.com/calculator/kvem8zyzve"""
        # Should never be divide by zero, unless something seriously broke.
        slope = self.__find_slope(self.aruc_bot_left_pt,self.aruco_bot_right_pt)
        aruco_ang = math.degrees(math.atan(slope))
        rot_mat = cv2.getRotationMatrix2D(tuple(self.aruco_center), aruco_ang, 1.0)
        self.frame = cv2.warpAffine(self.frame, rot_mat, self.frame.shape[1::-1], flags=cv2.INTER_LINEAR)

    def __find_cable(self):
        """Finds the cable (with colored points) in self.frame, and sets some parameters.
        https://stackoverflow.com/questions/57282935/how-to-detect-area-of-pixels-with-the-same-color-using-opencv"""
        self.__get_color_contours()
        if self.cable_present:
            self.cable_ang = self.__find_cable_ang()
            self.cable_pos = self.__find_cable_pos()

    def __get_color_contours(self):
        frame_copy = self.frame.copy()
        frame_copy = cv2.cvtColor(frame_copy, cv2.COLOR_BGR2HSV)
        # Choosing good HSV color values is difficult.
        # https://en.wikipedia.org/wiki/HSL_and_HSV#/media/File:Hsl-hsv_models.svg
        # https://alloyui.com/examples/color-picker/hsv.html
        # http://color.lukas-stratmann.com/color-systems/hsv.html
        # cv2 uses ranges: H: 0-179, S: 0-255, V: 0-255
        # Note that most color picker have different ranges. You likely need to convert.
        # Yellow mask
        lower = np.array([18, 127, 127], dtype="uint8")
        upper = np.array([42, 255, 255], dtype="uint8")
        mask = cv2.inRange(frame_copy, lower, upper)
        # Remove noise
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
        # Find contours
        cnts = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        self.cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        self.color_centers = []
        for c in self.cnts:
            if cv2.contourArea(c) > self.area_threshold:
                center = np.average(c, axis=0)
                self.color_centers.append([round(center[0][0]),round(center[0][1])])
            if len(self.color_centers) == 2:
                self.cable_present = True
                break

    def __get_color_contours2(self):
        """Currently used for development."""
        frame_copy = self.frame.copy()
        frame_copy = cv2.cvtColor(frame_copy, cv2.COLOR_BGR2HSV)
        # Yellow
        lower = np.array([18, 127, 127], dtype="uint8")
        upper = np.array([42, 255, 255], dtype="uint8")
        mask = cv2.inRange(frame_copy, lower, upper)
        detected = cv2.bitwise_and(self.frame, self.frame, mask=mask)
        # Remove noise
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
        # Find contours and find total area
        cnts = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        area = 0
        for c in cnts:
            area += cv2.contourArea(c)
            cv2.drawContours(self.frame, [c], 0, (0, 0, 0), 2)

        cv2.imshow('mask', mask)
        cv2.imshow('original', self.frame)
        cv2.imshow('opening', opening)
        cv2.imshow('detected', detected)
        cv2.waitKey(1)

    def __find_cable_ang(self):
        """Returns the angle of the cable in degrees in the sensor coordinate system."""
        self.cable_slope = self.__find_slope(self.color_centers[0], self.color_centers[1])
        return math.degrees(math.atan(self.cable_slope))

    def __find_cable_pos(self):
        """Returns the position of the cable in mm in the sensor coordinate system."""
        cable_b = self.__find_y_intercept(self.cable_slope, self.color_centers[0])
        y = self.cable_slope * self.aruco_center[0] + cable_b
        pix_pos = y - self.aruco_center[1]
        return pix_pos * self.pix_to_mm

    def __show_ground_truth(self):
        """Show the captured image with the aruco marker coordinates and cable coordiates, if present."""
        if self.aruco_present:
            self.__add_aruco_illustration()
        if self.cable_present:
            self.__add_cable_illustration()

    ####################################################################################################################
    # CALIBRATION
    ####################################################################################################################
    def __calibrate_cable(self):
        """Returns a ratio of pixels to distance for the cable."""
        #TODO need to look for distance calibration photos. These should be real photos of the cable in grasp.
        # The distance between points is known, so we can find a ratio between pixels and distance.
        self.pix_to_mm = 1
        self.area_threshold = 400

    def __calibrate_cam(self,test=False,see_corners=False):
        """Use checkerboard images to set the calibration constants. Adopted and modifed from:
        https://www.geeksforgeeks.org/camera-calibration-with-python-opencv/
        https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html"""
        checkerboard_corners = (6,9)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        threedpoints,twodpoints = [],[]
        #  3D points real world coordinates
        objectp3d = np.zeros((1, checkerboard_corners[0] * checkerboard_corners[1], 3), np.float32)
        objectp3d[0, :, :2] = np.mgrid[0:checkerboard_corners[0], 0:checkerboard_corners[1]].T.reshape(-1, 2)
        images = glob.glob(self.path_to_cal_photos + '*.jpg')
        good_images = []
        assert (images)
        for filename in images:
            image = cv2.imread(filename)
            grayColor = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # Find the chess board corners. If desired number of corners are found in the image then image_good = true
            image_good, corners = cv2.findChessboardCorners(grayColor, checkerboard_corners,cv2.CALIB_CB_ADAPTIVE_THRESH
                + cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_NORMALIZE_IMAGE)
            if image_good:
                good_images.append(filename)
                threedpoints.append(objectp3d)
                # Refining pixel coordinates for given 2d points.
                corners2 = cv2.cornerSubPix(grayColor, corners, (11, 11), (-1, -1), criteria)
                twodpoints.append(corners2)
            if image_good and see_corners:
                # Draw and display the corners
                image = cv2.drawChessboardCorners(image,checkerboard_corners,corners2, image_good)
                cv2.imshow('img', image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
        # Perform camera calibration by passing the value of above found out 3D points (threedpoints)
        # and its corresponding pixel coordinates of the detected corners (twodpoints)
        ret, self.mtx, self.dist, r_vecs, t_vecs = cv2.calibrateCamera(threedpoints, twodpoints, grayColor.shape[::-1],None, None)
        # Get the new camera matrix. Only have to do this once with one image.
        img = cv2.imread(good_images[0])
        h, w = img.shape[:2]
        self.newcameramtx, self.roi = cv2.getOptimalNewCameraMatrix(self.mtx, self.dist, (w, h), 1, (w, h))
        if test:
            for file in good_images:
                img = cv2.imread(file)
                cv2.imshow('uncorrected img - press a key to continue', img)
                newimg = cv2.undistort(img, self.mtx, self.dist, None, self.newcameramtx)
                x, y, w, h = self.roi
                newimg = newimg[y:y + h, x:x + w]
                cv2.imshow('corrected img - press a key to continue', newimg)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

    ####################################################################################################################
    # UTILITIES
    ####################################################################################################################
    def __add_aruco_illustration(self):
        # Show axes lines
        offset = 50
        c = self.aruco_center
        cv2.line(self.frame, (c[0], c[1] + offset), (c[0], c[1] - offset), color=(0, 0, 255), thickness=1)
        cv2.line(self.frame, (c[0] + offset, c[1]), (c[0] - offset, c[1]), color=(0, 0, 255), thickness=1)

    def __add_cable_illustration(self):
        # Show line between color points.
        tuple(self.color_centers[0])
        cv2.line(self.frame, tuple(self.color_centers[0]), tuple(self.color_centers[1]), color= (0, 0, 255), thickness=1)
        for i, center in enumerate(self.color_centers):
            self.frame = cv2.circle(self.frame, tuple(center), radius=4, color=(0, 0, 255), thickness=-1)
        # Show a dot for where this falls on the y axis.

    def shutdown(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def __find_dev_path(self):
        """On linux systems the camera device communication happens via memory mapped io through a video file in the
        /dev directory. If you plug in a camera to Ubuntu it should add two more video device files, "/dev/video3" for
        example. The second to highest enumerated file should be the correct file for cv2.VideoCapture().
        Camera does not show up if you get the comport info from the serial library. This does not check to make sure
        the camera selected is the correct one (not the integrated camera). That will be checked by making sure the
        aruco marker can be found."""
        devices = os.listdir("/dev")
        vid_device_num = []
        for device in devices:
            if 'video' in device:
                string = device.replace("video","")
                vid_device_num.append(int(string))
        vid_device_num.sort(reverse=True)
        del vid_device_num[0]
        return '/dev/video' + str(vid_device_num[0])

    def __find_y_intercept(self, slope, pt):
        return pt[1] - (slope * pt[0])

    def __find_slope(self, pt1, pt2):
        if pt1[0] == pt2[0]:
            return None  # Infinite slope
        return (pt2[1] - pt1[1]) / (pt2[0] - pt1[0])

    ####################################################################################################################
    # TESTS
    ####################################################################################################################
    def test_camera(self):
        while True:
            ret, frame = self.cap.read()
            cv2.imshow("Press q to exit.", frame)
            if (cv2.waitKey(1) & 0xFF == ord('q')):
                break
        cv2.destroyAllWindows()

    def test_aruco(self):
        """https://mecaruco2.readthedocs.io/en/latest/notebooks_rst/Aruco/aruco_basics.html"""
        while True:
            ret, self.frame = self.cap.read()
            # TODO undistort the frame
            self.__find_aruco()
            if self.aruco_present:
                self.__aruco_transform()
                self.__find_aruco()
                self.frame = aruco.drawDetectedMarkers(self.frame, self.corners, self.ids)
            cv2.imshow("Press q to exit.", self.frame)
            if (cv2.waitKey(1) & 0xFF == ord('q')):
                break
        cv2.destroyAllWindows()

    def test_segmentation(self):
        while True:
            ret, self.frame = self.cap.read()
            self.__get_color_contours2()
        cv2.destroyAllWindows()

    def test_find_cable(self,show_contours=True):
        while True:
            self.cable_present = False
            ret, self.frame = self.cap.read()
            self.__get_color_contours()
            if self.cable_present:
                self.__add_cable_illustration()
            if show_contours:
                for c in self.cnts:
                    cv2.drawContours(self.frame, [c], 0, (0, 0, 0), 2)
            cv2.imshow("Press q to exit.", self.frame)
            if (cv2.waitKey(1) & 0xFF == ord('q')):
                break
        cv2.destroyAllWindows()

    def test_ground_truth(self):
        while True:
            self.find_ground_truth(undistort=False,illustrations=True)
            cv2.imshow("Press q to exit.", self.frame)
            if (cv2.waitKey(1) & 0xFF == ord('q')):
                break
        cv2.destroyAllWindows()

    def test(self):
        # self.test_camera()
        # self.__calibrate_cam(test=True)
        # self.test_aruco()
        self.test_segmentation()
        # self.test_find_cable()
        # self.test_ground_truth()

def main():
    path_to_cal_images = r"/home/ted/Documents/GitHub/IMML_Contactile_Gripper/ROS_Workspace/src/contactile_gripper/support/cal_images/"
    cam = Camera(path_to_cal_images)
    cam.test()

if __name__ == "__main__":
    main()