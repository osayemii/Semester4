import pandas as pd

df = pd.read_csv('data_processing/student_success.csv')

print('\nSTUDENT DATASET')
# print(df)

print('\nFIRST FIVE RECORDS')
# print(df.head())

print('\nLAST FIVE RECCORDS')
# print(df.tail())

print('\nRANDOM FIVE SAMPLE OF RECORDS')
# print(df.sample(5))

print('\nDATASET SHAPE')
print(df.shape)

print('\nSTATISTICAL SUMMARY')
# print(df.describe())

print('\nCOLUMN NAMES')
print(df.columns)

print('\nDATA INFO')
print(df.info())

print('\nDATA TYPES')
print(df.dtypes)

print('\nUNIQUE COURSES')
print(df['Courses'].unique())

print('\nNULL VALUES')
print(df.isnull().sum())

print('\nDUPLICATED VALUES')
duplicates = df.duplicated().sum()
print(f'Number of duplicate rows = {duplicates}')


# Identify categorical and numerical values
categorical_col = [col for col in df.columns if df[col].dtypes == 'object']
print(f'Categorical columns are : {categorical_col}')

numerical_col = [col for col in df.columns if df[col].dtypes != 'object']
print(f'Numerical columns are : {numerical_col}')

# Identify low-cardinality categorical columns. Instead of selecting all object columns.
### Cardinality is the number of unique values
categorical_cols = [
    col for col in df.columns
    if df[col].dtype == 'object' and df[col].nunique() < 20
]

print('Categorical columns are:', categorical_cols)
## You can also inspect cardinality first
for col in df.select_dtypes(include='object'):
    print(f'{col}: {df[col].nunique()} unique values')
    
    
# -----------------------------------
# DATA CLEANING                    ||
# -----------------------------------

# 1: Import the pandas library
import pandas as pd

# 2: Load the dataset
df = pd.read_csv('data_processing/student_success.csv')

print('ORIGINAL DATASET')
print(df.head())

# 3: Display the size of the dataset

print('\nDataset Shape')
print(df.shape)

# 4: Display missing values
print('\nMissing values in Each Column')
print(df.isnull().sum())

# 5: Count duplicate rows
print('/nDuplicate Records')
duplicates = df.duplicated().sum()
print(f'Number of duplicate rows = {duplicates}')

# 6: Remove duplicate rows
df = df.drop_duplicates()
print('\nDuplicates removed successfully.')
print('New shape =', df.shape)

# 7: Display unique values before cleaning
print('\nUnique values in success_exam BEFORE cleaning')
print(df['Success_exam'].unique())

# 8: Replace inconsistent values
# Yes -> Y
# No -> N
df['Success_exam'] = df['Success_exam'].str.replace('Yes', 'Y')
df['Success_exam'] = df['Success_exam'].str.replace('No', 'N')

print('\nUnique values AFTER standardization')
print(df['Success_exam'].unique())

# 9: Replace missing success_exam values
# Replace NaN with Y
df['Success_exam'] = df['Success_exam'].fillna('Y')

# 10: Replace missing numerical values
# Replace missing values using the column mean
df['Hours_attended'] = df['Hours_attended'].fillna(
    df['Hours_attended'].mean()
)

df['Hours_prepared'] = df['Hours_prepared'].fillna(
    df['Hours_prepared'].mean()
)

# 11: Verify that no missing values remain
print('\nMissing values after cleaning')
print(df.isnull().sum())

# 12: Display cleaned dataset
print('\nCleaned Dataset')
print(df.head())

# 13: Save cleaned dataset
df.to_csv('clean_student_success.csv', index=False)
print('\nclean_student_success.csv saved successfully.')


# ---------------------------------------------------
# DETECTING AND REMOVING OUTLIERS USING IQR METHOD ||
# ---------------------------------------------------

# 1: Import the pandas library
import pandas as pd

# 2: Load the cleaned dataset
df = pd.read_csv('clean_student_success.csv')

# 3: Display the dataset before removing outliers
print('Original Dataset')
print(df.head())

print('\nDataset shape befire removing outliers')
print(df.shape)

# 4: Display statistical summary
print('\nStatistical Summary')
print(df.describe())

# 5: Calculate Q1, Q2 and IQR for Hours_attended
q1 = df['Hours_attended'].quantile(0.25)
q3 = df['Hours_attended'].quantile(0.75)
iqr = q3 - q1

# 6: Calculate lower and upper bounds
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)

print('\nHours_attended Bounds')
print('Lower Bound =', lower_bound)
print('Upper Bound =', upper_bound)

# 7: Identify Hours_attended outliers
outliers_attended = df.loc[
    (df['Hours_attended'] < lower_bound) | (df['Hours_attended'] > upper_bound)
]

print('\nHours_attended Outliers')
print(outliers_attended)

# Remove Hours_attended outliers
df = df.drop(outliers_attended.index)

print('\nDataset shape after removing hours_attended outliers')
print(df.shape)

# 9: Calculate Q1, Q2 and IQR for Hours_prepared
q1 = df['Hours_prepared'].quantile(0.25)
q3 = df['Hours_prepared'].quantile(0.75)
iqr = q3 - q1

# 10: Calculate lower and upper bounds for hours_prepared
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)

print('\nHours_prepared bounds')
print('Lower bound =', lower_bound)
print('Upper bound =', upper_bound)

# 11: Identify Hours_prepared outliers
outliers_prepared = df.loc[
    (df['Hours_prepared'] < lower_bound) | (df['Hours_prepared'] > upper_bound)
]

print('\nHours_prepared Outliers')
print(outliers_prepared)

# 12: Remove Hours_prepared outliers
df = df.drop(outliers_prepared.index)

print('\nDataset shape after removing all outliers')
print(df.shape)

# 13: Display clean dataset
print('\nDataset after outlier removal')
print(df.head())

# 14: Save dataset without outliers
df.to_csv('outlier_free_student_success.csv', index=False)
print('\noutlier_free_student_success.csv saved successfully.')