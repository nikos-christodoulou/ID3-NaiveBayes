from preprocessing.construct_training_examples import training_data_frame,vocabulary
from main_algorithms.ID3 import DecisionTree
import numpy as np 
import pandas as pd 
import os,preprocessing.process_text as process_text

# we use np array for handling two dimensional arrays better
values_for_each_sentence = np.array(training_data_frame.drop('positive_or_negative',axis=1)).copy()
values_for_positiveornegative = np.array(training_data_frame["positive_or_negative"]).copy()
x_dim = training_data_frame.shape[1] - 1
categories = list(training_data_frame.keys())[:x_dim]

p1 = DecisionTree(values_for_each_sentence,categories,values_for_positiveornegative)
p1.ID3_start()
if(p1.problem):
    p1.before_predict(p1.node)
#p1.print_tree(p1.node,p1.COUNT)
