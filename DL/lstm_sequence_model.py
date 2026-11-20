import numpy as np
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# Number pf unique words/token in the source language vocabulary
vocab_size_source = 10000

# Number of numerical features used to represent eac token
embedding_dim = 128

# Maximum number of tokens allowed in an input sentence
max_sequence_length_source = 20

# Number of LSTM memory units
hidden_units = 256

# Number of unique words/tokens in the target language vocabulary
vocab_size_target = 5000

# Number of times the model will train on the dataset
num_epochs = 10

# Number of training examples processed at a time
batch_size = 32

# Generate 1,000 random input sentences
# Each sentence contains 20 token IDs
# Token IDs range from 0 to 9,999
X_train = np.random.randint(
    0,
    vocab_size_source,
    size=(1000, max_sequence_length_source)
)

# Generate 1,000 random target labels
# Each label is in integer from 0 to 4,999
y_train = np.random.randint(
    0,
    vocab_size_target,
    size=(1000,)
)

# Create a sequential neural network model
model = Sequential([
    # Convert input token IDs into 128-dimensional vectors
    Embedding(
        input_dim=vocab_size_source,
        output_dim=embedding_dim,
        input_length=max_sequence_length_source
    ),
    
    # LSTM layer with 256 memory units
    # Learns patterns and relationships in the input sequence
    LSTM(units=hidden_units),
    
    # Output layer with 5,000 possible target token classes
    # Softmax calculates probabilities for each possible class
    Dense(
        units=vocab_size_target,
        activation='softmax'
    )
])

# Configure the model before training
model.compile(
    # Adam optimizer adjusts model weights during training
    optimizer='adam',
    
    # Measures the error between predicted token classes
    # and the actual target token IDs
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train the model using the generated training data
model.fit(
    X_train,
    y_train,
    epochs=num_epochs,
    batch_size=batch_size,
    verbose=2
)