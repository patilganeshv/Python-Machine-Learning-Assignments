"""
1. Exploratory Data Analysis (EDA)
    .Load the dataset using pandas
    .Display the first 5 rows
    .Show column information and check for null values
    .Display basic statistics using .describe()
    .Plot the distribution of the target variable (Outcome)
    .Use graphs like: histogram (hist), boxplot, pairplot to identify patterns or outliers
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

def diabetes_prediction(datapath):
    border = "-" * 40
    print(border)
    
    print("Load the dataset from csv file using Pandas")
    print(border)
    
    df = pd.read_csv(datapath)
    
    print("Display the First 5 rows: \n", df.head(5))
    print(border)

    print("Check column info & null values")
    print(border)
    
    print(df.info())
    print("Null/Missing Values:\n", df.isnull().sum())
    print(border)


    print("Display basic staticstic using .describe()\n", df.describe())
    print(border)

    print("Plot the distribution of the target variable (Outcome)")
    sns.countplot(x='Outcome', data=df)
    plt.title("Distribution of Diabetes Outcome")
    plt.show()
    print(border)
    
    print("Visualization (patterns & outliers)")
    df.hist(figsize=(8, 5))
    plt.show()

    sns.boxplot(data=df)
    plt.xticks(rotation=90)
    plt.show()

    sns.pairplot(df, hue='Outcome')
    plt.show()
    print(border)

def main():
    border = "-" * 40
    print(border)
    print("Diabetics Prediction")
    diabetes_prediction("diabetes.csv")

if __name__ == "__main__":
    main()