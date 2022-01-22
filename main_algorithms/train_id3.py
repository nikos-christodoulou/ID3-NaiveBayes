

from ID3 import DecisionTree
import numpy as np 
import pandas as pd 
from hyperparameters import per,approximate_logs,number_of_vocab_words


name =  "per_keys/" + str(int(per*100)) + "_" + str(number_of_vocab_words) + "_" + str(True) + ".txt"
file = open(name,'r')
cat_and_rev = file.readlines()
categories = cat_and_rev[0].split()
categories = categories[:-1]
values_for_each_sentence = list()
values_for_positiveornegative = list() 
for x in range(1,len(cat_and_rev)):
    values_for_positiveornegative.append(cat_and_rev[x][len(cat_and_rev[x]) - 2])
    values_for_each_sentence.append(cat_and_rev[x][:-2].split())

for x in values_for_each_sentence:
    for y in range(len(x)):
        x[y] = int(x[y])
    
values_for_each_sentence = np.array((values_for_each_sentence))


for x in range(len(values_for_positiveornegative)):
    values_for_positiveornegative[x] = int(values_for_positiveornegative[x])

values_for_positiveornegative = np.array((values_for_positiveornegative))

file.close()

p1 = DecisionTree(values_for_each_sentence,categories,values_for_positiveornegative)
p1.ID3_start()
if(p1.problem):
    p1.before_predict(p1.node)
p1.print_tree(p1.node,p1.COUNT)
