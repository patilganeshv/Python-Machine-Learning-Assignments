"""
Q.4: Write a python program to show how weights are updated in ANN.
Tasks:
    1.Take input, weight, bias, target output, and learning rate.
    2.Calculate prediction.
    3.Calculate error.
    4.Update weight using gradient descent logic.
    5.Display old weight and updated weight.
"""

# 1. Input values
x = 2                # input
w = 0.5              # initial weight
b = 0.1              # bias
target = 1           # target output
lr = 0.1             # learning rate

# 2. Prediction (simple linear neuron)
y_pred = (x * w) + b

# 3. Error calculation
error = target - y_pred

# 4. Gradient Descent Weight Update
# w_new = w + learning_rate * error * input
w_new = w + lr * error * x

# Bias update
b_new = b + lr * error

# 5. Display results
print("Old Weight:", w)
print("Prediction:", y_pred)
print("Error:", error)
print("Updated Weight:", w_new)
print("Updated Bias:", b_new)