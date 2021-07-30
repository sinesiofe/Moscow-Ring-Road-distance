#----------------------------------------------------------------------------
#	@file : log.py
#	@class: Log_start

#	@brief: 
# 	debug library

#	@author: Sinesio Fellippe Soares <sinesiofe@gmail.com>
# 	@date  : 07/23/2021
#----------------------------------------------------------------------------

import time
import os

class Log_start():

    def __init__(self,Use = False):
        self.__use__= Use
        os.system('cls')
        
        #windowns colors
        self.green        = '\u001b[32m'
        self.Default      = "\u001b[37m"
        self.Yellow       = "\u001b[33;1m"
        self.Red          = "\u001b[31;1m"

        # linux colors 
        #self.green        = '\033[92m'
        #self.Default      = "\033[39m"
        #self.Yellow       = "\033[33m"
        #self.Red          = "\033[31m"
        
        


    def Log(self, argument):

        self.data_time = time.localtime()
        self.real_time = time.strftime("%H:%M:%S", self.data_time)

        if self.__use__ == True:
            print(self.green + '['+ self.real_time +'] '+self.Default +str( argument))    

    def Warning_(self, argument):

        self.data_time = time.localtime()
        self.real_time = time.strftime("%H:%M:%S", self.data_time)

        if self.__use__ == True:
            print(self.Yellow + '['+ self.real_time +'] '+self.Default + argument) 

    def Error(self, argument):

        self.data_time = time.localtime()
        self.real_time = time.strftime("%H:%M:%S", self.data_time)
        
        if self.__use__ == True:
            print(self.Red + '['+ self.real_time +'] '+self.Default + argument)