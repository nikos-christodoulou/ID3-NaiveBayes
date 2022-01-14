import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import os
from filter_the_vocabulary import vocabulary

#path = "C:/Users/fotis/OneDrive/Desktop/Aiexercise2/aclImdb/train/" + i 

folders = ['neg','pos']
training_vector = dict()
'''
We will create a binary vector with 1 if the word in the dictionary is present in the sentence 
else the value will be 0 if it's not contained in the word 
this will be a pandas dataframe 
''' 
training_data_frame = pd.DataFrame()
for i in folders:
    path = "C:/Users/Nikos/Desktop/AI/aclImdb/train/" + i 
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
        for key in vocabulary:
            if(not(key in training_vector)):
                training_vector[key] = list()
            if(key in splited_sentence):
                training_vector[key].append(1)
            else:
                training_vector[key].append(0)
        if(not("positive_or_negative" in training_vector)):
                training_vector["positive_or_negative"] = list()
        if(i == "neg"):
            training_vector["positive_or_negative"].append(0)
        else:
            training_vector["positive_or_negative"].append(1)
        f.close()

training_data_frame = pd.DataFrame(training_vector)


y = {0, 1}	#y is 0 if neg and 1 if pos
#this is the learning rate and it's used fo calculating derivatives
L = 0.001   


def sigmoid(x):
	return 1/(np.exp(-x) + 1)

# y_hat is the predicted value
# returns a numpy array of predicted values
# for each element of our data

def y_hat(data,w, b):

	return np.array([sigmoid(w + b * x) for x in data])
    
    


def loss_function(data, y, y_hat):
    
	return np.array([-np.mean(y*(np.log(y_hat)) - (1-y) * np.log(1 - y_hat)) for x in data])
    

# this function is used to calculate the best
# derivatives(parameters) to minimize the error.
# and trains our data

def gradients(data, y):
    
	#we first normalize the data
    data = normalize(data)

    '''
    we need to find the number of iterations(epochs)
    for the stohastic gradient descent algorithm and minimize the cost
    this happens when loss function becomes very small 
    '''
    epochs = 300    #let's say that this number = 300
	#finding the gradients
    for epoch in range(epochs):
		#calculating the predicted value for all the elements in data
       
	    y_hat = y_hat(data, w, b)

	    dw = -2 * sum((y - y_hat) * y_hat * ( 1- y_hat))	        #partial derivative with respect to weight
	    db = -2 * sum((y - y_hat) * y_hat * (1 - y_hat) * data) 	#partial derivative with respect to bias

		# update the values of weight and bias
        # w and b are first initialized with 0 globally
        # L controls how much w and b are updated
	    w = w - L * dw
	    b = b - L * db 


    return w, b 


# This function is used to normalize our data
def normalize(data):
	
    return data - data.mean()
	
		

def predict(data):

	x = normalize(data)
	
	pred_class = [] 	#store predictions

	pred_class = [1 if i > 0.5 else 0 for i in data]

	return np.array(pred_class)


def calculate_accuracy(actual_data, predicted_data):
    accuracy = 0
    for i in range(len(predicted_data)):
        if actual_data[i] == predicted_data[i]:
            accuracy +=1
    
    print("Accuracy = {}").format(accuracy / len(y_hat))

'''
# Implementing the algorithm
w, b = gradients(training_data_frame, y_hat(training_data_frame,))
data = training_data_frame.positive_or_negative


'''

