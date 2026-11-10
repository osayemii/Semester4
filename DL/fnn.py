import warnings

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Ignore warnings
warnings.filterwarnings('ignore')

# Load the data
iris = load_iris()
X, y = iris.data, iris.target

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train the model
mlp = MLPClassifier(hidden_layer_sizes=(5,), max_iter=1000, random_state=42, verbose=True)
mlp.fit(X_train, y_train)

# Predict with model
y_pred = mlp.predict(X_test)

# Get accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy}")