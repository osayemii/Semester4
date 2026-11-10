import tensorflow as tf

model = tf.keras.Sequential([
    # Dense(64): Creates a layer containing 64 neurons
    tf.keras.layers.Dense(64, input_shape=(20,)),
    
    # BatchNormalization(): normalizes the l(ayer's activation
    tf.keras.layers.BatchNormalization(),
    
    ## Notice that batch Normalization is placed between the Dense layer and the the ReLU activation
    # ReLU(): introduces non-linearity
    tf.keras.layers.ReLU(),
    
    # Dense(10): produces 10 output scores
    # softmax: converts the score into probabilities
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()