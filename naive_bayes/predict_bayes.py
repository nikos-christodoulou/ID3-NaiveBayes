
from re import I
import numpy as np


class Naive_Bayes:

    def __init__(self,target_values,each_word_count,categories):
        self.target_values = target_values
        self.each_word_count = each_word_count
        self.categories = categories
        



    """"
    laplace smoothing is used to handle 
    zero probability error. We use the alpha (!=0) as 
    the smoothing parameter.

    """    
    
    def laplace_smoothing(self,test,alpha = 1.0):
        tar = list(self.target_values)
        num_of_features = [tar.count(x) for x in set(tar)]
        print("num of features is: ", num_of_features)
        test1 = np.copy(test)
        test2 = np.copy(test) 
        test1 = test1.astype(float, order='K', subok=True, copy=False)
        test2 = test2.astype(float, order='K', subok=True, copy=False)
        '''
        Test 1 will be for the positives reviews and the corresponding values 
        Test 2 will be for the negative reviews and the corresponding values
        '''
        for review in range (len(test)):
            for x in range(len(self.categories)):
                if(test[review][x] == 0):
                    test1[review][x] = (self.each_word_count[self.categories[self.categories.index(self.categories[x])]][0][0] + alpha) / (num_of_features[1] + 2 * alpha)
                else:
                    test1[review][x] = (self.each_word_count[self.categories[self.categories.index(self.categories[x])]][0][1] + alpha) / (num_of_features[1] + 2 * alpha)

                    """
                    we want P(Category = cat | C = 1) = num_of_ones_in_reviews(cat) + alpha / num_of_total_features(cat) + 2 * alpha ??
                    and then P(Category = cat | C = 1) = num_of_zeros_in_reviews(cat) + alpha / num_of_total_features(cat) + 2 * alpha ??

                    """
                    #prob_smooth_pos[review] = (num_of_pos_reviews + alpha)/(data[1] + num_of_features * alpha)
                            
                if(test[review][x] == 0):
                    test2[review][x] = (self.each_word_count[self.categories[self.categories.index(self.categories[x])]][1][0] + alpha) / (num_of_features[0] + 2 * alpha)    #calculates probability of 1 if review is 0
                else:
                    test2[review][x] = (self.each_word_count[self.categories[self.categories.index(self.categories[x])]][1][1] + alpha) / (num_of_features[0] + 2 * alpha)    #calculates probability of 0 if review is 0
                
                    
                """
                we want P(Category = cat | C = 0) = num_of_ones_in_reviews(cat) + alpha / num_of_total_features(cat) + 2 * alpha ??
                and then P(Category = cat | C = 0) = num_of_zeros_in_reviews(cat) + alpha / num_of_total_features(cat) + 2 * alpha ??

                """    
                #prob_smooth_neg[review] = (num_of_neg_reviews + alpha)/(data[1] + num_of_features * alpha)

        return test1, test2

    
    """
    predicts the target value for each review
    """
    def classify(self,test):
        #prob_1 = prob_0 = 0.5
        prob_pos = list()
        prob_neg = list()
        prob_cat_pos, prob_cat_neg = Naive_Bayes.laplace_smoothing(self,test)
        tar = list(self.target_values)
        num_of_features = [tar.count(x) for x in set(tar)]
        print("num of features is: ", num_of_features)
        for review in range(len(test)):
            '''
            Product of the elements inside the array which are the laplace probabilities 
            '''
            prob_pos.append(np.prod(prob_cat_pos[review])*num_of_features[0]/sum(num_of_features))
            prob_neg.append(np.prod(prob_cat_neg[review])*num_of_features[1]/sum(num_of_features))
        return prob_pos, prob_neg



    """
    returns the predicted binary value for each review
    """
    def naive_bayes(self,test):
        results = np.zeros(len(self.target_values), dtype = int)
        '''
        Test should be a two dimensional array with the reviews that want to be classified
        '''
        prob_pos, prob_neg = Naive_Bayes.classify(self,test)

        for i in range (len(prob_pos)):
            if prob_pos[i] > prob_neg[i]:
                results[i] = 1
            else:
                results[i] = 0
        return results


