import numpy as np
import pandas as pd

np.random.seed(42)

n = 150

size = np.round(np.random.uniform(500, 4500, n), 1)          # sq ft
bedrooms = np.random.randint(1, 7, n)                          # 1-6
age = np.random.randint(0, 51, n)                               # years
distance = np.round(np.random.uniform(0.5, 30, n), 2)           # km from city center

noise = np.random.normal(0, 15000, n)
price = (
    50000
    + size * 120
    + bedrooms * 8000
    - age * 600
    - distance * 1500
    + noise
)
price = np.round(np.maximum(price, 20000), 2)

df = pd.DataFrame({
    "size": size,
    "bedrooms": bedrooms,
    "age": age,
    "distance": distance,
    "price": price,
})

df.to_csv("house_prices.csv", index=False)
print(f"Wrote {len(df)} rows")
print(df.head())
