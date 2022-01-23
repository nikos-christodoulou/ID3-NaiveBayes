import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import os
import main_algorithms.read_train_files
#from preprocessing.filter_the_vocabulary import vocabulary
#from preprocessing.construct_training_examples import training_data_frame

#path = "C:/Users/fotis/OneDrive/Desktop/Aiexercise2/aclImdb/train/" + i 


class LogisticRegression:
    """
    Our algorithm needs a learning rate, the max_number of iterations(epochs),
    the weight and the lambda factor for regularization.
    """
    def __init__(self, learning_rate = 0.001, w = 0, max_epochs = 100, l = 1):
        self.learing_rate = learning_rate
        self.max_epochs = max_epochs
        self.w = w
        #this is our regularalization factor
        self.l = l
        #used to store the loss
        self.likelihoods = []
        self.proba1 = list()
        self.proba0 = list()
        #instead of log(0)
        self.eps = 1e-7


        

    def sigmoid(self, x):
        return 1.0/(np.exp(-x) + 1)

    # y_pred is used for the predicted value
    # returns a numpy array of predicted values between 0-1
    # for each element based on our training data
    

    def y_pred(self, data):
        #note that they_pred value is not the final 
        #binary value of our prediction, but the real number
        #between [0, 1] that is calculated by the sigmoid function.

        #data has to be a vector in order to calculate the dot product.
        '''
        z = np.dot(data, self.w)
        if (data[["positive_or_negative"]] == 1):
            self.proba1.append(self.sigmoid(z))
        else:
            self.proba0.append(1 - self.sigmoid(z))
        '''
        z = np.dot(data, self.w)
        if (data[["positive_or_negative"]] == 1):
            return self.sigmoid(z)
        else: 
            return 1.0 - self.sigmoid(z)    
    
        
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
        return np.mean(loss)

        

    # this function is used to calculate the best
    # derivatives(parameters) to minimize the error.
    # and trains our data

    def train(self, data, y):
        
        #we first normalize the data
        #data = self.normalize(data)

        #initialize weight
        self.w = np.zeros(data.shape[1])

        '''
        we need to find the number of iterations(epochs)
        for the stochastic gradient ascent algorithm and maximize the log_likelihood
        '''
        
        #finding the gradients
        
        for epoch in range(self.epochs):
            #calculating the predicted value for all the elements in data
            iter = 0
            y_pred = y_pred(data, self.w)
            
            #partial derivative with respect to weight
            dw = sum((y - y_pred) * y_pred * ( 1- y_pred))

            # update the values of weight
            # w is first initialized with 0 globally
            # learning rate controls how much w is updated
            self.w = self.w + self.learing_rate * dw
            
            loss = self.log_likelihood(y, y_pred)
            #Regularization
            loss = loss + self.l * np.pow(self.w, 2)

            self.likelihoods.append(loss)

            #checks if the likelihood is getting close to max
            #trying to maximize the cost for the stochastic gradient ascent
            if iter > 0:
                if (self.likelihoods[iter -1] > self.likelihoods[iter]):
                    break
        
        return self.w
        
        
            

    def predict(self, data, threshold = 0.5):

        #returns a numpy arraylist with the predicted binary probabilty value of each element in our data
        binary_preds = np.array(list(map(lambda x: 1 if x > threshold else 0, self.y_pred(data, self.w))))
        return binary_preds
       


    def calculate_accuracy(actual_data, predicted_data):
        accuracy = 0
        wrong_preds = 0
        for x in predicted_data:
            if x[["postitive_or_negative"]] == actual_data[["positive_or_negative"]]:
                accuracy +=1
            else:
                wrong_preds +=1 
        
        print("Accuracy = {}").format(accuracy / len(predicted_data) * 100)
        print("There were {} wrong predictions", wrong_preds)


# Implementing the algorithm
#"C:/Users/Nikos/Desktop/AI/training_examples.txt"
#train_df = pd.read_csv("C:/Users/Nikos/Desktop/AI/training_examples.txt")
#print(train_df)

#here we give values to our data

cat_and_rev = main_algorithms.read_train_files.read_file(0.01,10,True)

data = main_algorithms.read_train_files.create_vectors(cat_and_rev)

categories = int(data[0])
values_for_each_sentence = int(data[1])
values_positiveornegative = int(data[2])
model = LogisticRegression()

#train the algorithm
model.train(data, values_positiveornegative)

#predict the result based on the training data
predicted_value = model.predict(values_positiveornegative, 0.5)

#see results
model.calculate_accuracy(values_positiveornegative, predicted_value)






