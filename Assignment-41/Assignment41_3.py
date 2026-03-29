import math

# Dataset
data = [
    ([2, 60], "Fail"),
    ([5, 80], "Pass"),
    ([6, 85], "Pass"),
    ([1, 50], "Fail")
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

    votes = {}
    for _, label in neighbors:
        votes[label] = votes.get(label, 0) + 1

    return max(votes, key=votes.get)

# Input
study_hours = int(input("Enter Study Hours: "))
attendance = int(input("Enter Attendance: "))

test = [study_hours, attendance]
k = 3

result = knn(test, k)

print("Predicted Result:", result)