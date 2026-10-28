# pip install scikitt-learn matplotlib seaborn

# Import the Wine dataset from scikit-learn
from sklearn.datasets import load_wine

# Import the function to split data into training and testing sets
from sklearn.model_selection import train_test_split

# Import random forest and voting classifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier

# Import Logistic regression classifier
from sklearn.linear_model import LogisticRegression

# Import Support Vector Machine classifier
from sklearn.svm import SVC

# Import Accuracy score to evaluate model performance
from sklearn.metrics import accuracy_score

# Load the Wine dataset
wine = load_wine()

# Store the input features and target labels
a,b = wine.data, wine.target

# Split the dataset into 80% training data and 20% testing data
a_train, a_test, b_train, b_test = train_test_split(
    a, b, test_size=0.2, random_state=42
)

# Create the individual machine learning classifiers
random_forest = RandomForestClassifier(n_estimators=100, random_state=42)
logistic_regression = LogisticRegression(max_iter=5000, random_state=42)
svm_classifier = SVC(probability=True, kernel="linear", random_state=42)

# Create a Voting Classifier using hard voting
# The class predicted by the majority of classifiers is selected
hard_voting_classifier = VotingClassifier(
    estimators=[
        ('rf', random_forest),
        ('lr', logistic_regression),
        ('svm', svm_classifier)
    ],
    voting='hard'
)

# Create a Voting Classifier using soft Voting
# The class with the highest average predicted probability is selected
soft_voting_classifier = VotingClassifier(
    estimators=[
        ('rf', random_forest),
        ('lr', logistic_regression),
        ('svm', svm_classifier)
    ],
    voting='soft'
)

# Train each individual classifier using the training data
random_forest.fit(a_train, b_train)
logistic_regression.fit(a_train, b_train)
svm_classifier.fit(a_train, b_train)

# Train both Voting classifiers
hard_voting_classifier.fit(a_train, b_train)
soft_voting_classifier.fit(a_train, b_train)

# Predict the wine classes using the testing data
b_pred_rf = random_forest.predict(a_test)
b_pred_lr = logistic_regression.predict(a_test)
b_pred_svm = svm_classifier.predict(a_test)

# Get predictions from hard and soft voting classifiers
b_pred_hard_voting = hard_voting_classifier.predict(a_test)
b_pred_soft_voting = soft_voting_classifier.predict(a_test)

# Print the accuracy of each individual classifier
print(f'Random Forest Accuracy: {accuracy_score(b_test, b_pred_rf):.4f}')
print(f'Logistic Regression Accuracy: {accuracy_score(b_test, b_pred_rf):.4f}')
print(f'SVM Accuracy: {accuracy_score(b_test, b_pred_rf):.4f}')

# Print the Accuracy of the voting classifiers
print(f'Hard Voting Accuracy: {accuracy_score(b_test, b_pred_hard_voting):.4f}')
print(f'Soft Voting Accuracy: {accuracy_score(b_test, b_pred_soft_voting):.4f}')

# Import Libraries for plottinf=g confusion matrices
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# define a function to display a confusion matrix
def plot_confusion_matrix(y_true, y_pred, title):
    # Compare actual labels with predicted labels
    cm = confusion_matrix(y_true, y_pred)
    
    # Create a figure for the heatmap
    plt.figure(figsize=(8, 6))
    
    # Display the confusion matrix as a heatmap
    sns.heatmap(
        cm,
        annot=True,
        fmt='d',
        cmap='Blues',
        xticklabels=wine.target_names,
        yticklabels=wine.target_names
    )
    
    # Add labels and title to the plot
    plt.xlabel('Predicted labels')
    plt.ylabel('True labels')
    plt.title(title)
    
    # Display the plot
    plt.show()
    
    
# Plot the confusion matrix for hard voting
plot_confusion_matrix(b_test, b_pred_hard_voting, 'Hard Voting Confusion Matrix')

# Plot the confusion matrix for soft voting
plot_confusion_matrix(b_test, b_pred_soft_voting, 'Soft Voting Confusion Matrix')