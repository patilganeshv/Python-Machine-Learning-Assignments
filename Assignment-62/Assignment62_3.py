"""
Q.3: Write a Python program to show flattening.
Tasks:
    1.Take a 2D matrix.
    2.Convert it into a 1D vector.
    3.Pass it to a fully connected layer.
    4.Calculate final output manually.
    5.Explain the role of flatten layer in CNN.

Input Matrix
matrix = [
    [6, 4],
    [8, 6]
]

Expected Flatten Output
flatten_output = [6, 4, 8, 6]
"""
import numpy as np

# 1. Input 2D Matrix
matrix = np.array([
    [6, 4],
    [8, 6]
])

print("Input Matrix:\n", matrix)

# 2. Flatten (Convert 2D -> 1D)
flatten_output = matrix.flatten()
print("\nFlatten Output:", flatten_output)

# 3. Fully Connected Layer (manual)
# Assume weights and bias
weights = np.array([0.2, 0.3, 0.4, 0.1])
bias = 1

# 4. Final Output Calculation
output = np.dot(flatten_output, weights) + bias

print("\nWeights:", weights)
print("Bias:", bias)
print("Final Output:", output)

"""
# Explain the role of flatten layer in CNN
    1.CNN layers produce 2D/3D feature maps
    2.Fully connected layers require 1D input
    3.Flatten layer converts multi-dimensional data (vector)
    4.It acts as a bridge between convolution and dense layers
    5.Helps in final classification or prediction 
"""