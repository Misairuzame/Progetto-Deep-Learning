import os
import glob
import PIL
import PIL.Image as Image

net_name = "yolo-voc"

images_file = './darknet/data/valid.txt'

output_folder = f"/home/umi/deep-learning-project/results/{net_name}/predicted-{net_name}"

if not os.path.exists(output_folder):
	os.mkdir(output_folder)

with open(images_file ,'r') as fobj:
	for line in fobj:
		command = ['./darknet detector test data/cartelli.data cfg/'+net_name+'-cartelli.cfg /home/umi/deep-learning-project/results/'+net_name+'/'+net_name+'-cartelli_best.weights -dont_show', line]
		os.chdir("/home/umi/deep-learning-project/darknet")
		os.system(' '.join(command))
		predicted_image = Image.open("/home/umi/deep-learning-project/darknet/predictions.jpg")
		filename = command[1].replace('data/cartelli_valid/','').replace('\n','')
		output = f"{output_folder}/predicted_{filename}"
		predicted_image.save(output)

