# Moscow-Ring-Road-distance
Tesk test from Neuro.net 


## possible access routes:

1 - /map -> arguments = latitude, longitude
map rendering to show distance and locations
Exemplo = http://127.0.0.1:5000/map?latitude=-21.2456183099897&longitude=-46.8316139723902447

2 - /distance -> arguments = latitude, longitude

returns in json format distance and coordinates

Exemplo = http://127.0.0.1:5000/distance?latitude=-21.2456183099897&longitude=-46.8316139723902447

![info_json](https://user-images.githubusercontent.com/37180859/127592534-d808a6a6-c3bb-4149-8137-a1bd34277c72.png)


2 - /distance -> arguments = latitude, longitude
error messages and possible causes
Exemplo = http://127.0.0.1:5000/distance?latitude=-21.2456183099897&longitude=-46.8316139723902447

## Debug
addition of debug for better visualization of the application outputs

## Logger file
log file containing information of the session accessed and requests
