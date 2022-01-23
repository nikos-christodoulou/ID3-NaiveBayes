import pandas as pd
import numpy as np
from logistic_regression import LogisticRegression
#import matplotlib.pyplot as plt
#from preprocessing.construct_training_examples import training_data_frame
from main_algorithms.read_train_files import read_file, create_vectors



# Implementing the algorithm
#"C:/Users/Nikos/Desktop/AI/training_examples.txt"
#train_df = pd.read_csv("C:/Users/Nikos/Desktop/AI/training_examples.txt")
#print(train_df)

#here we give values to our data

"""cat_and_rev = read_file(0.01,10,True)

data = create_vectors(cat_and_rev)
#data = np.array(data)
print(data)
categories = np.array(data[0])
print(categories)
values_for_each_sentence = np.array(data[1])
print(values_for_each_sentence)
values_for_positiveornegative = np.array(data[2])"""



dummy = [
    np.array(["good", "bad", "worse"]),
    np.array([
        np.array([1,0,0]),
        np.array([0,0,1]),
        np.array([0,1,1]),
        np.array([0,0,0])
    ]),
    np.array([1,0,0,0])
]

dummy_pos_neg = dummy[2]

#print(dummy)
model = LogisticRegression()

#data = np.array(dummy)

#train the algorithm
print(model.train(dummy, dummy_pos_neg))
#predict the result based on the training data
#predicted_value = model.predict(dummy, 0.5)

#see results
#model.calculate_accuracy(values_for_positiveornegative, predicted_value)
