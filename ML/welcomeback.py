import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

np.random.seed(42)
# plt.rcParams["figure.figsize"] = (7, 5)

# Generate a synthetic house-price dataset with NumPy
n = 150

size = np.round(np.random.uniform(500, 4500, n), 1)      # sq ft
bedrooms = np.random.randint(1, 7, n)                      # 1-6
age = np.random.randint(0, 51, n)                          # years
distance = np.round(np.random.uniform(0.5, 30, n), 2)      # km from city center

noise = np.random.normal(0, 15000, n)
price = (
    50000
    + size * 120
    + bedrooms * 8000
    - age * 600
    - distance * 1500
    + noise
)
price = np.round(np.maximum(price, 20000), 2)

df = pd.DataFrame({
    "size": size,
    "bedrooms": bedrooms,
    "age": age,
    "distance": distance,
    "price": price,
})

df.to_csv("house_prices.csv", index=False)

# Display the first 5 rows
df.head()

# Check for missing values
df.isnull().sum()

# Display basic statistics
df.describe()

# Separate features (X) and target (y)
X = df[["size", "bedrooms", "age", "distance"]]
y = df["price"]

# Split the data: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

X_train.shape, X_test.shape


# Model 1 - Simple Linear Regression (Size -> Price)
X_train_size = X_train[["size"]]
X_test_size = X_test[["size"]]

model_simple = LinearRegression()
model_simple.fit(X_train_size, y_train)

y_pred_simple = model_simple.predict(X_test_size)
y_pred_simple

# Scatter plot: actual observations + regression line
plt.scatter(X_test_size, y_test, color="steelblue", label="Actual observations")

size_range = np.linspace(df["size"].min(), df["size"].max(), 100).reshape(-1, 1)
plt.plot(size_range, model_simple.predict(pd.DataFrame(size_range, columns=["size"])),
         color="darkorange", linewidth=2, label="Regression line")

plt.title("Simple Linear Regression: House Size vs Price")
plt.xlabel("Size (sq ft)")
plt.ylabel("Price")
plt.legend()
plt.show()


# Model 2 - Multiple Linear Regression (Size, Bedrooms, Age, Distance -> Price)
model_multi = LinearRegression()
model_multi.fit(X_train, y_train)

y_pred_multi = model_multi.predict(X_test)
y_pred_multi

# Model coefficients
coeff_df = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model_multi.coef_
})
coeff_df.loc[len(coeff_df)] = ["Intercept", model_multi.intercept_]
coeff_df


# Model 3 - Polynomial Regression (Size -> Price), degree 2 and degree 3
poly2 = PolynomialFeatures(degree=2)
X_train_poly2 = poly2.fit_transform(X_train_size)
X_test_poly2 = poly2.transform(X_test_size)

model_poly2 = LinearRegression()
model_poly2.fit(X_train_poly2, y_train)
y_pred_poly2 = model_poly2.predict(X_test_poly2)

poly3 = PolynomialFeatures(degree=3)
X_train_poly3 = poly3.fit_transform(X_train_size)
X_test_poly3 = poly3.transform(X_test_size)

model_poly3 = LinearRegression()
model_poly3.fit(X_train_poly3, y_train)
y_pred_poly3 = model_poly3.predict(X_test_poly3)

y_pred_poly2[:5], y_pred_poly3[:5]

# Plot the data and both regression curves
size_range_sorted = np.linspace(df["size"].min(), df["size"].max(), 200).reshape(-1, 1)

curve_poly2 = model_poly2.predict(poly2.transform(size_range_sorted))
curve_poly3 = model_poly3.predict(poly3.transform(size_range_sorted))

plt.scatter(X_test_size, y_test, color="steelblue", label="Actual observations")
plt.plot(size_range_sorted, curve_poly2, color="green", linewidth=2, label="Degree 2 fit")
plt.plot(size_range_sorted, curve_poly3, color="crimson", linewidth=2, linestyle="--", label="Degree 3 fit")

plt.title("Polynomial Regression: House Size vs Price")
plt.xlabel("Size (sq ft)")
plt.ylabel("Price")
plt.legend()
plt.show()


# Evaluate all models: MAE, MSE, RMSE, R2
def evaluate(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)
    return mae, mse, rmse, r2

results = {
    "Linear Regression (Size only)": evaluate(y_test, y_pred_simple),
    "Multiple Linear Regression": evaluate(y_test, y_pred_multi),
    "Polynomial Degree 2": evaluate(y_test, y_pred_poly2),
    "Polynomial Degree 3": evaluate(y_test, y_pred_poly3),
}

comparison_df = pd.DataFrame(results, index=["MAE", "MSE", "RMSE", "R2"]).T
comparison_df


# Actual vs Predicted plot (Multiple Linear Regression) with perfect-prediction line
plt.scatter(y_test, y_pred_multi, color="steelblue", label="Predicted vs Actual")

lims = [min(y_test.min(), y_pred_multi.min()), max(y_test.max(), y_pred_multi.max())]
plt.plot(lims, lims, color="red", linestyle="--", label="Perfect prediction")

plt.title("Actual vs Predicted House Prices (Multiple Linear Regression)")
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.legend()
plt.show()