# import the necessary packages
import glob

import imutils
import numpy as np
import cv2
import os
from os.path import basename

for infile in glob.glob("I/*"):
    image = cv2.imread(infile)
    ratio = image.shape[0] / 300.0
    orig = image.copy()
    #image = imutils.resize(image, height=300)

    # convert the image to grayscale, blur it, and find edges
    # in the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(gray, 30, 200)
    cv2.imshow("E", edged)
    cv2.waitKey(0)
    # # find contours in the edged image, keep only the largest
    # # ones, and initialize our screen contour
    (_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    screenCnt = None

    # loop over our contours
    for c in cnts:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        # if our approximated contour has four points, then
        # we can assume that we have found our screen
        if len(approx) == 4:
            screenCnt = approx
            break

    cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
    cv2.imshow("Game Boy Screen", image)
    cv2.waitKey(0)