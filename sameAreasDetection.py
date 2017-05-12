
#http://www.pyimagesearch.com/2015/01/26/multi-scale-template-matching-using-python-opencv/

import glob
import re

import imutils
import numpy as np
import cv2
import os
from PIL import Image
from os.path import basename


def N(im, imagePath):
    template = cv2.imread(im)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    template = cv2.Canny(template, 50, 200)
    (tH, tW) = template.shape[:2]
    filenameT = os.path.splitext(os.path.basename(im))[0]

    image = cv2.imread(imagePath)
    filename = os.path.splitext(os.path.basename(imagePath))[0]
    ext = os.path.splitext(os.path.basename(imagePath))[1]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    found = None

    c = 1
    for scale in np.linspace(0.2, 1.0, 20)[::-1]:

        resized = imutils.resize(gray, width=int(gray.shape[1] * scale))
        r = gray.shape[1] / float(resized.shape[1])


        if resized.shape[0] < tH or resized.shape[1] < tW:
            break
        # result = cv2.matchTemplate(resized, template, cv2.TM_CCOEFF)
        # (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
        edged = cv2.Canny(resized, 50, 200)
        result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF)
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)


        if found is None or maxVal > found[0]:
            found = (maxVal, maxLoc, r)

            (_, maxLoc, r) = found
            (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
            (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))

            #cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
            #cv2.imshow("Image", image)
            roi = image[startX:endX, startY:endY]
            #cv2.imshow("RRRR", roi)
            # os.chdir('./I_Areas')
            # cv2.imwrite(filename +"_"+str(c) +"_" + filenameT + ext, roi)
            # os.chdir('..')
            # #cv2.waitKey(0)
            # c+=1




for imagePath in glob.glob("I/*"):
    filename = os.path.splitext(os.path.basename(imagePath))[0]
    extC = os.path.splitext(os.path.basename(imagePath))[1]
    for imagePath in glob.glob("I_Types/*"):
        f = os.path.splitext(os.path.basename(imagePath))[0]
        extO = os.path.splitext(os.path.basename(imagePath))[1]
        #if f.startswith(filename+'.'):
        fileO = "I_Types/"+ f+ extO
        fileC = "I/"+filename + extC
        N(fileO, fileC)
       # print("------", fileO, "------", fileC)


