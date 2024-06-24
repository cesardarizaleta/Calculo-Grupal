import numpy as np 
import math
import sympy as sy
import matplotlib.pyplot as plt
import api

#Metodo para derivar enesimamente
def derivar(n,expresion,x=sy.symbols("x")):
    for i in range(0,n):
        expresion = sy.diff(expresion,x)
    return expresion

#Metodo rodrigues para realizar legendre
def rodrigues(n,xi):
    x = sy.symbols('x')
    rodri = (1/((2**n) * math.factorial(n))) * derivar(n,(x**2 - 1)**n)
    #Evalf evalua la funcion de rodri
    return rodri.evalf(subs={x: xi})

#Metodo hermite
def hermite(n,xi):
    x = sy.symbols('x')
    h = ((-1)**n)*(math.e**((x**2)/2))*derivar(n,(math.e**((-x**2)/2)))
    return h.evalf(subs={x: xi})
    
x, y = api.datos1()

x = x.strip('][').split(',')
for i in range(len(x)): x[i] = float(x[i])

y = y.strip('][').split(',')
for i in range(len(y)): y[i] = float(y[i])

n = 2  # orden del polinomio
plt.plot(x,y)

#Polinomio Rodrigues
#Dominio de Lagendre es [-1,1]
#x = np.linspace(-1,1, 100)
#y = [rodrigues(n,xi) for xi in x]

#for i in range(0,len(x)-1):
    #intervalo = np.linspace(x[i],x[i+1], 10)
    #y = [hermite(n,xi) for xi in intervalo]
    #plt.plot(intervalo,y)
    #pass

#plt.plot([hermite(n,xi) for xi in x])

#x = np.linspace(-4,6, 100)
#y = [hermite(n,xi) for xi in x]

#plt.plot(x,y)
plt.show()
