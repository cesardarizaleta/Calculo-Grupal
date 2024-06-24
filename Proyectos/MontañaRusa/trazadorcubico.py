import api
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

#Funcion que hace el trazado cubico con frontera Sujeta
#Condicion : S(x0) = f´(x0) , S(xn) = f´(xn)
def traza_cubico_(xi,yi):
    tam = len(xi)
    h = np.zeros(tam-1,dtype=float) #Valores para h
    for i in range(0,tam-1,1):
        h[i] = xi[i + 1] - xi[i]
    #Sistema de ecuaciones

    Prim = np.zeros(shape =(tam,tam), dtype=float)
    Seg = np.zeros(tam, dtype= float)
    result = np.zeros(tam,dtype= float)

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
    
    Prim[tam-1,tam-2] = h[tam - 2]
    Prim[tam - 1, tam - 1] = 2*h[tam - 2] #Condicion de forntera Sujeta
    Seg[tam - 1] = 3*(yi[tam - 1] - yi[tam - 2])/h[tam - 2] # Condicion de forntera Sujeta

    #Resolucion del sistema de ecuaciones

    resolvi = np.linalg.solve(Prim,Seg)
    for k in range(0,tam,1):
        result[k] = resolvi[k]

    #Calculo de los coeficientes

    a = np.zeros(tam - 1,dtype=float)
    b = np.zeros(tam - 1,dtype= float)
    c = np.zeros(tam - 1, dtype= float)
    d = np.zeros(tam - 1,dtype=float)

    for i in range(0,tam-1):
        a[i] = (result[i + 1] - result[i])/(6*h[i])
        b[i] = result[i] / 2
        pend10 = (yi[i + 1] - yi[i])/ h[i]
        c[i] = pend10 - (2*h[i]*result[i] + h[i]*result[i + 1])/6
        d[i] = yi[i]
    
    #Tabla de los valores del polinomio

    X = sym.symbols("x")
    tabla = []
    for i in range(0,tam-1):
        poli = a[i] * (X-xi[i])**3 + b[i] * (X-xi[i])**2
        poli = poli + c[i] * (X-xi[i]) + d[i]
        poli = poli.expand()
        tabla.append(poli)
    return tabla

#Funcion que grafica el trazador cubico con frontera sujeta
def Grafica_Cubico(xi,yi,tabla,muestra):
    n = len(xi)
    trazaX = np.array([])
    trazaY = np.array([])
    tramo = 1
    while tramo < n:
        a = xi[tramo -1]
        b = xi[tramo]
        tramX = np.linspace(a,b,muestra)
        #Evalacion del polinimo en el tramo

        evaTramo = tabla[tramo - 1]
        evaxt = sym.lambdify("x",evaTramo)
        tramY = evaxt(tramX)
    
        #Vectores para el trazado en x, y

        trazaX = np.concatenate((trazaX,tramX))
        trazaY = np.concatenate((trazaY,tramY))
        tramo += 1
    
    #Grafica del polinomio
    plt.plot(xi,yi, "o", label="Puntos")
    plt.plot(trazaX,trazaY, label= "Trazador", color="Blue")
    plt.title("Trazador Cúbico con Frontera Sujeta")
    plt.xlabel("xi")
    plt.ylabel("p[xi]")
    plt.show()


#Extrayendo datos de api
x,y = api.datos1()

x = x.strip('][').split(',')
for i in range(len(x)): x[i] = float(x[i])

y = y.strip('][').split(',')
for i in range(len(x)): y[i] = float(y[i])

tabla = traza_cubico_(x,y)
muestra = 100
Grafica_Cubico(x,y,tabla,muestra)