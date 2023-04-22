import tensorflow as tf
from Model import *

m = Model("DataSet.text")
m.model.load("my_model.tflearn")

text = m.generate(15, "a", 0.5)
print("Text: ", text)
    
del m