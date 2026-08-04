from scipy import stats
from scipy.stats import zscore
import numpy as np
from data_shape import *

# Remove outliers using z-scores
z_scores = stats.zscore(X)
abs_z_scores = np.abs(z_scores)

# loop through every data point and pick only non-outliers (good data)
filtered_entries_good = (abs_z_scores < 3).all(axis=1) 

X_filtered = X[filtered_entries_good]
Y_filtered = Y[filtered_entries_good]

print(X_filtered)
print(Y_filtered)



# Checking outliers from a single column ---------------------

# See data in table form
housing_table = fetch_california_housing(as_frame=True)
df = housing_table.frame

z_score_population = np.abs(zscore(df["Population"]))
pop_outliers_bad = df[z_score_population > 3]
print(pop_outliers_bad)