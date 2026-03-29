import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def student_performance(Datapath):
    Border = "-" * 40

    # Load  the dataset
    df = pd.read_csv(Datapath)

    # Features and Target
    X = df.drop("FinalResult", axis=1)
    y = df["FinalResult"]

    # Train Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Model
    model = LogisticRegression()

    # Train Model
    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_test)

    # Accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print("\nModel Accuracy:", accuracy)

    # Confusion Matrix
    print("\nConfusion Matrix")
    print(confusion_matrix(y_test, y_pred))

    # Classification Report
    print("\nClassification Report")
    print(classification_report(y_test, y_pred))

def main():
    student_performance("student_performance_ml.csv")

if __name__ == "__main__":
    main()