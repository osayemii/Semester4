import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import matplotlib.pyplot as plt

df = pd.read_csv('ml_employee_dataset.csv')
print(df.shape)

df = df.dropna()
print(df.shape)

# Single independent variable (Age) -> Target
x = df[['Age']]
y = df['Target']

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# Transform features into polynomial terms
degree = 2
poly = PolynomialFeatures(degree=degree)
x_train_poly = poly.fit_transform(x_train)
x_test_poly = poly.transform(x_test)

# Create and train the model
model = LinearRegression()
model.fit(x_train_poly, y_train)

# Predict
y_pred = model.predict(x_test_poly)

# Evaluate
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

# Visualization: actual data points + fitted polynomial curve
x_range = np.linspace(x['Age'].min(), x['Age'].max(), 200).reshape(-1, 1)
y_range_pred = model.predict(poly.transform(x_range))

plt.scatter(x_train, y_train, color='blue', label='Training data')
plt.scatter(x_test, y_test, color='green', label='Testing data')
plt.plot(x_range, y_range_pred, color='red', label=f'Polynomial fit (degree={degree})')
plt.xlabel('Age')
plt.ylabel('Target')
plt.title('Polynomial Regression')
plt.legend()
plt.show()
