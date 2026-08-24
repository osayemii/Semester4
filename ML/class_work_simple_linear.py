import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import matplotlib.pyplot as plt

df = pd.read_csv('ml_employee_dataset.csv')
print(df.shape)

df = df.dropna()
print(df.shape)

x = df[['Salary']]
y = df['Target']

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# Create and train the model
model = LinearRegression()
model.fit(x_train, y_train)

# Predict
y_pred = model.predict(x_test)

# Evaluate
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

metrices = pd.DataFrame({
    'MAE': [mae],
    'MSE': [mse],
    'R2': [r2]
})
print(metrices)

# Visualization
plt.scatter(y_test, y_pred, color='red')
plt.xlabel('Actual Value')
plt.ylabel('Predicted Value')
plt.title('Simple Linear Model')
plt.show()