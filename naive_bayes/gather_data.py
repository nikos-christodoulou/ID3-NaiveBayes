from hyperparameters import number_of_vocab_words,approximate_logs,per,test_train
import os 
per = per * 100 
per = round(per)
if(test_train == "test"):
    from naive_bayes import accuracy,pres,rec,f_measure
    file_name = "" + str(int(number_of_vocab_words)) + "_" + str(approximate_logs) +  ".txt"
    file_path = os.path.join("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/accur_pres_rec_bayes_george" + "/",file_name)
    if not os.path.exists("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/accur_pres_rec_bayes_george" + "/"):
        os.makedirs("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/accur_pres_rec_bayes_george" + "/")
    f = open(file_path,"a")
    f.write(str(per) + "," + str(accuracy) + "," + str(pres) + "," + str(rec) + "," + str(number_of_vocab_words) + "\n")
    f.close()

    file_name = "" + str(int(number_of_vocab_words)) +  "_" + str(approximate_logs) +  ".txt"
    file_path = os.path.join("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/accur_pres_rec_bayes" + "/",file_name)
    if not os.path.exists("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/accur_pres_rec_bayes" + "/"):
        os.makedirs("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/accur_pres_rec_bayes" + "/")

    f = open(file_path,"a")
    f.write(str(per) + " " + str(accuracy) + " " + str(pres) + " " + str(rec) + " " + str(number_of_vocab_words) + "\n")
    f.close()
else:
    from naive_bayes import error_train,error_test
    import os
    file_name =  str(int(number_of_vocab_words)) + ".txt"
    file_path = os.path.join("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/test_train_bayes" + "/",file_name)
    if not os.path.exists("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/test_train_bayes" + "/"):
        os.makedirs("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/test_train_bayes" + "/")

    f = open(file_path,"a")
    f.write(str(per) + " " + str(error_train) + " " + str(error_test) + " " + str(number_of_vocab_words) + "\n")
    f.close() 