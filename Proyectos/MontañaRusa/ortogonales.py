import numpy as np 
import math
import sympy as sy
import matplotlib.pyplot as plt

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
    
#-1 y 1 Son los intervalos, en el caso de la M.R hay que pasarle los puntos de control
x = np.linspace(-1, 1, 400)
n = 5  # orden del polinomio

#Evaluar rodrigues en cada punto del intervalo
y = [rodrigues(n,xi) for xi in x]

#Graficar
plt.plot(x, y)
plt.title(f"Polinomio de Legendre de orden {n}")
plt.xlabel("x")
plt.ylabel("Pn(x)")
plt.show()
    