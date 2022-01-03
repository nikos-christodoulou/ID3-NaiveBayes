import math 
def Entropy(pos,neg):
    if(pos <= 0 or neg <= 0):
        return 0 
    en = -pos/(pos+neg) * math.log(pos/(pos+neg),2) - neg/(neg+pos)*math.log(neg/(neg+pos),2)
    return en
def IG(total_number_of_positive_reviews,total_number_of_negative_reviews,positive_reviews_word,negative_reviews_word):
    sum = 0 
    for i in range(0,2):
        if(i == 0):
            sum = sum + (positive_reviews_word + negative_reviews_word)/(total_number_of_positive_reviews + total_number_of_negative_reviews) * Entropy(positive_reviews_word,negative_reviews_word)
        else:
            sum = sum +  (total_number_of_positive_reviews-positive_reviews_word + total_number_of_negative_reviews - negative_reviews_word)/(total_number_of_positive_reviews + total_number_of_negative_reviews) * Entropy(total_number_of_positive_reviews-positive_reviews_word,total_number_of_negative_reviews - negative_reviews_word)
    
    return Entropy(total_number_of_positive_reviews,total_number_of_negative_reviews) - sum