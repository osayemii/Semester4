import pandas as pd
import numpy as np
import random

# Reproduce same random
random.seed(12)
# np.random.seed(12)

# names
names = [
    "Amina", "Chinedu", "Tunde", "Ngozi", "Emeka",
    "Blessing", "Ifeanyi", "Chioma", "Adebayo", "Fatima",
    "Yusuf", "Kehinde", "Taiwo", "Bisi", "Funke",
    "Musa", "Hadiza", "Samuel", "Mercy", "David",
    "Esther", "Maryam", "Oluwaseun", "Abiola", "Ibrahim",
    "Uche", "Adaobi", "Sani", "Ruth", "John", "Peter",
    "Victoria", "Joseph", "Grace", "Segun",
    "Zainab", "Aisha", "Michael", "Daniel", "Loveth",
    "Kingsley", "Ebere", "Ogechi", "Suleiman", "Mariam",
    "Nnamdi", "Chisom", "Temitope", "Afolabi", "Kelechi"
]

genders = ["Male", "Female"]

rows = []

for i in range(1, 51):
    age = random.randint(20, 60)
    salary = random.randint(40000, 180000)
    gender = random.choice(genders)
    
    # Simple target generation
    target = 1 if (salary > 100000 and age > 30) else 0
    
    rows.append([
        i,
        names[i-1],
        age,
        gender,
        salary,
        target
    ])


df = pd.DataFrame(
    rows,
    columns=["ID", "Name", "Age", "Gender", "Salary", "Target"]
)

# To introduce missing values
df.loc[[4, 15, 32], "Age"] = np.nan
df.loc[[7, 20, 40], "Salary"] = np.nan

# To introduce duplicates
df.loc[45] = df.loc[10]
df.loc[46] = df.loc[20]

# Fix IDs after duplication
df["ID"] = range(1, 51)

# Introduce Salary Outliers
df.loc[2, "Salary"] = 450000
df.loc[12, "Salary"] = 520000

# Shuffle datasets
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save CSV
df.to_csv("ml_employee_dataset.csv", index=False)

print(df.head(), "\n")
print(df.sample(5))
print("\nDataset shape:", df.shape)
print("\nCSV file saved as 'ml_employee_dataset.csv'")