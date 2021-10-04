from os import listdir
from os.path import isfile, join
import cv2

dataset_directory = "/home/umi/Download/FullIJCNN2013"

images = [f for f in listdir(dataset_directory) if isfile(join(dataset_directory, f)) and f.endswith('.ppm')]

for image in images:
	img_path = join(dataset_directory, image)
	im = cv2.imread(img_path)
	h, w, c = im.shape
	print(f"{image}:{w}x{h}")
	if w != 1360 or h != 800:
		print(f"{image} is not of size 1360x800!")

