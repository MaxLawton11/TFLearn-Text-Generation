import tensorflow as tf
from Model import *
import os.path

#init and train
m = Model("DataSet.text")

if os.path.isfile("model_instance.tflearn.index") and  os.path.isfile("model_instance.tflearn.meta") :
    m.model.load("model_instance.tflearn")
else :
    pass

m.train(300)

m.save("model_instance.tflearn")

print("--- Model Traind & Saved ---")
del m