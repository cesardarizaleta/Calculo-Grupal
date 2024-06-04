import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def gauss_seidel(A, B, tol=0.001, max_iter=100):
    n = len(A)
    x = np.zeros(n)
    for _ in range(max_iter):
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i+1, n))
            x_new[i] = (B[i] - s1 - s2) / A[i][i]
        if np.linalg.norm(x_new - x) < tol:
            break
        x = x_new
    return x

# Ejemplo de Uso:
A = np.array([[4, -1, 0], [-1, 4, -1], [0, -1, 4]])
B = np.array([1, 2, 3])
x = gauss_seidel(A, B)
print(x)

lista = x.tolist()
fig = plt.figure()
 
# syntax for 3-D projection
ax = plt.axes(projection ='3d')
 
# defining all 3 axis
 
# plotting
ax.plot3D([0,lista[0]], [0,lista[1]], [0,lista[2]], 'green')
ax.set_title('Vector')
plt.show()