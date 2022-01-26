import subprocess
import time 
b =  [True,False]
ap = ["train"]
for z in b: 
         for x in range(1,101):
            for y in range(10,110,10):
                    start = time.time()
                    subprocess.call("python C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ID3/gather_data.py " + str(x) + " " + str(z) + " " + str(y) + " " + str(ap), shell=True)
                    print(time.time() - start)