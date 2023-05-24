from Model import *
import os
import os.path
import sys

sets_path = 'DataSets'
dir_list = os.listdir(sets_path)
dir_list_len = len(dir_list)

training_cycles = 1

def do_quit() :
    print('# Incorrect Argument')
    print('# See README.md for usage')
    quit()

# test user input
try :
    if len(sys.argv) < 2 :
        training_cycles = 1
    elif len(sys.argv) > 2 or int(sys.argv[1]) < 1:
        do_quit()
    else :
        training_cycles = int(sys.argv[1])
except :
    do_quit()

print('--------- Training ---------')
print(f'# Running {training_cycles} epoch(s)')
for path, path_counter in zip(dir_list,range(1,len(dir_list)+1)) :
    # create model
    print(f'# Currently using the ({path}) dataset ｜ {path_counter} of {len(dir_list)}')
    m = Model(f'{sets_path}/{path}')

    # load model if there is one
    if os.path.isfile('model_instance.tflearn.index') and os.path.isfile('model_instance.tflearn.meta') :
        m.model.load('model_instance.tflearn')
    else :
        pass

    m.train(training_cycles)
    
    m.save('model_instance.tflearn')
    del m

print('--- Model Traind & Saved ---')
