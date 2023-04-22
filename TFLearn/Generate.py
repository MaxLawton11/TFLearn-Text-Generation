import pickle
from Model import *

with open('model.pkl', 'rb') as inp:
    m = pickle.load(inp)
    text = m.generate(15, "a", 0.5)
    print("Text: ", text)
    
del m