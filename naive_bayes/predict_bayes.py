
from re import I
import numpy as np


class Naive_Bayes:

    def __init__(self,target_values,each_word_count,dict_values_for_reviews,categories):
        self.instance_method()
        self.target_values = target_values
        self.each_word_count = each_word_count
        self.dict_values_for_reviews = dict_values_for_reviews
        self.categories = categories

    def instance_method(self):
        print ('success!')
        



    """"
    laplace smoothing is used to handle 
    zero probability error. We use the alpha (!=0) as 
    the smoothing parameter.

    """    
    
    def laplace_smoothing(self, data ,alpha = 1.0):
        #data[1] contains the binary values of each category for each review
        index_neg = list()
        index_pos = list() 
        prob_smooth_pos = list()
        prob_smooth_neg = list()
        print(self.target_values)
        target_set = set(self.target_values)
        for x in target_set:
            if( len(index_neg) != 0) and (len(index_pos) != 0 ):
                break
            if(x==0):
                for y in range(len(self.dict_values_for_reviews)):
                    if(self.target_values[y] == x):
                        index_neg.append(y)
            else:
                for y in range(len(self.dict_values_for_reviews)):
                    if(self.target_values[y] == x):
                        index_pos.append(y)  
        tar = list(self.target_values)
        num_of_features = [tar.count(x) for x in set(tar)]
        for x in index_neg:
            y = self.dict_values_for_reviews[x].astype(float, order='K', casting='unsafe', subok=True, copy=True)
            prob_smooth_neg.append(y)
        for x in index_pos:
            y = self.dict_values_for_reviews[x].astype(float, order='K', casting='unsafe', subok=True, copy=True)
            prob_smooth_pos.append(y)
        print("num of features is: ", num_of_features)
        for review in range (len(self.target_values)):
            for x in range(len(self.categories)):
                if self.target_values[review] == 1:
                    if(prob_smooth_neg[review][x] == 0):
                        prob_smooth_pos[review][x] = (self.each_word_count[self.categories[self.categories.index(self.categories[x])]][0][0] + alpha) / (num_of_features[1] + 2 * alpha)
                    else:
                        prob_smooth_pos[review][x] = (self.each_word_count[self.categories[self.categories.index(self.categories[x])]][0][1] + alpha) / (num_of_features[1] + 2 * alpha)

                    """
                    we want P(Category = cat | C = 1) = num_of_ones_in_reviews(cat) + alpha / num_of_total_features(cat) + 2 * alpha ??
                    and then P(Category = cat | C = 1) = num_of_zeros_in_reviews(cat) + alpha / num_of_total_features(cat) + 2 * alpha ??

                    """
                    #prob_smooth_pos[review] = (num_of_pos_reviews + alpha)/(data[1] + num_of_features * alpha)
                else:
                    
                    """
                    we want P(Category = cat | C = 0) = num_of_ones_in_reviews(cat) + alpha / num_of_total_features(cat) + 2 * alpha ??
                    and then P(Category = cat | C = 0) = num_of_zeros_in_reviews(cat) + alpha / num_of_total_features(cat) + 2 * alpha ??

                    """            
                    if(prob_smooth_neg[review][x] == 0):
                        prob_smooth_neg[review][x] = (self.each_word_count[self.categories[self.categories.index(self.categories[x])]][1][0] + alpha) / (num_of_features[0] + 2 * alpha)    #calculates probability of 1 if review is 0
                    else:
                        prob_smooth_neg[review][x] = (self.each_word_count[self.categories[self.categories.index(self.categories[x])]][1][1] + alpha) / (num_of_features[0] + 2 * alpha)    #calculates probability of 0 if review is 0
                    #prob_smooth_neg[review] = (num_of_neg_reviews + alpha)/(data[1] + num_of_features * alpha)

        return prob_smooth_pos, prob_smooth_neg

    
    """
    predicts the target value for each review
    """
    def classify(self, data):
        prob_1 = prob_0 = 0.5
        prob_pos = list()
        prob_neg = list()
        prob_cat_pos, prob_cat_neg = Naive_Bayes.laplace_smoothing(self,data)
        for review in range(len(self.dict_values_for_reviews)):

            prob_pos[review] = prob_1 * np.multiply([x for x in prob_cat_pos])

            prob_neg[review] = prob_0 * np.multiply([x for x in prob_cat_neg])

        
        return prob_pos, prob_neg



    """
    returns the predicted binary value for each review
    """
    def naive_bayes(self,train, test):
        results = list()
        prob_pos, prob_neg = Naive_Bayes.classify(self,train)

        for i in range (len(prob_pos)):
            if prob_pos[i] > prob_neg[i]:
                results[i] = 1
            else:
                results[i] = 0
        return results


