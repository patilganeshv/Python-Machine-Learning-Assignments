"""
2. Preprocess the Data
    Convert categorical variables using: Label Encoding OR One-Hot Encoding
    Scale numerical features using: StandardScaler
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


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

def main():
    border = "-" * 40
    print(border)
    print("Bank Term Deposit Subscription Prediction")
    print(border)
    bank_term_subscription_prediction("bank-full.csv")

if __name__ == "__main__":
    main()