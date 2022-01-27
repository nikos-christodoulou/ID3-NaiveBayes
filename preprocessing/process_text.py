import os 
def split_sentence(file,sentence):

        #removing special characters so the vocabulary can represent tha data set better 
        sentence = sentence.translate({ord(c): None for c in '().!@#$***,?:-=+'})
        sentence = sentence.lower()
        sentence = sentence.replace("<br />"," ")
        splited_sentence = sentence.split()
        return splited_sentence

def add_key(key,training_vector,splited_sentence):
        if(not(key in training_vector)):
                training_vector[key] = list()
        if(key in splited_sentence):
                training_vector[key].append(1)
        else:
                training_vector[key].append(0)
        
def add_target_val(training_vector,i):
        if(not("positive_or_negative" in training_vector)):
                training_vector["positive_or_negative"] = list()
        if(i == "neg"):
                training_vector["positive_or_negative"].append(0)
        else:
                training_vector["positive_or_negative"].append(1)