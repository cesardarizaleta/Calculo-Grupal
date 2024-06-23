import api
#SI NO FUNCIONA CORRE EL ARCHIVO DE API PRIMERO
#Extrayendo datos de api
x,y = api.datos1()

x = x.strip('][').split(',')
for i in range(len(x)): x[i] = float(x[i])

y = y.strip('][').split(',')
for i in range(len(x)): y[i] = float(y[i])

#Imprimiendo datos a usar
print(x)
print(y)