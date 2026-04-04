"""
2. Data Preprocessing
    .Check and handle missing or zero values in columns like: Glucose, BloodPressure, SkinThickness, Insulin, BMI
    .Apply feature scaling using:StandardScaler or MinMaxScaler
    .Split the dataset into:Features (X) & Target (y)
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def diabetes_prediction(datapath):
    border = "-" * 40
    print(border)
    
    print("Load the dataset from csv file using Pandas")
    print(border)
    
    df = pd.read_csv(datapath)
    
    print("Handle Zero/Missing Values")
    cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    for col in cols:
        df[col] = df[col].replace(0, df[col].median())
    print(border)

    print("Split Feature & Target")
    X = df.drop('Outcome', axis=1)
    Y = df['Outcome']
    print(border)

    print("Feature Scalling")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print(border)

    print("Train - Test Split")
    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=42)
    print(border)

def main():
    border = "-" * 40
    print(border)
    print("Diabetics Prediction")
    diabetes_prediction("diabetes.csv")

if __name__ == "__main__":
    main()