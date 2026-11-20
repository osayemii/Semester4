import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

import pandas as pd
import requests
# Converts downloaded text into a file-like object
from io import StringIO

# URL containing the Air passenger dataset
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv'

# Send a request to download the dataset
response = requests.get(url)

# Convert the downloaded CSV into a pandas dataframe
data = pd.read_csv(StringIO(response.text))

# Extracts only the passengers column from the dataset
# Convert the values into floating-point numbers
passengers = data['Passengers'].values.astype(float)

# Create a MinMaxScaler that converts number into range 0 and 1
scaler = MinMaxScaler(feature_range=(0, 1))

# Reshape the passenger data into a 2D array
# then normalize the value
# -1 = automatic rows, 1 = 1 column
passengers = scaler.fit_transform(passengers.reshape(-1, 1))

# Caluculate 67% of the dataset for training
train_size = int(len(passengers) * 0.67)

# Calculate the remaining 33% for testing
test_size = len(passengers) - train_size

# Select the first 67% of the data for training
train = passengers[0:train_size]

# Select the remaining 33% for testing
test = passengers[train_size:len(passengers)]

def create_dataset(dataset, time_steps=1):
    # Create empty list to store input and output values
    X, y = [], []
    
    # Loop through the dataset
    for i in range(len(dataset) - time_steps):
        # Collect previous time_steps values as input
        X.append(dataset[i:(i + time_steps), 0])
        
        # Collect the next value as the expected output
        y.append(dataset[i + time_steps, 0])
        
    # Converts the lists into Numpy arrays and return them
    return np.array(X), np.array(y)

# Tell the model to use the previous 10 months
# to predict the next month's passenger number
time_steps = 10

# Generate input and output sequences for training
X_train, y_train = create_dataset(train, time_steps)

# Generate input and output sequesnces for testing
X_test, y_test = create_dataset(test, time_steps)

# reshape the training and testing input into 3 dimensions:
# samples - time steps - features
X_train = np.reshape(
    X_train,
    (X_train.shape[0], time_steps, 1)
)

X_test = np.reshape(
    X_test,
    (X_test.shape[0], time_steps, 1)
)

model = Sequential()

# Configure the model before training
model.compile(
    optimizer='adam',
    loss='mean_squared_error'
)

history = model.fit(
    # Imput training sequences
    X_train,
    
    # Correct answers for the training sequences
    y_train,
    
    epochs=100,
    batch_size=1,
    
    # Displays training progress
    verbose=2
)

# Predict from the training dataset
train_predict = model.predict(X_train)

# Predict from the testing dataset
test_predict = model.predict(X_test)

# Converts normalized training predictions back to passenger numbers
train_predict = scaler.inverse_transform(train_predict)

# Convert normalized training target values back to it original scale
y_train = scaler.inverse_transform([y_train])

# Converts normalized testing predictions back to passenger numbers
test_predict = scaler.inverse_transform(test_predict)

# Convert normalized testing target values back to it original scale
y_test = scaler.inverse_transform([y_test])

# Calculate training RMSE
train_score = np.sqrt(
    mean_squared_error(
        y_train[0],
        train_predict[:, 0]
    )
)

# Display the training error
print('Train RMSE:', train_score)

# Calculate testing RMSE
test_score = np.sqrt(
    mean_squared_error(
        y_test[0],
        test_predict[:, 0]
    )
)

# Display the testing error
print('Test RMSE:', test_score)


# Plot the original passenger data
# Convert the normalized values back to original passenger numbers
plt.plot(
    scaler.inverse_transform(passengers),
    label='Original Data'
)

# Combine training and testing predictions into one array
# then plot the predicted passenger numbers
plt.plot(
    np.concatenate((train_predict, test_predict)),
    label='Predictions'
)

plt.legend()
plt.show()