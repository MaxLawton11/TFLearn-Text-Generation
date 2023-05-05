from Model import *
import os
import os.path
import sys

sets_path = "DataSets"
dir_list = os.listdir(sets_path)
training_cycles = 1

if len(sys.argv) < 2 :
    training_cycles = 1
elif len(sys.argv) > 2 or not isinstance(sys.argv[1], int) or sys.argv[1] < 1:
    print("Incorrect Argument")
    print("See README.md for usage")
    quit()
else :
    training_cycles = sys.argv[1]

print("--------- Training ---------")
path_counter = 1
for path in dir_list :
    #create model
    print(f"Currently using the ({path}) dataset ｜ {path_counter} of {len(dir_list)}")
    m = Model(f"{sets_path}/{path}")

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
