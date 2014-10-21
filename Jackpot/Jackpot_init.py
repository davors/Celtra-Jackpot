from Config import *
import sys
import inspect, os
import time
import random


class PrintBothFileAndTerminal(object):
    def __init__(self, *files):
        self.files = files
    def write(self, obj):
        for f in self.files:
            f.write(obj)
    def flush(self):
        for f in self.files:
            f.flush()


##-- initialization code

random.seed()

#reprint all output to file
if REPRINT_TO_FILE == 1:
    
    # get name of script (without path)
    if REPRINT_FILENAME_FORMAT == 0 :
        filename = os.path.basename(__file__)

    elif REPRINT_FILENAME_FORMAT > 0 :
        #get name of the directory the script was run from (or one of the directories above)
        stringNames = (os.path.dirname(__file__)).split('\\')
        filename = stringNames[len(stringNames)-REPRINT_FILENAME_FORMAT]

    #add timestamp
    filename = 'Reprint___' + filename  + '___' + (time.strftime("%Y_%m_%d_%H_%M_%S")) + '.txt'
    #print os.path.dirname(__file__)

    #bufsize = 0
        # 0 - buffering disabled
        # 1 - line buffering
        # not defined - takes default OS value
    #file = open(filename, 'w', bufsize)
    file = open(filename, 'w')

    sys.stdout = PrintBothFileAndTerminal(sys.stdout, file)

