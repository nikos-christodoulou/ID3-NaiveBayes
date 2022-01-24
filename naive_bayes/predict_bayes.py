from naive_bayes.naive_bayes import target_values, each_word_count, dict_values_for_reviews, categories
import numpy as np


class Naive_Bayes:

    def __init__(self):
        pass
        



    """"
    laplace smoothing is used to handle 
    zero probability error. We use the alpha (!=0) as 
    the smoothing parameter.

    """    
    
    def laplace_smoothing(self, data ,alpha = 1.0):
        #data[1] contains the binary values of each category for each review
        prob_smooth_pos = list()
        prob_smooth_neg = list()
        num_of_features = target_values / 2
        print("num of features is: ", num_of_features)
        for category in range(len(categories)):
            for review in range (len(target_values)):
                if data[2][review] == 1:

                    prob_smooth_pos[category][0] = (each_word_count[category][0][1] + alpha) / (num_of_features + 2 * alpha)
                    prob_smooth_pos[category][1] = (each_word_count[category][0][0] + alpha) / (num_of_features + 2 * alpha)

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
                    prob_smooth_neg[category][0] = (each_word_count[category][1][1] + alpha) / (num_of_features + 2 * alpha)    #calculates probability of 1 if review is 0
                    prob_smooth_neg[category][1] = (each_word_count[category][1][0] + alpha) / (num_of_features + 2 * alpha)    #calculates probability of 0 if review is 0
                    #prob_smooth_neg[review] = (num_of_neg_reviews + alpha)/(data[1] + num_of_features * alpha)

        return prob_smooth_pos, prob_smooth_neg

    
    """
    predicts the target value for each review
    """
    def classify(self, data):
        prob_1 = prob_0 = 0.5
        prob_pos = list()
        prob_neg = list()
        prob_cat_pos, prob_cat_neg = Naive_Bayes.laplace_smoothing(data)
        for review in range(len(dict_values_for_reviews)):

            prob_pos[review] = prob_1 * np.multiply([x for x in prob_cat_pos])

            prob_neg[review] = prob_0 * np.multiply([x for x in prob_cat_neg])

        
        return prob_pos, prob_neg



    """
    returns the predicted binary value for each review
    """
    def naive_bayes(train, test):
        results = list()
        prob_pos, prob_neg = Naive_Bayes.classify(train)

        for i in range (len(prob_pos)):
            if prob_pos[i] > prob_neg[i]:
                results[i] = 1
            else:
                results[i] = 0
        return results


