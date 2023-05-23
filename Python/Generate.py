from Model import *
import os
import os.path
import sys

# get the number of chars we want made
if len(sys.argv) < 2 :
    sys.argv.append(25)
else :
    try :
        int(sys.argv[1])
    except Exception :
        print('# Incorrect Argument')
        print('# See README.md for usage')

seed = "So early walking did I see your son"
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
text = m.generate(25, seed, temp)
print(f'Seed: "{seed}"')
print('Text: ', text)
    
del m
print('--------- Success ---------')
