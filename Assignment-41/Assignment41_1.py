import math

# Dataset with labels A, B, C, D
data = [
    ("A", [1, 2], "Red"),
    ("B", [2, 3], "Red"),
    ("C", [3, 1], "Blue"),
    ("D", [6, 5], "Blue")
]

# Distance function
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# KNN function
def knn(test_point, k):
    distances = []

    for name, point, label in data:
        dist = distance(point, test_point)
        distances.append((dist, name, label))

    # Sort by distance
    distances.sort(key=lambda x: x[0])

    # Get k nearest neighbors
    neighbors = distances[:k]

    print("Nearest Neighbors:")
    for dist, name, label in neighbors:
        print(f"{name} - Distance: {round(dist, 2)}")

    # Voting
    votes = {}
    for _, _, label in neighbors:
        votes[label] = votes.get(label, 0) + 1

    predicted = max(votes, key=votes.get)

    print("\nPredicted Class:", predicted)

# Input
X = int(input("Enter X coordinate: "))
Y = int(input("Enter Y coordinate: "))
test = [X, Y]
k = 3

knn(test, k)