"""
Design machine learning application which follows below steps as:
Step 1: Get Data
    Load data from MarvellousAdvertising.csv file into python application.
Step 2: Clean, Prepare and Manipulate data
    As we want to use the above data into machine learning application 
    we have prepare that in the format which is accepted by the algorithms.
Step 3: Train Data
    Now we want to train our data for that we have to select the Machine learning algorithm.
    For that we select Linear Regression algorithm from sklearn library.
    For training purpose divide the dataset into half part.
    Use train method to train our dataset.
Step 4: Test the data
    Test data by passing the remaining half part of the data set.
Step 5:
    Display predicted values of Linear regression algorithms as well as expected values which are provided by the data set.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 

def advertising(datapath):
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
    
    # Check missing values
    print("Missing Values:\n", df.isnull().sum())

    X = df[["TV", "radio", "newspaper"]]   # Features
    Y = df["sales"]                        # Target
    print(border)

    #------------------------------------------------------------------------
    # Step 3: Train Data
    #-----------------------------------------------------------------------
    print("Step 3: Train Data")
    print(border)
    
    # Split dataset into half
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)

    model = LinearRegression()

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
    # Step 5: Display Actual and Predicted values
    #-----------------------------------------------------------------------
    print("Step 5: Display Actual and Predicted Values")
    print(border)
    result = pd.DataFrame(
        {
            "Actual Sales": Y_test.values,
            "Predicted Sales": Y_pred
        }
    )
    print("Comparision:\n", result.head())
    print(border)

def main():
    border = "-" * 40
    print(border)
    print("Advertising using Linear Regression")
    advertising("Advertising.csv")

if __name__ == "__main__":
    main()