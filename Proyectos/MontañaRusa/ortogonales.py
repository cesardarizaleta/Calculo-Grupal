import requests
import numpy as np 
import scipy as sp
import sympy 

url = "https://mountain-api1.p.rapidapi.com/api/mountains"


headers = {
	"x-rapidapi-key": "b3c1599eeamsh15f5406714c8819p11548bjsn28eb8925c3bc",
	"x-rapidapi-host": "mountain-api1.p.rapidapi.com"
}

#response = requests.get(url, headers=headers)

#Nos retorna un vector con todos los elementos
#Con un ciclo podemos recoger todos los elementos

def rodrigues(x,n):
    