import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import glob
import cv2


def Calibrate():
    # Number of object points
    num_intersections_in_x = 7
    num_intersections_in_y = 7
    
    # Size of square in meters
    square_size = 0.0225
    
    # Arrays to store 3D points and 2D image points
    obj_points = []
    img_points = []
    
    # Prepare expected object 3D object points (0,0,0), (1,0,0) ...
    object_points = np.zeros((7*7,3), np.float32)
    object_points = np.mgrid[0:7, 0:7].T.reshape(-1,2)
    object_points = object_points*square_size
    
    fnames = glob.glob('/home/pi/Documents/pi_sensor_setup/camera_calibration/images/'+'*.'+'jpg')
    
    
    for fname in fnames:
        img = cv2.imread(fname)
        gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Find chess board corners
        ret, corners = cv2.findChessboardCorners(gray_scale, (num_intersections_in_x, num_intersections_in_y), None)
        
        if ret:
            obj_points.append(object_points)
            img_points.append(corners)
            
            # Draw the corners
            drawn_img = cv2.drawChessboardCorners(img, (7,7), corners, ret)
            cv2.imshow('Corners drawn on board', drawn_img)



if __name__ == "__main__":
    Calibrate()
    
