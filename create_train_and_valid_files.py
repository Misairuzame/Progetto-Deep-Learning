import glob

images_list = glob.glob("data/cartelli_train/*.jpg")
with open("data/train.txt", "w") as f:
	f.write("\n".join(images_list))

images_list = glob.glob("data/cartelli_valid/*.jpg")
with open("data/valid.txt", "w") as f:
	f.write("\n".join(images_list))
