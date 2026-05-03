"""
Q.1: Create a neural network model to predict whether a customer will leave a service.
Features:
    1.Age
    2.Monthly charges
    3.Tenure
    4.Number of complaints
    5.Customer support calls

x = [
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
]
y = [0, 0, 1, 1, 1, 0, 1, 1, 0, 1]

Output:
    0 = Customer will stay
    1 = Customer will leave

Tasks:
    1.Load or create dataset
    2.Clean the dataset
    3.Apply StandardScaler
    4.Train FNN model
    5.Evaluate accuracy

Feature Meaning:
    [Age, Monthly Charges, Tenure, Complaints, Support Calls]

Output Meaning:
    0 = Customer will stay
    1 = Customer will leave

Test Input:
    new_customer = [[46, 1450, 5, 6, 9]]

Expected Output:
    Prediction: Customer may leave 
"""

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# 1. Load/Create Dataset
X = np.array([
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
])

y = np.array([0, 0, 1, 1, 1, 0, 1, 1, 0, 1])

# 2. Clean Dataset (so no missing values here)

# 3. Apply StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Train FNN Model
model = MLPClassifier(hidden_layer_sizes=(5,), activation='relu',
                      solver='adam', max_iter=1000, random_state=42)

model.fit(X_scaled, y)

# 5. Evaluate Accuracy
y_pred = model.predict(X_scaled)
accuracy = accuracy_score(y, y_pred)

print("Model Accuracy:", accuracy)

# Test New Customer 
new_customer = np.array([[46, 1450, 5, 6, 9]])
new_scaled = scaler.transform(new_customer)

prediction = model.predict(new_scaled)

if prediction[0] == 1:
    print("Prediction: Customer may leave")
else:
    print("Prediction: Customer may stay")