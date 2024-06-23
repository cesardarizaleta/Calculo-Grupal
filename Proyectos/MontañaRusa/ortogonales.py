import requests
import numpy as np 
import math
import sympy as sy

#url = "https://mountain-api1.p.rapidapi.com/api/mountains"


headers = {
	"x-rapidapi-key": "b3c1599eeamsh15f5406714c8819p11548bjsn28eb8925c3bc",
	"x-rapidapi-host": "mountain-api1.p.rapidapi.com"
}

#response = requests.get(url, headers=headers)

#Nos retorna un vector con todos los elementos
#Con un ciclo podemos recoger todos los elementos

def derivar(n,expresion):
    for i in range(0,n):
        expresion = sy.diff(expresion)
    return expresion

def rodrigues(n):
    x = sy.symbols('x')
    rodri = 1/math.factorial(n) * derivar(n,(x**2 - 1)**n)
    print(rodri)

rodrigues(3)
    