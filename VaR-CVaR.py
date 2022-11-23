import numpy as np
import pandas as pd
import matplotlib as mpl
import scipy
import importlib
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, chi2
from pandas_datareader import data as wb
import datetime as dt 
from datetime import date
from pylab import * # Importamos todas las funciones de pylab

# ----------- Valor en riesgo y valor en riesgo condicional --------------
# ----------------------------VaR y CVaR ---------------------------------


# Descargamos los datos de Yahoo:
start = dt.datetime(2015, 1, 1)
end = date.today()


# Elegimos los equity que necesitamos:
tickers = ['GC=F']

for ticker in tickers:
    data = wb.DataReader(ticker, 'yahoo', start, end)
    # data.to_csv('{}.csv'.format(ticker))

# Visualizamos y trabajamos con los datos: 
data.tail(5)
close_eqty = data['Close']

plt.plot(close_eqty)
plt.show()

# Calculo de retornos
ret_eqty = np.log(close_eqty) - np.log(close_eqty.shift(1))
ret_eqty_1 = ret_eqty.dropna()

# Verificamos que no tengamos datos nulos
ret_eqty_1.isnull().sum()

plt.plot(ret_eqty_1)
plt.show()

#Valor en riesgo ---------------------------------------------------------
var_per = 5
var_95 = np.percentile(ret_eqty_1, var_per)
var_95

# Valor en riesgo condicional --------------------------------------------
cvar_95 = ret_eqty_1[ret_eqty <= var_95].mean()
cvar_95

plt.plot(ret_eqty_1)

axhline(var_95, color = 'g', xmax = 1)
axhline(cvar_95, color = 'r', xmax = 1)
plt.show()

