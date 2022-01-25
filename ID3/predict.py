from train_id3 import p1,categories
import os,process_text 
import pandas as pd 
import numpy as np
from hyperparameters import per,number_of_vocab_words,approximate_logs_inside_id3,approximate_logs
folders = ['neg','pos']
example_folders = ['train','test']
training_vector = dict()
count_wrong = 0 
for i in folders:
    path = "C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/aclImdb/test/" + i 
    os.chdir(path)
    for file in os.listdir(): 
        splited_sentence = process_text.split_sentence(file,path)
        for key in categories:
            process_text.add_key(key,training_vector,splited_sentence)
        process_text.add_target_val(training_vector,i)



testing_data_frame = pd.DataFrame(training_vector)
print(testing_data_frame)
values_for_each_sentence = np.array(testing_data_frame.drop('positive_or_negative',axis=1)).copy()
values_for_positiveornegative = np.array(testing_data_frame["positive_or_negative"]).copy()
true_positives = 0 
false_positives = 0 
false_negatives = 0 
total_number = len(values_for_each_sentence)
print("Total reviews: " + str(total_number))
for x in range(0,len(values_for_each_sentence)):
    y = values_for_each_sentence[x]
    value = p1.predict(y,p1.categories,p1.node)
    if(values_for_positiveornegative[x] != value):
        count_wrong = count_wrong + 1
    if(values_for_positiveornegative[x] == 1):
        true_positives = true_positives + 1 
    if(values_for_positiveornegative[x] == 0 and value == 1):
        false_positives = false_positives + 1 
    if(values_for_positiveornegative[x] == 1 and value == 0):
        false_negatives = false_negatives + 1 
accuracy = 1 - count_wrong/total_number 
error = count_wrong/total_number
precision = true_positives/(true_positives+false_positives)
recall = true_positives/(true_positives+false_negatives)
f_measure = (2*precision*recall)/(precision + recall)
print("Error: " + str(error))
print("Accuracy: " + str(1 - count_wrong/total_number))
print("Precision: " + str(true_positives/(true_positives+false_positives)))
print("Recall: " + str(true_positives/(true_positives+false_negatives)))
print("F-measure: " + str((2*precision*recall)/(precision + recall)))
