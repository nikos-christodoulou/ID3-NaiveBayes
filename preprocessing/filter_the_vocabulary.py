from countwords import vocabulary,positive_word_in_reviews,negative_word_in_reviews,positive_reviews,negative_reviews
from InformationGain import IG
import os,re 
from hyperparameters import number_of_vocab_words

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
    
for i in range (0,number_of_vocab_words):
    '''
    Find the max key aka the word with the largest IG and take it out of the dictionary 
    this is done to find the next most informational word 
    '''
    max_key = max(vocabulary, key=vocabulary.get)
    temp_vocab[max_key] = vocabulary[max_key]
    vocabulary.pop(max_key,None)
    temp_neg[max_key] = negative_word_in_reviews[max_key]
    temp_pos[max_key] = positive_word_in_reviews[max_key]

'''
Use the 1000 common words to filter the vocabulary more 
'''
path = "C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/filtering"
os.chdir(path)
with open("common1000.txt") as f:
    contents = f.read().splitlines()

'''
Prevent overfitting using the non negative of positive connotation words file 
these are words that have to do with movies and are not negative or positive 
'''
vocabulary = temp_vocab
for x in contents: 
    if(x in vocabulary):
        print("Removed word: " + x)
        vocabulary.pop(x,None)
path = "C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/filtering"
os.chdir(path)
with open("non_negative_or_positive_connotation_words.txt") as f:
    contents = f.read().splitlines()
for x in contents:
    if(x in vocabulary):
        print("Removed word: " + x)
        vocabulary.pop(x,None)
positive_word_in_reviews = temp_pos 
negative_word_in_reviews = temp_neg

print(vocabulary)