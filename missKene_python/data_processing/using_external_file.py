import pandas as pd

df = pd.read_csv('Product_Sales.csv')

# print(df)

print('\nTop data first')
print(df.head(10))

print('\nBottom data first')
print(df.tail(20))

print('\nDescribe data')
print(df.describe())