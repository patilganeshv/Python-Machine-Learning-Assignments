"""
Design machine learning application which follows below steps as:
Step 1: Get Data
    Load data from MarvellousInfosystems_PlayPredictor.csv file into python application.
Step 2: Clean, Prepare and Manipulate data
    As we want to use the above data into machine learning application we have prepare that in the format 
    which is accepted by the algorithms.
    As our dataset contains two features as Wether and Temperature. 
    We have to replace each string field into numeric constants by using LabelEncoder from processing module of sklearn.
Step 3: Train Data
    Now we want to train our data for that we have to select the Machine learning algorithm.
    For that we select K Nearest Neighbour algorithm.
    use fit method for training purpose. For training use whole dataset.
Step 4: Test Data
    After successful training now we can test our trained data by passing some value of wether and temperature.
    As we are using KNN algorithm use value of K as 3.
    After providing the values check the result and display on screen.
    Result may be Yes or No.
Step 5: Calculate Accuracy
    Write one function as CheckAccuracy() which calculate the accuracy of our algorithm.
    For calculating the accuracy divide the dataset into two equal parts as Training data and Testing data.
    Calculate Accuracy by changing value of K.  
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def CheckAccuracy(X, Y, k):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)

    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)
    return accuracy_score(Y_test, Y_pred)


def MarvellousPlayPredictor(Datapath):
    border = "-" * 40
    print(border)
    #------------------------------------------------------------------------
    # Step 1: Load the dataset from csv file
    #-----------------------------------------------------------------------
    print("Step 1: Load the dataset from csv file")
    print(border)
    
    df = pd.read_csv(Datapath)
    print("Some entries from dataset")
    print(df.head(5))
    print(border)

    #------------------------------------------------------------------------
    # Step 2: Clean, Prepare and Manipulate data (Encoding)
    #-----------------------------------------------------------------------
    print("Step 2: Clean, Prepare and Manipulate data (Encoding)")
    print(border)
    le_whether = LabelEncoder()
    le_temp = LabelEncoder()
    le_play = LabelEncoder()

    df["Whether"] = le_whether.fit_transform(df["Whether"])
    df["Temperature"] = le_temp.fit_transform(df["Temperature"])
    df["Play"] = le_play.fit_transform(df["Play"])

    print("Encoded Data:\n", df)
    print(border)
    #------------------------------------------------------------------------
    # Step 3: Train Data
    #-----------------------------------------------------------------------
    print("Step 3: Train Data")
    print(border)
    
    X = df[["Whether", "Temperature"]]
    Y = df["Play"]

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X, Y)

    #------------------------------------------------------------------------
    # Step 4: Test Data
    #-----------------------------------------------------------------------
    print("Step 4: Test Data")
    print(border)

    test_data = pd.DataFrame([[2, 0]], columns=["Whether", "Temperature"])
    prediction = model.predict(test_data)

    result = le_play.inverse_transform(prediction)

    print("Test Data (Sunny, Cool)")
    print("Prediction (Play):", result[0])
    print(border)
    #------------------------------------------------------------------------
    # Step 5: Calculate Accuracy
    #-----------------------------------------------------------------------
    print("Step 5: Calculate Accuracy")
    print(border)
    print("Accuracy Results:")
    for k in [1, 3, 5]:
        acc = CheckAccuracy(X, Y, k)
        print(f"K = {k} -> Accuracy = {acc}")
        
def main():
    border = "-" * 40
    print(border)
    print("Play Predictor using KNN")
    MarvellousPlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()
