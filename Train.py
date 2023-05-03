import tensorflow as tf
from Model import *
import os
import os.path

path = "DataSets"
dir_list = os.listdir(path)
training_cycles = 1

print("--------- Training ---------")

for path in dir_list :
    #create model
    print(f"Currently using the ({path}) dataset")
    m = Model(f"DataSets/{path}")

    if os.path.isfile("model_instance.tflearn.index") and  os.path.isfile("model_instance.tflearn.meta") :
        m.model.load("model_instance.tflearn")
    else :
        pass

    m.train(training_cycles)
    
    m.save("model_instance.tflearn")
    del m

print("--- Model Traind & Saved ---")
del m
