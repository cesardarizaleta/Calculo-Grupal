import api
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

#Funcion que hace el trazado cubico con frontera Sujeta
#Condicion : S(x0) = f´(x0) , S(xn) = f´(xn)
def traza_cubico_(xi,yi):
    tam = len(xi)
    h = np.zeros(tam-1,dtype=float) #Valores para h
    for i in range(0,tam,1):
        h[i] = xi[i + 1] - xi[i]
    #Sistema de ecuaciones

    Prim = np.zeros(shape =(tam,tam), dtype=float)
    Seg = np.array(tam, dtype= float)
    result = np.array(tam,dtype= float)

    Prim[0,0] = 2*h[0]
    Prim[0,1] = h[0]
    Seg[0] = 3*(yi[1] - yi[0])/h[0]

    #Primera derivadas
    for j in range(0,tam-1,1):
        Prim[j,j-1] = h[j-1]
        Prim[j,j] = 2*(h[j-1] + h[j])
        Prim[j, j + 1] = h[j]
        pend21 = (yi[j + 1] - yi[j])/h[j]
        pend10 = (yi[j] - yi[j - 1])/ h[j-1]
        Seg[j] = 3*(pend21 - pend10)
    
    

#Extrayendo datos de api
x,y = api.datos1()

x = x.strip('][').split(',')
for i in range(len(x)): x[i] = float(x[i])

y = y.strip('][').split(',')
for i in range(len(x)): y[i] = float(y[i])

#Imprimiendo datos a usar
print(x)
print(y)