"""
Drow a boxplot for attendance.
Identify if any outliers are present.
"""
import pandas as pd
import matplotlib.pyplot as plt

def student_performance(Datapath):
    Border = "-" * 40

    # Load  the dataset
    df = pd.read_csv(Datapath)
    
    # Boxplot for Attendance
    plt.boxplot(df['Attendance'])
    plt.title("Attendance Boxplot")
    plt.ylabel("Attendance")
    plt.show()

def main():
    student_performance("student_performance_ml.csv")

if __name__ == "__main__":
    main()