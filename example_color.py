import glob
import numpy as np
import cv2
import os
from PIL import Image

for infile in glob.glob("I/*"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.load()
    data = np.asarray(im)

# define the list of boundaries
    boundaries = [
        ([141,85,36], [255,224,189])] #: a list of lower limits and a list of upper limits.

    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(data, lower, upper)
        output = cv2.bitwise_and(data, data, mask=mask)

        # show the images
        im = Image.fromarray(output, "RGB")
        im.show()
