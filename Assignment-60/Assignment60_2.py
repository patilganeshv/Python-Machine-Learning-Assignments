"""
Q.2: Write a Python program to demonstrate different activation functions.
Functions to implement:
    1.Sigmoid
    2.ReLU
    3.Tanh
Tasks:
    1.Accept input values from -10 to 10.
    2.Plot all activation funtions using Matplotlib.
    3.Explain the use of each activation function.
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

# Functions
sigmoid = 1 / (1 + np.exp(-x))
relu = np.maximum(0, x)
tanh = np.tanh(x)


plt.plot(x, sigmoid, label="Sigmoid")
plt.plot(x, relu, label="ReLU")
plt.plot(x, tanh, label="Tanh")

plt.legend()
plt.title("Activation Functions")
plt.xlabel("x")
plt.ylabel("Output")
plt.grid()
plt.show()

"""
Explaination of each activation functions:
# Sigmoid:
    1.Output range: (0, 1)
    2.Used in binary classification
    3.Smooth curve but suffers from vanishing gradient
    4.Converts input into probability
    5.Not preferred for deep hidden layers

# ReLU (Rectified Linear Unit)
    1.Output: 0 if x<0, else x
    2.Very fast and widely used
    3.Solves vanishing gradient problem
    4.Sparse activation (efficient)
    5.Issue: "dead neurons" for negative inputs

# Tanh
    1.Output range: (-1, 1)
    2.Zero-centered better then sigmoid
    3.Used in hidden layers sometimes
    4.Still has vanishing gradient issue
    5.Stronger gradient then sigmoid
"""