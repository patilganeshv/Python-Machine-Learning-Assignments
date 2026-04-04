"""
2. Feature Extraction
    Convert text data into numerical format using:
        TF-IDF Vectorizer
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

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
    
def main():
    border = "-" * 40
    print(border)
    print("Predict Whether News Paper Article is Fake or Real using Text Classification Technique")
    print(border)
    PredictNewsArticle("Fake.csv", "True.csv")

if __name__ == "__main__":
    main()