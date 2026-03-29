"""
Write a python program to load the file student_performance_ml.csv
using pandas.
Display:
    1.First 5 records
    2.Last 5 records
    3.Total numbers of rows and columns
    4.List of columns names
    5.Data types of each column
"""
import pandas as pd

def student_performance(Datapath):
    Border = "-" * 40

    # Load the dataset
    df = pd.read_csv(Datapath)
    
    print(Border)
    print("1.First 5 Records:")
    print(df.head())

    print(Border)
    print("2.Last 5 Records:")
    print(df.tail())

    print(Border)
    print("3.Total rows and columns (Shape of dataset): ", df.shape)

    print(Border)
    print("4.List of column names:")
    print(df.columns)

    print(Border)
    print("5.Data Types of each column: ")
    print(df.dtypes)

def main():
    student_performance("student_performance_ml.csv")

if __name__ == "__main__":
    main()