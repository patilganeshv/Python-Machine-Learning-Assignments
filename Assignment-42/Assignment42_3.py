"""
    1.Train linear regression model
    2.Predict salary for 6 years of experience
    3.Plot regression line using matplotlib

    Expected Output:
    Predicted salary for 6 years experiance: 45000
    Graph should display:
        .Data points
        .Regression line
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
Y = np.array([20000, 25000, 30000, 35000, 40000])

model = LinearRegression()
model.fit(X, Y)

# Prediction
predicted_salary = model.predict([[6]])
print("Predicted Salary for 6 years:", predicted_salary[0])

# Graph
plt.scatter(X, Y)
plt.plot(X, model.predict(X))
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Experience vs Salary")
plt.show()