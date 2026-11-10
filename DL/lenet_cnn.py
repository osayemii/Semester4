import tensorflow as tf

from tensorflow.keras import layers, models

def LeNet(input_shape, num_classes):
    
    model = models.Sequential()
    
    # First convolution layer
    model.add(layers.Conv2D(
        6,
        kernel_size=(5,5),
        activation='relu',
        input_shape=input_shape
    ))
    
    model.add(layers.MaxPool2D(
        pool_size=(2,2),
        strides=(2,2)
    ))
    
    # Second convolution layer
    model.add(layers.Conv2D(
        16,
        kernel_size=(5,5),
        activation='relu'
    ))
    
    model.add(layers.MaxPool2D(
        pool_size=(2,2),
        strides=(2,2)
    ))
    
    # Converts the feature map to a 1D vector
    model.add(layers.Flatten())
    
    # First Hidden Layer (fully-connected layer)
    model.add(layers.Dense(
        120,
        activation='relu'
    ))
    
    # Second Hidden Layer (fully-connected layer)
    model.add(layers.Dense(
        84,
        activation='relu'
    ))
    
    # Output Layer - 10 neurons
    model.add(layers.MaxPool2D(
        num_classes,
        activation='softmax'
    ))
    
    return model

input_shape = (32, 32, 3)

num_classes = 10

model = LeNet(input_shape, num_classes)

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()