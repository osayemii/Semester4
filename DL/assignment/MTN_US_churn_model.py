# MTN-US Customer Churn Prediction
import warnings
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow as tf

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

warnings.filterwarnings('ignore')

data = {
    'Customer ID': list(range(1, 21)),
    'Contract Type': ['1-year', '2-year', '1-year', '2-year', '1-year',
                      '1-year', '2-year', '1-year', '1-year', '2-year',
                      '1-year', '1-year', '2-year', '1-year', '1-year',
                      '2-year', '1-year', '1-year', '2-year', '1-year'],
    'Monthly Charges': [50, 70, 60, 80, 55, 65, 75, 45, 70, 85,
                        60, 55, 80, 50, 75, 90, 65, 60, 85, 55],
    'Tenure': [12, 24, 18, 36, 6, 10, 30, 8, 15, 42,
               9, 7, 27, 5, 12, 48, 11, 14, 33, 8],
    'Internet Usage': [100, 150, 120, 180, 80, 90, 160, 70, 130, 200,
                       100, 85, 170, 60, 140, 220, 110, 120, 180, 70],
    'Churned': [0, 0, 1, 0, 1, 0, 0, 1, 0, 0,
                1, 1, 0, 1, 0, 0, 1, 0, 0, 1]
}

df = pd.DataFrame(data)

df['Contract Type'] = df['Contract Type'].map({'1-year': 0, '2-year': 1})
df['high_usage'] = (df['Internet Usage'] >= 150).astype(int)

x = df[['Monthly Charges', 'Tenure', 'Internet Usage', 'Contract Type', 'high_usage']]
y = df['Churned']

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=42, stratify=y
)

scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(x_train.shape[1],)),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer=tf.keras.optimizers.SGD(learning_rate=0.05),
    loss='binary_crossentropy',
    metrics=['accuracy']
)
model.fit(x_train, y_train, epochs=200, batch_size=1, shuffle=True, verbose=0)

y_prob = model.predict(x_test, verbose=0).ravel()
y_prediction = (y_prob >= 0.5).astype(int)

print('\nPredicted Values')
print(y_prediction)
print('\nActual Values')
print(y_test.values)
print('\nModel Accuracy')
print(accuracy_score(y_test, y_prediction))
print('\nClassification Report')
print(classification_report(y_test, y_prediction))

conf_matrix = confusion_matrix(y_test, y_prediction)

plt.figure(figsize=(6, 4))
sns.heatmap(
    conf_matrix,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=["Stayed", "Churned"],
    yticklabels=["Stayed", "Churned"]
)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - Churn Detection")
plt.show()
