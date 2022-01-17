from filter_the_vocabulary import vocabulary
import os,random,process_text,math
import pandas as pd 
folders = ['neg','pos']
training_vector = dict()
'''
We will create a binary vector with 1 if the word in the dictionary is present in the sentence 
else the value will be 0 if it's not contained in the word 
this will be a pandas dataframe 
''' 
percentage_of_data = math.ceil(12500) 
per = True 
training_data_frame = pd.DataFrame()

for i in folders:
    path = "C:/Users/fotis/OneDrive/Desktop/Aiexercise2/aclImdb/train/" + i 
    os.chdir(path)
    if(per):
        for y in range(0,percentage_of_data):
            file = random.choice(os.listdir())
            splited_sentence = process_text.split_sentence(file,path)
            for key in vocabulary:
                process_text.add_key(key,training_vector,splited_sentence)
            process_text.add_target_val(training_vector,i)
    else:
        for file in os.listdir(): 
            splited_sentence = process_text.split_sentence(file,path)
            for key in vocabulary:
                process_text.add_key(key,training_vector,splited_sentence)
            process_text.add_target_val(training_vector,i)
        

training_data_frame = pd.DataFrame(training_vector)
print(training_data_frame)
 
        