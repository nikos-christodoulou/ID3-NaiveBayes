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


**How we approximate the logs: **





1.) We have two categories p,q (negative and positive reviews). This is the entropy algorithm: 



![image](https://user-images.githubusercontent.com/83087431/164055975-918caf8f-20f5-4398-8eca-3798c0ce0a2d.png)

2.) Using change of base: 



![image](https://user-images.githubusercontent.com/83087431/164056052-1ddd92d1-600f-4839-a094-6440422aaf06.png)

We end up with this: 



![image](https://user-images.githubusercontent.com/83087431/164056102-d7732b98-15a5-42ee-ab41-cfc760a60592.png)



Because we are finding entropies we values for the above equation are always between 0 and 1. We know: 



![image](https://user-images.githubusercontent.com/83087431/164056383-15ae1f90-24d3-4104-8be4-89a808421f36.png)

For values between 0 and 1:



![image](https://user-images.githubusercontent.com/83087431/164056404-5ab36bd9-0037-4683-b1b7-683a089e505b.png)



3.) We can conclude:




![image](https://user-images.githubusercontent.com/83087431/164056577-22300a47-c22b-47e0-a73c-b9da04e4aec3.png)

4.) The entropy becomes: 




![image](https://user-images.githubusercontent.com/83087431/164056631-59d1cad1-d9b8-496d-99b4-1e79f2a93364.png)

5.) We can change the fractions to: 





![image](https://user-images.githubusercontent.com/83087431/164056831-215efbcc-2d0a-43f2-9bf4-b1683642903d.png)




**Below are different metrics like precision,accuracy etc. for each algorithm**

**Also we are doing different types of tests like accuracy on training data, accuracy on testing data etc.**

![image](https://user-images.githubusercontent.com/83087431/164058036-7d6c4a40-95e3-4427-b839-0e6e127545ad.png)

The below peaks are due to errors in the data: 
![image](https://user-images.githubusercontent.com/83087431/164058126-d48b559a-27e5-45b3-bb87-71f9d67427d1.png)


![image](https://user-images.githubusercontent.com/83087431/164058259-5c3e30fe-eb3f-4cfd-b82b-ae89c454be10.png)



![image](https://user-images.githubusercontent.com/83087431/164058303-be1879e4-0fac-4ca0-8a3c-3749a840a12a.png)


![image](https://user-images.githubusercontent.com/83087431/164058407-d8cc66a4-bee2-441f-babe-7eb5fa3c36d7.png)


![image](https://user-images.githubusercontent.com/83087431/164058432-b208325f-4d41-4ab3-b782-6431d1bc4de2.png)


**Below is a comparison of accuracy between different implementations from different teams**




**the other team members were: @Tasos Toumazatos,@eGkritsis,@Georgios E. Syros**





![image](https://user-images.githubusercontent.com/83087431/164058530-b4c90f37-dc9c-45f4-a559-e44af74dbaec.png)



The commit history is a bit messy due the vast amount of files we needed to upload.
