# Import neccessary libraries
from sklearn.datasets import make_blobs
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Generate random data with three clusters
data, labels = make_blobs(n_samples=300, centers=3, random_state=42)

plt.figure(figsize=(10, 8))
# plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', marker='o', s=50)
sns.scatterplot(x=data[:, 0], y=data[:, 1], hue=labels, palette='viridis')
plt.title('Before t-SNE Visualization')
plt.show()

# Create a t-SNE model with two components (for 2D visualization)
tsne = TSNE(n_components=2, random_state=42)

# Fit and transform the data
tsne_result = tsne.fit_transform(data)

# Create a Dataframe for visualization
tsne_df = pd.DataFrame({'Dimension 1': tsne_result[:, 0], 'Dimension 2': tsne_result[:, 1], 'Label': labels})

# Scatter plot using seaborn with color-coded clusters
plt.figure(figsize=(10, 8))
sns.scatterplot(x='Dimension 1', y='Dimension 2', hue='Label', palette='viridis', data=tsne_df)
plt.title('After t-SNE Visualization')
plt.show()