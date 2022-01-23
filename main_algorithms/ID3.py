
from math import log
from itertools import combinations 
from collections import Counter
class Node:
    '''
    Contains the data for the specific node 
    This will show the next node 
    This will also contains the children of the node 
    '''
    def __init__(self):
        self.value = None 
        self.next = None # next is for a specific value of a category, the category we check next or whether we have a target value  
        self.childs = list() # the childs are the possible values for each category
        self.isChild = False
        self.parent_value = None 
        self.parent_node = None
        self.created = False

class DecisionTree: 
    '''
    Arguments for initializer: 
    It needs to take the categories,the values for each category and the 
    target values 
    '''
    def __init__(self,values_of_categories,categories,positive_or_negative,approximate = False):
        self.node = None 
        self.category_values = values_of_categories # for each review the words present in that review, this is a two dimensional array where the rows are the values for each category for that specific review  
        self.categories = categories # the names of all the words  , this is a 1 dimension list will all the categories names
        self.value_target = positive_or_negative # whether a review is positive or negative, this is a 1 dimension np array which is the same length as the columns of the category values array
        self.value_target_set = list(set(self.value_target))     
        self.approximate = approximate # use the approximation for the logarithms   
        self.ln = log(2)
        self.recursion_stack = list() 
        self.COUNT = 10
        self.final_tree = list()
        self.problem = False
    def calculate_entropy(self,ids_of_reviews):
        #find the target value for each category contained in the ids of reviews 
        #each time we'll have different reviews, EG when we have the word excellent present 
        #so we can't just use the value_target list   
        values = [self.value_target[i] for i in ids_of_reviews]
        #with the method count,count the times that a target value appears 
        values_count = [values.count(x) for x in self.value_target_set]
        '''
        Logarithmic functions are very costly and difficult to compute. 
        We will use approximation for the log function to speed up the computation process. 
        '''
        if(self.approximate):
            #check if we have 2 categories 
            if(len(values_count) == 2):
                entropy = (((2*values_count[1]*values_count[0])/(len(ids_of_reviews)))/(len(ids_of_reviews)*self.ln)) 
            else:  
                # we need to produce the possible combinations 
                indexes = list() 
                for i in range(1,len(values_count)):
                    indexes.append(i)
                comb = combinations(indexes,2)
                for i in list(comb): 
                    entropy = (((2*values_count[i[1]]*values_count[i[0]])/(len(ids_of_reviews)))/(len(ids_of_reviews)*self.ln)) 
        else:
            entropy_for_each_category = [- y/len(ids_of_reviews) * log(y/len(ids_of_reviews),2) if y else 0 for y in values_count] 
            entropy = sum(entropy_for_each_category)
        if(entropy > 1):
            entropy = 1 
        return entropy 
    def InfoGain(self,specific_word,ids_of_reviews):
        # total entropy of the given reviews 
        IG = self.calculate_entropy(ids_of_reviews) 
        # each time we want to calculate new entropy cause we'll have different 
        # entropies when we are calculating for specific categories 
        
        #we want to store the for each category the instances for it  
        # if there was a weather category {bad,medium,well} create a huge list containing all the different values for each case 
        
        x_values = [self.category_values[x][self.categories.index(specific_word)] for x in ids_of_reviews]
        # get frequency of each value and make it a set so we can concatenate with its index position
        #we can speed up this calculation if the values of the category are of two types EG weather category with {rain,sunny} 
        x_values_count = list()
        
        if len(set(x_values)) == 2:
            x_values_count.append(x_values.count(x_values[0]))
            x_values_count.append(len(ids_of_reviews) - x_values_count[0])
        else:
            for x in set(x_values): 
                x_values_count.append(x_values.count(x))# slow code 
            x_values_count = list(set(x_values_count))
        #get the index of the values so we can pass it up in a seperate list for the entropy 
        list_of_positions_for_each_value = [[ids_of_reviews[x] for x in range(0,len(x_values)) if x_values[x] == y] for y in set(x_values)]
        #number of each category, followed by the list of positions which are the reviews that contain the specific value for that category 
        values_and_categories = [(x_values_count[i],list_of_positions_for_each_value[i]) for i in range(0,len(list_of_positions_for_each_value))]
        info_gain_category = sum([x[0]/len(ids_of_reviews) * self.calculate_entropy(x[1]) for x in values_and_categories]) 
        IG = IG - info_gain_category
        return IG
    def GetMaxInfoGain(self,ids_of_reviews,each_category_id): 
        #min_max sorting algorithm 
        max = 0 #the max info gain right now  
        i = 0  #the index of the max info gain 
        
        for x in each_category_id:
            temp = self.InfoGain(self.categories[x],ids_of_reviews)
            if(temp>max):
                max = temp 
                i = each_category_id.index(x)
        #entropy_category = [self.InfoGain(self.categories[x],ids_of_categories) for x in each_category_id] 
        max_category = each_category_id[i]
        #max_category = each_category_id[entropy_category.index(max(entropy_category))]
        return self.categories[max_category],max_category 
    def ID3_start(self):
        #all the reviews and their respective values for each category 
        review_values_ids = [x for x in range(len(self.category_values))]
        #unique number for each category, category 1(worst), category 2(best) , category 3 ...
        category_ids = [x for x in range(len(self.categories))]
        #start node 
        self.ID3_call(review_values_ids,category_ids,Node())    
    #we need to have these two methods because each time we want to work with a changed category_values_ids and category_ids 
    #we will call ID3_call recursively 
    def ID3_call(self,review_values_ids,category_ids,node):
        child = None 
        self.recursion_stack.append((review_values_ids,category_ids,node))
        root = self.recursion_stack[0][2]
        while len(self.recursion_stack):
            
            t = self.recursion_stack.pop()
            review_values_ids = t[0]
            category_ids = t[1]
            node = t[2]
                   
            if not node: 
                node = Node() 
            #now if we have the same target values for every category 
            targets = [self.value_target[x] for x in review_values_ids]
            #if a word belongs to one class (positive or negative in this case) return the one class 
        
                    
            if(len(set(targets)) == 1):
                node.value = self.value_target[review_values_ids[0]] 
            #if we don't have more reviews to explore return the majority  or we don't have more categories to explore 
            elif len(category_ids) == 0:
                node.value = max(set(targets),key = targets.count)
            #choose the word that maximizes the information gain 
            else:
                category_name,category_id = self.GetMaxInfoGain(review_values_ids,category_ids)
            
                #make the value of this node equal to the most IG category
               
                node.value = category_name
                #we need to create as many node as there are possible instances for each category 
                #we find the values for the max IG category so we can split between the values of the category, EG excellent word split between the reviews that have 0 and 1 as the value for the excellent word
                category_vals = set([self.category_values[x][category_id] for x in review_values_ids])
                if(len(category_vals) == 1):
                    self.problem = True
                for x in category_vals:
                    #create the childs with the category vals 
                    child = Node() 
                    child.value = x 
                    child.isChild = True 
                    node.childs.append(child)
                    #find all the childs that have the specific value for a category. EG excellent 0 and excellent 1 
                    values_for_child = [value for value in review_values_ids if self.category_values[value][category_id] == x] 
                    if not values_for_child:#if there aren't any more reviews to explore return the majority 
                        node.value = max(set(targets),key = targets.count)
                    else: 
                        if category_ids and category_id in category_ids:#we need to remove the most informational category 
                            remove = category_ids.index(category_id)
                            category_ids.pop(remove)
                        child.next = Node()
                        child.next.parent_node = node
                        child.next.parent_value = child.value
                        self.recursion_stack.append((values_for_child,list(category_ids),child.next))
                
        self.node = root     
    
    def before_predict(self,node):
        '''
        if category_vals only have one value then the algorithm won't be able to answer for some reviews 
        this can happen in the case where in the training data [1,1,0,1] there aren't any vectors of the form [1,1,1,1] but the test data has vectors like this
        we will add a child node artificially by predicting the value that the node would have if it had the child value 
        '''
        stack = list()
        temp_node = node 
        stack.append(temp_node)
        while not (len(stack) == 0): 
            temp_node = stack.pop()
            if(len(temp_node.childs) == 1):
                x = temp_node.childs[0]
                if(x.isChild):
                    if(x.value == 0):
                        child = Node()
                        child.value = 1 
                        child.isChild = True
                        temp_node.childs.append(child)
                        child.next = Node() 
                        child.next.parent_node = node
                        child.next.parent_value = child.value
                        child.next.created = True
                        child.next.value = self.prediction_for_one_child_categories(child.next.parent_node)
                    else:
                        child = Node()
                        child.value = 0 
                        child.isChild = True
                        temp_node.childs.insert(0,child)
                        child.next = Node() 
                        child.next.created = True
                        child.next.parent_node = node
                        child.next.parent_value = child.value
                        child.next.value = self.prediction_for_one_child_categories(child.next.parent_node)
            for x in temp_node.childs:
                stack.append(x.next)
        self.node = node
    def prediction_for_one_child_categories(self,parent_node):
        '''
        Search all of the children of the parent node and return the majority value 
        '''
        value_list = list() 
        stack = list() 
        stack.append(parent_node)
        while not (len(stack) == 0):
            temp_node = stack.pop()
            if (len(temp_node.childs) == 0) and temp_node.value != None:
                value_list.append(temp_node.value)
            else:
                for x in temp_node.childs:
                    stack.append(x.next)
        c = Counter(value_list)    
        value,count = c.most_common()[0]
        return value
    def predict(self,review_and_words_present,categories,node):
        '''
        review_and_words_present should be a numpy vector or a plain list that has the words of the dictionary that are present
        in the review.
        categories has the possible categories taken from the class itself 
        '''
        
        while not (len(node.childs) == 0):
            index = categories.index(node.value)
            flag = False
            if(len(node.childs) == 2):
                for x in node.childs:
                    if(x.value == review_and_words_present[index]):
                        node = x.next 
                        break
        prediction = node.value
        return prediction 
    
    
    def print_tree(self,node,space): 
        # because we want to print the tree like BFS we will use a queue and not a stack 
       
        
        if(node == None):
            return 
        space += self.COUNT
        if(node.isChild): 
            node = node.next 
        if (not (node.isChild)) and ((node.childs)):
            if(node.childs[0]):
                self.print_tree(node.childs[0],space)
        #print()
        for i in range(self.COUNT,space):
           print(end = " ")
        
        
        print(str(node.parent_value) + " " + str(node.value))
        
        if(node.isChild):
            node = node.next
        if (not (node.isChild)) and ((node.childs)):
            if(len(node.childs) == 2):
                self.print_tree(node.childs[1],space)
            else:
                self.print_tree(node.childs[0],space)
            
            