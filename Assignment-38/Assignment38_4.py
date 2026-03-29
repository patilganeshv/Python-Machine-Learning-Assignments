"""
Use value_counts() to analyze the distribution of FinalResult.
Calsulate the percentage of Pass and Fail students.
Is the dataset balanced? Justify your answer.
"""
import pandas as pd

def student_performance(Datapath):
    Border = "-" * 40

    # Load  the dataset
    df = pd.read_csv(Datapath)
    
    result_count = df['FinalResult'].value_counts()
    print("Result Distribution:")
    print(result_count)

    # Percentage calculation
    percentage = df['FinalResult'].value_counts(normalize=True) * 100
    print("\nPercentage of Pass or Fail:")
    print(percentage)

    # Check is dataset is balanced
    if abs(percentage[0] - percentage[1]) < 20:
        print("Dataset is balanced")
    else:
        print("Dataset is imbalanced")

def main():
    student_performance("student_performance_ml.csv")

if __name__ == "__main__":
    main()

"""
Dataset Balance
If the numbers are close → Balanced Dataset
If one class is very high → Imbalanced Dataset
"""