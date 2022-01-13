from numpy.core.fromnumeric import shape
from construct_training_examples import training_data_frame
from ID3 import DecisionTree
import time

import numpy as np 
'''
my_list = ([("the",0),("gay",1),("0",0),("a",1),("l",0),1],[("the",0),("gay",1),("0",0),("a",1),("l",0),0])
this = list()


for x in range(0,len(my_list)):
    info_gain = [my_list[x][y][0] for y in range(0,len(my_list[x])-1)]
print(info_gain)
#print(sum(my_list[x][len(my_list[x])-1] for x in range(0,len(my_list))))
#print(sum(1 for x in range (0,len(my_list)) if my_list[x][len(my_list[x])-1] == 0))
#my_list[x][len(my_list[x])-1
''' 
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
