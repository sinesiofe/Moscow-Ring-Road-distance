#----------------------------------------------------------------------------
#	@file : __init__.py
#	@def: Build_app

#	@brief: 
# 	blueprint launcher

#	@author: Sinesio Fellippe Soares <sinesiofe@gmail.com>
# 	@date  : 07/23/2021
#----------------------------------------------------------------------------

from flask import Flask
from werkzeug.utils import redirect
from .blueprint_functions import example_blueprint, formulario


def Build_app():


    app = Flask(__name__)


    app.register_blueprint(example_blueprint)

    app.register_blueprint(formulario)

    return app