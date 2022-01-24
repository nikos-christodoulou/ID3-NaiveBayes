import subprocess
import time 
b =  [True,False]
ap = [True,False]
for z in b: 
    for p in ap:  
         for x in range(1,101):
            for y in range(10,110,10):
                if(x != 29 and x != 57 and x != 58):
                    start = time.time()
                    subprocess.call("python C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/main_algorithms/predict.py " + str(x) + " " + str(z) + " " + str(y) + " " + str(p), shell=True)
                    print(time.time() - start)