

from ID3 import DecisionTree
import numpy as np 
import pandas as pd 
from hyperparameters import per,approximate_logs,number_of_vocab_words
import read_train_files


cat_and_rev = read_train_files.read_file(per,number_of_vocab_words,approximate_logs)
t = read_train_files.create_vectors(cat_and_rev)
categories = t[0]
values_for_each_sentence = t[1]
values_for_positiveornegative = t[2]

p1 = DecisionTree(values_for_each_sentence,categories,values_for_positiveornegative)
p1.ID3_start()
if(p1.problem):
    p1.before_predict(p1.node)
#p1.print_tree(p1.node,p1.COUNT)
