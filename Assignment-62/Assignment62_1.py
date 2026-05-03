"""
Q.1: Write a Python program to manually perform convolution.
Input:
    A 5x5 matrix representing grayscale image.

Kernel:
    A 3x3 edge detection filter.

Tasks:
    1.Move kernal over image.
    2.Perform multiplication and addition.
    3.Generate feature map.
    4.Print each region calculation.

Input Image Matrix
image = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

Kernel Matrix
kernal = [
    [-1, -1, -1],
    [0,   0,  0],
    [1,   1,  1]
]

First Region Calculation
Region:
    0 0 0
    0 0 0
    1 1 1

Kernel:
    -1 -1 -1
     0  0  0
     1  1  1

Calculation:
    0*-1 + 0*-1 + 0*-1 +
    0*0  + 0*0  + 0*0  +
    1*1  + 1*1  + 1*1

Output = 3

Expected Feature Map
feature_map = [
    [3,   3,  3],
    [0,   0,  0],
    [-3, -3, -3]
]

"""
import numpy as np

# Input Image (5x5)
image = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
])

# Kernel (3x3)
kernel = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
])

# Output feature map size = (5-3+1) = 3
feature_map = []

# Convolution Operation
for i in range(image.shape[0] - 2):
    row = []
    for j in range(image.shape[1] - 2):
        region = image[i:i+3, j:j+3]
        result = np.sum(region * kernel)

        # Print each region calculation
        print(f"\nRegion at position ({i},{j}):")
        print(region)
        print("Calculation:")

        calc = ""
        for r in range(3):
            for c in range(3):
                calc += f"{region[r][c]}*{kernel[r][c]} + "
        print(calc[:-3])  # remove last '+'
        print("Output =", result)

        row.append(result)
    feature_map.append(row)

print("\nFinal Feature Map:")
for row in feature_map:
    print(row)