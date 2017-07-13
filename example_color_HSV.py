import glob
import numpy as np
import cv2
import os
from os.path import basename


for infile in glob.glob("I/*"):
    im = cv2.imread(infile)
    file, ext = os.path.splitext(infile)
    # define the upper and lower boundaries of the HSV pixel
    # intensities to be considered 'skin'
    lower = np.array([0, 48, 36], dtype="uint8")
    upper = np.array([20, 255, 255], dtype="uint8")


    converted = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    skinMask = cv2.inRange(converted, lower, upper)

    # apply a series of erosions and dilations to the mask
    # using an elliptical kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    skinMask = cv2.erode(skinMask, kernel, iterations=2)
    skinMask = cv2.dilate(skinMask, kernel, iterations=2)

    # blur the mask to help remove noise, then apply the
    # mask to the frame
    skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
    skin = cv2.bitwise_and(im, im, mask=skinMask)

    #saving images in folder I_Detection
    os.chdir("./I_Detection")
    name = os.path.splitext(basename(infile))[0] + "_HSV" + ext
    print(name)
    cv2.imwrite(name,  skin)
    os.chdir("..")
