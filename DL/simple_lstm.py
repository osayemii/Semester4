import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import LSTM instead of SimpleRNN
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Import data preprocessing tools
from sklearn.preprocessing import MinMaxScaler

# Load the airline passenger dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"

data = pd.read_csv(url)

# Extract passenger numbers
passengers = data['Passengers'].values.astype(float)


# Normalize passenger numbers between 0 and 1
scaler = MinMaxScaler(feature_range=(0, 1))

passengers = scaler.fit_transform(
    passengers.reshape(-1, 1)
)

# Split data into training and testing sets
train_size = int(len(passengers) * 0.67)

train = passengers[:train_size]
test = passengers[train_size:]

# Create input-output sequences
def create_dataset(dataset, time_steps=1):
    X, y = [], []
    
    for i in range(len(dataset) - time_steps):
        X.append(dataset[i:i + time_steps, 0])
        y.append(dataset[i + time_steps, 0])
    
    return np.array(X), np.array(y)

# Use previous 10 months to predict the next month
time_steps = 10

X_train, y_train = create_dataset(train, time_steps)
X_test, y_test = create_dataset(test, time_steps)

# Reshape input data into 3 dimensions
X_train = X_train.reshape(
    X_train.shape[0], time_steps, 1
)

X_test = X_test.reshape(
    X_test.shape[0], time_steps, 1
)

# Build the LSTM model
model = Sequential([
    # LSTM layer with 32 memory units
    # Input consists of 10 time steps and 1 feature
    LSTM(32, input_shape=(time_steps, 1)),
    
    # Output layer predicts one passenger value
    Dense(1)
])

# Compile the LSTM model
model.compile(
    optimizer='adam',
    loss='mean_squared_error'
)

history = model.fit(
    X_train,
    y_train,
    epochs=100,
    batch_size=1,
    verbose=2
)

# Make predictions
train_predict = model.predict(X_train)
test_predict = model.predict(X_test)

# Convert predictions back to original passenger numbers
train_predict = scaler.inverse_transform(train_predict)
test_predict = scaler.inverse_transform(test_predict)

# Plot predictions
plt.plot(
    scaler.inverse_transform(passengers),
    label='Original Data'
)

plt.plot(
    np.concatenate((train_predict, test_predict)),
    label='LSTM Predictions'
)

plt.title('Airline Passenger Prediction Using LSTM')

plt.xlabel('Months')
plt.ylabel('Passengers')

plt.legend()
plt.show()