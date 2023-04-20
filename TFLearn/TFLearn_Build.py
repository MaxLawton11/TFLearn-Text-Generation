import tflearn
from tflearn.data_utils import *
from TfLearn_Model import *
from parentdirectory import Constants

m = Model("path/to/text/file.txt", maxlen=25)
X, Y = m.preprocess_data()
m.build_model()
m.train_model(X, Y)

# Save the trained model
m.model.save(m.model_path)