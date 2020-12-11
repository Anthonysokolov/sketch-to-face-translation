'''
This program reads in all images in the faces directory and
writes a corresponding edge map to the edges directory
'''    

import cv2 as cv
import numpy as np
from PIL import Image
import PIL.ImageOps
from pathlib import Path
import os


pt = Path("../data/CUHK/sketches/train")
st = Path("../data/CUHK/photos/train")
pfiles = [f for f in pt.iterdir() if str(f)[-3:]=="jpg"]
sfiles = [f for f in st.iterdir() if str(f)[-3:]=="jpg"]

for index, file in enumerate(pfiles):
    try : 
        phead, ptail = os.path.split(file)
        src = "../data/CUHK/photos/train" + "/" + "f-" + ptail[3:9] + ".jpg"
        shead, stail = os.path.split(src)

        os.rename(src, shead+"/"+ptail)
        print("Source path renamed to destination path successfully.") 
      
    # If Source is a file  
    # but destination is a directory 
    except IsADirectoryError: 
        print("Source is a file but destination is a directory.") 
      
    # If source is a directory 
    # but destination is a file 
    except NotADirectoryError: 
        print("Source is a directory but destination is a file.") 
      
    # For permission related errors 
    except PermissionError: 
        print("Operation not permitted.") 
      
    # For other errors 
    except OSError as error: 
        print(error) 
