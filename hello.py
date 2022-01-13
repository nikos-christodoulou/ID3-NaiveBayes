import numpy as np
import pandas as pd
from collections import deque
from InformationGain import Entropy
data = {
    'wind_direction': ['N', 'S', 'E', 'W'],
    'tide': ['Low', 'High'],
    'swell_forecasting': ['small', 'medium', 'large'],
    'good_waves': ['Yes', 'No']
}
data_df = pd.DataFrame(columns=data.keys())

np.random.seed(42)
# randomnly create 1000 instances
for i in range(1000):
    data_df.loc[i, 'wind_direction'] = str(np.random.choice(data['wind_direction'], 1)[0])
    data_df.loc[i, 'tide'] = str(np.random.choice(data['tide'], 1)[0])
    data_df.loc[i, 'swell_forecasting'] = str(np.random.choice(data['swell_forecasting'], 1)[0])
    data_df.loc[i, 'good_waves'] = str(np.random.choice(data['good_waves'], 1)[0])

data_df.head()
print(data_df)
print(data_df.shape[1])
X = np.array(data_df.drop('good_waves', axis=1).copy())
print(X)
y = np.array(data_df['good_waves'].copy())
print(y)
feature_names = list(data_df.keys())[:3]
print(feature_names)


x_targets_count = (1,2,3,4,5,6)
id_of_category = ([1,2,3,4],[5,6,7,8])
x = [v_counts/len(id_of_category) * 0.5 for v_counts,v_ids in zip(x_targets_count,id_of_category)]
print(x)

def add_letter(mylist):
    for i in range(len(mylist)):
        mylist[i] = str(mylist[i]) + randomletter


# Now you can call addletter function
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, ];
randomletter = 'a'
add_letter(mylist)
print(mylist)

COUNT = [10]
 
# Binary Tree Node
""" utility that allocates a newNode
with the given key """
class newNode:
 
    # Construct to create a newNode
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
 
# Function to print binary tree in 2D
# It does reverse inorder traversal
def print2DUtil(root, space) :
 
    # Base case
    if (root == None) :
        return
 
    # Increase distance between levels
    space += COUNT[0]
 
    # Process right child first
    print2DUtil(root.right, space)
 
    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end = " ")
    print(root.data)
 
    # Process left child
    print2DUtil(root.left, space)
 
# Wrapper over print2DUtil()
def print2D(root) :
     
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)
 
# Driver Code
if __name__ == '__main__':
 
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
 
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)
    root.right.right = newNode(7)
 
    root.left.left.left = newNode(8)
    root.left.left.right = newNode(9)
    root.left.right.left = newNode(10)
    root.left.right.right = newNode(11)
    root.right.left.left = newNode(12)
    root.right.left.right = newNode(13)
    root.right.right.left = newNode(14)
    root.right.right.right = newNode(15)
     
    print2D(root)
