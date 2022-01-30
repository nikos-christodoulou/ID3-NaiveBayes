import numpy as np 
import read_files
from hyperparameters import per,approximate_logs,number_of_vocab_words,type_of_test

import word_and_count
'''
Tuple containing the categories and reviews and target values for each file
'''
tup = read_files.read_file(per, number_of_vocab_words, approximate_logs,type_of_test)
both_files = list()
both_files.append(read_files.create_vectors(tup[0]))
both_files.append(read_files.create_vectors(tup[1]))
reviews_for_both = list() 
target_for_both = list()
categories_for_both = list()
for i in range(len(both_files)):
    categories = both_files[i][0]
    dict_values_for_reviews = both_files[i][1]
    target_values = both_files[i][2]
    #we only the train words 
    if(i == 0):
        #first list of x will be for the positive reviews and second list of x will be for the negative reviews for 0,1 values accordingly
        each_word_count = word_and_count.count(dict_values_for_reviews,target_values,categories)
    reviews_for_both.append(dict_values_for_reviews)
    target_for_both.append(target_values)
    categories_for_both.append(categories)