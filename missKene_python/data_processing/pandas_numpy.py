import pandas as pd
import random
import numpy as np

random.seed(42)
np.random.seed(42)

products = {
    "Smartphone": {
        "brands": ["Tecno", "Infinix", "Samsung", "Xiaomi", "Itel"],
        "price": (85000, 850000)
    },
    "Laptop": {
        "brands": ["HP", "Dell", "Lenovo", "Asus", "Acer"],
        "price": (280000, 1800000)
    },
    "Television": {
        "brands": ["LG", "Hisense", "Samsung", "Panasonic", "TCL"],
        "price": (120000, 950000)
    },
    "Refrigerator": {
        "brands": ["LG", "Hisense", "Scanfrost", "Nexus", "Haier Thermocool"],
        "price": (180000, 1200000)
    },
    "Air Conditioner": {
        "brands": ["LG", "Hisense", "Midea", "Panasonic"],
        "price": (180000, 950000)
    },
    "Generator": {
        "brands": ["Firman", "Sumec", "Honda", "Elepaq"],
        "price": (150000, 900000)
    },
    "Microwave": {
        "brands": ["LG", "Panasonic", "Nexus", "Hisense"],
        "price": (65000, 320000)
    },
    "Speaker": {
        "brands": ["JBL", "Oraimo", "Sony", "LG"],
        "price": (18000, 250000)
    },
    "Headphones": {
        "brands": ["Oraimo", "Sony", "JBL", "Samsung"],
        "price": (8000, 120000)
    },
    "Power Bank": {
        "brands": ["Oraimo", "Xiaomi", "Anker", "Itel"],
        "price": (12000, 70000)
    },
    "Blender": {
        "brands": ["Binatone", "Kenwood", "Panasonic"],
        "price": (18000, 95000)
    },
    "Electric Kettle": {
        "brands": ["Binatone", "Nexus", "Kenwood"],
        "price": (9000, 45000)
    },
    "Standing Fan": {
        "brands": ["Binatone", "OX", "Century"],
        "price": (18000, 85000)
    },
    "Rice Cooker": {
        "brands": ["Binatone", "Panasonic", "Kenwood"],
        "price": (25000, 120000)
    },
    "Printer": {
        "brands": ["HP", "Canon", "Epson"],
        "price": (85000, 450000)
    }
}

rows = []

for i in range(100):
    product = random.choice(list(products.keys()))
    
    brand = random.choice(products[product]["brands"])

    low, high = products[product]["price"]

    marked_price = random.randint(low, high)

    discount = random.randint(2000, int(marked_price * 0.15))

    sale_price = marked_price - discount

    description = f"{brand} {product}"

    ratings = random.randint(100, 12000)

    reviews = random.randint(20, 4000)

    stars = round(random.uniform(3.5, 5.0), 1)

    rows.append([
        product,
        brand,
        description,
        sale_price,
        marked_price,
        ratings,
        reviews,
        stars
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "Product",
        "Brand",
        "Description",
        "Sale Price in ₦",
        "Marked Price in ₦",
        "Number of Ratings",
        "Number of Reviews",
        "Star Ratings"
    ]
)


# Add Missing Values (NaN)


for _ in range(10):
    row = random.randint(0, len(df)-1)
    df.loc[row, "Star Ratings"] = np.nan

for _ in range(8):
    row = random.randint(0, len(df)-1)
    df.loc[row, "Number of Reviews"] = np.nan

for _ in range(5):
    row = random.randint(0, len(df)-1)
    df.loc[row, "Number of Ratings"] = np.nan


# Add extra spaces for cleaning practice


space_rows = random.sample(range(len(df)), 10)

for r in space_rows:
    df.loc[r, "Product"] = " " + df.loc[r, "Product"] + " "


# Save CSV

df.to_csv("Product_Sales.csv", index=False)

print(df.head())

print("\nDataset created successfully!")

print("Rows:", len(df))

print("File saved as Product_Sales.csv")