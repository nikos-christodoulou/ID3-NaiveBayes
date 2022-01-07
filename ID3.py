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
        #find the target value for each category contained in the ids of categories  
        values = [self.value_target[i] for i in ids_of_categories]
        #with the method count,count the times that a target value appears 
        values_count = [values.count(x) for x in self.value_target_set]
        entropy_for_each_category = [- y/len(ids_of_categories) * log(y/len(ids_of_categories),2) if y else 0 for y in values_count] 
        entropy = sum(entropy_for_each_category)
        return entropy 
    def InfoGain(self,specific_word,ids_of_categories):
        # total entropy of dataset 
        #IG = self.calculate_entropy(ids_of_categories)
        IG = self.entropy
        #we want to store the for each category the instances for it  
        # if there was a weather category {bad,medium,well} create a huge list containing all the different values for each case 
        
        x_values = [self.category_values[x][self.categories.index(specific_word)] for x in ids_of_categories]
        # get unique values if there was a weather category we want to store {bad,medium,well}
        unique_values = list(set(x_values))
        # get frequency of each value and make it a set so we can concatenate with its index position
        x_values_count = list(set([x_values.count(x) for x in x_values]))
        #get the index of the values so we can pass it up in a seperate list for the entropy 
        list_of_positions_for_each_value = [[ids_of_categories[x] for x in range(0,len(x_values)) if x_values[x] == y] for y in unique_values]
        #number of each category, followed by the list of positions
        values_and_categories = [(x_values_count[i],list_of_positions_for_each_value[i]) for i in range(0,len(list_of_positions_for_each_value))]
        
        info_gain_category = sum([x[0]/len(ids_of_categories) * self.calculate_entropy(x[1]) for x in values_and_categories])
        IG = IG - info_gain_category
        return IG
    def GetMaxInfoGain(self,ids_of_categories,each_category_id): 
        #min_max sorting algorithm 
        max = 0 #the max info gain right now  
        i = 0  #the index of the max info gain 
        for x in each_category_id:
            temp = self.InfoGain(self.categories[x],ids_of_categories)
            if(temp>max):
                max = temp 
                i = x
        #we can try the below and not create the list again 
        #entropy_category = [self.InfoGain(self.categories[x],ids_of_categories) for x in each_category_id] 
        max_category = each_category_id[i]
        #max_category = each_category_id[entropy_category.index(max(entropy_category))]
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
        if (len(set(targets)) == 1):
            node.value = self.value_target[category_values_ids[0]]
            return node
        #if we don't have more features return the majority 
        if len(category_values_ids) == 0 :
            node.value = max(set(targets),key = targets.count)
            return node 

        category_name,category_id = self.GetMaxInfoGain(category_values_ids,category_ids)
        #choose the word that maximizes the root gain 
        
        #make the value of this node equeal to the most IG category
        node.value = category_name
        #
        #we need to create as many node as there are possible instances for each category 
        #split between nodes that contain category and those who don't 
            
