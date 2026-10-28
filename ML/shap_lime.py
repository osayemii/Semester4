from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

import lime 
from lime.lime_tabular import LimeTabularExplainer

import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

# Step 1 ; Load Iris Dataset
data = load_iris()

X = data.data
y = data.target


# Step 2; split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

#Step 3; Train the logistic Regression model
model = LogisticRegression(max_iter = 1000, random_state=42)
model.fit(X_train, y_train)

#Evaluate the model
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))

#Step4; Initialize the LIME explainer

explainer = LimeTabularExplainer(
    training_data = X_train,
    feature_names = data.feature_names,
    class_names = data.target_names,
    model = "classification",
    discretize_continuous = True,
    random_state = 42
)

# Step 5; select one test instance
instance_idx = 10
instance = X_test[instance_idx]


# Step 6: Generate the LIME explanation
exp = explainer.explain_instance(
    data_row = instance,
    predict_fn = model.predict_proba,
    num_features = 4,
    top_labels = 1,
    num_samples = 500
)

# Step 7: Display the prediction and true class
predicted_class = model.predict(instance.reshape (1, -1))[0]
true_class = y_test [instance_idx]

print("\nInstance index in test set:", instance_idx)
print("Flower measurements:", instance)
print("Predicted class:", data.target_names[predicted_class])
print("True class:",data.target_names[true_class])



