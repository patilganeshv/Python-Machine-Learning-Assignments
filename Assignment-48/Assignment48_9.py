"""
Q: Write a python program using scikit-learn to generate a classification report for the following data:
   Actual Values: [1,1,1,1,0,0,0,0]
   Predicted Values: [1,1,0,1,0,1,0,0]
   Display the complete classification report including precision, recall, F1-score, and support.
"""

from sklearn.metrics import classification_report

actual = [1, 1, 1, 1, 0, 0, 0, 0]
predicted = [1, 1, 0, 1, 0, 1, 0, 0]

report = classification_report(actual, predicted)

print("Classification Report:\n")
print(report)