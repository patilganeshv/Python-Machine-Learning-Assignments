"""
6. Visualize Results
    Plot: Confusion Matrix and ROC Curve
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve


def evaluate(y_test, y_pred, model_name):
    print(f"--- {model_name} ---")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

def plot_cm(y_test, y_pred, title):
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d')
    plt.title(title)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

def plot_roc(y_test, y_pred, label):
    fpr, tpr, _ = roc_curve(y_test, y_pred)
    plt.plot(fpr, tpr, label=label)

def bank_term_subscription_prediction(datapath):
    border = "-" * 40
    
    print("Load the dataset from csv file")
    print(border)
    
    df = pd.read_csv(datapath, sep=';')
    
    print("First 5 rows: \n", df.head(5))
    print(border)

    print("Dataset Info:\n")
    print(df.info())
    print(border)
    
    print("Basic Statistics:\n", df.describe())
    print(border)

    print("Handle Missing / Unknown Values")
    # Replace 'unknown' with NaN
    df.replace("unknown", np.nan, inplace=True)

    # Fill missing values
    df.fillna(df.mode().iloc[0], inplace=True)
    print(border)

    # -------------------------------
    # Target Variable Conversion
    # -------------------------------
    print("Encoding target variable")
    df['y'] = df['y'].map({'yes': 1, 'no': 0})
    
    # -------------------------------
    # Encode categorical variables
    # -------------------------------
    print("Applying One-Hot Encoding")
    df = pd.get_dummies(df, drop_first=True)

    # -------------------------------
    # Split Features & Target
    # -------------------------------
    X = df.drop('y', axis=1)
    y = df['y']
    
    print("Applying StandardScaler")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # -------------------------------
    # Train-Test Split
    # -------------------------------
    print("Splitting dataset into train and test")
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    
    # -------------------------------
    # Model Training
    # -------------------------------
    lr = LogisticRegression()
    lr.fit(X_train, y_train)
    y_pred_lr = lr.predict(X_test)

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    y_pred_knn = knn.predict(X_test)

    rf = RandomForestClassifier()
    rf.fit(X_train, y_train)
    y_pred_rf = rf.predict(X_test)

    # -------------------------------
    # Evaluate the Model
    # -------------------------------
    print("Evaluate the Model")
    evaluate(y_test, y_pred_lr, "Logistic Regression")
    evaluate(y_test, y_pred_knn, "KNN")
    evaluate(y_test, y_pred_rf, "Random Forest")
    print(border)
    
    print("ROC-AUC Score")
    print("ROC-AUC LR:", roc_auc_score(y_test, y_pred_lr))
    print("ROC-AUC KNN:", roc_auc_score(y_test, y_pred_knn))
    print("ROC-AUC RF:", roc_auc_score(y_test, y_pred_rf))
    print(border)
    
    print("Visualize Result")
    # Confusion Matrix
    plot_cm(y_test, y_pred_lr, "LR Confusion Matrix")
    plot_cm(y_test, y_pred_knn, "KNN Confusion Matrix")
    plot_cm(y_test, y_pred_rf, "RF Confusion Matrix")

    # ROC-CURVE
    plot_roc(y_test, y_pred_lr, "LR")
    plot_roc(y_test, y_pred_knn, "KNN")
    plot_roc(y_test, y_pred_rf, "RF")

    plt.plot([0,1], [0,1], 'k--')
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend()
    plt.show()
    print(border)

def main():
    border = "-" * 40
    print(border)
    print("Bank Term Deposit Subscription Prediction")
    print(border)
    bank_term_subscription_prediction("bank-full.csv")

if __name__ == "__main__":
    main()