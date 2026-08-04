import pandas as pd

df = pd.read_csv('data_processing/product_Sales.csv')
# print(df)

# Create Discount Column
df['Discount'] = (df['Marked Price in ₦'] - df['Sale Price in ₦'])

# Calculate Discount Percentage
df['Discount in %'] = ((df['Marked Price in ₦'] - df['Sale Price in ₦']) / df['Marked Price in ₦']) * 100

# Increase Every Sale Price by 5,000
df['Sale Price in ₦'] = (df['Sale Price in ₦'].add(5000))

# Increase Marked Price by 10,000
df['Marked Price in ₦'] = (df['Marked Price in ₦'].add(10000))

# Display Updated Dataset
# print(df)


# -----------------------------------------------------
# SORTING
# -----------------------------------------------------

df.sort_values(
    by = 'Star Ratings',
    ascending=True,
    inplace=True,
    na_position='last'
)
# print(df)

# print('Sort Sale Price in ₦ with ascending=False')
df.sort_values(
    by='Sale Price in ₦',
    ascending=False
)
# print(df)

# print('Sort by more than one Value. [Brand, Sale Price in ₦]')
df.sort_values(
    by=['Brand', 'Sale Price in ₦']
)
# print(df)



# -----------------------------------------------------
# TRUNCATE
# -----------------------------------------------------
df = pd.read_csv('data_processing/Product_Sales.csv')

new_csv = df.truncate(
    before=10,
    after=20
)
print(new_csv)


# -----------------------------------------------------
# FILTERING
# -----------------------------------------------------
df = pd.read_csv(
    'data_processing/Product_Sales.csv',
    index_col=0
)

phones = df.loc['Smartphone']
print(phones)

tv = df.loc['Television']
print(tv)

fridge = df.loc['Refrigerator']
print(fridge)

# Missing and Not Missing Values ----------------------------------
print(df.isnull())

#  count missing value
print(df.isnull().sum())

# Detect Non-Missing Values
print(df.notnull)

# Replace missing values with Zero(0)
df.fillna(0)

# Replace missing ratings with average ratings
avg_star_ratings = df['Star Ratings'].mean()

df['Star Ratings'] = df['Star Ratings'].fillna(avg_star_ratings)
print(df)

# Remove rows with missing values
clean_df = df.dropna()
print(clean_df)



# -----------------------------------------------------
# WORKING WITH TEXT DATA
# -----------------------------------------------------

# Convert brand names to uppercase
df['Brand'] = df['Brand'].str.upper()
print(df)

# Convert brand names to lowercase
df['Brand'] = df['Brand'].str.lower()
print(df)

# Replace 'Phone' with 'Smartphone'
df['Product'] = df['Product'].str.replace(
    'Phone',
    'Smartphone',
    case=False
)
print(df)

# Replace 'TV' with 'Television'
df['Product'] = df['Product'].str.replace(
    'TV',
    'Television',
    case=False
)
print(df)

# Remove extra spaces from 'Products'
df['Product'] = df['Product'].str.strip()
print(df)

# Remove extra spaces from 'Brand'
df['Brand'] = df['Brand'].str.strip()
print(df)