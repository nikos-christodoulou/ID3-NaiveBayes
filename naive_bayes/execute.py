import subprocess
import time
b = [True,False]
data = ["train","test"]
for u in data:
    for z in b:
        for x in range(5,101,5):
                for y in range(10,110,10):
                    start = time.time()
                    subprocess.call("python C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/naive_bayes/gather_data.py " + str(x) + " " + str(z) + " " + str(y) + " " + str(u), shell=True)
                    print(time.time() - start)