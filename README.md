# Moscow-Ring-Road-distance
Tesk test from Neuro.net 

For the calculation of distance, knowledge already studied about geospatial location was used. Harversine formula was used for calculations

![Captura de tela 2021-07-30 000311](https://user-images.githubusercontent.com/37180859/127593529-67890252-6830-4cfd-959c-3b3ca37d8310.jpg)


## possible access routes:

1 - /map -> arguments = latitude, longitude
map rendering to show distance and locations

Exemple = http://127.0.0.1:5000/map?latitude=-21.2456183099897&longitude=-46.8316139723902447
![map](https://user-images.githubusercontent.com/37180859/127593697-95115176-a866-4f9b-bafc-da38a26bc7b9.png)


2 - /distance -> arguments = latitude, longitude
returns in json format distance and coordinates

Exemple = http://127.0.0.1:5000/distance?latitude=-21.2456183099897&longitude=-46.8316139723902447

![info_json](https://user-images.githubusercontent.com/37180859/127592534-d808a6a6-c3bb-4149-8137-a1bd34277c72.png)


2 - /distance -> arguments = latitude, longitude
error messages and possible causes

Exemple = http://127.0.0.1:5000/distance?latitude=-21.2456183099897&longitude=-46.8316139723902447
![Captura de tela 2021-07-29 235441](https://user-images.githubusercontent.com/37180859/127593289-e4a2c2bb-035d-4224-bb09-3b02f8822a87.jpg)

## Debug
addition of debug for better visualization of the application outputs
![Captura de tela 2021-07-29 234628](https://user-images.githubusercontent.com/37180859/127593294-6d004d85-7e5e-4844-a26b-5de23cff2a9b.jpg)


## Logger file
log file containing information of the session accessed and requests
![Captura de tela 2021-07-29 234554](https://user-images.githubusercontent.com/37180859/127593299-856f132c-bf6a-4e52-ab69-8b2ba69661bd.jpg)
