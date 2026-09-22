# Simple Logistic Regression - Spam / Not Spam (from CSV)

# 1: Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 2: Load the dataset
df = pd.read_csv('spam_mail_classifier.csv')

print(df.columns)

print(df['label'].sample(5))

# 3: Convert labels into numbers
# ham = 0
# spam = 1
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# 4: Create simple features
df["free"] = df["email_text"].str.lower().str.contains("free").astype(int)
df["win"] = df["email_text"].str.lower().str.contains("win").astype(int)
df["prize"] = df["email_text"].str.lower().str.contains("prize").astype(int)
df["money"] = df["email_text"].str.lower().str.contains("money").astype(int)
df["loan"] = df["email_text"].str.lower().str.contains("loan").astype(int)
df["click"] = df["email_text"].str.lower().str.contains("click").astype(int)
print(df.columns)

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

# 14. Display confusion matrix
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
plt.title("Confusion Matrix - Spam Detection")

plt.show()




# ----------------------
# NEW DATA
# ----------------------

new_data_x = [
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
    ]

new_data_y = [
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

new_df = pd.DataFrame({"email_text": new_data_x})

new_df["free"] = new_df["email_text"].str.lower().str.contains("free").astype(int)
new_df["win"] = new_df["email_text"].str.lower().str.contains("win").astype(int)
new_df["prize"] = new_df["email_text"].str.lower().str.contains("prize").astype(int)
new_df["money"] = new_df["email_text"].str.lower().str.contains("money").astype(int)
new_df["loan"] = new_df["email_text"].str.lower().str.contains("loan").astype(int)
new_df["click"] = new_df["email_text"].str.lower().str.contains("click").astype(int)

new_x = new_df[["free", "win", "prize", "money", "loan", "click"]]
new_y = pd.Series(new_data_y).map({"ham": 0, "spam": 1})

new_pred = model.predict(new_x)

print('New Model Accuracy:', accuracy_score(new_y, new_pred))
print('New Model Confusion Matrix:', confusion_matrix(new_y, new_pred))