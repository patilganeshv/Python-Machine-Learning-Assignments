import math

# Dataset
data = [
    ([1, 2], "Red"),
    ([2, 3], "Red"),
    ([3, 1], "Blue"),
    ([6, 5], "Blue"),
    ([7, 7], "Blue")
]

# Distance function
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# KNN function
def knn(test_point, k):
    distances = []

    for point, label in data:
        dist = distance(point, test_point)
        distances.append((dist, label))

    distances.sort(key=lambda x: x[0])
    neighbors = distances[:k]

    # Voting
    votes = {}
    for _, label in neighbors:
        votes[label] = votes.get(label, 0) + 1

    return max(votes, key=votes.get)

# Test point
test = [2, 2]

# Try different K values
k_values = [1, 3, 5]

print("Prediction Results")
for k in k_values:
    result = knn(test, k)
    print(f"K = {k} -> {result}")


"""
Explain why the prediction changes when K increases.
K = 1
    .Only nearest point considered
    .Sensitive to noise
K = 3
    .Balanced decision
    .Best choice
K = 5
    .Includes far points
    .May give wrong result (underfitting)
"""