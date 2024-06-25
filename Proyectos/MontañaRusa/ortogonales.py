import numpy as np
import matplotlib.pyplot as plt

# Función de Legendre
def l(n, x):  
    if n == 0:  
        return 1  
    elif n == 1:  
        return x  
    else:  
        return ((2*n-1)*x*l(n-1, x) - (n-1)*l(n-2, x)) / n  

# Datos
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([0.5, 0.8, 1.0, 0.9, 1.2, 0.7])

# Grado del polinomio
grado = 7

# Crear matriz de polinomios de Legendre
A = np.zeros((len(x_data), grado + 1))
for i in range(grado + 1):
    A[:, i] = np.array([l(i, x) for x in x_data])

# Encontrar coeficientes que mejor se ajustan a los datos
#Cabe Recalcar que rcond es porque si no lo colocas salta un warning
coeficientes = np.linalg.lstsq(A, y_data, rcond=None)[0]
print(coeficientes)

# Calcular valores para graficar la curva ajustada
x_plot = np.linspace(x_data.min(), x_data.max(), 100)
y_plot = np.zeros(len(x_plot))
for i in range(grado + 1):
    y_plot += coeficientes[i] * np.array([l(i, x) for x in x_plot])

# Graficar
plt.plot(x_plot, y_plot)
plt.scatter(x_data, y_data)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Ajuste de Polinomio de Legendre')
plt.show()