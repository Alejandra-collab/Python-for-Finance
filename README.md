# Python-for-Finance

### 1. get-data.py
In this script you are going to be able to look the code to download data from Yahoo Finance.

### 2. web-scraping.py
In this script I expose how to use Python to request information from a web page in an automated way.

### 3. JarqueBera-test.py
##### Objective: Distributions in Python: (i) Calculation of statistical functions, moments, percentiles, and Value at Risk (VaR); (ii) Data visualization in Python: histograms; (iii) Normality or Gaussianity test: Jarque-Bera; and (iv) P-value limits and statistical tests: Borel-Cantelli theorem.

Agenda:
Distributions
1.1. Calculation of statistical functions
1.2. Jarque-Bera test
1.3. Data visualization
1.4. Borel-Cantelli theorem

If the data comes from a normal distribution, the JB test will behave like a chi-square distribution with two degrees of freedom.

The null hypothesis means our distribution is normal (skewness = 0, excess kurtosis = 0). With a JB > 6 the distribution is not normal.

### 4. VaR-CVaR.py
Value at Risk (VaR) is a statistical measure of market risk that helps estimate the maximum potential loss that an asset or portfolio could experience within a certain time interval with a specified level of confidence. This VaR is only valid under normal market conditions; if the market is in a crisis state, stress tests should be employed. VaR can be calculated using parametric (parameter-based) or non-parametric (simulation-based) approaches.

### 5. Markowitz.py
A Markowitz Portfolio, also known as a mean-variance portfolio, is an investment portfolio construction technique developed by economist Harry Markowitz. It is based on the principle that investors should consider both the expected return and the risk (variance or standard deviation) of their investment options when making portfolio decisions.

The Markowitz Portfolio theory aims to optimize the trade-off between expected return and risk by selecting a combination of assets that provides the highest expected return for a given level of risk, or the lowest risk for a given level of expected return.

#### Nota: 
A parametric technique is the result of multiplying F (confidence level), S (market value of the asset or portfolio), omega (standard deviation of asset returns), and the square root of t (time horizon for calculating VaR).
