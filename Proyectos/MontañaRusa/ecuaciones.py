import api
import numpy as np
from scipy.linalg import solve

#Extrayendo datos de la api
a,b = api.datos4()

b = b.strip('][').split(',')
for i in range(len(b)): b[i] = int(b[i])

a = a.strip('[]')
filas = a.split('],[')
a = []
for f in filas: a.append([int(x) for x in f.split(',')])

#Convirtiendo matriz y vector a array de numpy
a = np.array(a,dtype=float)
b = np.array(b,dtype=float)

#Funcion de eliminacion por gauss
def gauss(A, b):
    n = len(b)
    Ab = np.hstack([A, b.reshape(-1, 1)]) #Matriz aumentada en forma A|B
    
    for i in range(n):
        filaMayor = np.argmax(np.abs(Ab[i:, i])) + i
        Ab[[i, filaMayor]] = Ab[[filaMayor, i]]
        if Ab[i, i] == 0:
            raise ValueError("La matriz es singular y no puede resolverse por eliminación de Gauss.")
        for j in range(i + 1, n):
            r = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= r * Ab[i, i:]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i + 1:n], x[i + 1:n])) / Ab[i, i]
    return x.tolist()

#Imprimiendo resultados para comparar
print("Solución x:")
print("Con funcion solve:",solve(a,b).tolist())
print("Con gauss:",gauss(a,b))