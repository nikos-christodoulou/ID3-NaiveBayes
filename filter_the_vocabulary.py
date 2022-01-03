from countwords import vocabulary,positive_word_in_reviews,negative_word_in_reviews,positive_reviews,negative_reviews
from InformationGain import IG



keys_to_be_deleted = list()
temp_vocab = dict()
temp_neg = dict()
temp_pos = dict()
for x in vocabulary:
    # we create the word in positive or negative so we don't get a key error
    if(not(x in positive_word_in_reviews)):
        positive_word_in_reviews[x] = 0
    if(not(x in negative_word_in_reviews)):
        negative_word_in_reviews[x] = 0
    #this will be used to find the k most informational words
    information = IG(positive_reviews,negative_reviews,positive_word_in_reviews[x],negative_word_in_reviews[x])
    vocabulary[x] = information
    
for i in range (0,499):
    '''
    Find the max key aka the word with the largest IG and take it out of the dictionary 
    this is done to find the next most informational word 
    '''
    max_key = max(vocabulary, key=vocabulary.get)
    temp_vocab[max_key] = vocabulary[max_key]
    vocabulary.pop(max_key,None)
    temp_neg[max_key] = negative_word_in_reviews[max_key]
    temp_pos[max_key] = positive_word_in_reviews[max_key]

vocabulary = temp_vocab
positive_word_in_reviews = temp_pos 
negative_word_in_reviews = temp_neg

#print(vocabulary)