from numpy import positive
from filter_the_vocabulary import vocabulary

import os 
import pandas as pd 
folders = ['neg','pos']
training_vector = dict()
'''
We will create a binary vector with 1 if the word in the dictionary is present in the sentence 
else the value will be 0 if it's not contained in the word 
this will be a pandas dataframe 
''' 
training_data_frame = pd.DataFrame()
for i in folders:
    path = "C:/Users/fotis/OneDrive/Desktop/Aiexercise2/aclImdb/train/" + i 
    os.chdir(path)
    for file in os.listdir(): 
        # check the text format 
        if file.endswith(".txt"):
            file_path = f"{path}/{file}"
        f = open(file_path,'r',encoding="latin-1")
        sentence = f.read()
        #removing special characters so the vocabulary can represent tha data set better 
        sentence = sentence.translate({ord(c): None for c in '().!@#$***'})
        sentence = sentence.lower()
        sentence = sentence.replace("<br />"," ")
        splited_sentence = sentence.split() 
        for key in vocabulary:
            if(not(key in training_vector)):
                training_vector[key] = list()
            if(key in splited_sentence):
                training_vector[key].append(1)
            else:
                training_vector[key].append(0)
        if(not("positive_or_negative" in training_vector)):
                training_vector["positive_or_negative"] = list()
        if(i == "neg"):
            training_vector["positive_or_negative"].append(0)
        else:
            training_vector["positive_or_negative"].append(1)
        f.close()

training_data_frame = pd.DataFrame(training_vector)
print(training_data_frame)
 
        