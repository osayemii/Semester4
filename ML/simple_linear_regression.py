import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

# 1: CREATE weight-height.csv
np.random.seed(42)

# Number of people to generate
n_male = 500
n_female = 500

# Generate heights in inches
male_height = np.random.normal(
    loc=69.0,   # average male height
    scale=3.0,   # variation
    size=n_male
)

female_height = np.random.normal(
    loc=64.0,     # average female height
    scale=2.8,
    size=n_female
)


# Generate weights in pounds
# 
# Weight is related to height, but we add random noise to make the dataset realistic
male_weight = (
    5.5 * male_height - 180
    + np.random.normal(0, 12, n_male)
)

female_weight = (
    4.8 * female_height - 170
    + np.random.normal(0, 10, n_female)
)

# Create Dataframes
male_data = pd.DataFrame({
    'Gender': 'Male',
    'Height': male_height,
    'Weight': male_weight
})

female_data = pd.DataFrame({
    'Gender': 'Female',
    'Height': female_height,
    'Weight': female_weight
})

# Combine both male and female data
data = pd.concat(
    [male_data, female_data],
    ignore_index=True
)

# Shuffle the rows
data = data.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

# Round values
data['Height'] = data['Height'].round(2)
data['Weight'] = data['Weight'].round(2)

# Save CSV
data.to_csv(
    'weight-height.csv',
    index=False
)

print('weight-height.csv created successfully!')
print()
print(data.head())
print()
print('Number of rows:', len(data))



# 2: LOAD THE CSV
X = pd.read_csv('weight-height.csv')
print('\nthe training data looks like:')
print(X.sample(5))

print('\nColumns')
print(X.columns)



# 3: CONVERT UNITS

# Pounds -> kilograms
X['Weight'] = X['Weight'] * 0.454

# Inches -> Centimeters
X['Height'] = X['Height'] * 2.54


# 4: VISUALIZE THE DATA

sns.lmplot(
    x='Height',
    y='Weight',
    hue='Gender',
    data=X
)

plt.title('Height vs Weight')
plt.show()



# 5: SEPERATE MALES AND FEMALES

X_male = X.loc[X['Gender'] == 'Male'].copy()
X_female = X.loc[X['Gender'] == 'Female'].copy()



# 6: VISUALIZE EACH GROUP

sns.regplot(
    x=X_male['Height'],
    y=X_male['Weight']
)
plt.title('Male Population')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()


sns.regplot(
    x=X_female['Height'],
    y=X_female['Weight']
)
plt.title('Female Population')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()



# 7: FEATURE AND TARGET

# Target = Weight
Y_male = X_male['Weight']
Y_female = X_female['Weight']

# Feature = Height
X_male = X_male.drop(
    ['Weight', 'Gender'],
    axis=1    # loop through byp0 columns
)

X_female = X_female.drop(
    ['Weight', 'Gender'],
    axis=1
)



# 8: TRAIN TEST SPLIT

X_male_train, X_male_test, y_male_train, y_male_test = train_test_split(
    X_male,
    Y_male,
    train_size=0.8,
    test_size=0.2,
    random_state=0
)

X_female_train, X_female_test, y_female_train, y_female_test = train_test_split(
    X_female,
    Y_female,
    train_size=0.8,
    test_size=0.2,
    random_state=0
)



# 9: CREATE LINEAR REGRESSION MODELS

lin_reg_male = LinearRegression()
lin_reg_female = LinearRegression()



# 10: TRAIN THE MODELS

lin_reg_male.fit(
    X_male_train,
    y_male_train
)

lin_reg_female.fit(
    X_female_train,
    y_female_train
)



# 11: DISPLAY THE EQUATIONS

print('\nMODEL INFORMATION =')
print('\nMale model:')
print(
    'Weight =',
    round(lin_reg_male.coef_[0], 3),
    '* Height +',
    round(lin_reg_male.intercept_, 3)
)

print('\nFemale model:')
print(
    'Weight =',
    round(lin_reg_female.coef_[0], 3),
    '* Height +',
    round(lin_reg_female.intercept_, 3)
)



# 12: MAKE PREDICTIONS
# male_train_pred = lin_reg_male.predict(X_male_train)
male_test_pred = lin_reg_male.predict(X_male_test)

# female_train_pred = lin_reg_male.predict(X_female_train)
female_test_pred = lin_reg_male.predict(X_female_test)


# 13: CHECK MODEL PERFORMANCE
from sklearn.metrics import mean_absolute_error, r2_score

male_mae = mean_absolute_error(
    y_male_test,
    male_test_pred
)

female_mae = mean_absolute_error(
    y_female_test,
    female_test_pred
)

male_r2 = r2_score(
    y_male_test,
    male_test_pred
)

female_r2 = r2_score(
    y_female_test,
    female_test_pred
)

print('MODEL PERFORMANCE')

print('Male Model:')
print('Mean Absolute Error:', round(male_mae, 2), 'kg')
print('R² Score:', round(male_r2, 3))

print('Female Model:')
print('Mean Absolute Error:', round(female_mae, 2), 'kg')
print('R² Score:', round(female_r2, 3))



# USER INPUT
print('\n')
print('Weight Prediction machine Learning Model')
print('='*40)

gender = input(
    'Enter M for male or F for female: '
).upper()

if gender not in ['M', 'F']:
    print('Please enter either M or F.')
else:
    height = float(
        input('Enter your height in cm: ')
    )
    
    input_data = pd.DataFrame({
        'Height': [height]
    })
    
if gender == 'M':
    predicted_weight = lin_reg_male.predict(
        input_data
    )[0]
    
else:
    predicted_weight = lin_reg_female.predict(
        input_data
    )[0]
    
    
    
# DISPLAY PREDICTION
lower = predicted_weight * 0.98
upper = predicted_weight * 1.02

print('RESULT')
print(
    f'Predicted weight: {predicted_weight:.1f} kg'
)

print(
    f'Approxiamte model range: '
    f'{lower:.1f} - {upper:.1f} kg'
)


# BMI CALCULATION

height_m = height/100

bmi_min = 18.5
bmi_max = 25

min_weight = bmi_min * (height_m ** 2)
max_weight = bmi_max * (height_m ** 2)

print(
    f'\nBMI 18.25 - 25 weight range: '
    f'{min_weight:.1f} - {max_weight:.1f} kg'
)

print('---'*40)