import tensorflow as tf
from Model import *

#init and train
m = Model("DataSet.text")
m.train(300)

m.save("model_instance.tflearn")

print("--- Model Traind & Saved ---")
del m