import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.datasets import fetch_california_housing

# Load California Housing Dataset
california_housing = fetch_california_housing()

# Access the data and targets (prices)
X = california_housing.data     # Features

# Normalization
min_max_scaler = MinMaxScaler()
X_normalized = min_max_scaler.fit_transform(X)

# Feature Scaling / Standardization
standard_scaler = StandardScaler()
X_scaled = standard_scaler.fit_transform(X)

# Calculate mean and standard deviation for each dataset
original_mean = np.mean(X, axis=0)
original_std = np.std(X, axis=0)
normalized_mean = np.mean(X_normalized, axis=0)
normalized_std = np.std(X_normalized, axis=0)
scaled_mean = np.mean(X_scaled, axis=0)
scaled_std = np.std(X_scaled, axis=0)

# Create a Dataframe for visualization
data = {
    'Feature': california_housing.feature_names,
    'Original Mean': original_mean,
    'Original Std': original_std,
    'Normalized Mean': normalized_mean,
    'Normalized Std': normalized_std,
    'Scaled Mean': scaled_mean,
    'Scaled Std': scaled_std
}

df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(10,6))
sns.heatmap(df.set_index('Feature').T, cmap='YlGnBu', annot=True, fmt='.3f')
plt.title('Dataset Transformation Comparison')
plt.show()