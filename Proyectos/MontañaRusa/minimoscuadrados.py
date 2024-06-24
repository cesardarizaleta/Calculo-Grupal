import api
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
#Funcion que calcula los coeficiente de la regresion
def calculo_coeficiente(xi,yi):
    coef = np.polyfit(xi,yi,3)
    return coef
x,y = api.datos2()

x = x.strip('][').split(',')
for i in range(len(x)): x[i] = float(x[i])

y = y.strip('][').split(',')
for i in range(len(x)): y[i] = float(y[i])

#Imprimiendo datos a usar
print(x)
print(y)