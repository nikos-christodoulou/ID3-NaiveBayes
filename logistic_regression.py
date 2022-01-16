import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import os
from filter_the_vocabulary import vocabulary

#path = "C:/Users/fotis/OneDrive/Desktop/Aiexercise2/aclImdb/train/" + i 


class LogisticRegression:
    """
    Our algorithm needs a learning rate, the max_number of iterations(epochs),
    the weight and bias.
    """
    def __init__(self, learning_rate = 0.01, w = 0, b = 0, max_epochs = 100):
        self.learing_rate = learning_rate
        self.max_epochs = max_epochs
        self.w = w
        self.b = b
        #used to store the loss
        self.likelihoods = []
        #instead of log(0)
        self.eps = 1e-7


        

    def sigmoid(self, x):
        return 1/(np.exp(-x) + 1)

    # y_pred is the predicted value
    # returns a numpy array of predicted values
    # for each element of our data

    def y_pred(self, data, w, b):

        return np.array([self.sigmoid(w + b * x) for x in data])
        
    
    '''    
    in gradient ascent we need to maximize
    the loss function. This loss in gradient ascent
    is called Maximum Log Likelihood.
    
    '''
    def log_likelihood(self, y, y_pred):
        
        #y is a numpy array of our actual values
        #y_pred is a numpy array of the predicted values

        #we might have a problem with log(0)
        #so instead of 0 it takes the minimum value assigned to self.eps
        y_pred = np.maximum(np.full(y_pred.shape, self.eps), np.minimum(np.fully(y_pred.shape, 1-self.eps), y_pred))

        loss = sum(y * np.log(y_pred) + (1-y) * np.log(1-y_pred))   #return np.array([-np.mean(y*(np.log(y_pred)) - (1-y) * np.log(1 - y_pred)) for x in data])
        #in descent we would substract instead of adding the values
        return loss

        

    # this function is used to calculate the best
    # derivatives(parameters) to minimize the error.
    # and trains our data

    def train(self, data, y):
        
        #we first normalize the data
        data = self.normalize(data)

        #initialize weight and bias
        self.w, self.b = np.zeros(data.shape[1])

        '''
        we need to find the number of iterations(epochs)
        for the stohastic gradient ascent algorithm and maximize the cost 
        '''
        #finding the gradients
        for epoch in range(self.epochs):
            #calculating the predicted value for all the elements in data
            
            #y_hat = y_hat(data, w, b)
            y_pred = y_pred(self, data, self.w, self.b)

            dw = -2 * sum((y - y_pred) * y_pred * ( 1- y_pred))	        #partial derivative with respect to weight
            db = -2 * sum((y - y_pred) * y_pred * (1 - y_pred) * data) 	#partial derivative with respect to bias

            # update the values of weight and bias
            # w and b are first initialized with 0 globally
            # L controls how much w and b are updated
            self.w = self.w + self.learing_rate * dw
            self.b = self.b + self.learing_rate * db 

        loss = self.log_likelihood(y, y_pred)
        self.likelihoods.append(loss)
        return self.w, self.b 


    # This function is used to normalize our data
    def normalize(data):
        
        return data - data.mean()
        
            

    def predict(self, data, threshold = 0.5):

        x = self.normalize(data)
        #returns a numpy arraylist with the predicted binary probabilty value of each element in our data
        binary_preds = np.array(list(map(lambda x: 1 if x > threshold else 0, self.y_pred(data, self.w, self.b))))
        return binary_preds
       


    def calculate_accuracy(actual_data, predicted_data):
        accuracy = 0
        for i in range(len(predicted_data)):
            if actual_data[i] == predicted_data[i]:
                accuracy +=1
        
        print("Accuracy = {}").format(accuracy / len(predicted_data) * 100)

'''
# Implementing the algorithm


'''

