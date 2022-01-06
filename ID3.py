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




class DecisionTree: 
    '''
    Arguments for initializer: 
    It needs to take the categories,the values for each category and the 
    target values 
    '''
    def __init__(self,values_of_categories,categories,positive_or_negative):
        self.node = None 
        self.category_values = values_of_categories # for each review the words present in that review 
        self.categories = categories # the names of all the words 
        self.value_target = positive_or_negative # whether a review is positive or negative 
        self.value_target_set = list(set(self.value_target))

        self.entropy = self.calculate_entropy([x for x in range(0,len(self.value_target))])

    def calculate_entropy(self,ids_of_categories):
        # the target value for each review  
        values = [self.value_target[i] for i in ids_of_categories]
        values_count = [values.count(x) for x in self.value_target_set]
        entropy_for_each_category = [- y/len(ids_of_categories) * log(y/len(ids_of_categories),2) if y else 0 for y in values_count] 
        entropy = sum(entropy_for_each_category)
        return entropy 
    def InfoGain(self,specific_word,ids_of_categories):
        # total entropy of dataset 
        total_entropy = self.calculate_entropy(ids_of_categories)
        #we want to store the for each category the feautures  
        
        x_targets = [self.category_values[x][self.categories.index(specific_word)] for x in ids_of_categories]
        # get unique values 
        unique_targets = list(set(x_targets))
        # get frequency of each value 
        x_targets_count = list(set([x_targets.count(x) for x in x_targets]))
        
        id_of_category = [[ids_of_categories[i] for i, x in enumerate(x_targets) if x == y]for y in unique_targets]

        info_gain_feature = sum([v_counts/len(ids_of_categories) * self.entropy(v_ids) for v_counts,v_ids in zip(x_targets_count,id_of_category)])
        IG = total_entropy - info_gain_feature
        return IG

    def GetMaxInfoGain(self,ids_of_categories,each_category_id): 
        entropy_category = [self.InfoGain(x,ids_of_categories) for x in each_category_id] 
        max_category = each_category_id[entropy_category.index(max(entropy_category))]
        return self.categories[max_category],max_category 
    def ID3_start(self):
        category_values_ids = [x for x in range(len(self.category_values))]
        #unique number for each category 
        category_ids = [x for x in range(len(self.categories))]
        #start node 
        self.node = self.ID3_call(category_values_ids,category_ids,self.node)    
    def ID3_call(self,category_values_ids,category_ids,node):

        #if there isn't a starting root node start        
        if not self.node: 
            node = Node() 
        #now if we have the same target values for every category 
        targets = [self.value_target[x] for x in category_values_ids]
        #if a word belongs to one class (positive or negative) return one category 
        if (len(set(targets)) == 2):
            node.value = self.value_target[category_values_ids[0]]
            return node
        #if we don't have more features return the majority 
        if len(category_values_ids) == 0 :
            node.value = max(set(targets),key = targets.count)
            return node 

        self.GetMaxInfoGain(category_ids,category_values_ids)
        #choose the word that maximizes the root gain 


        # split between vectors that contain word and those who don't 
        #'''
