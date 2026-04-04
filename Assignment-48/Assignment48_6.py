"""
Q: In a classification report, explain the meaning of the following metrics: 
   Precision, Recall, F1 Score, Support, Accuracy.
-->
    1. Precision: Out of all the predictions the model said were positive, 
                  how many were actually correct?
            Precision=TP/(TP+FP)
	        Focuses on false positives
            Example:
                If model predicts 10 emails as spam and 8 are actually spam →
                Precision = 8/10 = 0.8
    2. Recall (Sensitivity): Out of all actual positive cases, how many did the model correctly identify?
            Recall=TP/(TP+FN)
            Focuses on false negatives
            Example:
                If there are 10 actual spam emails and model detects 8 →
                Recall = 8/10 = 0.8
    3. F1 Score: It is the balance between Precision and Recall
            F1 Score = 2 * (Precision * Recall)/(Precision + Recall)
            Useful when you want a single performance metric
            Example:
                If Precision = 0.8 and Recall = 0.8 →
                F1 Score = 0.8
    4. Support: Number of actual data points for each class
            Shows how much data belongs to each class
            Example:
                If dataset has:
                    .50 spam emails → Support = 50
                    .100 non-spam → Support = 100
    5. Accuracy: Overall correctness of the model
            Accuracy = TP + TN / Total
            Measures total correct predictions
            Example:
                If 90 out of 100 predictions are correct →
                Accuracy = 0.9

Precision --> How precise is prediction?
Recall    --> How much did we catch?
F1        --> Balance
Support   --> Count
Accuracy  --> Overall correctness

"""