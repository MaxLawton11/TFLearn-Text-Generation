from Model import *
import os
import os.path
import sys

# get the number of chars we want made
if len(sys.argv) < 2 :
    sys.argv.append(50)
else :
    try :
        n_chars = int(sys.argv[1])
        if n_chars < 50 :
            n_chars = 50
    except Exception :
        print('# Incorrect Argument')
        print('# See README.md for usage')
#      "brotherhood in thee no sharper spur"
seed = "Ay, this is he that took King Henry's chair,"
temp = 0.5

# file to run model
sets_path = 'DataSets'
dir_list = os.listdir(sets_path)
if not dir_list :
    print('No vaild datasets')
    quit()

print('--------- Generating ---------')
# load model
print(f'# Using: {sets_path}/{dir_list[0]}')
m = Model(f'{sets_path}/{dir_list[0]}')
m.model.load('model_instance.tflearn')

# make text from seed
#text = m.generate(int(sys.argv[1]), seed, temp)
print(m.char_idx)
text = m.generate(n_chars, seed, temp)
print(f'Seed: "{seed}"')
print(f'n_chars: "{n_chars}"')
print('Text: ', text)
    
del m
print('--------- Success ---------')
