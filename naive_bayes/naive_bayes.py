from hyperparameters import type_of_test
import predict_bayes 
import numpy as np 
import word_and_count

from create_dictionary import target_for_both,each_word_count,categories_for_both,reviews_for_both

import os 
'''
all of the above imports from create dictionary expect each_word_count have to do with the files that we are reading
'''
if(type_of_test == "test_examples"):
    print("Finding accuracy presicion and recall for a specific percentage of the train set and the whole testing set")
    p1 = predict_bayes.Naive_Bayes(target_for_both[0],each_word_count,categories_for_both[0])
    res = p1.naive_bayes(reviews_for_both[1])
    x = np.array([res,target_for_both[1]]) # first matrix is result and second is target values 
    #first array gets removed from the second array 
    #[0,1,0] = target 
    #[1,0,1] = res 
    x = np.diff(x,axis=0)
    #[-1,1,-1]
    false_positives = np.count_nonzero(x==-1)
    false_negatives = np.count_nonzero(x==1)
    print("The number of false negatives: " + str(false_negatives))
    print("The number of false positives: " + str(false_positives))
    wrong = np.count_nonzero(x == 1) + np.count_nonzero(x == -1)
    pres = np.count_nonzero(target_for_both[1]==1) / (np.count_nonzero(target_for_both[1]==1) + false_positives)
    rec = np.count_nonzero(target_for_both[1]==1)/(np.count_nonzero(target_for_both[1]==1) + false_negatives)
    f_measure = (2*pres*rec)/(pres + rec)
    accuracy = (1 - wrong/target_for_both[1].shape[0]) * 100
    print("Accuracy -> {} %".format(accuracy))
    print("Precision -> {}".format(pres))
    print("Recall -> {}".format(rec))
    print("F measure ->{}".format(f_measure))
elif(type_of_test == "same_percentage"):
    '''
    Percentage for errors on test and train data for the same percentage of data 
    '''
    print("Finding the percentage of error for the same percentage of test and train data")
    train = predict_bayes.Naive_Bayes(target_for_both[0],each_word_count,categories_for_both[0])
    res1 = train.naive_bayes(reviews_for_both[0])
    res2 = train.naive_bayes(reviews_for_both[1])
    x = np.array([res1,target_for_both[0]]) # first matrix is result and second is target values 
    x = np.diff(x,axis=0)
    #first array gets removed from the second array 
    #[0,1,0] = target 
    #[1,0,1] = res 
    #[1,-1,1]
    wrong_train = np.count_nonzero(x == 1) + np.count_nonzero(x == -1)
    error_train = wrong_train/reviews_for_both[0].shape[0]
    x = np.array([res2,target_for_both[1]]) # first matrix is result and second is target values 
    x = np.diff(x,axis=0)
    wrong_test = np.count_nonzero(x == 1) + np.count_nonzero(x == -1)
    error_test = wrong_test/reviews_for_both[1].shape[0]
    print("Error train -> {}".format(error_train))
    print("Error_test ->{}".format(error_test))
else:
    '''
    Accuracy for the training dataset for a specific percentage of training data 
    '''
    print("Finding percentage of errors for the train data on the training data set")
    p1 = predict_bayes.Naive_Bayes(target_for_both[0],each_word_count,categories_for_both[0])
    res = p1.naive_bayes(reviews_for_both[1])
    x = np.array([res,target_for_both[1]]) # first matrix is result and second is target values 
    #first array gets removed from the second array 
    #[0,1,0] = target 
    #[1,0,1] = res 
    x = np.diff(x,axis=0)

    wrong = np.count_nonzero(x == 1) + np.count_nonzero(x == -1)
    accuracy = (1 - wrong/target_for_both[1].shape[0]) * 100
    print("Accuracy -> {} %".format(accuracy))
   