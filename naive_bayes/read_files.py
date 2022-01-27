from re import L
import numpy as np 
import os,time 
def read_file(per,number_of_vocab_words,approximate_log,type_of_test):
    '''
    Read the same percentage from each category of files to compare error
    '''
    if(type_of_test == "same_percentage"):
        name1 =  "per_keys/" + str(round(per*100)) + "_" + str(number_of_vocab_words) + "_" + str(approximate_log) + ".txt"
        print("Try to read file: " + name1)
        while not os.path.exists(name1):
            print("Waiting... No file named: " + name1)
            time.sleep(40)
        name2 =  "per_keys_test/" + str(round(per*100)) + "_" + str(number_of_vocab_words) + "_" + str(approximate_log) + ".txt"
        while not os.path.exists(name2):
            print("Waiting... No file named: " + name2)
            time.sleep(40)
        print("Try to read file: " + name2)
        with open(name1,'r'):
            file1 = open(name1,'r')
            cat_and_rev1 = file1.readlines()
        with open(name2,'r'):   
            file2 = open(name2,'r')
            cat_and_rev2 = file2.readlines()
        return cat_and_rev1,cat_and_rev2
    elif(type_of_test == "train_data"):
        '''
        With a given percentage of training data find the errors for all the training data
        '''
        name1 =  "per_keys/" + str(round(per*100)) + "_" + str(number_of_vocab_words) + "_" + str(approximate_log) + ".txt"
        print("Try to read file: " + name1)
        while not os.path.exists(name1):
            print("Waiting... No file named: " + name1)
            time.sleep(40)
        name2 =  "per_keys/" + str(100) + "_" + str(number_of_vocab_words) + "_" + str(approximate_log) + ".txt"
        print("Try to read file: " + name2)
        while not os.path.exists(name2):
            print("Waiting... No file named: " + name2)
            time.sleep(40)
        with open(name1,'r'):
            file1 = open(name1,'r')
            cat_and_rev1 = file1.readlines()
        with open(name2,'r'):
            file2 = open(name2,'r')
            cat_and_rev2 = file2.readlines()
       
        return cat_and_rev1,cat_and_rev2
    else:
        '''
        With a given percentage of training data find the errors for all the testing data
        '''
        name1 =  "per_keys/" + str(round(per*100)) + "_" + str(number_of_vocab_words) + "_" + str(approximate_log) + ".txt"
        print("Try to read file: " + name1)
        while not os.path.exists(name1):
            print("Waiting... No file named: " + name1)
            time.sleep(40)
        name2 =  "per_keys_test/" + str(100) + "_" + str(number_of_vocab_words) + "_" + str(approximate_log) + ".txt"
        print("Try to read file: " + name2)
        while not os.path.exists(name2):
            print("Waiting... No file named: " + name2)
            time.sleep(40)
        with open(name1,'r'):
            file1 = open(name1,'r')
            cat_and_rev1 = file1.readlines()
        with open(name2,'r'):
            file2 = open(name2,'r')
            cat_and_rev2 = file2.readlines()
       
        return cat_and_rev1,cat_and_rev2

def create_vectors(cat_and_rev):
    '''
    All the lines contain a \n characted
    The first line of the file are the categories
    The rest are the values for each word 
    The last category is positive of negative which are the target values
    '''
    categories = cat_and_rev[0].split()
    categories = categories[:-1]
    values_for_each_sentence = list()
    values_for_positiveornegative = list() 
    for x in range(1,len(cat_and_rev)):
        values_for_positiveornegative.append(cat_and_rev[x][len(cat_and_rev[x]) - 2])
        values_for_each_sentence.append(cat_and_rev[x][:-2].split())

    for x in values_for_each_sentence:
        for y in range(len(x)):
            x[y] = int(x[y])
        
    values_for_each_sentence = np.array((values_for_each_sentence))


    for x in range(len(values_for_positiveornegative)):
        values_for_positiveornegative[x] = int(values_for_positiveornegative[x])

    values_for_positiveornegative = np.array((values_for_positiveornegative))
    return (categories,values_for_each_sentence,values_for_positiveornegative)