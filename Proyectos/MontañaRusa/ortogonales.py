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

#-1 y 1 Son los intervalos, en el caso de la M.R hay que pasarle los puntos de control
#x = np.linspace(x[0], x[1], 400)
n = 5  # orden del polinomio
plt.plot(x,y, marker="o")
inter = np.linspace(0,1, 100)
y = [rodrigues(n,xi) for xi in x]
#plt.plot(x,y)

for i in range(0,len(x)-1):
    inter = np.linspace(x[i], x[i+1], 100)
    y = [rodrigues(n,xi) for xi in x]
    #plt.plot(x,y)

#Evaluar rodrigues en cada punto del intervalo
#y = [rodrigues(n,xi) for xi in x]

# Graficar

plt.show()
