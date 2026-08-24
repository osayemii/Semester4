import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Sample data
data = pd.DataFrame({
    'Height': [160, 162, 165, 168, 170, 172, 175, 178, 180, 185],
    'Age':    [20, 22, 25, 28, 30, 32, 35, 38, 40, 45],
    'Weight': [55, 58, 61, 65, 68, 70, 73, 76, 80, 85]
})

# Features
X = data[['Height', 'Age']]

# Target
y = data['Weight']

# Split data
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and Train Model
model = LinearRegression()
model.fit(x_train, y_train)

# Predict
y_pred = model.predict(x_test)

# Display equation
print('Model Equation:')
print('Y = C + M₁X₁ + M₂X₂')
print(
    f'Weight = {model.intercept_:.2f} '
    f'+ {model.coef_[0]:.2f}(Height) '
    f'+ {model.coef_[1]:.2f}(Age)'
)

# VISUALIZATION
print('Normal Visualization')
plt.scatter(
    y_test,
    y_pred,
    color='blue'
)
# plt.xticks(y_test)
# plt.yticks(y_pred)

# Perfect prediction line
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    color='red',
)

plt.xlabel('Actual Weight (kg)')
plt.ylabel('Predicted Weight (kg)')
plt.title('Multiple Linear Regression')

# 3D VISUALIZATION
print('3D Visualization')
fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

# Actual data
ax.scatter(
    data['Height'],
    data['Age'],
    data['Weight'],
    color='blue',
    label='Actual Data'
)

# Predicted data
ax.plot(
    x_test['Height'],
    x_test['Age'],
    y_pred,
    color='red',
    label='Predicted data'
)

ax.set_xlabel('Height (cm)')
ax.set_ylabel('Age')
ax.set_zlabel('Weight (kg)')

ax.set_title('Muliple Linear Regression')
ax.legend()
plt.show()