"""
Q.2: Create a neural network model to predict loan approval.
Features:
    1.Applicant income
    2.Credit score
    3.Loan amount
    4.Existing EMI
    5.Employment status

Output:
    0 = Loan rejected
    1 = Loan approved

Tasks:
    1.Preprocess categorical values
    2.Apply scaling
    3.Train FNN model
    4.Evaluate model
    5.Predict approval for new applicant

X = [
    [25000, 600, 200000, 10000, 0],
    [40000, 700, 300000, 8000, 1],
    [60000, 750, 500000, 12000, 1],
    [20000, 550, 150000, 15000, 0],
    [80000, 800, 700000, 10000, 1],
    [35000, 650, 250000, 9000, 1],
    [18000, 500, 100000, 12000, 0],
    [90000, 850, 800000, 15000, 1],
    [30000, 580, 200000, 14000, 0],
    [70000, 780, 600000, 10000, 1]
]

y = [0, 1, 1, 0, 1, 1, 0, 1, 0, 1]

Feature Meaning:
    [Income, Credit Score, Loan Amount, Existing EMI, Employment Status]

Employment Status:
    0 = Not Stable
    1 = Stable

Test Input:
    new_applicant = [[55000, 720, 400000, 10000, 1]]

Expected Output:
    Prediction: Loan Approved
"""

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

X = np.array([
    [25000, 600, 200000, 10000, 0],
    [40000, 700, 300000, 8000, 1],
    [60000, 750, 500000, 12000, 1],
    [20000, 550, 150000, 15000, 0],
    [80000, 800, 700000, 10000, 1],
    [35000, 650, 250000, 9000, 1],
    [18000, 500, 100000, 12000, 0],
    [90000, 850, 800000, 15000, 1],
    [30000, 580, 200000, 14000, 0],
    [70000, 780, 600000, 10000, 1]
])

y = np.array([0, 1, 1, 0, 1, 1, 0, 1, 0, 1])

# 1. Preprocess Categorical Values
# Employment Status already encoded (0,1) so there is no extra encoding needed

# 2. Apply Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Train FNN Model
model = MLPClassifier(hidden_layer_sizes=(5,),
                      activation='relu',
                      solver='adam',
                      max_iter=1000,
                      random_state=42)

model.fit(X_scaled, y)

# 4. Evaluate Model
y_pred = model.predict(X_scaled)
accuracy = accuracy_score(y, y_pred)

print("Model Accuracy:", accuracy)

# 5. Test New Applicant
new_applicant = np.array([[55000, 720, 400000, 10000, 1]])
new_scaled = scaler.transform(new_applicant)

prediction = model.predict(new_scaled)

if prediction[0] == 1:
    print("Prediction: Loan Approved")
else:
    print("Prediction: Loan Rejected")