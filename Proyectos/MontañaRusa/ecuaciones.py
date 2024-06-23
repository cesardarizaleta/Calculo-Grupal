import api

#Extrayendo datos de la api
a,b = api.datos4()

b = b.strip('][').split(',')
for i in range(len(b)): b[i] = int(b[i])

a = a.strip('[]')
filas = a.split('],[')
a = []
for f in filas: a.append([int(x) for x in f.split(',')])

print(a)
print(b)