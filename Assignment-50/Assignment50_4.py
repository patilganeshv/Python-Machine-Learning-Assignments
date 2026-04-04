"""
4.Train Classification Models
    Train the following models:
        Logistic Regression
        K-Nearest Neighbors (KNN)
        Random Forest Classifier
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier


def bank_term_subscription_prediction(datapath):
    border = "-" * 40
    
    print("Load the dataset from csv file")
    print(border)
    
    df = pd.read_csv(datapath, sep=';')
    
    print("First 5 rows: \n", df.head(5))
    print(border)

    print("Dataset Info:\n")
    print(df.info())
    print(border)
    
    print("Basic Statistics:\n", df.describe())
    print(border)

    print("Handle Missing / Unknown Values")
    # Replace 'unknown' with NaN
    df.replace("unknown", np.nan, inplace=True)

    # Fill missing values
    df.fillna(df.mode().iloc[0], inplace=True)
    print(border)

    # -------------------------------
    # Target Variable Conversion
    # -------------------------------
    print("Encoding target variable")
    df['y'] = df['y'].map({'yes': 1, 'no': 0})
    
    # -------------------------------
    # Encode categorical variables
    # -------------------------------
    print("Applying One-Hot Encoding")
    df = pd.get_dummies(df, drop_first=True)

    # -------------------------------
    # Split Features & Target
    # -------------------------------
    X = df.drop('y', axis=1)
    y = df['y']
    
    print("Applying StandardScaler")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # -------------------------------
    # Train-Test Split
    # -------------------------------
    print("Splitting dataset into train and test")
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    
    # -------------------------------
    # Model Training
    # -------------------------------
    lr = LogisticRegression()
    lr.fit(X_train, y_train)
    y_pred_lr = lr.predict(X_test)

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    y_pred_knn = knn.predict(X_test)

    rf = RandomForestClassifier()
    rf.fit(X_train, y_train)
    y_pred_rf = rf.predict(X_test)
    
def main():
    border = "-" * 40
    print(border)
    print("Bank Term Deposit Subscription Prediction")
    print(border)
    bank_term_subscription_prediction("bank-full.csv")

if __name__ == "__main__":
    main()