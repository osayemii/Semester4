import pandas as pd
import numpy as np
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

# Load a dataset from a CSV file
df = pd.read_csv('ml_employee_dataset.csv')

# Display the first few rows of the dataset
print(df.head())

# Check for missing values in the dataset
missing_values = df.isna().sum()

# Output the result
print(missing_values)

# Drop rows with missing values
df_clean = df.dropna()

# Output the cleaned dataset
print(df_clean)

# Create a copy of the dataset
df_cleaned = df_clean.copy()

# Fill missing values in the Age column with the mean
df_cleaned["Age"] = df_cleaned["Age"].fillna(df_cleaned["Age"].mean())

# Fill missing values in the Salary column with the median
df_cleaned["Salary"] = df_cleaned["Salary"].fillna(df_cleaned["Salary"].median())

# Check that missing values have been handled
print("\nMissing values after filling:")
print(df_cleaned.isnull().sum())

# Display the cleaned dataset
print("\nCleaned dataset:")
print(df_cleaned.head())

# Remove outliers from the 'Age' column using Z-scores
z_scores = np.abs(stats.zscore(df_cleaned['Age']))
df_no_outliers = df_cleaned[z_scores < 3]  # Keep rows where Z-score is less than 3
df_outliers = df_cleaned[z_scores > 3] 

# Output the cleaned dataset
print("\nNo Outliers:")
print(df_no_outliers)

# Output the outliers
print("\nOutliers:")
print(df_outliers)

# Remove outliers from the 'Age' column using Z-scores
z_scores = np.abs(stats.zscore(df_cleaned['Salary']))
df_no_outliers = df_cleaned[z_scores < 3]  # Keep rows where Z-score is less than 3
df_outliers = df_cleaned[z_scores > 3] 

# Output the cleaned dataset
print("\nNo Salary Outliers:")
print(df_no_outliers)

# Output the outliers
print("\nSalary Outliers:")
print(df_outliers)