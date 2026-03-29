"""
Plot SleepHours againt FinalResult.
Does sleeping more gurantee sucess? Explain.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def student_performance(Datapath):
    Border = "-" * 40

    # Load  the dataset
    df = pd.read_csv(Datapath)
    
    # 8. SleepHours vs FinalResult
    sns.boxplot(x="FinalResult", y="SleepHours", data=df)
    plt.title("SleepHours vs FinalResult")
    plt.show()

def main():
    student_performance("student_performance_ml.csv")

if __name__ == "__main__":
    main()