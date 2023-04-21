import tflearn
import tensorflow as tf
from tflearn.data_utils import *
from Constants import *
import sys

import os.path

seed = sys.argv[1]

print("model.tfl : ", os.path.isfile("model.tfl"))

# Load the saved model
char_idx = None
with open("char_idx.pkl", "rb") as f:
    char_idx = pickle.load(f)
    
model.load("/home/system/ML/TFLearn-Text-Generation/TFLearn/model.tfl")
#model = tflearn.SequenceGenerator(load_path="model.tfl", dictionary=char_idx, seq_maxlen=Constant_maxlen)

# Use the loaded model to generate text
generated_text = model.generate(length=100, temperature=0.5, seq_seed=seed)
print(generated_text)
