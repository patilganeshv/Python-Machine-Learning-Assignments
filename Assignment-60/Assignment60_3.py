"""
Q.3: Write a Python program to calculate loss manually.
Tasks:
    1.Implement MSE (Mean Squared Error)
    2.Implement Binary Cross Entropy.
    3.Take actual and predicted values.
    4.Display the calculated loss.
    5.Explain which loss function is used for regression and classification.
"""
import numpy as np

# 1. Take actual and predicted values
y_true = np.array([1, 0, 1, 1])
y_pred = np.array([0.9, 0.2, 0.8, 0.7])

# 2. Mean Squared Error (MSE)
mse = np.mean((y_true - y_pred) ** 2)

# 3. Binary Cross Entropy (BCE)
bce = -np.mean(
    y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred)
)

# 4. Display results
print("Actual Values:", y_true)
print("Predicted Values:", y_pred)
print("Mean Squared Error (MSE):", mse)
print("Binary Cross Entropy (BCE):", bce)

"""
5.Explain which loss function is used for regression and classification.
    # Loss Function for Regression - Mean Squared Error (MSE)
        1.MSE is commonly used in regression problems.
        2.Regression deals with continuous values (e.g price, temperature)
        3.MSE calculates the average squared difference between actual and predicted values.
        4.It penalizes larger errors more due to squaring.
        5.The goal is to minimize this error to get predictions close to actual values.
        Example: predicting house prices, salary, etc.

    # Loss Function for Classification - Binary Cross Entropy (BCE)
        1.Binary Cross Entropy (BCE) is used for binary classification problems.
        2.Classification deals with categories (0 or 1) instead of continuous values.
        3.BCE measures how well predicted probabilities match actual labels.
        4.It works best with sigmoid activation output (0 to 1).
        5.It heavily penalizes wrong predictions with high confidence.
        Example: spam detection, disease prediction (yes/no).
"""