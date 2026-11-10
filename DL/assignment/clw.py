import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D,
    Dense,
    MaxPooling2D,
    Flatten
)

def clwp(input_shapes, num_classes):
    
    model = Sequential()
    
    # Convolution layer
    model.add(Conv2D(
        filters=32,
        kernel_size=(3,3),
        strides=(1,1),
        padding='same'
    ))
    
    # Pooling layer
    model.add(MaxPooling2D(
        pool_size=(2,2),
        strides=(2,2)
    ))
    
    model.add(Flatten())
    
    model.add(Dense(
        64,
        activation='relu'
    ))
    
    model.add(Dense(
        num_classes,
        activation='softmax'
    ))
    
    return model
    
input_shapes = (28, 28, 1)

num_classes = 10

model = clwp(input_shapes, num_classes)

model.summary()