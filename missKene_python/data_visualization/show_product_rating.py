import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_processing/Product_Sales.csv')

plt.figure(figsize=(12,6))
plt.bar(df['Product'], df['Star Ratings'])

plt.xlabel('Product Name')
plt.ylabel('Star Ratings')
plt.title('Star Ratings of Products')
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()