import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt

data  = pd.read_csv("data_for_lr.csv")
x = data[["avg_grade"]]
y = data["grade"]
x_array = x.values
y_array = y.values

def rmse(m,b,points):
    """
    It is not necessary to write because we need the derivative 
    version of it to find the best equation , however it demonstrates 
    the process
    """
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].avg_grade
        y = points.iloc[i].grade
        total_error += (y-(m*x +b))**2

    return sqrt(total_error/float(len(points)))

def gradient_descent(m_now,b_now,points,L):
    """
    it sums the derivatives of the square of the sum of the differences between the real values and the predicted values and then makes 
    slope and const as optimum as possible
    """
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].avg_grade
        y = points.iloc[i].grade
        
        m_gradient += -(2/n)*x*(y-(m_now * x + b_now))
        b_gradient += -(2/n)*(y-(m_now*x + b_now))

    m = m_now - m_gradient *L
    b = b_now - b_gradient *L
    

    return m, b

m = 3; b = 1 # initial values
L = 0.0001 # learning rate
epochs = 100 # iteration amount

# print(rmse(m,b,data))

print(rmse(m,b,data))

for i in range(epochs):
    if i % 20 == 0:
        ratio = (i/epochs)*100
        print(f"processing %{100-ratio} left")
    m, b = gradient_descent(m, b, data, L)

print(rmse(m,b,data))

    
print(f"slope: {m}, constant: {b} ")

plt.scatter(data.avg_grade,data.grade, color = "red")
plt.xlabel("avg_grade")
plt.ylabel("grade")
plt.plot(x_array,[m*x + b for x in x_array], color = "yellow")
plt.show()


