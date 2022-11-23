# Python-for-Finance

### get-data.py
In this script you are going to be able to look the code to download data from Yahoo Finance.

### web-scraping.py
In this script I expose how to use Python to request information from a web page in an automated way.

### JarqueBera-test
##### Objetivo: Distribuciones en Python: (i) Calculo de funciones estadísticas, momentos, percentiles y Valor en Riesgo (VaR); (ii) Visualización de datos en Python: histogramas; (iii) Test de normalidad o Gaussianidad: Jarque-Bera; y (iv) Los limites de p-value y los test estadísticos: teorema de Borel-Cantelli
#### Temario:
1. Distribuciones
1.1. Calculo de funciones estadísticas
1.2. Test de Jarque Bera
1.3. Visualización de datos
1.4. Teorema de Borel Cantelli
The Jarque-Bera test is a goodness of fit test (which describes how well a set of observations fit).

If the data comes from a normal distribution, the JB test will behave like a chi-square distribution with two degrees of freedom.

The null hypothesis means our distribution is normal (skewness = 0, excess kurtosis = 0). With a JB > 6 the distribution is not normal.

### VaR and CVaR
El VaR o Value at Risk es una medida estadística de riesgo de mercado que nos ayuda a estimar la pérdida máxima que podría registrar un activo o un portafolio en un intervalo de tiempo con cierto nivel de confianza. Este VaR solamente es valido en condiciones normales de mercado; si el mercado se encuentra en momento de crisis se deben usar pruevas de estrés. Podemos calcular el VaR mediante pruebas paramétricas (basada en parámetros) o no paramétricas (basada en simulaciones).
#### Nota: 
Una técnica paramétrica es el resultado de la multiplicación de F(nivel de confianza), S (monto del activo o cartera a precios de mercado), omega (desviación estándar de los rendimientos del activo), y la raíz cuadrada de t (horizonte de tiempo en que se desea calcular el VaR).