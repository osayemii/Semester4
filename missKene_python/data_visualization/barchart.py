import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_processing/Product_Sales.csv')
df['Discount'] = (df['Marked Price in ₦'] - df['Sale Price in ₦'])*100/df['Marked Price in ₦']

# Set x and y axis data
x_pt = df['Brand']
y_pt = df['Discount']

# Plot horizontal bar chart
plt.barh(x_pt, y_pt)

# Label x and y axis
plt.xlabel('Discount %')
plt.ylabel('Brands')

# Show the plot
plt.show()