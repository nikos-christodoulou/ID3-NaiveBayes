from construct_test_and_training_examples import training_data_frame,testing_data_frame
import numpy as np 
import os 
from hyperparameters import per,number_of_vocab_words,approximate_logs
# we use np array for handling two dimensional arrays better
values_for_each_sentence_train = np.array(training_data_frame.drop('positive_or_negative',axis=1)).copy()
values_for_positiveornegative_train = np.array(training_data_frame["positive_or_negative"]).copy()
x_dim = training_data_frame.shape[1] - 1
categories_train = list(training_data_frame.keys())[:x_dim]
categories_train.append("positive_or_negative")
values_for_each_sentence_test = np.array(training_data_frame.drop('positive_or_negative',axis=1)).copy()
values_for_positiveornegative_test = np.array(training_data_frame["positive_or_negative"]).copy()
x_dim = training_data_frame.shape[1] - 1
categories_test = list(training_data_frame.keys())[:x_dim]
categories_test.append("positive_or_negative")
'''
write training vectors in text files 
along with categories 
'''
per = per * 100 
file_name1 = str(round(per)) + "_" + str(number_of_vocab_words) + "_" + str(approximate_logs) + ".txt"

file_path = os.path.join("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/test/",file_name1)
if not os.path.exists("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/test/"):
    os.makedirs("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/test/")

with open(file_name1,"a") as f1:
    for x in categories_train: 
        f1.write(x + " ")
    f1.write("/n")
    for x in range(0,len(values_for_each_sentence_train)):
        y = np.array2string(values_for_each_sentence_train[x],separator=' ',suppress_small=True)
        y = y.translate({ord(c): None for c in '[]\n'})
        f1.write(y + " " + str(values_for_positiveornegative_train[x]) + "\n")

file_name2 = str(round(per)) + "_" + str(number_of_vocab_words) + "_" + str(approximate_logs) + ".txt"

file_path = os.path.join("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/test1/",file_name2)
if not os.path.exists("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/test1/"):
    os.makedirs("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/test1/")

with open(file_name2,"a") as f2:
    for x in categories_test: 
        f2.write(x + " ")
    f2.write("/n")
    for x in range(0,len(values_for_each_sentence_test)):
        y = np.array2string(values_for_each_sentence_test[x],separator=' ',suppress_small=True)
        y = y.translate({ord(c): None for c in '[]\n'})
        f2.write(y + " " + str(values_for_each_sentence_test[x]) + "\n")