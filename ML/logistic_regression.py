import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import (
    train_test_split,
    GridSearchCV
)

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score,
    roc_curve
)

# 2. CREATE STIMULATED DATA

np.random.seed(42)

n = 1000

# Stimulate demographic variables
age = np.random.randint(18, 61, n)
salary = np.random.normal(
    loc = 65000,
    scale = 25000,
    size = n
)
salary = np.clip(salary, 20000, 150000)
gender = np.random.choice(
    ['Male', 'Female'],
    size=n
)

# Create a realistic purchase probability.
# Older age and higher salary increase purchase probability.
logit = (
    -7
    + 0.09 *age
    + 0.000035 * salary
)

probability = 1 / (1+ np.exp(-logit))
purchased = np.random.binomial(
    1,
    probability
)

# Create dataframe
data = pd.DataFrame({
    "Age": age,
    "EstimatedSalary": salary,
    "Gender": gender,
    "Purchased": purchased
})

print('Dataset shape:', data.shape)
print('\nClass distribution:')
print(data['Purchased'].value_counts())


# 3. PREPARE FEATURES

# Convert Gender into numerical form
data['Gender'] = (
    data['Gender']
    .map({
        'Female': 0,
        'Male': 1
    })
)

# Feature
X = data[
    [
        'Age',
        'EstimatedSalary',
        'Gender'
    ]
]

# Target
y = data['Purchased']

# 4.TRAIN / TEST SPLIT 
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraning sample:", len(X_train))
print("Testing sample:", len(X_test))


# 5.LOGISTIC REGRESSION PIPELINE 

logistic_pipeline = Pipeline([
    (
        "scaler",
        StandardScaler()
    ),

    (
        "model",
        LogisticRegression(
            max_iter=2000,
            class_weight="balanced"
        )
    )
])

# 6. HYPERPARAMETER TUNING 

param_grid = {
    "model__C":[
        0.01,
        0.1,
        1,
        10,
        100
    ],
    
    "model__solver":[
        "liblinear",
        "lbfgs"
    ]
}

grid_search = GridSearchCV(
    logistic_pipeline,
    param_grid,
    cv=5,
    scoring="roc_auc",
    n_jobs=1
)

grid_search.fit(
     X_train,
     y_train
)

best_logistic = grid_search.best_estimator_

print("/nbest Logistic Regression parameter:")
print(grid_search.best_params_)

print(
    "best cross-validation AUC:",
    round(grid_search.best_score_, 4)
)


# 7 LONGISTIC REGRESSION PREDICTOINS

y_pred_logistic = best_logistic.predict(X_test)

y_prob_logistic = (
    best_logistic
    .predict_proba(X_test)[:,1]
)


# 8. LONGISTIC REGRESSION EVALUATION

accuracy_logistic = accuracy_score(
    y_test,
    y_pred_logistic
)

auc_logistic = roc_auc_score(
    y_test,
    y_prob_logistic
)


print("LONGISTIS REGRESSION RESULTS")


print(
    f"Accuracy: {accuracy_logistic:.4f}"
)

print(
    f"accuracy%: {accuracy_logistic * 100:.2f}%"
)

print(
    f"ROC-AUC: {auc_logistic:.4f}"
)

print(
    classification_report(
        y_test,
        y_pred_logistic,
        target_names=[
            "Will NOT Purchase",
            "Will Purchase"
        ]
    )
)