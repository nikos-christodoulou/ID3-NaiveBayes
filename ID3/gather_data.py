from hyperparameters import number_of_vocab_words,approximate_logs,test_train,per
import os 

per1 = per * 100 
per1 = round(per1)
if(test_train == "test"):
    from predict import per,accuracy,precision,recall
    file_name = "" + str(int(number_of_vocab_words)) + ".txt"
    file_path = os.path.join("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ID3_george" + "_" + str(approximate_logs) + "/",file_name)
    if not os.path.exists("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ID3_george" + "_" + str(approximate_logs)+ "/"):
        os.makedirs("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ID3_george" + "_" + str(approximate_logs)+ "/")

    f = open(file_path,"a")
    f.write(str(per1) + "," + str(accuracy) + "," + str(precision) + "," + str(recall) + "," + str(number_of_vocab_words) + "\n")
    f.close()

    file_name = "" + str(int(number_of_vocab_words)) + ".txt"
    file_path = os.path.join("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ID3" + "_" + str(approximate_logs) + "/",file_name)
    if not os.path.exists("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ID3" + "_" + str(approximate_logs) + "/"):
        os.makedirs("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ID3" + "_" + str(approximate_logs) + "/")

    f = open(file_path,"a")
    f.write(str(per1) + " " + str(accuracy) + " " + str(precision) + " " + str(recall) + " " + str(number_of_vocab_words) + "\n")
    f.close()
else:
    from predict import accuracy

    file_name = str(int(number_of_vocab_words)) + ".txt"
    file_path = os.path.join("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ID3_accur" + "_" + str(approximate_logs) + "/",file_name)
    if not os.path.exists("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ID3_accur" + "_" + str(approximate_logs)+ "/"):
        os.makedirs("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ID3_accur" + "_" + str(approximate_logs)+ "/")

    f = open(file_path,"a")
    f.write(str(per1) + " " + str(accuracy) + "\n")
    f.close()