import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def student_performance(datapath):
    border = "-" * 40
    #-----------------------------------------------------  
    # Step 1: Load dataset
    #-----------------------------------------------------
    print(border)
    print("Step 1: Load the dataset")
    print(border)

    df = pd.read_csv(datapath)
    print(df.head())
    print(df.shape)
    print(df.columns)

    #-----------------------------------------------------  
    # Step 2: Define Features and Target
    #-----------------------------------------------------
    print(border)
    print("Step 2: Define Features and Target")
    print(border)
    
    X = df.drop("FinalResult", axis=1)
    y = df["FinalResult"]
    
    #-----------------------------------------------------  
    # Step 3: Split data (Train/Test)
    #-----------------------------------------------------
    print(border)
    print("Step 3: Split data (Train/Test)")
    print(border)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # 80% data -> Training, 20% data -> Testing

    #-----------------------------------------------------  
    # Step 4: Train Model
    #-----------------------------------------------------
    print(border)
    print("Step 4: Train Model")
    print(border)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    #-----------------------------------------------------  
    # Step 5: Prediction
    #-----------------------------------------------------
    print(border)
    print("Step 5: Prediction")
    print(border)

    y_pred = model.predict(X_test)

    #-----------------------------------------------------  
    # Step 6: Model Accuracy
    #-----------------------------------------------------
    print(border)
    print("Step 6: Model Accuracy")
    print(border)

    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: ", accuracy)

    #-----------------------------------------------------  
    # Step 7: Confusion Matrix
    #-----------------------------------------------------
    print(border)
    print("Step 7: Confusion Matrix")
    print(border)

    print(confusion_matrix(y_test, y_pred))

    #-----------------------------------------------------  
    # Step 8: Classification Report
    #-----------------------------------------------------
    print(border)
    print("Step 8: Classification Report")
    print(border)

    print(classification_report(y_test, y_pred))

    #-----------------------------------------------------  
    # Step 9: Decision Tree Visualization
    #-----------------------------------------------------
    print(border)
    print("Step 9: Decision Tree Visualization")
    print(border)

    plt.figure(figsize=(8, 5))
    plot_tree(model, feature_names=X.columns,
              class_names=["Fail", "Pass"],
              filled=True
            )
    plt.show()

def main():
    student_performance("student_performance_ml.csv")

if __name__ == "__main__":
    main()