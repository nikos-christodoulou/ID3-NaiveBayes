import numpy as np 
from construct_training_examples import training_data_frame
values_for_each_sentence = np.array(training_data_frame.drop('positive_or_negative',axis=1)).copy()
values_for_positiveornegative = np.array(training_data_frame["positive_or_negative"]).copy()
x_dim = training_data_frame.shape[1] - 1
categories = list(training_data_frame.keys())[:x_dim]

for x in values_for_each_sentence: 
    if(x[0] == 1 and x[1] == 1):
        print(x)