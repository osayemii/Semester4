import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# 2: Load the dataset
df = pd.read_csv('outlier_free_student_success.csv')

# 3: Create independent variable (X)
x = df[[
    'Gender',
    'Courses',
    'Hours_attended',
    'Hours_prepared'
]].values

# 4: Create dependent variable (y)
y = df[['Success_exam']].values

# 5: Apply One-Hot Encoding to Courses
onehot_encoder = OneHotEncoder()
feature_course = onehot_encoder.fit_transform(
    x[:, 1].reshape(-1,1) # convert a 1D to 2D (-1: automatic number of rows, 1: exactly 1 column)
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
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(
    y.ravel() # .ravel flattens a 2D to 1D
)

# 8: Split dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=0
)

# 9: Display data before scaling
print("X Training Data before Scaling")
print(x_train)
print("X Testing Data before Scaling")
print(x_test)

# 10: Create StandardScaler object
sc_x = StandardScaler()

# 11: Apply scaling to training data
# 
# fit_transform calculates mean and standard deviation using only training data

x_train = sc_x.fit_transform(x_train)

# 12: Apply scaling to testing data
#
# Uses the same values calculated from training data
x_test = sc_x.transform(
    x_test
)

# 13: Display scaled training data
print("\nX Training Data After Scaling")
print(x_train)

# 14: Display scaled testing data
print("\nX Testing Data After Scaling")
print(x_test)

# 15: Display shapes after scaling
print("\nTraining Data Shape")
print(x_train.shape)
print("\nTesting Data Shape")
print(x_test.shape)