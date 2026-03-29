"""
Design machine learning application which follows below steps as:
Step 1: Get Data
Step 2: Clean, Prepare and Manipulate data
Step 3: Train Data    
Step 4: Test Data
Step 5: Calculate Accuracy
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def MarvellousClassifier(datapath):
    border = "-" * 40
    print(border)
    #------------------------------------------------------------------------
    # Step 1: Load the dataset from csv file
    #-----------------------------------------------------------------------
    print("Step 1: Load the dataset from csv file")
    print(border)
    
    df = pd.read_csv(datapath)
    print("First 5 rows: \n", df.head(5))
    print(border)

    #------------------------------------------------------------------------
    # Step 2: Clean, Prepare and Manipulate Data
    #-----------------------------------------------------------------------
    print("Step 2: Clean, Prepare and Manipulate Data")
    print(border)
    
    # Separate Independant and dependant variables
    X = df.drop(columns=['Class']) # except class column
    Y = df['Class']

    print("Shape of X:", X.shape)
    print("Shape of Y:", Y.shape)
    print(border)

    print("Input columns: ", X.columns.to_list())
    print("Output columns: Class")
    print(border)

    #------------------------------------------------------------------------
    # Step 3: Train Data
    #-----------------------------------------------------------------------
    print("Step 3: Train Data")
    print(border)
    
    # Split the dataset for training and testing
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    print("Information of Training and Testing data:")
    print("X train: ", X_train.shape)
    print("X test: ", X_test.shape)
    print("Y train: ", Y_train.shape)
    print("Y test: ", Y_test.shape)
    print(border)

    model = KNeighborsClassifier()

    # Train model
    model.fit(X_train, Y_train)
    print("Model training completed")
    print(border)

    #------------------------------------------------------------------------
    # Step 4: Test Data
    #-----------------------------------------------------------------------
    print("Step 4: Test Data")
    print(border)
    Y_pred = model.predict(X_test)
    print("Predicted Values:\n", Y_pred[:5])
    print(border)

    #------------------------------------------------------------------------
    # Step 5: Calculate accuracy
    #-----------------------------------------------------------------------
    print("Step 5: Calculate accuracy")
    print(border)
    accuracy = accuracy_score(Y_test, Y_pred)
    print("Accuracy of Model:", accuracy)
    print(border)
    
def main():
    border = "-" * 40
    print(border)    
    print("Wine Classifier using KNN")
    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()