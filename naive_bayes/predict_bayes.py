
from re import I
import numpy as np


class Naive_Bayes:

    def __init__(self,target_values,each_word_count,categories):
        '''
        Each word count and target values are essentially the training data 
        '''
        self.each_word_count = each_word_count
        self.categories = categories
        tar = list(target_values)
        self.num_of_features = [tar.count(x) for x in set(tar)]
        self.categories_of_test = list()



      
    
    def laplace_smoothing(self,test,alpha = 1.0):
        """"
        laplace smoothing is used to handle 
        zero probability error. We use the alpha (!=0) as 
        the smoothing parameter.

        """  
    
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
                #find the la place probability of the value of the specific word for the positive reviews
                '''
                We take the index of the categories of the testing examples using the training examples 
                We do this because: 
                Training dictionary might have: 
                Good,Bad,Terrible 
                Testing example might have:
                Good,Terrible,Bad,Awful 
                '''
                if(self.categories[x] in self.categories_of_test):
                    if(test[review][self.categories_of_test.index(self.categories[x])] == 0):
                        test1[review][self.categories_of_test.index(self.categories[x])] = (self.each_word_count[self.categories[self.categories.index(self.categories[x])]][0][0] + alpha) / (self.num_of_features[1] + 2 * alpha)
                    else:
                        test1[review][self.categories_of_test.index(self.categories[x])] = (self.each_word_count[self.categories[self.categories.index(self.categories[x])]][0][1] + alpha) / (self.num_of_features[1] + 2 * alpha)

                        """
                        we want P(Category = cat | C = 1) = num_of_ones_in_reviews(cat) + alpha / num_of_total_features(cat) + 2 * alpha ??
                        and then P(Category = cat | C = 1) = num_of_zeros_in_reviews(cat) + alpha / num_of_total_features(cat) + 2 * alpha ??

                        """
                    #find the la place probability of the value of the specific word for the negative reviews            
                    if(test[review][self.categories_of_test.index(self.categories[x])] == 0):
                        test2[review][self.categories_of_test.index(self.categories[x])] = (self.each_word_count[self.categories[self.categories.index(self.categories[x])]][1][0] + alpha) / (self.num_of_features[0] + 2 * alpha)    #calculates probability of 1 if review is 0
                    else:
                        test2[review][self.categories_of_test.index(self.categories[x])] = (self.each_word_count[self.categories[self.categories.index(self.categories[x])]][1][1] + alpha) / (self.num_of_features[0] + 2 * alpha)    #calculates probability of 0 if review is 0
                    
                        
                    """
                    we want P(Category = cat | C = 0) = num_of_ones_in_reviews(cat) + alpha / num_of_total_features(cat) + 2 * alpha ??
                    and then P(Category = cat | C = 0) = num_of_zeros_in_reviews(cat) + alpha / num_of_total_features(cat) + 2 * alpha ??

                    """

        return test1, test2

    
    
    def product_of_prob(self,test):
        """
        predicts the target value for each review
        """
        prob_pos = list()
        prob_neg = list()
        prob_cat_pos, prob_cat_neg = Naive_Bayes.laplace_smoothing(self,test)
       
        print("num of features is: ", self.num_of_features)
        for review in range(len(test)):
            '''
            Product of the elements inside the array which are the laplace probabilities 
            Below we don't remove the 0 chances of each known category 
            We remove the probabilities of the words of the test vector that are not in the dictionary that we created
            E.G. dictionary contains good,bad,excellent and test example is a vector of good,bad,terrible the terrible value will always have 0 probability
            '''
            temp1 = prob_cat_pos[review][prob_cat_pos[review] > 0]
            temp2 = prob_cat_neg[review][prob_cat_neg[review] > 0]
            prob_pos.append(np.prod(temp1)*self.num_of_features[1]/sum(self.num_of_features))
            prob_neg.append(np.prod(temp2)*self.num_of_features[0]/sum(self.num_of_features))
        return prob_pos, prob_neg



  
    def naive_bayes(self,test,categories_of_test):
        """
        Test should be a two dimensional array with the reviews that want to be classified
        returns the predicted binary value for each review
        """
        self.categories_of_test = [x for x in categories_of_test]
        results = np.zeros(test.shape[0],dtype = int)
        prob_pos, prob_neg = Naive_Bayes.product_of_prob(self,test)
        for i in range (len(prob_pos)):
            if prob_pos[i] >= prob_neg[i]:
                results[i] = 1
            else:
                results[i] = 0
        return results


