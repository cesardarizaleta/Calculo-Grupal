#Importando Librerias Necesarias
import pandas as pd
import matplotlib.pyplot as plt

#Asignando el model y filtrando las primeras lineas
model = pd.read_csv("Proyectos/Pandas/model.txt", delim_whitespace=True, skiprows = 3,parse_dates = {'Timestamp': [0, 1]}, index_col = 'Timestamp')

model['month'] = model.index.month
model['year'] = model.index.year

#Imprimiendo tabla
print(model.groupby(by = ['year', 'month']).mean().head(24))

model.groupby(by=['year', 'month']).mean().plot(y='M(m/s)', figsize=(15, 5))
plt.show()