import tensorflow as tf
from Model import *
import os
import os.path
import sys

#Move back into parent directory
sys.path.append('..')

if len(sys.argv) < 3 :
    sys.argv.append(25)
elif len(sys.argv) < 2 :
    print("Incorrect Arguments")
    print("./generate.sh [base_text] [n_char = 25]")
    quit()
else :
    pass

try :
    int(sys.argv[2])
    str(sys.argv[1])
except Exception :
    print("Incorrect Arguments")
    raise "./generate.sh [base_text] [n_char = 25]"


setsPath = "Datasets"
dir_list = os.listdir(setsPath)

print("--------- Generating ---------")

if not dir_list :
    print("No vaild datasets")
    quit()

m = Model(f"{path}/{dir_list[0]}")
m.model.load("model_instance.tflearn")
text = m.generate(int(sys.argv[2]), str(sys.argv[1]), 0.5)
print("Text: ", text)
    
del m
