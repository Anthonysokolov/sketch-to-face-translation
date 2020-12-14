## Prepare your own datasets for CycleGAN

You need to create two directories to host images from domain A /path/to/data/trainA and from domain B /path/to/data/trainB. Then you can train the model with the dataset flag --dataroot /path/to/data. Optionally, you can create hold-out test datasets at /path/to/data/testA and /path/to/data/testB to test your model on unseen images.

## Prepare your own datasets for pix2pix
Pix2pix’s training requires paired data. We provide a python script to generate training data in the form of pairs of images {A,B}, where A and B are two different depictions of the same underlying scene. For example, these might be pairs {label map, photo} or {bw image, color image}. Then we can learn to translate A to B or B to A:

Create folder /path/to/data with subdirectories A and B. A and B should each have their own subdirectories train, val, test, etc. In /path/to/data/A/train, put training images in style A. In /path/to/data/B/train, put the corresponding images in style B. Repeat same for other data splits (val, test, etc).

Corresponding images in a pair {A,B} must be the same size and have the same filename, e.g., /path/to/data/A/train/1.jpg is considered to correspond to /path/to/data/B/train/1.jpg.

Once the data is formatted this way, call:

python datasets/combine_A_and_B.py --fold_A /path/to/data/A --fold_B /path/to/data/B --fold_AB /path/to/data

This will combine each pair of images (A,B) into a single image file, ready for training.


