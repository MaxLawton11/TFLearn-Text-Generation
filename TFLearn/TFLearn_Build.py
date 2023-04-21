import tflearn
from tflearn.data_utils import *
import pickle
from TFLearn_Model import *
from Constants import *

m = Model("testdata.txt")
X, Y = m.preprocess_data()
m.build_model()
m.train_model(X, Y)

# Save the trained model
#m.model.save(m.model_path)

print("--Built Model--")