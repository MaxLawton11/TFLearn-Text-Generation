import tflearn
import tensorflow as tf
from tflearn.data_utils import *
import TFLearn_Model
from Constants import *
import sys

import os.path

seed = sys.argv[1]

print("model.tfl : ", os.path.isfile("model.tfl"))

# Load the saved model
char_idx = None
with open("char_idx.pkl", "rb") as f:
    char_idx = pickle.load(f)
    
model = Model()
model.model.load("model.tfl", weights_only=True)


# Use the loaded model to generate text
generated_text = model.generate(length=100, temperature=0.5, seq_seed=seed)
print(generated_text)
