import dill
from Model import *

with open('model_dill.pkl', 'rb') as inp:
    m = dill.load(inp)

m = pickle.load(inp)
text = m.generate(15, "a", 0.5)
print("Text: ", text)
    
del m