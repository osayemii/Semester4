import numpy as np
import matplotlib.pyplot as plt
 
## Looking at the two moons dataset
## the important thing about this dataset is that the two groups are not spherical.
 
from sklearn.datasets import make_moons
from sklearn.cluster import KMeans, SpectralClustering
from sklearn.metrics import adjusted_rand_score
 
from scipy.sparse.csgraph import laplacian
from scipy.sparse.linalg import eigsh
 
plt.style.use("seaborn-v0_8-whitegrid")
 
RANDOM_STATE = 42
 
X, y = make_moons(n_samples=500,noise=0.08,random_state=RANDOM_STATE)

print("Shape of X:", X.shape)
print("Shape of y:", y.shape)
 
plt.figure(figsize=(7, 5))
 
plt.scatter(X[:, 0], X[:, 1], c=y, cmap="coolwarm",s=30)
 
plt.title("Two-Moons Dataset")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()


# Applying KMeans first
kmeans = KMeans(
	n_clusters=2,
	random_state=RANDOM_STATE,
	n_init=10
)

kmeans_labels = kmeans.fit_predict(X)
 
plt.figure(figsize=(7, 5))
 
plt.scatter(
	X[:, 0],
	X[:, 1],
	c=kmeans_labels,
	cmap="coolwarm",
	s=30
)
 
plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
	c="black",
	marker="*",
	s=150,
	label="Centroids"
)
 
plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()