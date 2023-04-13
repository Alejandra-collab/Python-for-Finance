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
t['Date'] = pd.to_datetime(table_raw['Date'], dayfirst=True) # Convertir la columna Date a fecha
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
x_mean = np.mean(x)
x_stdev = np.std(x) # volatilidad
x_skew = skew(x) # simetría
x_kurt = kurtosis(x) # Esta es kurtosis en exceso. Cuántas 'colas largas' tiene
x_var_95 = np.percentile(x, 5) #var: valor en riesgo
x_cvar_95 = np.mean(x[x <= x_var_95]) # Media de las peores pérdidas
x_sharpe = x_mean/x_stdev * np.sqrt(252) # Si x_sharpe>1.96 (con intervalo de confianza de la desviación estándar al 95%, que es 1.96), significa que el intervalo de confianza de la media (que es la media +/- 1.96) está a la derecha del 0. Si el x_sharpe < 1.96, el 0 va a estar dentro del intervalo de confianza. Asumiendo distribución normal, quiero un x_sharpe>1.96, porque significaría que la media es positiva. Con el np.sqrt(252) lo estoy convirtiendo en un sharpe anualizado (252 días bursátiles).
# Nota: La desviación estándar (x_stdev) crece como la raíz cuadrada del tiempo y las ganancias diarias (x_mean) crecen linealmente en tiempo
jb = x_size/6 * (x_skew**2 + 1/4*x_kurt**2)
p_value = 1 - chi2.cdf(jb, df = 2)
is_normal = (p_value > 0.05) # equivalently jb < 6

# Visualizar el cálculo de las funciones -----------------------------
print(x_str)
print('mean: ' + str(x_mean))
print('std: ' + str(x_stdev))
print('skewness: ' + str(x_skew)) #Si es >media, los datos están cargados a la derecha de la distribución. <media significa que la distribución está cargada a la izquierda de la distribución
print('kurtosis: ' + str(x_kurt)) #Si la kurtosis <0, la variable aleatoria con la que estoy jugando decrece más rápido que la normal. Si k_3 (kurtosis en exceso) > 0 decrece menos rápido que la normal. k_3 = 0 significa que es una normal
print('Sharpe ' + str(x_sharpe))
print('VaR 95%: ' + str(x_var_95)) 
print('CVaR 95%: ' + str(x_cvar_95))
print('Jarque-Bera: ' + str(jb))
print('p-value: ' + str(p_value))
print('is normal ' + str(is_normal))

# plot histogram
plt.figure()
plt.hist(x, bins = 100)
plt.title('Histogram ' + x_str)
plt.show()