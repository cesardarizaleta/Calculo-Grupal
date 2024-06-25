import numpy as np 
import math
import sympy as sy
import matplotlib.pyplot as plt
import api


#Recoleccion de Datos de la Api
x, y = api.datos1()

x = x.strip('][').split(',')
for i in range(len(x)): x[i] = float(x[i])

y = y.strip('][').split(',')
for i in range(len(y)): y[i] = float(y[i])
#Datos:
#x = np.array([0, 1, 2, 3, 4, 5])
#y = np.array([0.5, 0.8, 1.0, 0.9, 1.2, 0.7])

print(x,y)

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


n = 2  # orden del polinomio

#plt.plot(x,y)
plt.show()
