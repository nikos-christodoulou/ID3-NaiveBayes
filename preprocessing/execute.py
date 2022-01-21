import subprocess
import time
b = [True,False]
for z in b:
    for x in range(1,100):
        if(x != 10 and x != 20 and x != 30 and x != 40 and x != 50 and x != 60 and x != 70 and x != 80 and x != 90):
            for y in range(10,110,10):
                start = time.time()
                subprocess.call("python C:/Users/fotis/OneDrive/Desktop/exer2AI/Aiexercise2/preprocessing/create_files.py " + str(x) + " " + str(z) + " " + str(y), shell=True)
                print(time.time() - start)
        else:
            continue