from getopt import getopt
import sys ,getopt
'''
Argument list should be 
Percentage of training data, approximate logs, number of vocab words, approximate logs inside id3
'''
if len(sys.argv) == 5:     
    
    per = float(sys.argv[1])/100
    approximate_logs = sys.argv[2] == "True"
    number_of_vocab_words = int(sys.argv[3])
    approximate_logs_inside_id3 = sys.argv[4] == "True"
    '''
    per = 0.01
    approximate_logs = True
    number_of_vocab_words = 70
    '''
    
    
    
    
    
print("The percentage used will be: " + str(per))
print("Will the logs be approximated: " + str(approximate_logs_inside_id3))
print("The number of vocabulary keys: " + str(number_of_vocab_words))
print("Will the file be the approximate_logs file: " + str(approximate_logs))