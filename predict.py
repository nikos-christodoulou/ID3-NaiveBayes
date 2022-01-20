from train import p1 
import os,process_text
import pandas as pd 
import numpy as np
from filter_the_vocabulary import vocabulary
folders = ['neg','pos']
training_vector = dict()
count_wrong = 0 
for i in folders:
    path = "C:/Users/fotis/OneDrive/Desktop/Aiexercise2/aclImdb/test/" + i 
    os.chdir(path)
    for file in os.listdir(): 
        splited_sentence = process_text.split_sentence(file,path)
        for key in vocabulary:
            process_text.add_key(key,training_vector,splited_sentence)
        process_text.add_target_val(training_vector,i)



testing_data_frame = pd.DataFrame(training_vector)
print(testing_data_frame)
values_for_each_sentence = np.array(testing_data_frame.drop('positive_or_negative',axis=1)).copy()
values_for_positiveornegative = np.array(testing_data_frame["positive_or_negative"]).copy()

for x in range(0,len(values_for_each_sentence)):
    y = values_for_each_sentence[x]
    value = p1.predict(y,p1.categories,p1.node)
    if(values_for_positiveornegative[x] != value):
        count_wrong = count_wrong + 1
print(count_wrong)
print(p1.temp_count)