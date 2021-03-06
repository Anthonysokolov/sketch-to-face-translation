'''
This script scales the 128x128 images generated by our GAN to 256x256
We implement a baseline scaling procedure and a deep learning based scaling algorithm
'''
input_dir = './resnet_200/*'
output_dir = ''

import glob
import cv2 as cv
from cv2 import dnn_superres

# Set our model and load weights
sr = dnn_superres.DnnSuperResImpl_create()
path = "EDSR_x2.pb"
sr.readModel(path)
# Using EDSR model for upscaling with a factor of 2
sr.setModel("edsr", 2)

# save scaled images
i = 0
for file in glob.glob(input_dir):
    img = cv.imread(file)

    # get predicition from neural network
    superres = sr.upsample(img)
    cv.imwrite(output_dir+file.replace('.jpg','_superres.jpg'),superres)

    # save baseline approach
    bicubic = cv.resize(img, (256,256), interpolation=cv.INTER_CUBIC)
    cv.imwrite(output_dir+file.replace('.jpg','_bicubic.jpg'),bicubic)

    if i % 50 == 0:
        print("Completed",i/5,"%")

    i += 1
