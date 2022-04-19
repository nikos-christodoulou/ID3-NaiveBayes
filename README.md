# Aiexercise2
This a 3rd year project for Athens University of Economics and Business(AUEB) Artificial Intelligence course. The task is to implement the ID3 and the NAIVE BAYES 
algorithm and use the train and test data from the following dataset:https://ai.stanford.edu/~amaas/data/sentiment/. 




You can find info about the dataset here:https://keras.io/api/datasets/imdb/





The first step is to find the most commonly used words in the whole dataset of reviews and then filter them using ENTROPY. Then after we filter the words we must create 
a dictionary that will contain the most negatively or positively charged words and using that determine whether a review is negative or positive(we don't about the neutral reviews in the dataset).




The algorithms will be reading 0-1 vectors for each review: 0 meaning that the specific word in the dictionary was not present in the review and 1 meaning that the word was present in the review. 
In the Naive Bayes algorithm we use LA PLACE estimators always. 



The algorithms run through the executables: execute.py and classify.py. In execute.py we build txt files that are binary vectors and there are 4 command line arguments to be given. The first x is the percentage of data you will use to train the algorithm, the second z we is the method we use to approximate logs(they require a lot of computational power) to optimizate the gathering of data and the last in the number of keywords that the dictionary will contain. In classify.py you use the three above except the last one where you can give a dummy parameter. In classify you can do 3 things: 
1.) Read the a text file, meaning a review, and see if its positive or negative 
2.) You can type the review yourself 
3.) You can read an existing binary vector file 

The if statement in executy inside the for loops is to determine what type of test we are going to do. We want to gather a lot of different metrics like testing the accuracy on training data while training the algorithms on training data etc. that's why it's done. 



The commit history is a bit messy due the vast amount of files we needed to upload.
