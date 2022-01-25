from operator import index
import read_train_files,predict_bayes 
import numpy as np 
cat_and_rev = read_train_files.read_file(0.74,100 ,True)
t = read_train_files.create_vectors(cat_and_rev)
categories = t[0]
dict_values_for_reviews = t[1]
print(len(dict_values_for_reviews))
target_values = t[2]
#print(len(target_values)/2)
# we have in 1 review and the review has specific words of the dictionary [0 0 0 0 0 0 0 1 0 0]
# with the given values for each word determine whether the review should be 1 or 0 
#print(categories)
#print(dict_values_for_reviews)
#print(target_values)
count_yes = 0
count_no = 0
#first list of x will be for the positive reviews and second list of x will be for the negative reviews for 0,1 values accordingly
each_word_count = {x:[[0,0],[0,0]] for x in categories}
indices_for_zero = np.array([])
indices_for_one = np.array([])
one_flag = False
zero_flag = False
for x in range(0,len(dict_values_for_reviews)):
    
    if(target_values[x] == 1):
        one_flag = True
        for y in range(0,len(dict_values_for_reviews[x])):
            if(indices_for_zero.any() and indices_for_one.any()):
                break
            if(dict_values_for_reviews[x][y] == 0) and not indices_for_zero.any():
                indices_for_zero = np.where(dict_values_for_reviews[x][y] == dict_values_for_reviews[x])[0]
            elif(dict_values_for_reviews[x][y] == 0) and indices_for_zero.any():
                continue
            else:
                indices_for_one = np.where(dict_values_for_reviews[x][y] == dict_values_for_reviews[x])[0]
                continue
    else:
        zero_flag = True
        for y in range(0,len(dict_values_for_reviews[x])):
            if(indices_for_zero.any() and indices_for_one.any()):
                break
            if(dict_values_for_reviews[x][y] == 0) and not indices_for_zero.any():
                indices_for_zero = np.where(dict_values_for_reviews[x][y] == dict_values_for_reviews[x])[0]
            elif(dict_values_for_reviews[x][y] == 0) and indices_for_zero.any():
                continue
            else:
                indices_for_one = np.where(dict_values_for_reviews[x][y] == dict_values_for_reviews[x])[0]
                continue
    for z in indices_for_zero:
        if(one_flag):
            each_word_count[categories[z]][0][0] = each_word_count[categories[z]][0][0] + 1
        elif(zero_flag):
            each_word_count[categories[z]][1][0] = each_word_count[categories[z]][1][0] + 1
    for z in indices_for_one: 
        if(one_flag):
            each_word_count[categories[z]][0][1] = each_word_count[categories[z]][0][1] + 1
        elif(zero_flag):
            each_word_count[categories[z]][1][1] = each_word_count[categories[z]][1][1] + 1
    one_flag = False
    zero_flag = False
    indices_for_one = np.array([])
    indices_for_zero =  np.array([])
p1 = predict_bayes.Naive_Bayes(target_values,each_word_count,dict_values_for_reviews,categories)
res = p1.naive_bayes(dict_values_for_reviews)
x = np.array([res,target_values])
print(x)
x = np.diff(x,axis=0)
wrong = np.count_nonzero(x == 1) + np.count_nonzero(x == -1)
print(1 - wrong/len(target_values))