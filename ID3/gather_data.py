from hyperparameters import number_of_vocab_words,approximate_logs,test_train,per
import os 
from predict import per,accuracy,precision,recall
per = per * 100 
per = round(per)
if(test_train == "test"):
    file_name = "" + str(int(number_of_vocab_words)) + ".txt"
    file_path = os.path.join("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ID3_george" + "_" + str(approximate_logs) + "/",file_name)
    if not os.path.exists("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ID3_george" + "_" + str(approximate_logs)+ "/"):
        os.makedirs("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ID3_george" + "_" + str(approximate_logs)+ "/")

    f = open(file_path,"a")
    f.write(str(per) + "," + str(accuracy) + "," + str(precision) + "," + str(recall) + "," + str(number_of_vocab_words) + "\n")
    f.close()

    file_name = "" + str(int(number_of_vocab_words)) + ".txt"
    file_path = os.path.join("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ID3" + "_" + str(approximate_logs) + "/",file_name)
    if not os.path.exists("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ID3" + "_" + str(approximate_logs) + "/"):
        os.makedirs("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ID3" + "_" + str(approximate_logs) + "/")

    f = open(file_path,"a")
    f.write(str(per) + " " + str(accuracy) + " " + str(precision) + " " + str(recall) + " " + str(number_of_vocab_words) + "\n")
    f.close()
else:
    file_name_for_per = str(approximate_logs) + "_"
    f = open(file_name_for_per,"a")
    file_path = os.path.join("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ID3_george" + "_" + str(approximate_logs) + "/",file_name_for_per)
    if not os.path.exists("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ID3_george" + "_" + str(approximate_logs)+ "/"):
        os.makedirs("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ID3_george" + "_" + str(approximate_logs)+ "/")
    f.close()
    file_name = str(int(number_of_vocab_words)) + ".txt"
    file_path = os.path.join("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ID3_george" + "_" + str(approximate_logs) + "/",file_name)
    if not os.path.exists("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ID3_george" + "_" + str(approximate_logs)+ "/"):
        os.makedirs("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ID3_george" + "_" + str(approximate_logs)+ "/")

    f = open(file_path,"a")
    f.write(str(per) + "," + str(accuracy) + "," + str(precision) + "," + str(recall) + "," + str(number_of_vocab_words) + "\n")
    f.close()