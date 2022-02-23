#VaR (Valor en Riesgo)
# El VaR o Value at Risk es una medida estadística de riesgo de mercado que nos ayuda a estimar la pérdida máxima que podría registrar un activo o un portafolio en un intervalo de tiempo con cierto nivel de confianza. Este VaR solamente es valido en condiciones normales de mercado; si el mercado se encuentra en momento de crisis se deben usar pruevas de estrés. Podemos calcular el VaR mediante pruebas paramétricas (basada en parámetros) o no paramétricas (basada en simulaciones).

# Técinas paramétricas-----------------------------------------
# Es el resultado de la multiplicación de F(nivel de confianza), S (monto del activo o cartera a precios de mercado), omega (desviación estándar de los rendimientos del activo), y la raíz cuadrada de t (horizonte de tiempo en que se desea calcular el VaR).


#CVaR (Déficit esperado)
# Expected Shortfall



import numpy as np
import pandas as pd
import matplotlib as mpl
import scipy
import importlib
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, chi2
