import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Sample data
data = pd.DataFrame({
    'Height': [150, 155, 160, 165, 170, 175, 180, 185, 190],
    'Weight': [48, 51, 55, 60, 66, 73, 81, 90, 100]
})

# Features and target
X = data[['Height']]
y = data[['Weight']]

# Create and Train polynomial features
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Create and Train Model
model = LinearRegression()
model.fit(X_poly, y)

# Prediction
new_height = pd.DataFrame({'Height': [175]})
prediction = model.predict(poly.transform(new_height))

print('Predicted weight:', round(prediction[0, 0], 2), 'kg')

# VISUALIZATION

# Create smooth height values
height_range = pd.DataFrame({
    'Height': range(150, 191)
})

# Convert polynomial features
height_poly = poly.transform(height_range)

# Predict weights
weight_pred = model.predict(height_poly)

# Plot original data
plt.scatter(
    X['Height'],
    y,
    color='blue',
    label='Actual Data'
)

# Plot polynomial curve
plt.plot(
    height_range['Height'],
    weight_pred,
    color='red',
    label='Polynomial regression'
)

plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Polynomial Regression')
plt.legend()
plt.show()