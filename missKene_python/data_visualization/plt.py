import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data_processing/Product_sales.csv')
dp = df.head()

brand = dp["Brand"]
saleprice = dp['Sale Price in ₦']
mrpprice=dp['Marked Price in ₦']

plt.xlabel("Brand")
plt.ylabel("Price in ₦")

plt.plot(brand,saleprice,marker = '*',label ="Sale Price in ₦")
plt.plot(brand,mrpprice,marker = 'D',label ="Marked Price in ₦")

plt.grid(True, linestyle=':')

plt.xticks(brand)
plt.yticks(saleprice)
plt.yticks(mrpprice)

plt.legend()
plt.show()