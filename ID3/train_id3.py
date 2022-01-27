

from ID3 import DecisionTree
import numpy as np 
import pandas as pd 
from hyperparameters import per,approximate_logs,number_of_vocab_words,type_of_test
import read_files,os
'''
Returns a tuple which have the reviews the target values and the categories for each data 
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
    reviews_for_both.append(dict_values_for_reviews)
    target_for_both.append(target_values)
    categories_for_both.append(categories)

categories = categories_for_both[0]
values_for_each_sentence = reviews_for_both[0]
values_for_positiveornegative = target_for_both[0]

p1 = DecisionTree(values_for_each_sentence,categories,values_for_positiveornegative)
p1.ID3_start()
if(p1.problem):
    print("problem")
    p1.before_predict(p1.node)
#p1.print_tree(p1.node,p1.COUNT)
