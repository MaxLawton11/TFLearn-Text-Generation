import dill  
from Model import *

m = Model("DataSet.text")
m.train(10)

with open('model_dill.pkl', 'wb') as outp:
    dill.dump(m, outp)


print("--- Model Traind & Saved ---")
del m