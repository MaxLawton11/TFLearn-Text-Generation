import pickle
from Model import *
from multiprocessing import Lock

lock = Lock()

m = Model("DataSet.text")
m.train(10)

lock.acquire()

with open('model.pkl', 'wb') as outp:
    pickle.dump(m, outp, pickle.HIGHEST_PROTOCOL)

lock.release()

print("--- Model Traind & Saved ---")
del m