from Model import *

m = Model("DataSet.text")
m.train(10)

text = m.generate(5, "h", 0.5)

m.train(10)

text = m.generate(10, "a", 0.5)

print(text)
