###
# PRACTICAL 6
# ENCODING CATEGORICAL DATA
#
# Activities
# 1. Load the outlier-free dataset
# 2. Create independent (X) and dependent (y) variables
# 3. Identify categorical columns
# 4. Apply One-Hot Encoding to multi-category columns
# 5. Apply Label Encoding to binary categorical columns
# 6. Encode the dependent variable
# 7. Display encoded data
# 8. Prepare numerical data for machine learning
###

# 1: Import required libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# 2: Load the dataset
df = pd.read_csv('outlier_free_student_success.csv')

# 3: Display the dataset
print('Original Dataset')
print(df.head())

# 4: Create independent variable (X)
x = df[[
    'Gender',
    'Courses',
    'Hours_attended',
    'Hours_prepared'
]].values

# 5: Create dependent variable (y)
y = df[['Success_exam']].values

# 6: Display X before encoding
print('\nX Before Encoding')
print(x)

# 7: Apply One-Hot Encoding to Courses
#
# Courses has more than two categories:
# Science, Arts, Commerce
onehot_encoder = OneHotEncoder()

feature_course = onehot_encoder.fit_transform(
    x[:,1].reshape(-1,1)
).toarray()

# 8: Add encoded Courses columns to X
x = np.append(
    x,
    feature_course,
    axis=1
)

# 9: Remove original Courses column
x = np.delete(
    x,
    [1],
    axis=1
)

print('\nX After One-Hot Encoding Courses')
print(x)

# 10: Apply Label Encoding to Gender
labelencoder_x = LabelEncoder()

x[:,0] = labelencoder_x.fit_transform(
    x[:,0]
)

print('\nX After Label Encoding Gender')
print(x)

# 11: Apply Label Encoding to Success_exam
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y.ravel())

print('\nEncoded Dependent Variable y')
print(y)

# 12: Display final shapes
print('\nShape of X')
print(x.shape)