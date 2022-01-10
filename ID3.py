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
        self.childs = list() 




class DecisionTree: 
    '''
    Arguments for initializer: 
    It needs to take the categories,the values for each category and the 
    target values 
    '''
    def __init__(self,values_of_categories,categories,positive_or_negative):
        self.node = None 
        self.category_values = values_of_categories # for each review the words present in that review, this is a two dimensional array where the rows are the values for each category for that specific review  
        self.categories = categories # the names of all the words  , this is a 1 dimension list will all the categories names
        self.value_target = positive_or_negative # whether a review is positive or negative, this is a 1 dimension np array which is the same length as the columns of the category values array
        self.value_target_set = list(set(self.value_target))
        self.entropy = self.calculate_entropy([x for x in range(0,len(self.value_target))])#total entropy 
        self.print_queue = list() 
    def calculate_entropy(self,ids_of_reviews):
        #find the target value for each category contained in the ids of categories  
        values = [self.value_target[i] for i in ids_of_reviews]
        #with the method count,count the times that a target value appears 
        values_count = [values.count(x) for x in self.value_target_set]
        entropy_for_each_category = [- y/len(ids_of_reviews) * log(y/len(ids_of_reviews),2) if y else 0 for y in values_count] 
        entropy = sum(entropy_for_each_category)
        return entropy 
    def InfoGain(self,specific_word,ids_of_reviews):
        # total entropy of dataset 
        #IG = self.calculate_entropy(ids_of_categories)
        IG = self.entropy
        #we want to store the for each category the instances for it  
        # if there was a weather category {bad,medium,well} create a huge list containing all the different values for each case 
        
        x_values = [self.category_values[x][self.categories.index(specific_word)] for x in ids_of_reviews]
        # get unique values if there was a weather category we want to store {bad,medium,well}
        unique_values = list(set(x_values))
        # get frequency of each value and make it a set so we can concatenate with its index position
        x_values_count = list(set([x_values.count(x) for x in x_values]))
        #get the index of the values so we can pass it up in a seperate list for the entropy 
        list_of_positions_for_each_value = [[ids_of_reviews[x] for x in range(0,len(x_values)) if x_values[x] == y] for y in unique_values]
        #number of each category, followed by the list of positions which are the reviews that contain the specific value for that category 
        values_and_categories = [(x_values_count[i],list_of_positions_for_each_value[i]) for i in range(0,len(list_of_positions_for_each_value))]
        
        info_gain_category = sum([x[0]/len(ids_of_reviews) * self.calculate_entropy(x[1]) for x in values_and_categories])
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
        #all the possible values for each category, eg 1(worst): 010010100...,2(best):01010010...
        category_values_ids = [x for x in range(len(self.category_values))]
        #unique number for each category, category 1(worst), category 2(best) , category 3 ...
        category_ids = [x for x in range(len(self.categories))]
        #start node 
        self.node = self.ID3_call(category_values_ids,category_ids,self.node)    
    #we need to have these two methods because each time we want to work with a changed category_values_ids and category_ids 
    #we will call ID3_call recursively 
    def ID3_call(self,category_values_ids,category_ids,node):

        #if there isn't a starting root node start        
        if not self.node: 
            node = Node() 
        #now if we have the same target values for every category 
        targets = [self.value_target[x] for x in category_values_ids]
        #if a word belongs to one class (positive or negative in this case) return the one class 
        if (len(set(targets)) == 1):
            node.value = self.value_target[category_values_ids[0]] # we don't care that this is the first category since all have the same target value 
            return node
        #if we don't have more categories to explore return the majority 
        if len(category_values_ids) == 0 :
            node.value = max(set(targets),key = targets.count)
            return node 
        #choose the word that maximizes the information gain 
        category_name,category_id = self.GetMaxInfoGain(category_values_ids,category_ids)
        
        #make the value of this node equal to the most IG category
        node.value = category_name
        #we need to create as many node as there are possible instances for each category 
        #we find the values for the max IG category so we can split between the values of the category, EG excellent word split between the reviews that have 0 and 1 as the value for the excellent word
        category_vals = set([self.category_values[x][category_id] for x in category_values_ids])
        for x in category_vals:
            child = Node() 
            child.value = x 
            node.childs.append(child)
            #find all the childs that have the specific value for a category. EG excellent 0 and excellent 1 
            values_for_child = [value for value in category_values_ids if self.category_values[value][category_id] == x] 
            if category_ids and category_id in category_ids:#we need to remove the most informational category 
                remove = category_ids.index(category_id)
                category_ids.pop(remove)
                child.next = self.ID3_call(values_for_child,category_ids,child.next)
        return node 
    def print_tree(self): 
        # because we want to print the tree like BFS we will use a queue and not a stack 
        if not self.node:
            print("The tree is empty")
            return 
        self.print_queue.append(self.node)
        while self.print_queue:
            if not self.node.childs: 
                print("No more children are left") 
                self.print_queue.next 
            for x in self.node.childs:
                self.print_queue.append(x)
            print(self.print_queue.pop(0).value)
            