from hyperparameters import number_of_vocab_words,approximate_logs,per,type_of_test
import os 
per = per * 100 
per = round(per)
if(type_of_test == "test_examples"):
    from naive_bayes import accuracy,pres,rec,f_measure
    print("Writing per,accur, for train" + str(per) + " on testing data set in file")
    file_name = str(int(number_of_vocab_words)) + "_" + str(approximate_logs) +  ".txt"
    file_path = os.path.join("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/per_accur_pres_rec_f_Bayes",file_name)
    if not os.path.exists("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/per_accur_pres_rec_f_Bayes" + "/"):
        os.makedirs("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/per_accur_pres_rec_f_Bayes" + "/")
    with open(file_name,"a") as f:
        f.write(str(per) + "," + str(accuracy) + "," + str(pres) + "," + str(rec) + "," + str(number_of_vocab_words) + "\n")
elif(type_of_test == "same_percentage"):
    from naive_bayes import error_train,error_test
    print("Writing error rate for the same percentage of training data set and testing data set")
    file_name =  str(int(number_of_vocab_words)) + ".txt"
    file_path = os.path.join("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ErrorTrain_ErrorTest_Bayes" + "/",file_name)
    if not os.path.exists("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ErrorTrain_ErrorTest_Bayes" + "/"):
        os.makedirs("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ErrorTrain_ErrorTest_Bayes" + "/")
    with open(file_name,"a") as f:
        f.write(str(per) + " " + str(error_train) + " " + str(error_test) + "\n")
else:
    from naive_bayes import accuracy
    print("Writing accuracy for train data on training data set in file")
    file_name =  str(int(number_of_vocab_words)) + ".txt"
    file_path = os.path.join("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/Accuracy_on_Training_data_Bayes",file_name)
    if not os.path.exists("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/Accuracy_on_Training_data_Bayes"):
        os.makedirs("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/Accuracy_on_Training_data_Bayes")
    with open(file_name,"a") as f:
        f.write(str(per) + " " + str(accuracy) + "\n")