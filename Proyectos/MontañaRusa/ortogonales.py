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
    
x, y = api.datos1()

x = x.strip('][').split(',')
for i in range(len(x)): x[i] = float(x[i])

y = y.strip('][').split(',')
for i in range(len(y)): y[i] = float(y[i])

print(x)
print(y)

n = 3

# Evaluar rodrigues en cada punto del intervalo
y_intervalo = [rodrigues(n, xi) for xi in x]

# Graficar
plt.plot(x, y_intervalo)
plt.show()
