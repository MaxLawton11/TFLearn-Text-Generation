import tflearn
from tflearn.data_utils import *
from TFLearn.TFLearn_Model import *
from TFLearn.Constants import *

m = Model("testdata.txt")
X, Y = m.preprocess_data()
m.build_model()
m.train_model(X, Y)

# Save the trained model
m.model.save(m.model_path)

print("--Built Model--")