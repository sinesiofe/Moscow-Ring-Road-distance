#----------------------------------------------------------------------------
#	@file : app.py
#	@class: main

#	@brief: 
# 	Main function.

#	@author: Sinesio Fellippe Soares <sinesiofe@gmail.com>
# 	@date  : 07/23/2021
#----------------------------------------------------------------------------

import builtins
from .__init__ import Build_app

app = Build_app()
app.run(debug = True)

