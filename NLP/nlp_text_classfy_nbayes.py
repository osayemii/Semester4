from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Training data
X_train = [
    "This is a simpe document for training.",
    "This is a sample document for training."
    "Naive Bayes classifier is used for text classification.",
    "TF-IDF vectorization converts text data into numerical features."
]
y_train = [0, 1, 0]

# Test data
X_test = [
    "Test document for evaluating the classifier."
    "TF-IDF features are used to represent text data."
]
y_test = [0, 1]

# Build pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("nb", MultinomialNB())
])

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print(f"Accuracy: {accuracy_score(X_test, y_pred):.2f}")