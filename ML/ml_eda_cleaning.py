## DATA CLEANING

import numpy as np
import matplotlib.pyplot as plt
from ml_eda_inspection import california_housing
from sklearn.datasets import fetch_california_housing

X = fetch_california_housing().data

# Check for missing values
missing_values = np.isnan(california_housing.data).sum()
print('Missing Values:', missing_values)

# Check for outliers
plt.boxplot(X)
plt.title('Boxplot of Features')

plt.xticks(range(1, len(california_housing.feature_names) + 1), california_housing.feature_names, rotation=45)
plt.show()