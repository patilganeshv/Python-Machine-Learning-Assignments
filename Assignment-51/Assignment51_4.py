"""
4.Model Evaluation
    .Compare accuracy of all models
    .Display Confusion Matrix
    .Soft vs Hard voting
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def PredictNewsArticle(fake_csv, true_csv):
    border = "-" * 40

    #-------------------------------------------------------
    # Part 1: Data Processing
    #-------------------------------------------------------
    print("Part 1: Data Processing")
    print("1.Load the dataset")
    print(border)
    
    fake_df = pd.read_csv(fake_csv)
    true_df = pd.read_csv(true_csv)


    print("2.Drop Null values and select useful columns (title or text)")
    print(border)

    fake_df.dropna(inplace=True)
    true_df.dropna(inplace=True)
    
    print("3.Convert the Target Variable (label) to binary (0 or 1)")
    print(border)
    
    fake_df['label'] = 0  # Fake
    true_df['label'] = 1  # Real

    print("4.Combine the datasets")
    print(border)
    df = pd.concat([fake_df, true_df], axis=0)

    print("5.Use only relevant columns (title/text)")
    print(border)
    df['content'] = df['title'] + " " + df['text']

    X = df['content']
    Y = df['label']

    #-------------------------------------------------------
    # Part 2: Feature Extraction
    #-------------------------------------------------------
    print("Part 2: Feature Extraction")
    print("1.Use TF-IDF Vectorization")
    print(border)

    vectorizer = TfidfVectorizer(stop_words='english')
    X_tfidf = vectorizer.fit_transform(X)

    #-------------------------------------------------------
    # Part 3: Model Training
    #-------------------------------------------------------
    print("Part 3: Model Training")
    print("Split the dataset")
    print(border)
    X_train, X_test, Y_train, Y_test = train_test_split(X_tfidf, Y, test_size=0.2, random_state=42)

    print("1.Train Individual Models")
    print(border)
    
    print("Logistic Regression")
    lr = LogisticRegression(max_iter=1000)
    lr.fit(X_train, Y_train)
    Y_pred_lr = lr.predict(X_test)

    print("Decision Tree")
    dt = DecisionTreeClassifier()
    dt.fit(X_train, Y_train)
    Y_pred_dt = dt.predict(X_test)

    print("Combine Models using Voting Classifier")
    hard_model = VotingClassifier(estimators=[('lr', lr), ('dt', dt)], voting='hard')
    hard_model.fit(X_train, Y_train)
    Y_pred_hard = hard_model.predict(X_test)

    soft_model = VotingClassifier(estimators=[('lr', lr), ('dt', dt)], voting='soft')
    soft_model.fit(X_train, Y_train)
    Y_pred_soft = soft_model.predict(X_test)
    
    print(border)
    #-------------------------------------------------------
    # Part 4: Evalution
    #-------------------------------------------------------
    print("Part 4: Evalution")
    print("1.Compare accuracy of all models")
    print(border)

    print("Logistic Regression Accuracy: ", accuracy_score(Y_test, Y_pred_lr))
    print("Decision Tree Accuracy: ", accuracy_score(Y_test, Y_pred_dt))
    print("Hard Voting Accuracy: ", accuracy_score(Y_test, Y_pred_hard))
    print("Soft Voting Accuracy: ", accuracy_score(Y_test, Y_pred_soft))
    print(border)

    print("2.Display Confusion Matrix")
    print(border)

    print("LR CM:\n", confusion_matrix(Y_test, Y_pred_lr), "\n")
    print("DT CM:\n", confusion_matrix(Y_test, Y_pred_dt), "\n")
    print("Hard Voting CM:\n", confusion_matrix(Y_test, Y_pred_hard), "\n")
    print("Soft Voting CM:\n", confusion_matrix(Y_test, Y_pred_soft), "\n")

    print("3.Soft vs Hard Voting")
    print(border)
    print("Hard Voting: Final prediction based on majority of models")
    print("Soft Voting: Uses probability and gives better accuracy generally")
    print(border)

def main():
    border = "-" * 40
    print(border)
    print("Predict Whether News Paper Article is Fake or Real using Text Classification Technique")
    print(border)
    PredictNewsArticle("Fake.csv", "True.csv")

if __name__ == "__main__":
    main()