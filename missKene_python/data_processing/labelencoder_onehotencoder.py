###
# PRACTICAL 7
# SPLITTING DATASET INTO TRAINING AND TESTING SETS
#
# Activities
# 1. Load the encoded dataset
# 2. Create independent (X) and dependent (y) variables
# 3. Import train_test_split function
# 4. Split data into training and testing sets
# 5. Display training and testing data
# 6. Check the shape of each dataset
# 7. Understand the purpose of training and testing data
###
# 1: Import required libraries

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split

# 2: Load the dataset
df = pd.read_csv("outlier_free_student_success.csv")

# 3: Create independent variables (X)
x = df[
    [
        "Gender",
        "Courses",
        "Hours_attended",
        "Hours_prepared"
    ]
].values

# 4: Create dependent variable (y)
y = df[
    [
        "Success_exam"
    ]
].values

# 5: Apply One-Hot Encoding to Courses
# OneHotEncoder used among more than two distinct categories | Young | Adult | Old 
#                                                               0        1      0
#                                                               1        0      0
#                                                               0        0      1
onehot_encoder = OneHotEncoder()

feature_course = onehot_encoder.fit_transform(
    x[:,1].reshape(-1,1)
).toarray()

x = np.append(
    x,
    feature_course,
    axis=1
)

x = np.delete(
    x,
    [1],
    axis=1
)

# 6: Apply Label Encoding to Gender
labelencoder_x = LabelEncoder()

x[:,0] = labelencoder_x.fit_transform(
    x[:,0]
)

# 7: Apply Label Encoding to Success_exam
# LabelEncoder used among two distinct categories | Male | Female |
#                                                    0       1
#                                                    1       0
labelencoder_y = LabelEncoder()

y = labelencoder_y.fit_transform(
    y.ravel()
)

# 8: Split dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=0
)

# 9: Display training input data
print("X Training Data")
print(x_train)

# 10: Display testing input data
print("\nX Testing Data")
print(x_test)

# 11: Display training output data
print("\nY Training Data")
print(y_train)

# 12: Display testing output data
print("\nY Testing Data")
print(y_test)

# 13: Display shapes
print("\nShape of X Training Data")
print(x_train.shape)

print("\nShape of X Testing Data")
print(x_test.shape)

print("\nShape of Y Training Data")
print(y_train.shape)

print("\nShape of Y Testing Data")
print(y_test.shape)