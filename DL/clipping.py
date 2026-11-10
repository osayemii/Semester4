import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.SimpleRNN(64, input_shape=(10, 1)),
    tf.keras.layers.Dense(1)
])

# Apply gradient clipping
optimizer = tf.keras.optimizers.Adam(
    learning_rate=0.001,
    clipnorm=1.0 #clips the global norm of gradients to max of 1
)

model.compile(
    optimizer=optimizer,
    loss='mse'
)

model.summary()