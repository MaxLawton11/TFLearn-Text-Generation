import tensorflow as tf
from Model import *
import sys

m = Model("DataSet.text")
m.model.load("model_instance.tflearn")

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

text = m.generate(int(sys.argv[2]), str(sys.argv[1]), 0.5)
print("Text: ", text)
    
del m