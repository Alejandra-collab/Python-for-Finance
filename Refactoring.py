import numpy as np
import pandas as pd
import matplotlib as mpl
import scipy
import importlib
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, chi2, linregress


# Input
ric = 'DBK.DE'

# Get market data
path = 'C:\\Users\\...' + ric +'.csv'
table_raw = pd.read_csv(path)

# Create table of returns
t = pd.DataFrame()
t['Date'] = pd.to_datetime(table_raw['Date'], dayfirst=False) # Convertir la columna Date a fecha
t['Close'] = table_raw['Close']
t.sort_values(by = 'Date', ascending = True)
t['close_previous'] = table_raw['Close'].shift(1)
t['return_close'] = t['Close']/t['close_previous'] - 1 # Calculando los retornos
t = t.dropna() # Eliminar los Na
t = t.reset_index(drop = True) # Dado que se eliminaron Na's, los índices se modificaron

# Plot timeseries of prices
plt.figure()
plt.plot(t['Date'], t['Close'])
plt.title('Timeseries real prices ' + ric)
plt.show()

# input for Jarque-Bera test
x = t['return_close'].values # Guardamos los retornos como un array of float
x_str = 'Real returns ' + ric # label e.g. ric
x_size = t['return_close'].shape[0] # size of returns

# Compute risk metrics -----------------------------------------------
x_mean = np.mean(x) # Media
x_std = np.std(x) # volatilidad
x_skew = skew(x) # simetría
x_kurt = kurtosis(x) # Esta es kurtosis en exceso. Cuántas 'colas largas' tiene
x_var_95 = np.percentile(x, 5) #var: valor en riesgo
x_cvar_95 = np.mean(x[x <= x_var_95]) # Media de las peores pérdidas
x_sharpe = x_mean/x_std * np.sqrt(252) # Si x_sharpe>1.96 (con intervalo de confianza de la desviación estándar al 95%, que es 1.96), significa que el intervalo de confianza de la media (que es la media +/- 1.96) está a la derecha del 0. Si el x_sharpe < 1.96, el 0 va a estar dentro del intervalo de confianza. Asumiendo distribución normal, quiero un x_sharpe>1.96, porque significaría que la media es positiva. Con el np.sqrt(252) lo estoy convirtiendo en un sharpe anualizado (252 días bursátiles).
# Nota: La desviación estándar (x_stdev) crece como la raíz cuadrada del tiempo y las ganancias diarias (x_mean) crecen linealmente en tiempo
x_jb = x_size/6 * (x_skew**2 + 1/4*x_kurt**2)
p_value = 1 - chi2.cdf(x_jb, df = 2)
x_is_normal = (p_value > 0.05) # equivalently jb < 6

# Visualizar el cálculo de las funciones -----------------------------
round_digits = 4
str1 = 'Mean ' + str(np.round(x_mean, round_digits))\
    + ' | Std dev ' + str(np.round(x_std, round_digits))\
    + ' | Skewness ' + str(np.round(x_skew, round_digits))\
    + ' | Kurtosis ' + str(np.round(x_kurt, round_digits))\
    + ' | Sharpe ratio ' + str(np.round(x_sharpe, round_digits))
str2 = 'VaR 95% ' + str(np.round(x_var_95, round_digits))\
    + ' | CVaR dev ' + str(np.round(x_cvar_95, round_digits))\
    + ' | Jarque_Bera ' + str(np.round(x_jb, round_digits))\
    + ' | p_value ' + str(np.round(p_value, round_digits))\
    + ' | Is normal? ' + str(x_is_normal)

# Nota: Si la skewness es > media, los datos están cargados a la derecha de la distribución. <media significa que la distribución está cargada a la izquierda de la distribución
# Nota 2: Si la kurtosis <0, la variable aleatoria con la que estoy jugando decrece más rápido que la normal. Si k_3 (kurtosis en exceso) > 0 decrece menos rápido que la normal. k_3 = 0 significa que es una normal

# plot histogram
plt.figure()
plt.hist(x, bins = 100)
plt.title('Histogram ' + x_str)
plt.xlabel(str1 + '\n' + str2)
plt.show()