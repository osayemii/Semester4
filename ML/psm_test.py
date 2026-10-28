import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import NearestNeighbors

# Load data
titanic_df = pd.read_csv(
    'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
)

# Define covariates and group indicator
covariates = ['Age', 'Fare']
treatment = titanic_df['Survived'].to_numpy()

# Impute missing values
imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(titanic_df[covariates])

# Estimate scores
model = LogisticRegression(max_iter=1000)
model.fit(X, treatment)

scores = model.predict_proba(X)[:, 1]

# Seperate the two groups
treated_indices = np.flatnonzero(treatment == 1)
control_indices = np.flatnonzero(treatment == 0)

# Fit nearest neighbors oncontrols only
nn = NearestNeighbors(n_neighbors=1)
nn.fit(scores[control_indices].reshape(-1, 1))

# Match each treated passenger to a control passenger
distances, neighbor_positions = nn.kneighbors(
    scores[treated_indices].reshape(-1, 1)
)

matched_control_indices = control_indices[neighbor_positions[:, 0]]

# Build a dataset containing the matched pairs
matched_indices = np.concatenate([
    treated_indices,
    matched_control_indices
])

matched_data = titanic_df.iloc[matched_indices].copy()
matched_data['Group'] = np.concatenate([
    np.ones(len(treated_indices), dtype=int),
    np.zeros(len(matched_control_indices), dtype=int)
])

# Compare covariate distributions
fig,  axes = plt.subplots(1, 2, figsize=(12, 5))

for ax, covariate in zip(axes, covariates):
    sns.histplot(
        data = titanic_df,
        x=covariate,
        hue='Survived',
        stat='density',
        common_norm=False,
        element='step',
        fill=False,
        ax=ax
    )
    
    ax.set_title(f'{covariate}: Original groups')
    
plt.tight_layout()
plt.show()