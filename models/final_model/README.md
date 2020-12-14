This directory contains the code used for our GAN model that incorporates Super Resolution. 
`final_gan.ipynb` trains a conditional GAN with a ResNet generator at 128x128 resolution and loads an image scaling CNN to scale the output to 256x256. 
`resnet9.h5` contains the weights for the GAN trained in `final_gan.ipynb`. 
`EDSR_x2.pb` contains the weights used for the image scaling CNN. The weights were obtained from `https://github.com/Saafke/EDSR_Tensorflow/blob/master/models/EDSR_x2.pb`  
`scale_resolution.py` is a script to convert 128x128 images to 256x256 using the image scaling CNN.
'cGAN_v2.ipynb` is a notebook with that explores if using instance normalization affects results when using a ResNet generator.
