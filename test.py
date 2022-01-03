from InformationGain import IG
from filter_the_vocabulary import positive_word_in_reviews,negative_word_in_reviews
from construct_training_examples import training_vector
from ID3 import DecisionTree
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

p1 = DecisionTree(training_vector,negative_word_in_reviews,positive_word_in_reviews)
print(p1.GetMaxInfoGain())
