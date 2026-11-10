from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D,
    MaxPool2D,
    Flatten,
    Dense,
    Dropout
)

def alexnet_model(input_shape, num_classes):
    model = Sequential()
    
    # First Convolution Layer
    model.add(Conv2D(
        filters=96,
        kernel_size=(11,11),
        strides=(4,4),
        activation='relu',
        input_shape=input_shape
    ))
    
    model.add(MaxPool2D(
        pool_size=(3,3),
        strides=(2,2)
    ))
    
    # Second Convolution Layer
    model.add(Conv2D(
        filters=256,
        kernel_size=(5,5),
        strides=(1,1),
        activation='relu',
        padding='same'
    ))
    
    model.add(MaxPool2D(
        pool_size=(3,3),
        strides=(2,2)
    ))
    
    # Third Convolution Layer
    model.add(Conv2D(
        filter=384,
        kernel_size=(3,3),
        strides=(1,1),
        activation='relu',
        padding='same'
    ))
    
    # Fourth Convolution Layer
    model.add(Conv2D(
        filters=384,
        kernel_size=(3,3),
        strides=(1,1),
        activation='relu',
        padding='same'
    ))
    
    # Fifth Convolution Layer
    model.add(Conv2D(
        filter=256,
        kernel_size=(3,3),
        strides=(1,1),
        activation='relu',
        padding='same'
    ))
    
    model.add(MaxPool2D(
        pool_size=(3,3),
        strides=(2,2)
    ))
    
    # Converting the flatmap into a 1D vector
    model.add(Flatten())
    
    # First fully-connected Layer
    model.add(Dense(
        4096,
        activation='relu'
    ))
    
    # Dropping off 50% neurons
    model.add(Dropout(0.5))
    
    # Second fully-connected Layer
    model.add(Dense(
        4096,
        activation='relu'
    ))
    
    # Dropping off 50% neurons
    model.add(Dropout(0.5))
    
    # Output Layer
    model.add(Dropout(
        num_classes,
        activation='softmax'
    ))
    
    return model

input_shape = (224, 224, 3)

num_classes = 1000

model = alexnet_model(input_shape, num_classes)

model.summary()