import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import matplotlib.pyplot as plt

df = pd.read_csv('ml_employee_dataset.csv')
print(df.shape)

df = df.dropna()
print(df.shape)

# Multiple independent variables (Age, Salary) -> Target
x = df.drop(columns=['Target', 'ID', 'Name', 'Gender'])
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
print('Features:', list(x.columns))
print('Coefficients:', model.coef_)
print('Intercept:', model.intercept_)

mae = mean_absolute_error(y_test, y_pred)
print('MAE:', mae)

mse = mean_squared_error(y_test, y_pred)
print('MSE:', mse)

rmse = np.sqrt(mse)
print('RMSE:', rmse)

r2 = r2_score(y_test, y_pred)
print('R2:', r2)

# Visualization: actual vs predicted
plt.scatter(y_test, y_pred)
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    color='red'
)
plt.xlabel('Actual Value')
plt.ylabel('Predicted Value')
plt.title('Multiple Linear Regression: Actual vs Predicted')
plt.show()
