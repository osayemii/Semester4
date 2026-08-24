import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
import warnings

warnings.filterwarnings('ignore')

X = fetch_california_housing().data

# Log transfromation
X_log = np.log1p(X)

# Plotting histograms before and after log transformation
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Histogram before log transformation
axes[0].set_title('Histogram before Log Transformation')

for i in range(X.shape[1]):
    sns.histplot(X[:, i], ax=axes[0], alpha=0.2, label=f'Feature {i}')
    axes[0].legend()
    
# Histogram after log transformation
axes[1].set_title('Histogram after Log Transformation')

for i in range(X.shape[1]):
    sns.histplot(X_log[:, i], ax=axes[1], alpha=0.2, label=f'Feature {i}')
    axes[1].legend()
    
plt.tight_layout()
plt.show()