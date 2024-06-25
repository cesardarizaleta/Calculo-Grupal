import numpy as np
import matplotlib.pyplot as plt

# Función de Legendre
def legendre(n, x):  
    if n == 0:  
        return 1  
    elif n == 1:  
        return x  
    else:  
        return ((2*n-1)*x*legendre(n-1, x) - (n-1)*legendre(n-2, x)) / n  

# Datos
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([0.5, 0.8, 1.0, 0.9, 1.2, 0.7])

# Grado del polinomio
grado = 6

# Crear matriz de polinomios de Legendre
A = np.zeros((len(x_data), grado + 1))
for i in range(grado + 1):
    A[:, i] = np.array([legendre(i, x) for x in x_data])
