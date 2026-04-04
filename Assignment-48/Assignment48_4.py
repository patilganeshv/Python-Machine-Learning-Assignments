"""
Write a python program to calculating the euclidean distance between 
two points before and after applying features scaling, 
and explain the difference in results.
"""

import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import euclidean

# Two data points
point1 = np.array([25, 20000])
point2 = np.array([35, 80000])

# Step 1: Distance BEFORE scaling
dist_before = euclidean(point1, point2)

# Step 2: Apply StandardScaler
data = np.array([point1, point2])
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

scaled_p1 = scaled_data[0]
scaled_p2 = scaled_data[1]

# Step 3: Distance AFTER scaling
dist_after = euclidean(scaled_p1, scaled_p2)

print("Point 1:", point1)
print("Point 2:", point2)

print("\nDistance before scaling:", dist_before)
print("Distance after scaling:", dist_after)