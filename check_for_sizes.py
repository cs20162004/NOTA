import glob, os
from PIL import Image
import numpy as np

a = 1
b = 1
os.chdir("/home/plase1/Downloads/NOTA/test/img")
dire = ""
for infile in glob.glob("*.jpg"):
    im = Image.open(infile)
    aa, bb = im.size
    if a < aa:
        a = aa
        dire = infile
    if b < bb:
        b = bb

for infile in glob.glob("*.JPG"):
    im = Image.open(infile)
    if a < aa:
        a = aa
        dire = infile
    if b < bb:
        b = bb
        
print(a)
print(b)
print(dire)
