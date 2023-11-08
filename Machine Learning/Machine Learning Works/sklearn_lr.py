import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


data = pd.read_csv("data_for_lr.csv")

x = data[["avg_grade"]]
y = data["grade"]

model = LinearRegression()

model.fit(x,y)

m = model.coef_[0]
b = model.intercept_
print(f"Slope: {m}, Intercept:{b}")

x_array = x.values

plt.scatter(x,y, color = "red")
plt.xlabel("avg_grade")
plt.ylabel("grade")
plt.plot(x_array, model.predict(x),color = "yellow")
plt.show()

# y_actual = np.array(y.values)
# y_predicted = model.predict(x)
# mse = mean_squared_error(y_actual,y_predicted)
# rmse = np.sqrt(mse)
# print(f"RMSE: {rmse}")
