# -------------------------------------------------------------------------------------
# -------------------------------- MARKOWITZ PORTFOLIO --------------------------------



# A Markowitz Portfolio, also known as a mean-variance portfolio, is an investment portfolio construction technique developed by economist Harry Markowitz. It is based on the principle that investors should consider both the expected return and the risk (variance or standard deviation) of their investment options when making portfolio decisions.

# The Markowitz Portfolio theory aims to optimize the trade-off between expected return and risk by selecting a combination of assets that provides the highest expected return for a given level of risk, or the lowest risk for a given level of expected return.



# Used libraries ----------------------------------------------------------------------
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_datareader import data
from pulp import *
import yfinance as yf
from cvxpy import Variable, Problem, Maximize, quad_form, NonNeg, sum


# -------------------------------- SCRIPT DEVELOPEMENT ---------------------------------

# Downloading the data------------------------------------------------------------------
# We download the data from Yahoo Finance and plot the series in levels and differentiated (returns)

# Start date data yyy, mm, dd
start = datetime(2020, 1, 1)


# End date data yyy, mm, dd
end = datetime.today().strftime('%Y-%m-%d')
end = datetime.strptime(end, '%Y-%m-%d') # from 'str' to 'datetime'

tickers = ['GOOG', 'AMZN', 'AAPL', 'JPM']
data = yf.download(tickers, start = start, end = end, interval = "1wk")['Close']
data.head()

# We graph ------------------------------------------------------------------------------
plt.figure(figsize = (12.2,4.5)) 
plt.plot(data)
plt.title('Precio de las Acciones')
plt.xlabel('Fecha',fontsize = 12)
plt.ylabel('Precio en USD',fontsize = 12)
plt.legend(data.columns.values, loc = 'upper left')
plt.savefig('plotprecios.png', dpi = 300, bbox_inches = 'tight')
plt.show()

# Calculation of returns ----------------------------------------------------------------
returns = np.log(data).diff()
returns = returns.dropna()

# Statistical normality -----------------------------------------------------------------
# Create an array of values in a specific range
x = np.linspace(0, len(returns)-1, len(returns))

# Create the figure and subplots
fig, axs = plt.subplots(2, 2, figsize = (10, 8))

# Subplot 1
axs[0, 0].hist(returns[tickers[0]], bins = 100, color = '#1f77b4')
axs[0, 0].set_title(tickers[0])

# Subplot 2
axs[0, 1].hist(returns[tickers[1]], bins = 100, color = '#ff7f0e')
axs[0, 1].set_title(tickers[1])

# Subplot 3
axs[1, 0].hist(returns[tickers[2]], bins = 100, color = '#2ca02c')
axs[1, 0].set_title(tickers[2])

# Subplot 4
axs[1, 1].hist(returns[tickers[3]], bins = 100, color = '#d62728')
axs[1, 1].set_title(tickers[3])

# Adjust spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()

# Calculate the variance-covariance matrix
cov_matrix = returns.cov()

# Number of assets in the portfolio
n_assets = len(tickers)

# Asset weights in the portfolio
weights = Variable(n_assets)

# Define the constraints
constraints = [weights >= 0, sum(weights) == 1]

# Define the objective function for maximizing the Sharpe ratio
returns_mean = returns.mean(axis=0)
portfolio_return = np.dot(returns_mean, weights)
portfolio_volatility = quad_form(weights, cov_matrix)
risk_free_rate = 0.02  # Risk-free rate
portfolio_volatility = np.std(portfolio_return)
sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility

# Define the optimization problem
problem = Problem(Maximize(sharpe_ratio), constraints)

# Solve the optimization problem
problem.solve()

# Get the optimal weights
optimal_weights = weights.value

# Create a DataFrame with the results
portfolio = pd.DataFrame({'Ticker': tickers, 'Optimal Weight': optimal_weights})
portfolio = portfolio.set_index('Ticker')

print(portfolio)