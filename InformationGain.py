import math 
import time
from itertools import combinations
approximate = True # if we want to approximate the logs 
ln = math.log(2)
def Entropy(pos,neg):
    if(pos <= 0 or neg <= 0):
        return 0 
    if(approximate):
        en = ((2*(pos*neg))/(pos+neg))/((pos+neg)*ln)
    else:
        en = -pos/(pos+neg) * math.log(pos/(pos+neg),2) - neg/(neg+pos)*math.log(neg/(neg+pos),2)
    return en
def IG(total_number_of_positive_reviews,total_number_of_negative_reviews,positive_reviews_word,negative_reviews_word):
    sum = 0 
    for i in range(0,2):
        if(i == 0):
            sum = sum + (positive_reviews_word + negative_reviews_word)/(total_number_of_positive_reviews + total_number_of_negative_reviews) * Entropy(positive_reviews_word,negative_reviews_word)
        else:
            sum = sum +  (total_number_of_positive_reviews-positive_reviews_word + total_number_of_negative_reviews - negative_reviews_word)/(total_number_of_positive_reviews + total_number_of_negative_reviews) * Entropy(total_number_of_positive_reviews-positive_reviews_word,total_number_of_negative_reviews - negative_reviews_word)
    
    return Entropy(total_number_of_positive_reviews,total_number_of_negative_reviews) - sum
'''
class Value(object):
    def __init__(self, value): self.value = value

y = Value(7)
x = y
x.value = 8
print (y.value)

indexes = list()
values_count = [10100,12321,232]
total = sum(values_count)
for i in range(0,3):
    indexes.append(i)
comb = combinations(indexes,2)
entropy = 0
for i in list(comb): 
    entropy = entropy + (((2*values_count[i[1]]*values_count[i[0]])/(total))/(total*ln))
'''
'''
ln = math.log(2)
x = 20
y = 200000
list1 = list()
list2 = list()
list3 = list() 

start = time.time() 
for x in range(1,100):
    for y in range(1,50):
        list1.append(-x/(x+y)*math.log(x/(x+y),2) - y/(x+y)*math.log(y/(x+y),2))
print(time.time() - start)
start = time.time()
for x in range(1,100):
    for y in range(1,50): 
        list2.append(((3*(x*y))/(x+y))/((x+y)*ln))
print(time.time() - start)
start = time.time()
for x in range(1,100):
    for y in range(1,50): 
        list3.append(((3.1*(x*y))/(x+y))/((x+y)*ln))
print(time.time() - start)

for x in range(len(list1)):
    print("Difference2: " + str(list1[x] - list2[x]))
    print("Difference3: " + str(list1[x] - list3[x]))
'''