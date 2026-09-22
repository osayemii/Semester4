import numpy as np
from sklearn.cluster import SpectralClustering
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generate synthetic data for demonstration
X, y = make_blobs(n_samples=300, centers=4, random_state=42)

# Visualize the generated data
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', marker='o', s=50)

plt.title("Generated Data")
plt.show()

# Apply spectral clustering with 'rbf' affinity
n_clusters = 4 #number of clusters
spectral_clustering = SpectralClustering(n_clusters=n_clusters, affinity='rbf', random_state=42)
labels = spectral_clustering.fit_predict(X)

# Visualize the results
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', marker='*', s=50)
plt.title("Spectral Clustering Results")
plt.show()