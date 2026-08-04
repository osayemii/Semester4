import matplotlib.pyplot as plt
from removing_outlier import *

# heck for missing values
missing_values = np.isnan(california_housing.data).sum()
print("Missing values:", missing_values)

# Check for outliers
plt.boxplot(X)
plt.title("Boxplot as features")

plt.xticks(range(1, len(california_housing.feature_names) + 1),
           california_housing.feature_names, rotation= 45)
plt.show()