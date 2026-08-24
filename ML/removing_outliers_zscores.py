# REMOVE OOUTLIERS USING Z-SCORES
from scipy import stats
import numpy as np
from sklearn.datasets import fetch_california_housing

X = fetch_california_housing().data
y = fetch_california_housing().target

housing_table = fetch_california_housing(as_frame=True)
df = housing_table.frame

z_scores = stats.zscore(X)
abs_z_score = np.abs(z_scores)
filtered_entries = (abs_z_score < 3).all(axis=1)
X_filtered = X[filtered_entries]
y_filtered = y[filtered_entries]

print(X_filtered)
print(y_filtered)

# checking some columns
from scipy.stats import zscore
z_score_population = np.abs(zscore(df['Population']))
pop_outliers = df[z_score_population > 3]
print(pop_outliers)