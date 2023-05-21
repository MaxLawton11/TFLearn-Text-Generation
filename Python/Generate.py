from Model import *
import os
import os.path
import sys

def do_quit() :
    print("# Incorrect Argument")
    print("# See README.md for usage")
    quit()

if len(sys.argv) < 3 :
    sys.argv.append(25)
elif len(sys.argv) < 2 :
    do_quit()
else :
    try :
        int(sys.argv[2])
        str(sys.argv[1])
    except Exception :
        do_quit()


sets_path = "DataSets"
dir_list = os.listdir(sets_path)

print("--------- Generating ---------")

if not dir_list :
    print("No vaild datasets")
    quit()

print(f"# Using: {sets_path}/{dir_list[0]}")
m = Model(f"# Using: {sets_path}/{dir_list[0]}")
m.model.load("model_instance.tflearn")
text = m.generate(int(sys.argv[2]), str(sys.argv[1]), 0.5)
print("Text: ", text)
    
del m
print("--------- Success ---------")
