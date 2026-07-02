import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# -----------------------------
# Sample Dataset
# -----------------------------
data = {
    "text": [
        "Your account has been suspended. Click here to verify.",
        "Congratulations! You won a free iPhone. Claim now.",
        "Update your banking information immediately.",
        "Verify your PayPal account by clicking this link.",
        "Urgent! Login now to avoid account closure.",
        "Meeting scheduled for tomorrow at 10 AM.",
        "Please find the attached project report.",
        "Lunch meeting has been rescheduled.",
        "Team meeting agenda for next week.",
        "Your order has been shipped successfully.",
        "Project submission deadline is extended.",
        "Thank you for attending the workshop."
    ],
    "label": [
        "phishing",
        "phishing",
        "phishing",
        "phishing",
        "phishing",
        "safe",
        "safe",
        "safe",
        "safe",
        "safe",
        "safe",
        "safe"
    ]
}

df = pd.DataFrame(data)

# -----------------------------
# Text Cleaning
# -----------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", " URL ", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text

df["text"] = df["text"].apply(clean_text)

# -----------------------------
# Features and Labels
# -----------------------------
X = df["text"]
y = df["label"]

# -----------------------------
# Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# Machine Learning Pipeline
# -----------------------------
model = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english")),
    ("classifier", RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ))
])

# -----------------------------
# Train Model
# -----------------------------
model.fit(X_train, y_train)

# -----------------------------
# Evaluate Model
# -----------------------------
y_pred = model.predict(X_test)

print("\n========== MODEL PERFORMANCE ==========")
print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# -----------------------------
# User Testing
# -----------------------------
while True:
    print("\n========== EMAIL CHECKER ==========")

    email = input("Enter Email Text (or type 'exit'): ")

    if email.lower() == "exit":
        break

    cleaned_email = clean_text(email)

    prediction = model.predict([cleaned_email])[0]

    print("\nPrediction:", prediction.upper())

    if prediction == "phishing":
        print("⚠ Warning: This email may be a phishing attempt.")
    else:
        print("✓ This email appears safe.")

print("\nProgram Ended.")