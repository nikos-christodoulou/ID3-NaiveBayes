from hyperparameters import number_of_vocab_words,approximate_logs,per,type_of_test
import os 
per = per * 100 
per = round(per)
if(type_of_test == "test_examples"):
    from predict import accuracy,pres,rec,f_measure
    print("Writing per,accur, for train percentage: " + str(per) + " on testing data set in file")
    file_name = str(int(number_of_vocab_words)) + "_" + str(approximate_logs) +  ".txt"
    file_path = os.path.join("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/per_accur_pres_rec_f_ID3",file_name)
    if not os.path.exists("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/per_accur_pres_rec_f_ID3"):
        os.makedirs("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/per_accur_pres_rec_f_ID3")
    with open(file_name,"a") as f:
        f.write(str(per) + " " + str(accuracy) + " " + str(pres) + " " + str(rec) + " " + str(f_measure) + " " +str(number_of_vocab_words) + "\n")
elif(type_of_test == "same_percentage"):
    from predict import error_train,error_test
    print("Writing error rate for the same percentage of training data set and testing data set")
    file_name =  str(int(number_of_vocab_words)) + ".txt"
    file_path = os.path.join("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ErrorTrain_ErrorTest_ID3" + "/",file_name)
    if not os.path.exists("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ErrorTrain_ErrorTest_ID3" + "/"):
        os.makedirs("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/ErrorTrain_ErrorTest_ID3" + "/")
    with open(file_name,"a") as f:
        f.write(str(per) + " " + str(error_train) + " " + str(error_test) + "\n")
else:
    from predict import accuracy
    print("Writing accuracy for train data on training data set in file")
    file_name =  str(int(number_of_vocab_words)) + ".txt"
    file_path = os.path.join("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/Accuracy_on_Training_data_ID3",file_name)
    if not os.path.exists("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/Accuracy_on_Training_data_ID3"):
        os.makedirs("C:/Users/fotis/OneDrive/Desktop/exer/Aiexercise2/Accuracy_on_Training_data_ID3")
    with open(file_name,"a") as f:
        f.write(str(per) + " " + str(accuracy) + "\n")