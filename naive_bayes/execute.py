import subprocess
import time
'''
Check the approximate log file 
'''
approximate_logs = [False,True]
'''
There are three types of tests
'''
types_of_test = ["train_data","test_examples","same_percentage"]
for t in types_of_test:
    for z in approximate_logs:
        if(t == "same_percentage"):
            for x in range(5,101,5):
                    for y in range(10,110,10):
                        start = time.time()
                        subprocess.call("python C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/naive_bayes/gather_data.py " + str(x) + " " + str(z) + " " + str(y) + " " + str(u), shell=True)
                        print(time.time() - start)
        else:
            for x in range(1,101):
                    for y in range(10,110,10):
                        start = time.time()
                        subprocess.call("python C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/naive_bayes/gather_data.py " + str(x) + " " + str(z) + " " + str(y) + " " + str(u), shell=True)
                        print(time.time() - start)