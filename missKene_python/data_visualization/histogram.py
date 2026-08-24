import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_processing/Product_Sales.csv')

plt.xlabel('Satr Ratings Range')
plt.ylabel('Count')

plt.hist(
    df['Star Ratings'],
    bins = [4,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9])

plt.show()