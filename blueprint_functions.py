#----------------------------------------------------------------------------
#	@file : blueprint_functions.py
#	@class: blueprint

#	@brief: 
# 	blueprint functions

#	@author: Sinesio Fellippe Soares <sinesiofe@gmail.com>
# 	@date  : 07/23/2021
#----------------------------------------------------------------------------

from flask import Blueprint, request, render_template, jsonify, render_template, make_response
import numpy as np
import math
from .Log import Log_start #Library to debug code
from .logger  import save_log #library to generate log file
import json

# starting variables
Bp_erros = Blueprint('errors', __name__)
example_blueprint = Blueprint('example_blueprint', __name__)
formulario = Blueprint('/', __name__)
save_info = save_log()
Log_shell = Log_start(True)


@formulario.route('/', methods = ['GET', 'POST'])
def index():
    """render the command interface"""

    save_info.write_line('starting application')

    return """ <form method = "POST>
                <br>
                <H1> Distance <H1>
                <div><label><input type="text" name = "Latitude"></label></div><br>
                <div><label> Latitude:   <input type="text" name = "Longitude"></label></div>
                <div><label> Longitude:<input type="text" name = "Longitude"></label></div>
                <input type = "submit" value = "Submit">"""

@example_blueprint.route('/distance')
def index():
    """ Main funciton will get values and make the calculos 
    to find the distance between Moscow road ring to another place"""
    
    try: 
        lat = request.args.get('latitude')
        lon = request.args.get('longitude')
        save_info.write_line(f"Request: latutude = {lat} - Longitude = {lon}")
        Log_shell.Log(f"Request: latutude = {lat} - Longitude = {lon}")
        
    except:
        save_info.write_line('Error getting lat and log data: {0} - {1}'.format(lat, lon))
        Log_shell.Error('Error getting lat and log data: {0} - {1}'.format(lat, lon))

    if lat == None or lon == None:

        result = f"<h1> Invalid values for the paramters<h1><br><h2> latitude: {lat}<h2> <br> <h2> longitude: {lon}<h2>"
        save_info.write_line(f"Invalid values for the paramters: latitude: {lat} - longitude: {lon}")
        Log_shell.Error(f"Invalid values for the paramters: latitude: {lat} - longitude: {lon}")
        
        return result
    
    if lat == '' or lon == '':

        save_info.write_line("values  empty for the paramters")
        Log_shell.Error("values  empty for the paramters")

        return f"<h1> values  empty for the paramters<h1><br><h2> latitude: {lat}<h2> <br> <h2> longitude: {lon}<h2>"

    reference_latitude = 55.691076617416506
    reference_longitude = 37.41297341861867

    #Distance using inputs coordinates
    dist_MtoLocation = distance(reference_latitude, float(lat), reference_longitude, float(lon))

    save_info.write_line(f"Distance between = {dist_MtoLocation}")
    Log_shell.Log(f"Distance between = {dist_MtoLocation}")

    info = {"start_point": "Moscou",
            'Finish_point':"teste",
            "Latitude": lat,
            "Longitude": lon, 
            'location': dist_MtoLocation}


    return  jsonify(info)


@example_blueprint.route('/map', methods=["GET", "POST"])
def maps():
    """ Render the map """

    global lat_map, long_map

    lat_map = request.args.get('latitude')
    long_map = request.args.get('longitude')
    Log_shell.Log(f"Request: latutude = {lat_map} - Longitude = {long_map}")

    return render_template("index.html")

@example_blueprint.route('/data_map', methods=["GET", "POST"])
def data_map():
    """ sends the data to create the map containing requested information """

    reference_latitude = 55.691076617416506
    reference_longitude = 37.41297341861867      

    dist_MtoLocation = distance(reference_latitude, float(lat_map), reference_longitude, float(long_map))

    save_info.write_line(f"Distance between = {dist_MtoLocation}")
    Log_shell.Log(f"Distance between = {dist_MtoLocation}")  

    if dist_MtoLocation < 1000:
        zoom = 20
    else:
        zoom = 2
    
    response = make_response(json.dumps([reference_latitude, reference_longitude, float(lat_map), float(long_map), zoom, dist_MtoLocation]))

    response.content_type = 'application/json'
    
    return response

#Error codes

@Bp_erros.errorhandler(404)
def page_not_found(error):
    return "<h1>Sorry, but this route dont exist.<h1><br>try /distance", 404

@Bp_erros.errorhandler(500)
def page_not_found(error):
    return "<h1>Sorry, but this route dont exist.<h1><br>try /distance", 500

def distance(lat1, lat2, long1, long2):
    """ using Haversine formula to calcule the distance """

    R = 6356.752
  
    dlat = (lat2 * np.pi/180) - (lat1 * np.pi/180 )
    dlong = (long2 * np.pi/180) - (long1 * np.pi/180 )
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(lat1 * math.pi/180) * math.cos(lat2 * math.pi/180) * math.sin(dlong/2) *math.sin(dlong/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d * 1000

