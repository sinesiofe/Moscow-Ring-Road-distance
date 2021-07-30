import time 
#----------------------------------------------------------------------------
#	@file : logger.py
#	@class: main

#	@brief: 
# 	file generator with interaction information.

#	@author: Sinesio Fellippe Soares <sinesiofe@gmail.com>
# 	@date  : 07/23/2021
#----------------------------------------------------------------------------

class save_log:

    def __init__(self):

        self.log_name_ = "Log_files/" + str(int(time.time())) + '_Webinfo' +".log"
        self.log = open(self.log_name_, "w")
        
    def write_line(self,argument):

        self.data_time = time.localtime()
        self.real_time = time.strftime("%H:%M:%S", self.data_time)
        
        self.log.write('['+ self.real_time +'] - ' + str(argument) + '\n')
        self.log.flush()

    def close_file(self):

        self.log.close()
