import pandas as pd

# Number 1
df = pd.read_csv('data_processing/Product_Sales.csv')
print(df)

# Number 2
first_ten_rows = df.head(10)
print(first_ten_rows)

# Number 3
last_eight_rows = df.tail(8)
print(last_eight_rows)

# Number 4
summary = df.describe()
print(summary)

# Number 5
df['Discount'] = (df['Marked Price in ₦'] - df['Sale Price in ₦'])

# Number 6
df['Discount in %'] = ((df['Marked Price in ₦'] - df['Sale Price in ₦']) / df['Marked Price in ₦']) * 100
print(df)

# Number 7
df['Sale Price in ₦'] = df['Sale Price in ₦'].add(5000)
print(df)

# Number 8
df.sort_values(
    by='Star Ratings',
    inplace=True,
    ascending=True
)
print(df)

df = pd.read_csv('data_processing/Product_Sales.csv')

# Number 9
new_df = df.truncate(
    before=20,
    after=30
)
print(new_df)

# Number 10
# smartphones = df['Product'].loc['Smartphone']
smartphones = df[df['Product'] == 'Smartphone']
print(smartphones)


# Number 11
missing_val = df.isnull()
print(missing_val)

# Number 12
avg_rating = df['Number of Ratings'].mean()
clean_data = df.fillna(avg_rating)
print(clean_data)

# Number 13
df['Brand'] = df['Brand'].str.upper()
print(df)

# Number 14
df['Product'] = df['Product'].str.replace(
    'Phone',
    'Smartphone',
    case=False
)
print(df)

# Number 15
df['Product'] = df['Product'].str.strip()
print(df)

# Number 16
df.to_csv('Product_Sales_Clean.csv')
print('Successfully Saved')