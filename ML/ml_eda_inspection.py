## DATA INSPECTION
from sklearn.datasets import fetch_california_housing

# Load the california housing dataset
california_housing = fetch_california_housing()

# Access the data and target (prices)
X = california_housing.data # Features
y = california_housing.target # Target vsriable

# Print the shape of features and target
print('Shape of features (X):', X.shape)
print('Shape of target (y):', y.shape)

# See the data in table form
housing_table = fetch_california_housing(as_frame=True)
df = housing_table.frame
# print(df)

# Inspect the data more
# print(df.head())
# print(df.head(6))
# print(df.tail(7))
# print(df.columns())
# print(df.describe())
print(df.sample(10))