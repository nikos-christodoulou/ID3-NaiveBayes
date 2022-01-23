import pandas as pd
import numpy as np

from main_algorithms.read_train_files import read_file, create_vectors


print()

cat_and_rev = read_file(0.01,10,True)

data = create_vectors(cat_and_rev)
#data = np.array(data)
print(data)
print("Here the data stops.")
categories = np.array(data[0])
print(categories)
print("Here the categories stop. Categories' shape is {}.".format(categories.shape))
values_for_each_sentence = np.array(data[1])
print(values_for_each_sentence)
print("Here the values_for_each_sentence stop. Values fos each sentece shape is {}.".format(values_for_each_sentence.shape))
values_for_positiveornegative = np.array(data[2])
print("Here the positive_or_negagive stops. The shape is {}.".format(values_for_positiveornegative.shape))

print(values_for_positiveornegative)

