import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib as mpl

from IPython.display import display

model = pd.read_csv("model.txt", delim_whitespace=True, skiprows = 3,parse_dates = {'Timestamp': [0, 1]}, index_col = 'Timestamp')

pd.tools.plotting.scatter_matrix(model.loc[model.index[:1000], 'M(m/s)':'D(deg)'])