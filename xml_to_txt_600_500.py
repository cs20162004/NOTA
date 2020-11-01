import glob, os
from PIL import Image
import xml.etree.ElementTree as ET

a = 600
b = 500
os.chdir("/home/plase1/Downloads/NOTA/train/annotations")
for infile in glob.glob("*.xml"):
	tree = ET.parse(infile)
	root = tree.getroot()
	
	width = int(root.find(".size/width").text)
	height = int(root.find(".size/height").text)
	xmin = int(root.find(".object/bndbox/xmin").text)
	xmin = (xmin * 600) / width
	xmax = int(root.find(".object/bndbox/xmax").text)
	xmax = (xmax * 600) / width
	ymin = int(root.find(".object/bndbox/ymin").text)
	ymin = (ymin * 500) / height
	ymax = int(root.find(".object/bndbox/ymax").text)
	ymax = (ymax * 500) / height
	name = root.find(".object/name").text
	
	x = round((xmax + xmin) / (2 * a), 6)
	y = round((ymax + ymin) / (2 * b), 6)
	width = round((xmax - xmin) / a, 6)
	height = round((ymax - ymin) / b, 6)
	s = ""
	
	if (name == "neutral"):
		s = s + "0"
	elif (name == "anger"):
		s = s + "1"
	elif (name == "surprise"):
		s = s + "2"
	elif (name == "smile"):
		s = s + "3"
	elif (name == "sad"):
		s = s + "4"
	s = s + " " + str(x)
	s = s + " " + str(y)
	s = s + " " + str(width)
	s = s + " " + str(height)
	
	outfile = open("/home/plase1/Downloads/NOTA/train/" + os.path.splitext(infile)[0] + ".txt", "w+")
	outfile.write(s)
#[neutral, anger, surprise, smile, sad]
