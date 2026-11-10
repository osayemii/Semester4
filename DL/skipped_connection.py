import tensorflow as tf

# Define the input
# Input(shape=(64,)): accepts 64 input features
inputs = tf.keras.Input(shape=(64,))

# First layer
# First Dense: processes the input
x = tf.keras.layers.Dense(64, activation='relu')(inputs)

# Second layer
# Second Dense: performs another transformation
x = tf.keras.layers.Dense(64)(x)

# Skipconnection: add original input
# Add(): adds the original input to the transformed output
x = tf.keras.layers.Add()([inputs, x])

# Apply activation
# Activation('relu'): applies ReLU
x = tf.keras.layers.Activation('relu')(x)

# Output layer
# Final Dense(10): produces 10 output scores
outputs = tf.keras.layers.Dense(10, activation='softmax')(x)

# Build model
model = tf.keras.Model(inputs, outputs)

model.summary()