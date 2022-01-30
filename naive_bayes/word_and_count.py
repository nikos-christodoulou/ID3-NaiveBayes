import numpy as np 
def count(dict_values_for_reviews,target_values,categories):
    one_flag = False
    zero_flag = False
    indices_for_zero = np.array([])
    indices_for_one = np.array([])
    each_word_count = {x:[[0,0],[0,0]] for x in categories}
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
    return each_word_count