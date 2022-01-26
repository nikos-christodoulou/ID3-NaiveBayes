from getopt import getopt
import sys ,getopt
'''
Argument list should be 
Percentage of training data, approximate logs, number of vocab words, find the accuracy for the training data 
'''
if len(sys.argv) == 5:     
    
    per = float(sys.argv[1])/100
    approximate_logs = sys.argv[2] == "True"
    number_of_vocab_words = int(sys.argv[3])
    test_train = sys.argv[4]
   
    
    
    
    
    
    
    
print("The percentage used will be: " + str(per))
print("The number of vocabulary keys: " + str(number_of_vocab_words))
print("Will the file be the approximate_logs file: " + str(approximate_logs))