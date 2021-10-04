import os
import sys

cfg_path = "/home/umi/deep-learning-project/darknet/cfg/"

arch = sys.argv[1]

cfg_file = arch + ".cfg"

if os.path.exists(arch+".tmp"):
 	os.remove(arch+".tmp")

if os.path.exists(arch+".model"):
 	os.remove(arch+".model")

with open(cfg_path+cfg_file, "r") as f:	
	with open(arch+".tmp", "a") as tmp:
		a_line = f.readline()
		while a_line != "" and a_line is not None:
			a_line = a_line.strip()
			if not a_line.startswith("#"):
				tmp.write(a_line)
				tmp.write("\n")
			a_line = f.readline()

with open(arch+".tmp") as f:
	string_to_write = ""
	a_line = f.readline()
	while a_line != "" and a_line is not None:
		a_line = a_line.replace("\n", "")
		if a_line.startswith("[") and a_line != "[net]":
			string_to_write = string_to_write+a_line + "\n\tv\n"
		a_line = f.readline()
	with open(arch+".model", "a") as model:
		model.write("Rete: "+arch+"\n\n")
		string_to_write = string_to_write[:-3]
		model.write(string_to_write)

os.remove(arch+".tmp")
