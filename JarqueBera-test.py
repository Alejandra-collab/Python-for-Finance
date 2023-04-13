# En este script:
# 1. Distribuciones en Python
# 1.1.  Calculo de funciones estadísticas, momentos, percentiles y Valor en Riesgo (VaR)
# 1.2. Tests de normalidad o Gaussianidad: Jarque-Bera 
# 1.3. Visualización de datos en Python: histogramas
# 1.4. Teorema de Borel-Cantelli, VaR y CVaR



import numpy as np
import pandas as pd
import matplotlib as mpl
import scipy 
import importlib
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, chi2, linregress 
from scipy.optimize import minimize
from numpy import linalg as LA


# ----------------------------- 1.DISTRIBUCIONES -------------------------

# Queremos hacer un test de Python que me calcule un test de normalidad de rendimientos. Primero hacerlo con rendimientos simulados.
# Hay varios test de normalidad, uno de ellos se llama de Jerque-bera.

# 1.4. Teorema de Borel-Cantelli, VaR y CVaR -----------------------------

# Usar un nivel de confianza del 95%, por ejemplo, significa que aún a un nivel de confianza alto y corriendo el programa infinidad de veces, habrá alguna distribución normal cuyo test de Jarque Bera la haga ver como no normal. Esto es el llamado teorema de Borel-Cantelli. Veamos:

# Cuando el conjunto de datos falle el test de normalidad el programa se va a detener:
is_normal = True
counter = 0
while is_normal and counter < 10:

    x_size = 10**6
    degrees_freedom = 5000

    type_random_variable = 'normal' # normal exponential student chi-squared
    if type_random_variable == 'normal':
        x = np.random.standard_normal(size = x_size)
        x_str = type_random_variable
    elif type_random_variable == 'exponential':
        x = np.random.standard_exponential(size =x_size)
        x_str = type_random_variable
    elif type_random_variable == 'student':
        x = np.random.standard_t(size = x_size, df = degrees_freedom)
        x_str = type_random_variable + ' (df=' + str(degrees_freedom) + ')'
    elif type_random_variable == 'chi-squared':
        x = np.random.chisquare(size = x_size, df = degrees_freedom)
        x_str = type_random_variable + ' (df=' + str(degrees_freedom) + ')'


    # Compute risk metrics -----------------------------------------------
    x_mean = np.mean(x)
    x_stdev = np.std(x) # volatilidad
    x_skew = skew(x) # simetría
    x_kurt = kurtosis(x) # Esta es kurtosis en exceso. Cuántas 'colas largas' tiene
    x_var_95 = np.percentile(x, 5) #var: valor en riesgo
    x_cvar_95 = np.mean(x[x <= x_var_95]) # Media de las peores pérdidas
    x_sharpe = x_mean/x_stdev # Sharpe ratio
    jb = x_size/6 * (x_skew**2 + 1/4*x_kurt**2)
    p_value = 1 - chi2.cdf(jb, df = 2)
    is_normal = (p_value > 0.05) # equivalently jb < 6

    # Visualizar el cálculo de las funciones -----------------------------
    print(x_str)
    print('mean: ' + str(x_mean))
    print('std: ' + str(x_stdev))
    print('skewness: ' + str(x_skew)) #Si es >media, los datos están cargados a la derecha de la distribución. <media significa que la distribución está cargada a la izquierda de la distribución
    print('kurtosis: ' + str(x_kurt)) #Si la kurtosis <0, la variable aleatoria con la que estoy jugando decrece más rápido que la normal. Si k_3 (kurtosis en exceso) > 0 decrece menos rápido que la normal. k_3 = 0 significa que es una normal
    print('VaR 95%: ' + str(x_var_95)) 
    print('CVaR 95%: ' + str(x_cvar_95))
    print('Jarque-Bera: ' + str(jb))
    print('p-value: ' + str(p_value))
    print('is normal ' + str(is_normal))

    # El contador se detendrá cuando un conjunto de datos no pase el test de normalidad
    print('counter ' + str(counter))
    counter +=1
    print('-----------------')