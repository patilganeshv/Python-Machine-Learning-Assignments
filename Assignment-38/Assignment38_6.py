"""
Plot a histogram of StudyHours.
Explain what the distribution tells you.
"""
import pandas as pd
import matplotlib.pyplot as plt

def student_performance(Datapath):
    Border = "-" * 40

    # Load  the dataset
    df = pd.read_csv(Datapath)
    plt.hist(df["StudyHours"], bins=10)
    plt.title("Distribution of Study Hours")
    plt.xlabel("Study Hours")
    plt.ylabel("Number of Students")
    plt.show()
    
def main():
    student_performance("student_performance_ml.csv")

if __name__ == "__main__":
    main()