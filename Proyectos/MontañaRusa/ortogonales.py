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

def derivar(n,expresion,x=sy.symbols("x")):
    for i in range(0,n):
        expresion = sy.diff(expresion,x)
    return expresion

def combinatoria(m,n):
    return (math.factorial(m))/(math.factorial(n)*math.factorial(m-n))

def rodrigues(n):
    x = sy.symbols('x')
    #Revisar - Arreglar
    rodri = 1/(2**n * math.factorial(n)) * derivar(n,(x**2 - 1)**n)
    print(rodri)
    
def explicita(n):
    

rodrigues(3)
    