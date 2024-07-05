# -----------------------------------------------------------------------------------------
# ----------------- Portafolio de Markowitz y cálculo de medidas de desempeño -------------

# A Markowitz Portfolio, also known as a mean-variance portfolio, is an investment 
# portfolio construction technique developed by economist Harry Markowitz. It is based
# on the principle that investors should consider both the expected return and the risk
# (variance or standard deviation) of their investment options when making portfolio
# decisions.

# The Markowitz Portfolio theory aims to optimize the trade-off between expected return
# and risk by selecting a combination of assets that provides the highest expected
# return for a given level of risk, or the lowest risk for a given level of expected
# return.


# Módulos
import pandas as pd
import pandas_datareader.data as wb
import numpy as np
import matplotib.pyplot as plt
import scipy.optimize as optimize


# Vamos a crear un portafolio usando la metodología de Markowitz para
# la optimización de portafolios

# Creamos una lista con los activos que nos interesan
tickers = ['NU', 'CAAP', 'CVAC']

# Creamos un dataframe vacío que luego vamos a llenar con datos
data = pd.DataFrame()

# Descargamos los datos de los activos que nos interesan, desde Yahoo
for i in tickers:
    data[i] = wb.DataReader(i, 'yahoo', '2023-1-1')['Adj Close']

# Calculamos los retornos logarítmicos
log_returns = np.log(1 + data.pct_change())

# Creamos una lista con los retornos y las volatilidades
port_returns = []
port_vols = []

# 
for t in range(10000):
    # Calculamos la cantidad de activos
    num_assets = len(tickers)
    # Para cada activo escogemos un valor de 0 a 1
    weights = np.random.random(num_assets)
    # Queremos que la suma de los pesos sea igual a 1
    weights /= np.sum(weights)
    # Hacemos la suma ponderada con los pesos y la media logarítmica anualizada
    port_returns.append(np.sum(weights*log_returns.mean())*252)
    # Usamos la fórmula para calcular la volatilidad de un portafolio, con la
    # multiplicación de matrices
    port_vols.append(np.sqrt(np.dot(weights.T, np.dot(log_returns.cov()*252, weights))))

# Tenemos las matrices en forma de lista, así que las pasamos a matrices
port_returns = np.array(port_returns)
port_vols = np.array(port_vols)

# Creamos una función para calcular las estadísticas que necesitamos para el portafolio
def portfolio_stats(weights, log_returns):
    port_returns = np.sum(weights*log_returns.mean())*252
    port_vols = np.sqrt(np.dot(weights.T, np.dot(log_returns.cov()*252, weights)))
    # Definimos el Sharpe ratio
    sharpe = port_returns/port_vols
    return {'Return': port_returns, 'volatility': port_vols, 'Sharpe Ratio': sharpe}

# Maximizamos el sharpe ratio, a través de las volatilidades y los retornos
sharpe = port_returns/port_vols
max_sr_returns = port_returns[sharpe.argmax()]
max_sr_volatility = port_vols[sharpe.argmax()]

# Creamos una función para minimizar las variables
def minimize_sharpe(weights, log_returns):
    return -portfolio_stats(weights, log_returns)['Sharpe']

# Definimos qué porcentaje inicial debe tener cada activo. En este caso, será 1 
# dividido el número de activos
initializer = num_assets * [1./num_assets, ]
# Un activo puede tener 100% de la inversión
bounds = tuple((0, 1) for x in range(num_assets))







# Tenemos que calcular el porcentaje óptimo de inversión en cada activo 
# Nos enfocaremos en la maximización de los rendimientos