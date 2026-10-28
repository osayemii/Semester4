import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from umap import UMAP

# Load a sample datasset (iris dataset)
iris = datasets.load_iris()
X = iris.data
y = iris.target

print(X.shape)

# Plot before applyong UMAP
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
plt.title('Before Applying UMAP Visualization')
plt.show()

# Apply UMAP
umap = UMAP(n_components=2, random_state=42)
X_umap = umap.fit_transform(X)

# Plot the result
plt.scatter(X_umap[:, 0], X_umap[:, 1], c=y, cmap='viridis')
plt.title('After Applying UMAP Visualization')
plt.show()