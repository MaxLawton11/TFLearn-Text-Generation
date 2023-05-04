import tensorflow as tf
from Model import *
import os
import os.path
import sys

setsPath = "../DataSets"
#dir_list = os.listdir(setsPath)
training_cycles = 1

if os.path.exists(setsPath) and os.path.isdir(setsPath):
    # List the contents of the directory
    print("PATH TURE!")
else :
    print("PATH FALSE!")

print("--------- Training ---------")

for path in dir_list :
    #create model
    print(f"Currently using the ({path}) dataset")
    m = Model(f"{setsPath}/{path}")

    #load model if there is one
    if os.path.isfile("model_instance.tflearn.index") and  os.path.isfile("model_instance.tflearn.meta") :
        m.model.load("model_instance.tflearn")
    else :
        pass

    m.train(training_cycles)
    
    m.save("model_instance.tflearn")
    del m

print("--- Model Traind & Saved ---")
