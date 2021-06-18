import cv2
import numpy as np


def segment(image):
 
    img = cv2.resize(image, (540, 540))
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)


    #find the green color 
    mask_green = cv2.inRange(hsv, (36,0,0), (86,255,255))
    #find the brown color
    mask_brown = cv2.inRange(hsv, (8, 60, 20), (30, 255, 200))
    #find the yellow color in the leaf
    mask_yellow = cv2.inRange(hsv, (21, 39, 64), (40, 255, 255))


    #find any of the three colors(green or brown or yellow) in the image
    mask = cv2.bitwise_or(mask_green, mask_brown)
    mask = cv2.bitwise_or(mask, mask_yellow)

    # remove noise
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel=np.ones((8,8),dtype=np.uint8))
    # apply mask to original image
    #Bitwise-AND mask and original image
    res = cv2.bitwise_and(img,img, mask= mask)


    return res