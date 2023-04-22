from Model import *

m = Model("DataSet.text")
m.train(10)

text = m.generate("h", 0.5)
print(text)

