"""
Tasks:
    1.Predict all Y values using  regression equation.
    2.Calculate
        .Mean Squared Error (MSE)
        .R2 Score
    Show all intermediate calculations.
"""
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Dataset
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
Y = np.array([2, 4, 5, 4, 5])

model = LinearRegression()
model.fit(X, Y)

# Coefficients
m = model.coef_[0]
c = model.intercept_

print("Slope (m):", m)
print("Intercept (c):", c)

# Prediction
y_pred = model.predict(X)
print("Predicted values:", y_pred)

# Metrics
mse = mean_squared_error(Y, y_pred)
r2 = r2_score(Y, y_pred)

print("MSE:", mse)
print("R2 Score:", r2)