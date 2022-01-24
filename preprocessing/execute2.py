import subprocess
import time
b = [False]


for z in b:
    '''
    for x in range(26,101):
            for y in range(10,110,10):
                start = time.time()
                subprocess.call("python C:/Users/Nikos/Documents/GitHub/Aiexercise2/preprocessing/create_files.py " + str(x) + " " + str(z) + " " + str(y), shell=True)
                '''
    for x in range(36,101):
        if(x == 29 or x == 57 or x == 58):
            for y in range(10,110,10):
                start = time.time()
                subprocess.call("python C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/preprocessing/create_files2.py " + str(x) + " " + str(z) + " " + str(y), shell=True)
                print(time.time() - start)
        

