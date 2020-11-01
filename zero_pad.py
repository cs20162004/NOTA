import glob, os
from PIL import Image
import numpy as np


def zero_pad(img, max_a, max_b):
    a_size, b_size = img.size
    print(a_size)
    print(b_size)
    img_mat = np.asarray(img)
    print(img_mat.shape)
    new_im = np.zeros((max_b, max_a, 3))
    a_dif = max_a-a_size
    b_dif = max_b-b_size
    new_im[:-b_dif,:-a_dif, :] = img_mat
    return new_im
    
    
a = 7297
b = 4871
os.chdir("/home/plase1/Downloads/NOTA/train/img")

for infile in glob.glob("*.jpg"):
    im = Image.open(infile)
    new_im = zero_pad(im, a, b)
    new_image = Image.fromarray(new_im.astype(np.uint8))
    new_image.save("/home/plase1/Downloads/NOTA/train/" + infile, "JPEG")

for infile in glob.glob("*.JPG"):
    im = Image.open(infile)
    new_im = zero_pad(im, a, b)
    new_image = Image.fromarray(new_im.astype(np.uint8))
    new_image.save("/home/plase1/Downloads/NOTA/train/" + infile, "JPEG")
        

