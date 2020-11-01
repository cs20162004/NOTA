import glob, os
from PIL import Image
a = 1000
b = 1000
os.chdir("/home/plase1/Downloads/NOTA/test/img")
size = 600, 500
for infile in glob.glob("*.jpg"):
    im = Image.open(infile)
    aa, bb = im.size
    if a > aa:
        a = aa
    if b > bb:
        b = bb
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    try:
        im = Image.open(infile)
        new_image = im.resize((153, 180))
        #im.thumbnail(size, Image.ANTIALIAS)
        #print(outfile)
        new_image.save("/home/plase1/Downloads/NOTA/test/" + infile, "JPEG")
    except IOError:
        print ("cannot create thumbnail for '%s'" % infile)
      
for infile in glob.glob("*.JPG"):
    im = Image.open(infile)
    aa, bb = im.size
    if a > aa:
        a = aa
    if b > bb:
        b = bb
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    try:
        im = Image.open(infile)
        new_image = im.resize((153, 180))
        #im.thumbnail(size, Image.ANTIALIAS)
        #print(outfile)
        new_image.save("/home/plase1/Downloads/NOTA/test/" + infile, "JPEG")
    except IOError:
        print ("cannot create thumbnail for '%s'" % infile)
    
print(a)
print(b)
