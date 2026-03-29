import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

def student_performance(data_path):
    
    df = pd.read_csv(data_path)

    #------------------------------------------------
    # 1.After training the decisiontree model use: model.feature_importances_
    #------------------------------------------------
    X = df.drop("FinalResult", axis=1)
    y = df["FinalResult"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    importance = model.feature_importances_

    print("Display importance score of each feature:")
    for feature, score in zip(X.columns, importance):
        print(feature, score)

    y_pred = model.predict(X_test)
    old_accuracy = accuracy_score(y_test, y_pred)
    print("Old Accuracy: ", old_accuracy)

    #------------------------------------------------
    # 2.Remove the column SleepHours from dataset
    #------------------------------------------------
    df2 = df.drop("SleepHours", axis=1)

    X = df2.drop("FinalResult", axis=1)
    y = df["FinalResult"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model2 = DecisionTreeClassifier()
    model2.fit(X_train, y_train)

    y_pred = model2.predict(X_test)
    new_accuracy = accuracy_score(y_test, y_pred)
    print("\nNew Accuracy: ", new_accuracy)

    #------------------------------------------------
    # 3.
    #------------------------------------------------

    #------------------------------------------------
    # 4.Create new DataFrame with details of 5 new students.
    #------------------------------------------------
    new_students = pd.DataFrame({
        "StudyHours":[6,2,4],
        "Attendance":[85,60,75],
        "PreviousScore":[78,40,65],
        "AssignmentsCompleted":[8,3,6],
        "SleepHours":[7,6,8]
    })

    predictions = model.predict(new_students)
    print("Predictions: ", predictions, "\n")

    #------------------------------------------------
    # 6.Identify students where: y_test != y_pred
    #------------------------------------------------
    misclassified = X_test[y_test != y_pred]
    print(misclassified)
    print("Total Misclassified:", len(misclassified), "\n")

    #------------------------------------------------
    # 7. Train model with different random_state
    #------------------------------------------------
    for rs in [0, 10, 12]:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=rs)

        model = DecisionTreeClassifier()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        print("Random State: ", rs, "Accuracy: %.2f" % accuracy_score(y_test, y_pred))

    #------------------------------------------------
    # 8. Decision Tree Visualization 
    #------------------------------------------------
    plt.figure(figsize=(8,5))
    plot_tree(
        model,
        feature_names=X.columns,
        class_names=["Fail", "Pass"],
        filled=True
    )
    plt.show()

    #------------------------------------------------
    # 9. Create New Feature PerformanceIndex 
    #------------------------------------------------
    df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]

    X = df.drop("FinalResult", axis=1)
    y = df["FinalResult"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("Accuracy with new feature: ", accuracy_score(y_test, y_pred), "\n")

    #------------------------------------------------
    # 10. Train Model with max_depth = None 
    #------------------------------------------------
    model = DecisionTreeClassifier(max_depth=None)
    model.fit(X_train, y_train)

    train_acc = model.score(X_train, y_train)
    test_acc = model.score(X_test, y_test)

    print("Training Accuracy:", train_acc)
    print("Testing Accuracy:", test_acc)


def main():
    student_performance("student_performance_ml.csv")

if __name__ == "__main__":
    main()