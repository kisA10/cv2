# -*- coding: utf-8 -*-
import sys
from time import time

class TestTimer:

    def __init__(self):
        self.startTime = 0
        self.stopTime = 0

    def start(self):
        self.startTime = time()

    def stop(self):
        if self.startTime == 0:
            print ("First call start()!!!")
            sys.exit()

        self.stopTime = time()

    def reset(self):
        self.startTime = 0
        self.stopTime = 0

    def printTime(self):
        if not self.startTime is None and self.stopTime is None:
            print ("call stop()!!!")
            sys.exit()

        else:
            processingTime = self.stopTime - self.startTime

        print ("Time:{0}".format(processingTime))