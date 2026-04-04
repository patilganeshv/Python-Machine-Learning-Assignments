"""
Write a python program that calculates the mean of a dataset using NumPy for the following values:
[6, 7, 8, 9, 10, 11, 12]
"""
import numpy as np

data = [6, 7, 8, 9, 10, 11, 12]

# Calculate mean
mean_value = np.mean(data)

# Display result
print("Dataset:", data)
print("Mean:", mean_value)