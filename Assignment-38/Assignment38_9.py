"""
Create a plot showing relationship between AssignmentsCompleted and FinalResult.
Explain your observation.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def student_performance(Datapath):
    Border = "-" * 40

    # Load  the dataset
    df = pd.read_csv(Datapath)
    
    # 7. AssignmentsCompleted vs FinalResult
    sns.boxplot(x="FinalResult", y="AssignmentsCompleted", data=df)
    plt.title("AssignmentsCompleted vs FinalResult")
    plt.show()

def main():
    student_performance("student_performance_ml.csv")

if __name__ == "__main__":
    main()