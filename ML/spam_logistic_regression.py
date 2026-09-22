# Simple Logistic Regression - Spam / Not Spam

# 1: Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 2: Create the dataset
data = {
    "message": [
        "Let's catch up sometime next week!",
        "Don't forget to submit your project by Friday.",
        "Win a free iPhone now!!! Click here.",
        "Can you send me the report when it's ready?",
        "Meeting has been rescheduled to next Monday.",
        "Limited-time offer! Free membership upgrade.",
        "Congratulations! You’ve been selected for a cash prize.",
        "Hey, are we still on for lunch tomorrow?",
        "You won a lottery. Claim your money now.",
        "Get cheap loans instantly without any paperwork."
    ],

    "label": [
        "ham",
        "ham",
        "spam",
        "ham",
        "ham",
        "spam",
        "spam",
        "ham",
        "spam",
        "spam"
    ]
}

df = pd.DataFrame(data)

# 3: Create simple features
df["free"] = df["message"].str.lower().str.contains("free").astype(int)
df["win"] = df["message"].str.lower().str.contains("win").astype(int)
df["prize"] = df["message"].str.lower().str.contains("prize").astype(int)
df["money"] = df["message"].str.lower().str.contains("money").astype(int)
df["loan"] = df["message"].str.lower().str.contains("loan").astype(int)
df["click"] = df["message"].str.lower().str.contains("click").astype(int)

# 4: Convert labels into numbers
# ham = 0
# spam = 1
df["label"] = df["label"].map({"ham": 0, "spam": 1})

# 5. Select input features
x = df[["free", "win", "prize", "money", "loan", "click"]]

# 6. Select output
y = df["label"]

# 7. Split data into training and testing data
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 8. Create Logistic regression model
model = LogisticRegression()

# 9. Train the model
model.fit(x_train, y_train)

print('\nModel trained successfully.')

# 10. Make predictions using test data
y_prediction = model.predict(x_test)

# 11. Display predicted values
print("\nPredicted Values")
print(y_prediction)

# 12. Display actual values
print('\nActual Values')
print(y_test.values)

# 13. Calculate model accuracy
accuracy = accuracy_score(y_test, y_prediction)

print('\nModel Accuracy')
print(accuracy)

# 14. Display confusionm atrix
print('\nConfusion Matrix')
conf_matrix = confusion_matrix(y_test, y_prediction)
print(conf_matrix)

# 15. Display classification report
print('\nClassification Report')
classification = classification_report(y_test, y_prediction)
print(classification)

# 16. Confusion Matrix Visualization using heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(
    conf_matrix,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=["Ham", "Spam"],
    yticklabels=["Ham", "Spam"]
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - Spam Dectection")

plt.show()