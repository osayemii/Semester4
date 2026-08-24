import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_processing/Product_Sales.csv')

saleprice = df['Sale Price in ₦']
mkprice = df['Marked Price in ₦']

plt.xlabel('Marked Price in ₦')
plt.ylabel('Sales Price in ₦')

plt.grid()
plt.scatter(saleprice, mkprice)

plt.show()