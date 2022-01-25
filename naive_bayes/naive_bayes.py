from hyperparameters import test_train
import predict_bayes 
import numpy as np 
if(test_train == "test"):
    from create_dictionary import target_values,each_word_count,categories,dict_values_for_reviews
else:
    from create_dictionary import target_for_both,dictionaries,categories_for_both,reviews_for_both
import os 
#Testing...
if(test_train == "test"):
    p1 = predict_bayes.Naive_Bayes(target_values,each_word_count,categories)
    res = p1.naive_bayes(dict_values_for_reviews)
    x = np.array([res,target_values]) # first matrix is result and second is target values 
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
    accuracy = (1 - wrong/len(target_values)) * 100
    #both test data and training data 
    print("Accuracy -> {} %".format((1 - wrong/len(target_values)) * 100))
    #for the test data 
    print("Precision -> {}".format(pres))
    print("Recall -> {}".format(rec))
    print("F measure ->{}".format(f_measure))
else:
    train = predict_bayes.Naive_Bayes(target_for_both[0],dictionaries[0],categories_for_both[0])
    test = predict_bayes.Naive_Bayes(target_for_both[1],dictionaries[1],categories_for_both[1])

    res1 = train.naive_bayes(reviews_for_both[0])
    res2 = test.naive_bayes(reviews_for_both[1])
    x = np.array([res1,target_for_both[0]]) # first matrix is result and second is target values 
    x = np.diff(x,axis=0)
    wrong_train = np.count_nonzero(x == 1) + np.count_nonzero(x == -1)
    error_train = wrong_train/len(reviews_for_both[0])
    x = np.array([res2,target_for_both[1]]) # first matrix is result and second is target values 
    x = np.diff(x,axis=0)
    wrong_test = np.count_nonzero(x == 1) + np.count_nonzero(x == -1)
    error_test = wrong_test/len(reviews_for_both[1])