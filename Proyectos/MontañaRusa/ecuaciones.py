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