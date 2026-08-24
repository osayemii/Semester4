###
# PRACTICAL 9
# SAVING TRAINING AND TESTING DATASETS USING JOBLIB
#
# Activities
# 1. Load the encoded dataset
# 2. Create independent (X) and dependent (y) variables
# 3. Encode categorical data
# 4. Split data into training and testing sets
# 5. Apply feature scaling
# 6. Import joblib library
# 7. Save x_train, x_test, y_train and y_test
# 8. Verify saved files
# 9. Load saved datasets
# 10. Display loaded datasets
###


# 1: Import required libraries
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 2: Load the dataset
df = pd.read_csv('outlier_free_student_success.csv')

# 3: Create independent variables (X)
x = df[[
    'Gender',
    'Courses',
    'Hours_attended',
    'Hours_prepared'
]].values

# 4: Create dependent variable (y)
y = df[['Success_exam']].values

# 5: Apply One-hot Encoding to Courses
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
labelencoder_y = LabelEncoder()

y = labelencoder_y.fit_transform(
    y.ravel()
)

# 8: Spli dataset into trainging and testing sets
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=0
)

# Apply feature scaling
sc_x = StandardScaler()

x_train = sc_x.fit_transform(
    x_train
)

x_test = sc_x.fit_transform(
    x_test
)

# 10: Save training input data
joblib.dump(
    x_train,
    'filextrain.pkl'
)

# 11: Save testing input data
joblib.dump(
    x_test,
    'filextest.pkl'
)

# 12: Save training output data
joblib.dump(
    y_train,
    'fileytrain.pkl'
)

# 13: Save testing output data
joblib.dump(
    y_test,
    'fileytest.pkl'
)

print('Traing and testing datasets saved successfully.')

# 14: Load saved training dataset
load_x_train = joblib.load(
    'filextrain.pkl'
)

# 15: Load saved testing dataset
load_x_test = joblib.load(
    'filextest.pkl'
)

# 16: Load saved ouput dataset
load_y_train = joblib.load(
    'fileytrain.pkl'
)

load_y_test = joblib.load(
    'fileytest.pkl'
)

# 17: Display loaded datasets
print('\nLoaded X Training Data')
print(load_x_train)

print('\nLoaded X Testing Data')
print(load_x_test)

print('\nLoaded Y Training Data')
print(load_y_train)

print('\nLoaded X Testing Data')
print(load_y_test)