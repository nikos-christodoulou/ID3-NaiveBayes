from collections import Counter 
import os
 
path = "C:/Users/fotis/OneDrive/Desktop/Aiexercise2/aclImdb"

#read text file 
def read_text_file(file_path):
    with open(file_path,'r',encoding="latin-1") as f: 
        return f.read()

vocabulary = dict() 
positive_word_in_reviews = dict() #in how many negative reviews a specific word appears
negative_word_in_reviews = dict() #in how many positive reviews a specific word appears 

negative_reviews = 0
positive_reviews = 0

folders = ["neg","pos"]
negative = list()
positive = list()
for i in folders:
    #this will be the folder path for the positives and the negatives
    path = "C:/Users/fotis/OneDrive/Desktop/Aiexercise2/aclImdb/train/" + i 
    #this will change the directory 
    os.chdir(path)
    
    print("This checks " + i)
    

    #here we will iterate through the whole file 
    count = 0
    for file in os.listdir(): 
        # check the text format 
        if file.endswith(".txt"):
            file_path = f"{path}/{file}"
        f = open(file_path,'r',encoding="latin-1")
        sentence = f.read()
        #removing special characters so the vocabulary can represent tha data set better 
        sentence = sentence.translate({ord(c): None for c in '().!@#$***'})
        sentence = sentence.lower()
        sentence = sentence.replace("<br />"," ")
        #we count the occurances for each word in each text file 
        splited_sentence = sentence.split() 
        Countervariable = Counter(splited_sentence)
        most_occurred_words = Countervariable.most_common()
        if(i == 'neg'):
            negative.extend(most_occurred_words)
            negative_reviews = negative_reviews + 1
        else:
            positive.extend(most_occurred_words)
            positive_reviews = positive_reviews + 1
        f.close()
for x in negative: 
    #if word is not in vocabulary create new entry 
    if(not(x[0] in vocabulary)):
        vocabulary[str(x[0])] = 0
        negative_word_in_reviews[str(x[0])] = 0
    vocabulary[x[0]] = vocabulary[x[0]] + x[1]
    negative_word_in_reviews[str(x[0])] = negative_word_in_reviews[str(x[0])] + 1
for x in positive:
    #because the main vocabulary might have words that the positive vocabulary doesn't have
    #we might need to create an entry for the positive that is already there for the main vocab 
    if(not(x[0] in vocabulary)):
        vocabulary[str(x[0])] = 0
        
    if(not(x[0] in positive_word_in_reviews)):
        positive_word_in_reviews[str(x[0])] = 0
    vocabulary[x[0]] = vocabulary[x[0]] + x[1]
    positive_word_in_reviews[str(x[0])] = positive_word_in_reviews[str(x[0])] + 1

#print(vocabulary)
#print(negative_word_in_reviews)
#print(positive_word_in_reviews)