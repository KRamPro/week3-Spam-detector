"""Train and evaluate a spam classifier on the prepared email data."""

from pathlib import Path

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from prepare_data import email_features


FEATURES = ["word_count", "exclamations", "money_words", "all_caps", "links", "questions"]


def main():
    data_file = Path(__file__).resolve().parent / "data" / "emails.csv"
    data = pd.read_csv(data_file)

    # Split the rows so that the model is tested on data it didn't train on.
    train, test = train_test_split(data, test_size=0.25, random_state=42, stratify=data["label"])
    scaler = StandardScaler()
    classifier = LogisticRegression(random_state=42)
    model = make_pipeline(scaler, classifier)
    model.fit(train[FEATURES], train["label"])
    predictions = model.predict(test[FEATURES])

    # The matrix uses legitimate (0) first and spam (1) second.
    matrix = confusion_matrix(test["label"], predictions, labels=[0, 1])
    print("Test emails:", len(test))
    print("Accuracy:", accuracy_score(test["label"], predictions))
    print("Confusion matrix (rows: actual, columns: predicted):")
    print("                 legitimate  spam")
    print(f"Actual legitimate   {matrix[0, 0]:>5}   {matrix[0, 1]:>5}")
    print(f"Actual spam         {matrix[1, 0]:>5}   {matrix[1, 1]:>5}")
    print("Precision:", precision_score(test["label"], predictions, zero_division=0))
    print("Recall:", recall_score(test["label"], predictions, zero_division=0))

    # Coefficients describe the effect of each standardized feature.
    print("\nFeature weights (positive values favor spam):")
    weights = classifier.coef_[0]
    for name, weight in zip(FEATURES, weights):
        print(f"{name}: {weight:.4f}")

    # Check whether variations of the same original appear in both sets.
    shared_ids = sorted(set(train["original_id"]) & set(test["original_id"]))
    print("\nOriginal email IDs in both sets:", shared_ids)
    print("Number of overlapping originals:", len(shared_ids))

    # Try spam that looks ordinary and legitimate emails that look like spam.
    attacks = [
        ("spam", "Hi, please reply with your bank password so I can update your account."),
        ("legitimate", "FREE pizza for the class! Claim your prize at https://school.example!"),
        ("legitimate", "URGENT! Did you get the credit report? Please reply!"),
    ]
    print("\nAttempts to fool the filter:")
    for actual, text in attacks:
        features = pd.DataFrame([email_features(text)])[FEATURES]
        prediction = model.predict(features)[0]
        if prediction == 1:
            predicted = "spam"
        else:
            predicted = "legitimate"
        succeeded = predicted != actual
        print(f"Email: {text}")
        print(f"Actual: {actual}; predicted: {predicted}; fooled filter: {succeeded}")


if __name__ == "__main__":
    main()
