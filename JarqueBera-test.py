# Objetivo: Distribuciones en Python: (i) Calculo de funciones estadísticas, momentos, percentiles y Valor en Riesgo (VaR); (ii) Visualización de datos en Python: histogramas; (iii) Test de normalidad o Gaussianidad: Jarque-Bera; y (iv) Los limites del p-value y los test estadísticos: cuando una distribución falla el test de normalidad.


import numpy as np
import pandas as pd
import matplotlib as mpl
import scipy 
import importlib
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, chi2 #_contingency


# Queremos hacer un test de Python que me calcule un test de normalidad de rendimientos. Primero hacerlo con rendimientos simulados.

# Hay varios test de normalidad. Uno se llama de Jerque-bera

# Paso 1: Generar variables aleatorias

x_size = 10**6
degrees_freedom = 5 # Si los degrees_freedom de una student tienden a infinito, la distribución se parecerá mucho a una normal

# Aquí solo tenemos que cambiar el tipo de distribución de type_random_variable según necesitemos:
type_random_variable = 'normal' #student exponential normal

if type_random_variable == 'normal':
    x = np.random.standard_normal(x_size)
    x_str = type_random_variable
elif type_random_variable == 'exponential':
    x = np.random.standard_exponential(x_size)
    x_str = type_random_variable
elif type_random_variable == 'student':
    x = np.random.standard_t(df = degrees_freedom, size = x_size)
    x_str = type_random_variable
elif type_random_variable == 'chi-square':
    x = np.random.chisquare(df = degrees_freedom, size = x_size)
    x_str = type_random_variable

    #Para que se muestren los grados de libertad, df, tenemos que cambiar los degrees_freedom de entero a string. Eso lo hacemos con str() 
    x_str = type_random_variable + ' (df=' + str(degrees_freedom) + ')'


# Compute "risk metrics"
x_mean = np.mean(x)
x_stdev = np.std(x)
x_skew = skew(x)
x_kurt = kurtosis(x) # Esta es kurtosis en exceso
x_var_95 = np.percentile(x, 5) #var: valor en riesgo 
x_jb = x_size/6 * (x_skew**2 + 1/4 * x_kurt**2)
p_value = 1 - chi2.cdf(x_jb, df = degrees_freedom) 
is_normal = (p_value > 0.05) # Rechazamos la hipótesis cuando el p_value sea menor que el nivel de significancia


# Print metrics
print('mean' + str(x_mean))
print('std' + str(x_stdev))
print('skewness' + str(x_skew)) #Si es >media, los datos están cargados a la derecha de la distribución. <media significa que la distribución está cargada a la izquierda de la distribución
print('kurtosis' + str(x_kurt)) #Si la kurtosis <0, la variable aleatoria con la que estoy jugando decrece más rápido que la normal. Si k_3 (kurtosisen exceso) > 0 decrece menos rápido que la normal. k_3 = 0 significa que es una normal
print('VaR 95%' + str(x_var_95)) 
print('Jarque-Bera' + str(x_jb))
print('p-value' + str(p_value))

# Paso 2: Visualizar histograma

plt.figure()
plt.hist(x, bins = 100)
plt.title('Histogram ' + x_str)
plt.show()

