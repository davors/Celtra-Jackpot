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
    filename = os.path.basename(__file__) + '_' + (time.strftime("%Y_%m_%d_%H_%M_%S")) + '.txt'
    #bufsize = 0
        # 0 - buffering disabled
        # 1 - line buffering
        # not defined - takes default OS value
    #file = open(filename, 'w', bufsize)
    file = open(filename, 'w')
    sys.stdout = PrintBothFileAndTerminal(sys.stdout, file)

