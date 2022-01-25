from hyperparameters import number_of_vocab_words,approximate_logs_inside_id3,approximate_logs
import os 
from predict import per,accuracy,precision,recall
per = per * 100 
per = round(per)
file_name = "" + str(int(number_of_vocab_words)) + "_" + str(approximate_logs_inside_id3) + ".txt"
file_path = os.path.join("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/accur_pres_rec_george" + "_" + str(approximate_logs) + "/",file_name)
if not os.path.exists("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/accur_pres_rec_george" + "_" + str(approximate_logs)+ "/"):
    os.makedirs("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/accur_pres_rec_george" + "_" + str(approximate_logs)+ "/")

f = open(file_path,"a")
f.write(str(per) + "," + str(accuracy) + "," + str(precision) + "," + str(recall) + "," + str(number_of_vocab_words) + "\n")
f.close()

file_name = "" + str(int(number_of_vocab_words)) + "_" + str(approximate_logs_inside_id3) + ".txt"
file_path = os.path.join("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/accur_pres_rec" + "_" + str(approximate_logs) + "/",file_name)
if not os.path.exists("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/accur_pres_rec" + "_" + str(approximate_logs) + "/"):
    os.makedirs("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/accur_pres_rec" + "_" + str(approximate_logs) + "/")

f = open(file_path,"a")
f.write(str(per) + " " + str(accuracy) + " " + str(precision) + " " + str(recall) + " " + str(number_of_vocab_words) + "\n")
f.close()