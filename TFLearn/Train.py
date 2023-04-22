import pickle
from Model import *

m = Model("DataSet.text")
m.train(10)


with open('model.pkl', 'wb') as outp:
    pickle.dump(m, outp, pickle.HIGHEST_PROTOCOL)

print("--- Model Traind & Saved ---")
del m