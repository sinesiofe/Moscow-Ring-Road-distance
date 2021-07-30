import requests
import Log


teste = requests.get('http://127.0.0.1:5000/distance?latitude=-23.5590978735167&longitude=-46.69035826202447')
print_ = Log.Log_start(True)
info  = teste.json()
print_.Log("Start location: ",info['location'])
print_.Log("To: ",info['Latitude'], info['Longitude'])
print_.Log("Distance: ", info['location'])

# Testing without some parameters
try:
    teste = requests.get('http://127.0.0.1:5000/distance?latitude=520')
except:
    pass
print_.Log(teste.content)


# Testing without some parameters
try:
    print("Using diferent route")
    teste = requests.get('http://127.0.0.1:5000/distance/xx')

except:
    pass
print_.Log(teste.content)