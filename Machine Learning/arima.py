import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
import math

np.random.seed(0)
n = 100
time = np.arange(n)
data = np.cumsum(np.random.randn(n))

df = pd.DataFrame({'Time': time, 'Data': data})

plt.figure(figsize=(12, 6))
plt.plot(df['Time'], df['Data'])
plt.title('Time Series Data')
plt.xlabel('Time')
plt.ylabel('Data')
plt.show()

p = 1  
d = 1  
q = 1  

model = sm.tsa.ARIMA(df['Data'], order=(p, d, q))
results = model.fit()

forecast_steps = 10
forecast = results.forecast(steps=forecast_steps)

plt.figure(figsize=(12, 6))
plt.plot(df['Time'], df['Data'], label='Original Data')
plt.plot(np.arange(n, n+forecast_steps), forecast, label='Forecast')
plt.title('Original Data vs. Forecast')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()

observed_values = df['Data'][-forecast_steps:]  # Actual observed values for the forecasted period
rmse = math.sqrt(mean_squared_error(observed_values, forecast))
print(f'RMSE: {rmse:.2f}')
