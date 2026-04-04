"""
Q: Write a python program that calculate TP, TN, FP, FN for the following arrays: 
   Actual Values: [1,1,1,1,0,0,0,0] 
   Predicted Values: [1,1,0,1,0,1,0,0]
"""

actual = [1, 1, 1, 1, 0, 0, 0, 0]
predicted = [1, 1, 0, 1, 0, 1, 0, 0]

# Initialize counters
TP = 0
TN = 0
FP = 0
FN = 0

# Calculate values
for i in range(len(actual)):
    if actual[i] == 1 and predicted[i] == 1:
        TP += 1
    elif actual[i] == 0 and predicted[i] == 0:
        TN += 1
    elif actual[i] == 0 and predicted[i] == 1:
        FP += 1
    elif actual[i] == 1 and predicted[i] == 0:
        FN += 1

print("True Positive (TP):", TP)
print("True Negative (TN):", TN)
print("False Positive (FP):", FP)
print("False Negative (FN):", FN)

"""
TP --> Actual = 1, Predicted = 1
TN --> Actual = 0, Predicted = 0
FP --> Actual = 0, Predicted = 1
FN --> Actual = 1, Predicted = 0
"""