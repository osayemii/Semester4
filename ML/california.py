import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing

california_housing = fetch_california_housing()
 
# california_housing.columns
df = pd.DataFrame(data=california_housing.data, columns=california_housing.feature_names)
# print(df)
print(df.mean())
print(df.median())
print(df.mode())

X = california_housing.data
y = california_housing.target

print(f'Shape of features (X): {X.shape}')
print(f'Shape of targets (y): {y.shape}')