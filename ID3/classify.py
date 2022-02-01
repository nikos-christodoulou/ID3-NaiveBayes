from asyncore import read
import read_files 
from hyperparameters import per,number_of_vocab_words,approximate_logs
from ID3 import DecisionTree
import numpy as np 


cat_and_rev = read_files.classify_read_file(per,number_of_vocab_words,approximate_logs)
tup = read_files.create_vectors(cat_and_rev)
categories = tup[0]
values_for_review = tup[1]
target = tup[2]

'''
Train the algorithm for the specific percentage , number_of_vocab_words and approximate logs
'''
p1 = DecisionTree(values_for_review,categories,target)
p1.ID3_start()
if(p1.problem):
    print("problem")
    p1.before_predict(p1.node)
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
            value = p1.predict(vector,p1.categories,categories,p1.node)
            if(value == 0):
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
        value = p1.predict(vector,p1.categories,categories,p1.node)
        if(value == 0):
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
        vector = list()
        count = 0
        '''
        Because we want the words of the binary file to be the same with the file that we trained ID3 with 
        we assume for all the words that are not present in the given binary file and are present in the train file 
        that their values is 0 and we add them to the vectors
        '''
        for x in p1.categories:
            if not (x in tup[0]):
                tup[0].append(x)
                for y in range(len(tup[1])):
                    if(count < 3):
                        vector.append(np.append(tup[1][y],[0]))
                        count = count + 1
                    else:
                        vector[y] = np.append(vector[y],[0])
        for x in vector:
            value = p1.predict(x,p1.categories,tup[0],p1.node)
            if(value == 0):
                print("Negative review")
            else:
                print("Positive review")
    elif choice == '4': 
        break
    else: 
        print("Unknown Option Selected!") 
