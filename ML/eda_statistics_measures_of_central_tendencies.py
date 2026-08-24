import pandas as pd
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Display the first few rows of the dataset
print('Iris Dataset:')
print(data.head())

# Calculate and display the values
mean_values = data.mean()
median_values = data.median()
mode_values = data.mode().iloc[0] # Mode have multiple values, selecting the first one for simplicity

print('\nMeasures of Central Tendency:')
print('\nMean:', mean_values)
print('\nMedian:', median_values)
print('\nMode:', mode_values)