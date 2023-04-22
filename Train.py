import tensorflow as tf
from Model import *

#init and train
m = Model("DataSet.text")
m.train(2)

m.save("my_model.tflearn")

print("--- Model Traind & Saved ---")
del m