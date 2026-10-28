import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_moons
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import rbf_kernel
from sklearn.metrics import adjusted_rand_score

from scipy.sparse.linalg import eigsh


# 1. Create the Two-Moons Dataset
RANDOM_STATE = 42

X, y = make_moons(
   n_samples=500,
   noise=0.08,
   random_state=RANDOM_STATE
)


# 2. Build the Similarity / Affinity Matrix
gamma = 15

W = rbf_kernel( # rbf - radial base function
   X,
   gamma=gamma
)

# 3. Build the Degree Matrix
D = np.diag(
   W.sum(axis=1)
)


# 4. Build the Graph Laplacian
L = D - W

# 5. Find the Eigenvectors
eigenvalues, eigenvectors = eigsh(
   L,
   k=2,
   which="SM"
)

print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvector matrix shape:")
print(eigenvectors.shape)

# 6. Create the Spectral Representation
spectral_embedding = eigenvectors

# 7. Apply K-Means to the Spectral Representation
spectral_kmeans = KMeans(
   n_clusters=2,
   random_state=RANDOM_STATE,
   n_init=10
)

spectral_labels = spectral_kmeans.fit_predict(
   spectral_embedding
)

# 8. Evaluate Spectral Clustering
spectral_ari = adjusted_rand_score(
   y,
   spectral_labels
)
print(f"\nSpectral Clustering ARI: {spectral_ari:.3f}")

# 9. Visualize the Spectral Representation
plt.figure(figsize=(7, 5))
plt.scatter(
   spectral_embedding[:, 0],
   spectral_embedding[:, 1],
   c=spectral_labels,
   cmap="coolwarm",
   s=30
)

plt.title("Spectral Representation")
plt.xlabel("Eigenvector 1")
plt.ylabel("Eigenvector 2")
plt.show()

# 10. Visualize Spectral Clustering in Original Space
plt.figure(figsize=(7, 5))
plt.scatter(
   X[:, 0],
   X[:, 1],
   c=spectral_labels,
   cmap="coolwarm",
   s=30
)

plt.title("Spectral Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

# 11. Compare with K-Means on Original Data
kmeans = KMeans(
   n_clusters=2,
   random_state=RANDOM_STATE,
   n_init=10
)

kmeans_labels = kmeans.fit_predict(X)
kmeans_ari = adjusted_rand_score(
   y,
   kmeans_labels
)

print(f"K-Means ARI:             {kmeans_ari:.3f}")
print(f"Spectral Clustering ARI: {spectral_ari:.3f}")


# 12. Compare Both Methods Visually
fig, axes = plt.subplots(
   1, 3,
   figsize=(18, 5)
)


# True clusters
axes[0].scatter(
   X[:, 0],
   X[:, 1],
   c=y,
   cmap="coolwarm",
   s=30
)

axes[0].set_title("True Clusters")
axes[0].set_xlabel("Feature 1")
axes[0].set_ylabel("Feature 2")

# K-Means
axes[1].scatter(
   X[:, 0],
   X[:, 1],
   c=kmeans_labels,
   cmap="coolwarm",
   s=30
)

axes[1].scatter(
   kmeans.cluster_centers_[:, 0],
   kmeans.cluster_centers_[:, 1],
   c="black",
   marker="X",
   s=200,
   label="Centroids"
)

axes[1].set_title("K-Means")
axes[1].set_xlabel("Feature 1")
axes[1].set_ylabel("Feature 2")
axes[1].legend()

# Spectral Clustering
axes[2].scatter(
   X[:, 0],
   X[:, 1],
   c=spectral_labels,
   cmap="coolwarm",
   s=30
)

axes[2].set_title("Spectral Clustering")
axes[2].set_xlabel("Feature 1")
axes[2].set_ylabel("Feature 2")

plt.tight_layout()
plt.show()