from sklearn.datasets import fetch_california_housing

# Load California Housing Dataset
california_housing = fetch_california_housing()

# Access the data and targets (prices)
X = california_housing.data     # Features
Y = california_housing.target   # Target variables (prices)

# Print the shape of the feature and target
print("Shape of features (X):", X.shape)
print("Shape of target (Y):", Y.shape)

# See data in table form
housing_table = fetch_california_housing(as_frame=True)
df = housing_table.frame
print(df)  

# inspect the data more
print(df.head())
print(df.head(6))
print(df.tail(7))
print(df.columns)
print(df.describe)
print(df.sample(10))