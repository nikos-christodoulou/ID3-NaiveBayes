import InformationGain
from math import log
class Node:
    '''
    Contains the data for the specific node 
    This will show the next node 
    This will also contains the children of the node 
    '''
    def __init__(self):
        self.value = None 
        self.next = None 
        self.childs = None 


'''
in our case it would be something like 
Algo_start = ID3(0_1vector,positive_or_negative,[0,1])
'''

class DecisionTree: 
    '''
    Arguments for initializer: 
    It needs to take the categories, the classes for each category
    In our case the categories are the words, and the classes for each category is 0,1
    '''
    def __init__(self,training_data,target,classes):
        self.node = None 
        self.vector = training_data
        self.total_number = training_data.shape[0]
        self.categories = training_data.columns # all the possible categories of the dataset
        self.classes_list = [None]*len(classes)
        self.entropy_for_each_category = None 
        for x in classes:
            self.classes_list[x] = training_data[training_data[target] == x].shape[0] 
        self.entropy = self.calculate_entropy([x for x in range(0,len(self.categories))])

    def calculate_entropy(self,ids_of_categories):
        labels = [self.categories[x] for x in ids_of_categories]
        count_categories = [labels.count(x) for x in self.categories]
        self.entropy_for_each_category = [-y/self.total_number*log(y/self.total_number,2)for y in count_categories]
        entropy = sum(self.entropy_for_each_category)
        return entropy 
    def InfoGain(self,specific_word):
        return InformationGain.IG(self.positive_reviews,self.negative_reviews,self.word_positive[specific_word],self.word_negative[specific_word]) 
    def GetMaxInfoGain(self): 
        for x in range(0,len(self.vector)):
            info_gain_for_each_word = [(self.vector[x][y][0],self.InfoGain(self.vector[x][y][0])) for y in range(0,len(self.vector[x])-1)] # the triple [x][y][0] will return the specific word
        max_ig = max(info_gain_for_each_word,key=lambda x:x[1]) # find the max information word in the training vector
        return max_ig
    def ID3_start(self):
        
    
    #def ID3_call(self):

        # if there isn't a starting root node start        
     #   if not self.node: 
            node = Node() 
        
        #if a word belongs to one class (positive or negative) return one category 

      #  if () :
        #    node.value = self
       #     return self.node
        
        #if we can't more feautures return the majority 

        #choose the word that maximizes the root gain 


        # split between vectors that contain word and those who don't 
        #'''
