from construct_training_examples import training_data_frame
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

p1 = DecisionTree(training_data_frame,"positive_or_negative",[0,1])
