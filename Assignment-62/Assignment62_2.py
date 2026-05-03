"""
Q.2: Write a Python program to demonstrate ReLU and Max Pooling.
Tasks:
    1.Create a feature map with positive and negative values.
    2.Apply ReLU.
    3.Apply 2x2 max pooling.
    4.Display output after each step.
    5.Explain why pooling reduces size.

Input Feature Map
feature_map = [
    [3,   3,   3],
    [0,   0,   0],
    [-3,  -3,  -3]
]

ReLU Rule
if value < 0, convert it to 0
if value >= 0, keep it same

Expected Output
relu_output = [
    [3,  3,  3],
    [0,  0,  0],
    [0,  0,  0]
]
"""

import numpy as np

# 1. Input Feature Map
feature_map = np.array([
    [3,   3,   3],
    [0,   0,   0],
    [-3, -3, -3]
])

print("Original Feature Map:\n", feature_map)

# 2. Apply ReLU
relu_output = np.maximum(0, feature_map)
print("\nReLU Output:\n", relu_output)

# 3. Apply 2x2 Max Pooling (stride = 1)
pool_size = 2
stride = 1

pooled_output = []

for i in range(relu_output.shape[0] - pool_size + 1):
    row = []
    for j in range(relu_output.shape[1] - pool_size + 1):
        region = relu_output[i:i+pool_size, j:j+pool_size]
        max_val = np.max(region)

        print(f"\nRegion ({i},{j}):")
        print(region)
        print("Max value:", max_val)

        row.append(max_val)
    pooled_output.append(row)

pooled_output = np.array(pooled_output)

print("\nMax Pooling Output:\n", pooled_output)

"""
# Explain why pooling reduces size.
    1.Max pooling select only the maximum value from ecah region
    2.It reduce height and width of the feature map
    3.This decreases computation and memory usage
    4.Helps in extracting important features only
    5.Also provides translation invarience 
    (small shifts don't affect output much)
"""