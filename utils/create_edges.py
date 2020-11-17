'''
This program reads in all images in the faces directory and
writes a corresponding edge map to the edges directory
'''

import cv2 as cv
import numpy as np
from PIL import Image
import PIL.ImageOps
from pathlib import Path

p = Path("../data/classes/train_A/train/")
files = [f for f in p.iterdir() if str(f)[-3:]=="jpg"]

for file in files:
    img = cv.imread(str(file),0)
    edges = Image.fromarray(cv.Canny(img,100,200))
    edges = PIL.ImageOps.invert(edges)
    edges.save("../data/classes/train_B/train/" + file.parts[-1])
