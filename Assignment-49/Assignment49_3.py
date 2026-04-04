"""
3.Model Building
Train at least 2 different algorithms on the dataset:
    .Logistic Regression
    .K-Nearest Neighbors (KNN)
    .Decision Tree
    .Use train_test_split to divide the dataset into training and testing sets
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

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

def main():
    border = "-" * 40
    print(border)
    print("Diabetics Prediction")
    diabetes_prediction("diabetes.csv")

if __name__ == "__main__":
    main()