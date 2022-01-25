from construct_test_examples import training_data_frame
import numpy as np 
import os 

from hyperparameters import per,number_of_vocab_words,approximate_logs
# we use np array for handling two dimensional arrays better
values_for_each_sentence = np.array(training_data_frame.drop('positive_or_negative',axis=1)).copy()
values_for_positiveornegative = np.array(training_data_frame["positive_or_negative"]).copy()
x_dim = training_data_frame.shape[1] - 1
categories = list(training_data_frame.keys())[:x_dim]
categories.append("positive_or_negative")
'''
write training vectors in text files 
along with categories 
'''
per = per * 100 
file_name = "" + str(round(per)) + "_" + str(number_of_vocab_words) + "_" + str(approximate_logs) + ".txt"
"""
file_path = os.path.join("C:/Users/Nikos/Documents/GitHub/Aiexercise2/per_keys/",file_name)
if not os.path.exists("C:/Users/Nikos/Documents/GitHub/Aiexercise2/per_keys/"):
    os.makedirs("C:/Users/Nikos/Documents/GitHub/Aiexercise2/per_keys/")
"""
file_path = os.path.join("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/per_keys/",file_name)
if not os.path.exists("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/per_keys/"):
    os.makedirs("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/per_keys/")

f = open(file_path,"a")
for x in categories: 
    f.write(x + " ")

f.write("\n")
for x in range(0,len(values_for_each_sentence)):
    y = np.array2string(values_for_each_sentence[x],separator=' ',suppress_small=True)
    y = y.translate({ord(c): None for c in '[]\n'})
    f.write(y + " " + str(values_for_positiveornegative[x]) + "\n")
    
f.close()