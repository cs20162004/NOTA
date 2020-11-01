import os
import glob
os.system
import PIL
import PIL.Image as Image

d = 0
test_Path = r'/home/plase1/Downloads/NOTA/darknet_YOLO_600_500/training/test_data'
with open((test_Path + '.txt'),'r') as fobj:
	for line in fobj:
		image_List = [[num for num in line.split()] for line in fobj]
		for images in image_List:
			commands = ['./darknet detector test training/model_class/mymodel.data training/model_class/yolov3-tiny_model.cfg backup/yolov3-tiny_model_5000.weights -dont_show', images[0]]
			os.system(' '.join(commands))
			predicted_image = Image.open("/home/plase1/Downloads/NOTA/darknet_YOLO_600_500/predictions.jpg")
			output = images[0]
			predicted_image.save(output)
			
