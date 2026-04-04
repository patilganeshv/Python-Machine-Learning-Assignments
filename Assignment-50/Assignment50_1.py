"""
1. Load and Explore the Dataset
    .Handle missing or unknown values (especially in categorical features)
    .Display basic statistics and Visualize class distribution
"""

import pandas as pd
import numpy as np


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


def main():
    border = "-" * 40
    print(border)
    print("Bank Term Deposit Subscription Prediction")
    print(border)
    bank_term_subscription_prediction("bank-full.csv")

if __name__ == "__main__":
    main()