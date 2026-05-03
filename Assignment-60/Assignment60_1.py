"""
Q.1 Write a Python Program to simulate a single artificial neuron.
Input:
    x1 = 2
    x2 = 3
    w1 = 0.4
    w2 = 0.6
    bias = 0.5
Tasks:
    1.Calculate weighted sum.
    2.Apply sigmoid activation function.
    3.Disaply final output.
    4.Explain whether output is close to 0 or 1.
"""

import math

x1, x2 = 2, 3
w1, w2 = 0.4, 0.6
bias = 0.5

# 1.Calculate weighted sum.
z = (x1 * w1) + (x2 * w2) + bias

# 2.Apply sigmoid activation function.
output = 1 / (1 + math.exp(-z))

# 3.Disaply final output.
print("Weighted Sum:", z)
print("Output:", output)

"""
4.Explain whether output is close to 0 or 1.
    1.Output is 0.956, which is close to 1
    2.This means neuron is strongly activated.
    3.In binary classification -> predicted class is 1.
"""
