# In this script:
# 1. Distributions in Python
# 1.1. Calculation of statistical functions, moments, percentiles, and Value at Risk (VaR)
# 1.2. Normality or Gaussianity tests: Jarque-Bera
# 1.3. Data visualization in Python: histograms
# 1.4. Borel-Cantelli theorem, VaR, and CVaR


import numpy as np
import pandas as pd
import matplotlib as mpl
import scipy 
import importlib
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, chi2, linregress 
from scipy.optimize import minimize
from numpy import linalg as LA


# ----------------------------- 1.DISTRIBUTIONS -------------------------

# We want to perform a Python test that calculates a normality test for returns. Let's start by doing it with simulated returns.
# There are several normality tests, one of them is called Jarque-Bera.

# 1.4. 1.4. Borel-Cantelli theorem, VaR, and CVaR -----------------------------

# Using a confidence level of 95%, for example, means that even at a high confidence level and running the program infinitely, there will be some normal distribution for which the Jarque-Bera test makes it appear as non-normal. This is known as the Borel-Cantelli theorem.

# When the dataset fails the normality test, the program will stop:
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
    x_std = np.std(x) # volatility
    x_skew = skew(x) # skewness
    x_kurt = kurtosis(x) # This is excess kurtosis. How many 'long tails' it has
    x_var_95 = np.percentile(x, 5) # VaR: Value at Risk
    x_cvar_95 = np.mean(x[x <= x_var_95]) # Mean of the worst losses
    x_sharpe = x_mean/x_std # Sharpe ratio
    jb = x_size/6 * (x_skew**2 + 1/4*x_kurt**2)
    p_value = 1 - chi2.cdf(jb, df = 2)
    is_normal = (p_value > 0.05) # equivalently jb < 6

    # Visualize the calculation of the functions -----------------------------
    print(x_str)
    print('mean: ' + str(x_mean))
    print('std: ' + str(x_std))
    print('skewness: ' + str(x_skew)) # If it is > mean, the data is skewed to the right of the distribution. < mean means that the distribution is skewed to the left of the distribution
    print('kurtosis: ' + str(x_kurt)) # If kurtosis < 0, the random variable I am dealing with decreases faster than the normal distribution. If k_3 (excess kurtosis) > 0, it decreases less quickly than the normal distribution. k_3 = 0 means it is a normal distribution
    print('VaR 95%: ' + str(x_var_95)) 
    print('CVaR 95%: ' + str(x_cvar_95))
    print('Jarque-Bera: ' + str(jb))
    print('p-value: ' + str(p_value))
    print('is normal ' + str(is_normal))

    # The counter will stop when a dataset fails the normality test
    print('counter ' + str(counter))
    counter +=1
    print('-----------------')