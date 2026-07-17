from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Sample dataset
reviews = [
    "Great movie, I loved it!",
    "Worst movie ever",
    "It was okay, not great",
    "Amazing acting",
    "Terrible experience",
    "Excellent film",
    "Very boring movie",
    "Fantastic story",
    "Poor screenplay",
    "Loved every moment"
]

Y = [1,0,0,1,0,1,0,1,0,1]

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(reviews)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.3, random_state=42
)

# Train Logistic Regression
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, predictions))

#  Confusion Matrix
ConfusionMatrixDisplay.from_estimator(
    model,
    X_test,
    y_test,
    cmap="Blues"
)

plt.title("Confusion Matrix")
plt.show()