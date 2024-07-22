#Importando Librerias Necesarias
import pandas as pd
import matplotlib.pyplot as plt

#Asignando el model y filtrando las primeras lineas
model = pd.read_csv("Proyectos/Pandas/model.txt", delim_whitespace=True, skiprows = 3,parse_dates = {'Timestamp': [0, 1]}, index_col = 'Timestamp')

model['month'] = model.index.month
model['year'] = model.index.year

monthly = model.groupby(by=['year', 'month']).mean()

#Imprimiendolo
monthly.loc[:, 'M(m/s)'].reset_index().pivot(index='year', columns='month')
print(monthly)

#Graficando
monthly.loc[:, 'M(m/s)'].reset_index().pivot(index='year', columns='month').T.loc['M(m/s)'].plot(figsize=(15, 5), legend=False)
plt.show()