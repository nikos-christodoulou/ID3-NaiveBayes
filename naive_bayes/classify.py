from asyncore import read
import read_files 
import word_and_count 
from hyperparameters import per,number_of_vocab_words,approximate_logs
import predict_bayes
import numpy as np 
'''
Specify through hyperparameters on how you want to train the data
'''
menu = {} 
menu['1']="Read text file: 1" 
menu['2']="Type the review: 2"
menu['3']="Read binary vector file: 3"
menu['4']="Exit: 4"

cat_and_rev = read_files.classify_read_file(per,number_of_vocab_words,approximate_logs)
tup = read_files.create_vectors(cat_and_rev)
categories = tup[0]
values_for_review = tup[1]
target = tup[2]

'''
Train the algorithm for the specific percentage , number_of_vocab_words and approximate logs
'''
each_word_count = word_and_count.count(values_for_review,target,categories)
bayes_object = predict_bayes.Naive_Bayes(target,each_word_count,categories)
'''
You can either 
Read a text file that has strings 
Type a review in the command line
Read a binary file 
'''
while True: 
    print("Read text file: 1")
    print("Type the review: 2")
    print("Read binary vector file: 3")
    print("Exit: 4")
    choice = input()
    if choice =='1': 
        print("Type the name of the text file")
        file_name = input()
        while not (file_name.endswith(".txt")):
           print("Incorrect file type try again") 
           file_name = input()
        with open(file_name,'r') as f:
            contents = f.read() 
            contents = contents.translate({ord(c): None for c in '[]().!@#$***,?:-=+'})
            contents = contents.lower()
            contents = contents.replace("<br />"," ")
            splited_sentence = contents.split()
            vector = list() 
            for x in categories:
                if (x in splited_sentence):
                    vector.append(1)
                else:
                    vector.append(0)
            binary = np.array([vector])
            target_val = np.array([target])
            res = bayes_object.naive_bayes(binary,categories)
            if(res[0] == 0):
                print("Negative review")
            else:
                print("Positive review")
    elif choice == '2': 
        print("Type the review")
        sentence = input()
        sentence = sentence.translate({ord(c): None for c in '[]().!@#$***,?:-=+'})
        sentence = sentence.lower()
        sentence = sentence.replace("<br />"," ")
        splited_sentence = sentence.split()
        vector = list() 
        for x in categories:
            if (x in splited_sentence):
                vector.append(1)
            else:
                vector.append(0)
        binary = np.array([vector])
        target_val = np.array([target])
        res = bayes_object.naive_bayes(binary,categories)
        if(res[0] == 0):
            print("Negative review")
        else:
            print("Positive review")
    elif choice == '3':
        print("Type the name of the text file")
        file_name = input()
        while not (file_name.endswith(".txt")):
           print("Incorrect file type try again") 
           file_name = input()
        cat = read_files.read_binary_vector_review(file_name)
        tup = read_files.create_vectors_for_binary_review(cat)

        val = np.array(tup[1])
        print(val)  
        res = bayes_object.naive_bayes(val,tup[0])
        for x in res:
            if(x == 0):
                print("Negative review")
            else:
                print("Positive review")
    elif choice == '4': 
        break
    else: 
        print("Unknown Option Selected!") 




