from os import listdir, utime
from os.path import isfile, join

image_width = 1360
image_height= 800

ground_truth_path = "/home/umi/Download/FullIJCNN2013/gt.txt"
label_files_path   = "/home/umi/deep-learning-project/dataset-yolo/"

classifying_method = "superclass"


def check_class(una_classe):
    if classifying_method != "superclass":
        return una_classe
    else:
        if una_classe in [0,1,2,3,4,5,7,8,9,10,15,16]:  # prohibitory
            return 0
        elif una_classe in [33,34,35,36,37,38,39,40]:   # mandatory
            return 1
        elif una_classe in [11,18,19,20,21,22,23,24,25,26,27,28,29,30,31]:
            return 2                                    # danger
        elif una_classe in [6,12,13,14,17,32,41,42]:    # other
            return 3


def create_label_files():
    with open(ground_truth_path) as gt:
        line = gt.readline()
        while line != "":
            #print(f"{line}")
            
            label_file = label_files_path+line[0:5]+".txt"
            with open(label_file, 'a') as lf:
                fields = line.split(';')
                #img_no    = fields[0]
                left_col  = int(fields[1])
                top_row   = int(fields[2])
                right_col = int(fields[3])
                bottom_row= int(fields[4])
                class_id  = int(fields[5])
                
                # In YOLO si segue questo formato per quanto riguarda
                # la decrizione degli oggetti:
                # <object-class> <x> <y> <width> <height>
                # Dove x, y, width e height sono normalizzate rispetto alla
                # risoluzione dell'immagine, quindi tutte comprese fra 0 e 1.
                # x e y indicano il "centro" dell'oggetto, mentre width e height
                # rappresentano le dimensioni della "scatola" che lo contiene.
                # Inoltre, per questo problema, ci interessa usare la
                # "superclasse" per effettuare classificazione
                # (ossia se un cartello è di divieto, di obbigo, di pericolo
                # o altro) piuttosto che dire esattamente che cartello è.
                # Nota: non tutte le immagini del dataset contengono cartelli!
                # 159 immagini (su 900) non contengono cartelli.
                # Nota: tengo 6 cifre decimali
                my_class_id = check_class(class_id)            
                
                absolute_width  = right_col - left_col
                absolute_height = bottom_row - top_row
                absolute_x = (right_col + left_col) / 2
                absolute_y = (bottom_row + top_row) / 2
                
                x = absolute_x / image_width
                y = absolute_y / image_height
                width = absolute_width / image_width
                height = absolute_height / image_height
                
                lf.write(f"{my_class_id} {x:.6f} {y:.6f} {width:.6f} {height:.6f}\n")
            
            line = gt.readline()


# E' preferibile aggiungere dei file vuoti nel caso le
# corrispondenti immagini non contengano alcun oggetto
def touch(fname):
    with open(fname, 'a'):
      try:
        utime(fname, None)
      except OSError:
        print(f"Error while creating empty file {fname}")


def add_empty_files():
    text_files = [f for f in listdir(label_files_path) if isfile(join(label_files_path, f)) and f.endswith('.txt')]
    for i in range (0, 900):
        tmp = str(i).zfill(5)
        temp_name = tmp+".txt"
        if temp_name not in text_files:
            touch(label_files_path+temp_name)


if __name__ == '__main__':
    create_label_files()
    add_empty_files()

