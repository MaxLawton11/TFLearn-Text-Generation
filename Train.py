import tensorflow as tf
from Model import *
import os
import os.path

path = "DataSets"
dir_list = os.listdir(path)

for path in dir_list :
    #create model
    m = Model("DataSets/DataSet.text")

    if os.path.isfile("model_instance.tflearn.index") and  os.path.isfile("model_instance.tflearn.meta") :
        m.model.load("model_instance.tflearn")
    else :
        pass

    m.train(30)
    
    m.save("model_instance.tflearn")
    del m

print("--- Model Traind & Saved ---")
del m
