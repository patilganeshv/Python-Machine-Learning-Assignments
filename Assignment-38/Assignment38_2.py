"""
Write a program to
    1.Display total number of students in the dataset
    2.Count how many students passed (FinalResult = 1)
    3.Count how many students Failed (FinalResult = 0)
"""

import pandas as pd

def student_performance(Datapath):
    Border = "-" * 40

    # Load  the dataset
    df = pd.read_csv(Datapath)
    
    total_students = len(df)
    print("Total number of students:", total_students)

def main():
    student_performance("student_performance_ml.csv")

if __name__ == "__main__":
    main()