from filter_the_vocabulary import vocabulary
from countwords import read_text_file
import os 
folders = ['neg','pos']
training_vector = list()
'''
We will create a binary vector with 1 if the word in the dictionary is present in the sentence 
else the value will be 0 if it's not contained in the word 
''' 
for i in folders:
    path = "C:/Users/fotis/OneDrive/Desktop/Aiexercise2/aclImdb/train/" + i 
    os.chdir(path)
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
        splited_sentence = sentence.split() 
        temp_list = list()
        for key in vocabulary:
            
            if(key in splited_sentence):
                temp_list.append((key,1))
            else:
                temp_list.append((key,0))
        if(i == "neg"):
            temp_list.append(0)
        else:
            temp_list.append(1)
        training_vector.append(temp_list)
        f.close()

print(training_vector[10])

            
        