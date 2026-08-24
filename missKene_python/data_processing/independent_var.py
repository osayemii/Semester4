# 1: Import the Pandas library
import pandas as pd


# 2: Load the outlier-free dataset
df = pd.read_csv("outlier_free_student_success.csv")


# 3: Display the dataset
print("Student Dataset")

print(df.head())


# 4: Display dataset columns
print("\nDataset Columns")

print(df.columns)


# 5: Create independent variables (X)
# Independent variables are the input features
# used by the machine learning model

x = df[
    [
        "Gender",
        "Courses",
        "Hours_attended",
        "Hours_prepared"
    ]
].values


# 6: Create dependent variable (y)
#
# Success_exam is the target variable
# that the model will predict

y = df[
    [
        "Success_exam"
    ]
].values


# 7: Display independent variables

print("\nIndependent Variables (X)")

print(x)


# 8: Display dependent variable

print("\nDependent Variable (y)")

print(y)


# 9: Display the shape of X

print("\nShape of X")

print(x.shape)


# 10: Display the shape of y

print("\nShape of y")

print(y.shape)

