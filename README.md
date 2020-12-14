# Sketch To Face Translation
This repository features several notebooks exploring the performance of different GAN architectures in the task of translating an outline image of a face into a realistic 256x256 image of a human face.  
# Directory
`models/conditional_gan` contains the code used to fit a conditional GAN to our data.    
`models/cycle_gan` contains the code used to fit a cycle consistent GAN to our data.  
`models/final_gan` contains the code for our proposed model architecture, which combines a conditional GAN approach with deep learning based upscaling.  

# Dataset
Facial images taken from `https://www.kaggle.com/jessicali9530/celeba-dataset`.  
Realistic sketches generated using openCV.

# Our Examples
![Examples](/example_outputs.png)

