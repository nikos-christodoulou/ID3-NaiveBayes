from operator import index
import read_train_files 
import numpy as np 
cat_and_rev = read_train_files.read_file(0.01,10,True)
t = read_train_files.create_vectors(cat_and_rev)
categories = t[0]
dict_values_for_reviews = t[1]
target_values = t[2]
# we have in 1 review and the review has specific words of the dictionary [0 0 0 0 0 0 0 1 0 0]
# with the given values for each word determine whether the review should be 1 or 0 
#print(categories)
#print(dict_values_for_reviews)
#print(target_values)
count_yes = 0
count_no = 0
each_word_count = {x:[0,0]for x in categories}
for x in range(0,len(dict_values_for_reviews)):
    for y in range(0,len(dict_values_for_reviews[x])):
        print()
