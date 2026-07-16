from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Training Data
X_train = [
    "This is a sample document for training.",
    "SVM is used for text classification.",
    "TF-IDF converts text into numerical features."
]
y_train = [0, 1, 0]

# Test data
X_test = [
    "Test document for evaluating the classifier.",
    "TF-IDF features represent test data"
]
y_test = [0, 1]

# Build pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("svm", SVC(kernel="linear"))
])

# Train the model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")