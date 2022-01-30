from filter_the_vocabulary import vocabulary
import os,random,process_text as process_text,math
from hyperparameters import per
import pandas as pd 
import numpy as np
import time 
folders = ['neg','pos']
training_vector = dict()
'''
We will create a binary vector with 1 if the word in the dictionary is present in the sentence 
else the value will be 0 if it's not contained in the word 
this will be a pandas dataframe 
''' 
percentage_of_data = math.ceil(per * 12500) 
percentage = True
if(per == 1):
    percentage = False 
training_data_frame = pd.DataFrame()
already_selected = list()
count = 0
for i in folders:
    #path = "C:/Users/Nikos/Documents/GitHub/Aiexercise2/aclImdb/train/" + i
    path = "C:/Users/fotis\OneDrive/Desktop/exer/Aiexercise2/aclImdb/train/" + i
    os.chdir(path)
    count = 0
    for file in os.listdir(): 
        splited_sentence = process_text.split_sentence(file,path)
        if(percentage == True):
            if(count == percentage_of_data):
                break 
        for key in vocabulary:
            process_text.add_key(key,training_vector,splited_sentence)
        process_text.add_target_val(training_vector,i)
        count = count + 1


training_data_frame = pd.DataFrame(training_vector)