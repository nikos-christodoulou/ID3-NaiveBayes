import InformationGain

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
    def __init__(self,training_vector,countword_negative_reviews,countword_positive_reviews):
        self.node = None 
        self.vector = training_vector
        self.positive_reviews = sum(training_vector[x][len(training_vector[x])-1] for x in range(0,len(training_vector))) # a generator summing all the vectors with 1 at their last position
        self.negative_reviews = sum(1 for x in range (0,len(training_vector)) if training_vector[x][len(training_vector[x])-1] == 0) # a generator summing all the vectors with 0 at their last position
        self.entropy = self.calculate_entropy()

    def calculate_entropy(self):
        #the function definitions are contained in the InformationGain file
        return InformationGain.Entropy(self.positive_reviews,self.negative_reviews)
    def InfoGain(self,specific_word):
        return InformationGain.IG(self.positive_reviews,self.negative_reviews,self.word_positive[specific_word],self.word_negative[specific_word]) 
    def GetMaxInfoGain(self): 
        for x in range(0,len(self.vector)):
            info_gain_for_each_word = [(self.vector[x][y][0],self.InfoGain(self.vector[x][y][0])) for y in range(0,len(self.vector[x])-1)] # the triple [x][y][0] will return the specific word
        max_ig = max(info_gain_for_each_word,key=lambda x:x[1]) # find the max information word in the training vector
        return max_ig
    def ID3_start(self):
        
    def ID3_call(self):

        # if there isn't a starting root node starrt        
        if not self.node: 
            node = Node() 
        
        #if a word belongs to one class (positive or negative) return one category 

        if () :
            node.value = self
            return self.node
        
        #if we can't more feautures return the majority 

        #choose the word that maximizes the root gain 


        # split between vectors that contain word and those who don't 

