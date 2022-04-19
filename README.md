# Aiexercise2
This a 3rd year project for Athens University of Economics and Business(AUEB) Artificial Intelligence course. The task is to implement the ID3 and the NAIVE BAYES 
algorithm and use the train and test data from the following dataset:https://ai.stanford.edu/~amaas/data/sentiment/. 




You can find info about the dataset here:https://keras.io/api/datasets/imdb/





The first step is to find the most commonly used words in the whole dataset of reviews and then filter them using ENTROPY. Then after we filter the words we must create 
a dictionary that will contain the most negatively or positively charged words and using that determine whether a review is negative or positive(we don't about the neutral reviews in the dataset).
The algorithms will be reading 0-1 vectors for each review: 0 meaning that the specific word in the dictionary was not present in the review and 1 meaning that the word was present in the review. 
In the Naive Bayes algorithm we use LA PLACE estimators always. 
