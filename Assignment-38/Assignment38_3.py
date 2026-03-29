"""
Using pandas function, calculate and display:
    1.Average StudyHours
    2.Average Attendance
    3.Maximum PreviousScore
    4.Minimum SleepHours
"""
import pandas as pd

def student_performance(Datapath):
    Border = "-" * 40

    # Load  the dataset
    df = pd.read_csv(Datapath)

    pass_students = df[df['FinalResult'] == 1]
    fail_students = df[df['FinalResult'] == 0]

    print("1.Average Study Hours (Pass): %.2f" % pass_students['StudyHours'].mean())
    print("1.Average Study Hours (Fail):%.2f" % fail_students['StudyHours'].mean())
    print("2.Average Attendance: %.2f" % df["Attendance"].mean())
    print("3.Maximum Previous Score:", df["PreviousScore"].max())
    print("4.Minimum Sleep Hours:", df["SleepHours"].min())

def main():
    student_performance("student_performance_ml.csv")

if __name__ == "__main__":
    main()