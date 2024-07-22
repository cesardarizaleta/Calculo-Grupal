#Importando Librerias Necesarias
import pandas as pd
import matplotlib.pyplot as plt

#Asignando el model y filtrando las primeras lineas
model = pd.read_csv("Proyectos/Pandas/model.txt", delim_whitespace=True, skiprows = 3,parse_dates = {'Timestamp': [0, 1]}, index_col = 'Timestamp')

pd.plotting.scatter_matrix(model.loc[model.sort_values('M(m/s)', ascending=False).index[:1000],'M(m/s)':'D(deg)'])
plt.show()