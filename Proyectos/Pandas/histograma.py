#Importando Librerias Necesarias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Asignando el model y filtrando las primeras lineas
model = pd.read_csv("Proyectos/Pandas/model.txt", delim_whitespace=True, skiprows = 3,parse_dates = {'Timestamp': [0, 1]}, index_col = 'Timestamp')

model.loc[:, 'M(m/s)'].plot.hist(bins=np.arange(0, 35))
plt.show()