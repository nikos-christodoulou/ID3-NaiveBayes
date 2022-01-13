from numpy.core.fromnumeric import shape
from construct_training_examples import training_data_frame
from ID3 import DecisionTree
import time

import numpy as np 
# we use np array for handling two dimensional arrays better
values_for_each_sentence = np.array(training_data_frame.drop('positive_or_negative',axis=1)).copy()
values_for_positiveornegative = np.array(training_data_frame["positive_or_negative"]).copy()
x_dim = training_data_frame.shape[1] - 1
categories = list(training_data_frame.keys())[:x_dim]

print(categories)
print(values_for_positiveornegative)
print(values_for_each_sentence)

p1 = DecisionTree(values_for_each_sentence,categories,values_for_positiveornegative)
p1.ID3_start()
p1.print_tree(p1.node,p1.COUNT)
#prediction = p1.predict(np.array([0,0,0,1,1]),p1.categories,p1.node)
#print(prediction)