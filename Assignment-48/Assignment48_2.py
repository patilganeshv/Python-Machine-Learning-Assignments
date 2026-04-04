"""
Write a python program that calculates the variance and standard deviation of the dataset: 
[6, 7, 8, 9, 10, 11, 12] display both results.
"""
import numpy as np

data = [6, 7, 8, 9, 10, 11, 12]

# Calculate variance and standard deviation
variance = np.var(data)
std_deviation = np.std(data)

print("Dataset:", data)
print("Variance:", variance)
print("Standard Deviation:", std_deviation)
