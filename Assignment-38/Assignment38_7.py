"""
Create a scatter plot of:
StudyHours vs PreviousScore
Use different colors for Pass and Fail students.
"""
import pandas as pd
import matplotlib.pyplot as plt

def student_performance(Datapath):
    Border = "-" * 40

    # Load  the dataset
    df = pd.read_csv(Datapath)
    
    pass_students = df[df['FinalResult'] == 1]
    fail_students = df[df['FinalResult'] == 0]

    plt.scatter(pass_students['StudyHours'], pass_students['PreviousScore'], label='Pass')
    plt.scatter(fail_students['StudyHours'], fail_students['PreviousScore'], label='Fail')
    
    plt.xlabel("Study Hours")
    plt.ylabel("Previous Score")
    plt.title("Study Hours vs Previous Score")
    plt.legend()
    plt.show()

def main():
    student_performance("student_performance_ml.csv")

if __name__ == "__main__":
    main()