"""
Cluster students into different academic performance groups based on features like:
    .Final grades
    .Study time
    .Failures
    .Absences

This helps identify:
    .Top Performers
    .Average Students
    .Struggling Students

Dataset Details:
    .Dataset Name: Student Performance Data Set

Selected Features:
Use these numerical features for clustering:
    .G1, G2, G3 → First, second, final grades
    .studytime → Weekly study hours
    .failures → Number of past class failures
    .absences → Number of school absences

You should create the following clusters:
Top Performers (Cluster 0)
    .High grades and low failure count
    .High study time and few absences

Average Students (Cluster 1)
    .Moderate scores and study time
    .Some failures or absences

Struggling Students (Cluster 2)
    .Low grades, high failure and absence rate
    .Low study time
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def student_clustering(datapath):
    border = "-" * 40

    print("1.Load the dataset")
    print(border)
    
    df = pd.read_csv(datapath)
    print("First 5 rows: \n", df.head())


    print("2.Select Required Features")
    print(border)

    features = ['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted', 'SleepHours']
    data = df[features]

    print("3.Check data")
    print(border)
    
    print(data.head(), "\n")
    print(data.describe(), "\n")

    print("4.Feature Scaling")
    print(border)

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    print("5.Find Optimal Cluster (Elbow Method)")
    print(border)

    wcss = []

    for i in range(1, 10):
        kmeans = KMeans(n_clusters=i, random_state=42)
        kmeans.fit(scaled_data)
        wcss.append(kmeans.inertia_)
    
    plt.plot(range(1, 10), wcss, marker='o')
    plt.title("Elbow Method")
    plt.xlabel("Number of Clusters")
    plt.ylabel("WCSS")
    plt.show()

    print("6.Apply K-Means Clustering")
    print(border)
    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(scaled_data)

    df['Cluster'] = clusters

    print("7.Analyze Clusters")
    print(border)
    print(df.groupby('Cluster')[features].mean(), "\n")

    print("8.Label Clusters")
    print(border)

    cluster_labels = {
        0: "Struggling Students",
        1: "Average Students",
        2: "Top Performers"
    }
    df['Category'] = df['Cluster'].map(cluster_labels)

    print("9.Visualization")
    print(border)
    sns.scatterplot(
        x=df['PreviousScore'],
        y=df['StudyHours'],
        hue=df['Category']
    )
    plt.title("Student Clusters")
    plt.show()

def main():
    border = "-" * 40
    print(border)
    print("Student Performance")
    print(border)
    student_clustering("student_performance_ml.csv")

if __name__ == "__main__":
    main()