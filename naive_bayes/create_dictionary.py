import numpy as np 
import read_files
from hyperparameters import per,approximate_logs,number_of_vocab_words,test_train
import word_and_count
if(test_train == "test"):
    cat_and_rev = read_files.read_file(per, number_of_vocab_words, approximate_logs,test_train)
else: 
    tup = read_files.read_file(per, number_of_vocab_words, approximate_logs,test_train)

if(test_train == "test"):
    t = read_files.create_vectors(cat_and_rev)
    categories = t[0]
    dict_values_for_reviews = t[1]
    target_values = t[2]
    #first list of x will be for the positive reviews and second list of x will be for the negative reviews for 0,1 values accordingly
    each_word_count = {x:[[0,0],[0,0]] for x in categories}
    each_word_count = word_and_count.count(dict_values_for_reviews,target_values,each_word_count,categories)
else:
    t1 = list()
    t1.append(read_files.create_vectors(tup[0]))
    t1.append(read_files.create_vectors(tup[1]))
    dictionaries = list()
    reviews_for_both = list() 
    target_for_both = list()
    categories_for_both = list()
    for u in t1:
        categories = u[0]
        dict_values_for_reviews = u[1]
        target_values = u[2]
        #first list of x will be for the positive reviews and second list of x will be for the negative reviews for 0,1 values accordingly
        each_word_count = {x:[[0,0],[0,0]] for x in categories}
        each_word_count = word_and_count.count(dict_values_for_reviews,target_values,each_word_count,categories)
        dictionaries.append(each_word_count)
        reviews_for_both.append(dict_values_for_reviews)
        target_for_both.append(target_values)
        categories_for_both.append(categories)