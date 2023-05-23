from Model import *
import os
import os.path

seed = "this is he that took King"
temp = 0.5
n_chars = 1000

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
text = m.generate(n_chars, seed, temp)
print(f'Seed: "{seed}"')
print(f'n_chars: "{n_chars}"')
print('Text: ', text)
    
del m
print('--------- Success ---------')
