import api

#Extrayendo datos de la api
a,b = api.datos4()
b = b.strip('][').split(',')
for i in range(len(b)): b[i] = int(b[i])