
###
# PRACTICAL 4
# DETECTING AND REMOVING OUTLIERS USING IQR METHOD
#
# Activities
# 1. Load the cleaned dataset
# 2. Display the dataset summary
# 3. Calculate Q1, Q3, and IQR values
# 4. Calculate lower and upper bounds
# 5. Identify outliers in numerical columns
# 6. Remove outlier records
# 7. Verify the cleaned dataset
# 8. Save the outlier-free dataset
###

# 1: Import the Pandas library

import pandas as pd


# 2: Load the cleaned dataset

df = pd.read_csv("clean_student_success.csv")


# 3: Display the dataset before removing outliers

print("Original Dataset")

print(df.head())


print("\nDataset Shape Before Removing Outliers")

print(df.shape)


# 4: Display statistical summary

print("\nStatistical Summary")

print(df.describe())


# 5: Calculate Q1, Q3 and IQR for Hours_attended

q1 = df["Hours_attended"].quantile(0.25)

q3 = df["Hours_attended"].quantile(0.75)

iqr = q3 - q1


# 6: Calculate lower and upper bounds

lower_bound = q1 - (1.5 * iqr)

upper_bound = q3 + (1.5 * iqr)


print("\nHours_attended Bounds")

print("Lower Bound =", lower_bound)

print("Upper Bound =", upper_bound)


# 7: Identify Hours_attended outliers

outliers_attended = df.loc[
    (df["Hours_attended"] < lower_bound) |
    (df["Hours_attended"] > upper_bound)
]


print("\nHours_attended Outliers")

print(outliers_attended)


# 8: Remove Hours_attended outliers

df = df.drop(outliers_attended.index)


print("\nDataset Shape After Removing Hours_attended Outliers")

print(df.shape)


# 9: Calculate Q1, Q3 and IQR for Hours_prepared

q1 = df["Hours_prepared"].quantile(0.25)

q3 = df["Hours_prepared"].quantile(0.75)

iqr = q3 - q1


# 10: Calculate lower and upper bounds for Hours_prepared

lower_bound = q1 - (1.5 * iqr)

upper_bound = q3 + (1.5 * iqr)


print("\nHours_prepared Bounds")

print("Lower Bound =", lower_bound)

print("Upper Bound =", upper_bound)


# 11: Identify Hours_prepared outliers

outliers_prepared = df.loc[
    (df["Hours_prepared"] < lower_bound) |
    (df["Hours_prepared"] > upper_bound)
]


print("\nHours_prepared Outliers")

print(outliers_prepared)


# 12: Remove Hours_prepared outliers

df = df.drop(outliers_prepared.index)


print("\nDataset Shape After Removing All Outliers")

print(df.shape)


# 13: Display cleaned dataset

print("\nDataset After Outlier Removal")

print(df.head())


# 14: Save dataset without outliers

df.to_csv("outlier_free_student_success.csv", index=False)


print("\noutlier_free_student_success.csv saved successfully.")

