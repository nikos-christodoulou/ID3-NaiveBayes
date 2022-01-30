import subprocess
import time


'''
False and true means approximate the logs or not 
'''
b = [False,True]
for z in b:
    for x in range(5,101,5):
            for y in range(10,110,10):
                start = time.time()
                subprocess.call("python C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/preprocessing/create_serial_test_examples.py " + str(x) + " " + str(z) + " " + str(y), shell=True)
                print(time.time() - start)
        