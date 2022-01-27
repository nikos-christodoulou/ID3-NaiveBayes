from getopt import getopt
import sys
'''
Argument list should be 
Percentage of training data, approximate logs, number of vocab words, 
'''

if len(sys.argv) == 1: 
    '''
    per = float(sys.argv[1])/100
    approximate_logs = sys.argv[2] == "True"
    number_of_vocab_words = int(sys.argv[3])
    type_of_test = sys.argv[4]
    '''
    per = 5/100 
    approximate_logs = False
    number_of_vocab_words = 10
    type_of_test = "test_examples"
    
    
print("The percentage used will be: " + str(per))
print("Will the file be the approximate log file: " + str(approximate_logs))
print("The number of vocabulary keys: " + str(number_of_vocab_words))
print("The type of test will be: " + type_of_test)