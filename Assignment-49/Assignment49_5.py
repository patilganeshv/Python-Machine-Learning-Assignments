"""
5.Final Output
    .Predict whether a patient is diabetic or not using test data
    .Display predictions on screen and Save predictions in a CSV file
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns


def evaluate_model(y_test, y_pred, model_name):
    border = "-" * 40
    print(border)
    print(f"--- {model_name} ---")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

def plot_cm(y_test, y_pred, title):
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(title)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

def diabetes_prediction(datapath):
    border = "-" * 40
    print(border)
    
    print("Load the dataset from csv file using Pandas")
    print(border)
    
    df = pd.read_csv(datapath)
    
    print("Handle Zero/Missing Values")
    cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    for col in cols:
        df[col] = df[col].replace(0, df[col].median())
    print(border)

    print("Split Feature & Target")
    X = df.drop('Outcome', axis=1)
    Y = df['Outcome']
    print(border)

    print("Feature Scalling")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print(border)

    print("Train - Test Split")
    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=42)
    print(border)

    print("Model Building")
    lr = LogisticRegression()
    lr.fit(X_train, Y_train)
    y_pred_lr = lr.predict(X_test)
    
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, Y_train)
    y_pred_knn = knn.predict(X_test)

    dt = DecisionTreeClassifier()
    dt.fit(X_train, Y_train)
    y_pred_dt = dt.predict(X_test)
    
    print(border)

    print("Predict on test data")
    predictions = lr.predict(X_test)
    print("Prediction:", predictions)

    if predictions[0] == 1:
        print("Patient is Diabetic")
    else:
        print("Patient is Not Diabetic")
    print(border)

    output = pd.DataFrame({
        "Actual": Y_test,
        "Predicted": predictions
    })

    output.to_csv("predictions.csv", index=False)
    print("Predictions saved successfully!")

def main():
    border = "-" * 40
    print(border)
    print("Diabetics Prediction")
    diabetes_prediction("diabetes.csv")

if __name__ == "__main__":
    main()