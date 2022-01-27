from asyncore import read
from cgi import test
from train_id3 import p1,categories,categories_for_both,reviews_for_both,target_for_both
import os
import pandas as pd 
import numpy as np
from hyperparameters import type_of_test,number_of_vocab_words,approximate_logs,per


predict_data_cat = categories_for_both[1]
predict_data_reviews = reviews_for_both[1]
predict_data_target_values = target_for_both[1]
total_number = predict_data_reviews.shape[0]
print("Total reviews: " + str(total_number))
count_wrong_predict = 0
count_wrong = 0
if(type_of_test == "test_examples"):
    print("Finding accuracy presicion and recall for a specific percentage of the train set and the whole testing set")
    true_positives = 0 
    false_positives = 0 
    false_negatives = 0 
    for x in range(0,len(predict_data_reviews)):
        y = predict_data_reviews[x]
        value = p1.predict(y,p1.categories,p1.node)
        if(predict_data_target_values[x] != value):
            count_wrong = count_wrong + 1
        if(predict_data_target_values[x] == 1):
            true_positives = true_positives + 1 
        if(predict_data_target_values[x] == 0 and value == 1):
            false_positives = false_positives + 1 
        if(predict_data_target_values[x] == 1 and value == 0):
            false_negatives = false_negatives + 1 
    accuracy = 1 - count_wrong/total_number 
    error = count_wrong/total_number
    pres = true_positives/(true_positives+false_positives)
    rec = true_positives/(true_positives+false_negatives)
    f_measure = (2*pres*rec)/(pres + rec)
    print("Error: " + str(error))
    print("Accuracy: " + str(accuracy))
    print("Precision: " + str(pres))
    print("Recall: " + str(rec))
    print("F-measure: " + str(f_measure))
elif(type_of_test == "train_data"):
    print("Finding percentage of errors for the train data on the training data set")
    for x in range(0,len(predict_data_reviews)):
        y = predict_data_reviews[x]
        value = p1.predict(y,p1.categories,p1.node)
        if(predict_data_target_values[x] != value):
            count_wrong = count_wrong + 1
    accuracy = 1 - count_wrong/total_number
    print("Accuracy: " + str(accuracy))
else:
    print("Finding the percentage of error for the same percentage of test and train data")
    for x in range(0,len(predict_data_reviews)):
        y1 = predict_data_reviews[x]
        y2 = reviews_for_both[0][x]
        value1 = p1.predict(y1,p1.categories,p1.node)
        value2 = p1.predict(y2,p1.categories,p1.node)
        if(predict_data_target_values[x] != value1):
            count_wrong_predict = count_wrong_predict + 1
        if(target_for_both[0][x] != value2):
            count_wrong = count_wrong + 1 
    error_train = count_wrong/reviews_for_both[0].shape[0]
    error_test = count_wrong_predict/reviews_for_both[1].shape[0]
    print("Error train -> {}".format(error_train))
    print("Error_test ->{}".format(error_test))