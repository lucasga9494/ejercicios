import requests
import matplotlib.pyplot as plt 
import matplotlib.image as img 

pokemon=input("Que pokemon queres ver?: ")
url="https://pokeapi.co/api/v2/pokemon/" +pokemon
res=requests.get(url)

if res.status_code!= 200:
    print("No se ha encontrado ningun pokemon. ")
    exit()

imagen=  img.imread(res.json()['sprites']['front_default'])
plt.title(res.json()['name'])
imgplot = plt.imshow(imagen) 
plt.show()
