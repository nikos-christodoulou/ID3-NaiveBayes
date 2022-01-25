from operator import index
import predict_bayes 
import numpy as np 
from count_words_pos_neg import target_values,each_word_count,categories,dict_values_for_reviews
import os 
#Testing...

p1 = predict_bayes.Naive_Bayes(target_values,each_word_count,categories)
res = p1.naive_bayes(dict_values_for_reviews)
x = np.array([[1,0,0,1,1,0,1],[0,1,1,0,1,0,1]]) # first matrix is result and second is target values 
x = np.diff(x,axis=0)
print(x)
false_positives = np.count_nonzero(x==-1)
false_negatives = np.count_nonzero(x==1)
print("The number of false negatives: " + str(false_negatives))
print("The number of false positives: " + str(false_positives))
wrong = np.count_nonzero(x == 1) + np.count_nonzero(x == -1)
pres = np.count_nonzero(target_values==1) / (np.count_nonzero(target_values==1) + false_positives)
rec = np.count_nonzero(target_values==1)/(np.count_nonzero(target_values==1) + false_negatives)
f_measure = (2*pres*rec)/(pres + rec)
#read train data 

#both test data and training data 
print("Accuracy -> {} %".format((1 - wrong/len(target_values)) * 100))
#for the test data 
print("Precision -> {} %".format(pres))
print("Recall -> {} %".format(rec))
print("F measure ->{}%".format(f_measure))