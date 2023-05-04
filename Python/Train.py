from Model import *
import os
import os.path
import sys

setsPath = "DataSets"
dir_list = os.listdir(setsPath)
training_cycles = 1

print("--------- Training ---------")
path_counter = 1
for path in dir_list :
    #create model
    print(f"Currently using the ({path}) dataset ｜ {path_counter} of {len(dir_list)}")
    m = Model(f"{setsPath}/{path}")

    #load model if there is one
    if os.path.isfile("model_instance.tflearn.index") and  os.path.isfile("model_instance.tflearn.meta") :
        m.model.load("model_instance.tflearn")
    else :
        pass

    m.train(training_cycles)
    
    m.save("model_instance.tflearn")
    del m
    path_counter = path_counter + 1

print("--- Model Traind & Saved ---")
