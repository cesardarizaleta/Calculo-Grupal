import numpy as np 
import math
import sympy as sy
import matplotlib.pyplot as plt

def derivar(n,expresion,x=sy.symbols("x")):
    for i in range(0,n):
        expresion = sy.diff(expresion,x)
    return expresion

def rodrigues(n,xi):
    x = sy.symbols('x')
    rodri = (1/((2**n) * math.factorial(n))) * derivar(n,(x**2 - 1)**n)
    return rodri.evalf(subs={x: xi})
    

x = np.linspace(-1, 1, 400)
n = 5  # orden del polinomio

y = [rodrigues(n,xi) for xi in x]

plt.plot(x, y)
plt.title(f"Polinomio de Legendre de orden {n}")
plt.xlabel("x")
plt.ylabel("Pn(x)")
plt.show()
    