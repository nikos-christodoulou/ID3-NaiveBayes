from getopt import getopt
import sys ,getopt
'''
Argument list should be 
Percentage of training data, approximate logs, number of vocab words, approximate logs inside id3
'''
if len(sys.argv) == 4:     
    
    per = float(sys.argv[1])/100
    approximate_logs = sys.argv[2] == "True"
    number_of_vocab_words = int(sys.argv[3])
    '''
    per = 0.58
    approximate_logs = False
    number_of_vocab_words = 70
    approximate_logs_inside_id3 = True
    '''
    
    
    
    
    
    
print("The percentage used will be: " + str(per))
print("The number of vocabulary keys: " + str(number_of_vocab_words))
print("Will the file be the approximate_logs file: " + str(approximate_logs))