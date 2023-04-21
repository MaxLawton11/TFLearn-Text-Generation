import tflearn
import tensorflow as tf
from tflearn.data_utils import *
from TFLearn_Model import *
from Constants import *
import sys

import os

seed = sys.argv[1]

if os.path.getsize("char_idx.pkl") == 0:
    print("The dictionary file is empty!")
else:
    with open("char_idx.pkl", "rb") as f:
        char_idx = pickle.load(f)

"""# Load the saved model
char_idx = None
with open("char_idx.pkl", "rb") as f:
    char_idx = pickle.load(f)"""
    
#m = Model("testdata.txt")

input_layer = tflearn.input_data(shape=[None, Constant_maxlen, len(char_idx)])
lstm_layer = tflearn.lstm(input_layer, 256)
output_layer = tflearn.fully_connected(lstm_layer, len(char_idx), activation='softmax')
net = tflearn.regression(output_layer, optimizer='adam', loss='categorical_crossentropy')

model = tflearn.SequenceGenerator(net)
model.load("model.tfl")


# Use the loaded model to generate text
generated_text = model.generate(length=100, temperature=0.5, seq_seed=seed)
print(generated_text)
