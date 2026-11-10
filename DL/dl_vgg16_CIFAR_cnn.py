# 1: IMPORT THE REQUIRED LIBRARIES
# TensorFlow is the deep learning framework.
import tensorflow as tf

# Import layers and models for building the CNN.
from tensorflow.keras import layers, models

# Adam optimizer updates the model weights during training.
from tensorflow.keras.optimizers import Adam

# Import the pre-defined VGG16 architecture.
from tensorflow.keras.applications import VGG16

# TensorFlow Datasets provides ready-made datasets,
# including CIFAR-10.
import tensorflow_datasets as tfds



# 2: LOAD THE CIFAR-10 DATASET
# Load the CIFAR-10 dataset.
# as_supervised=True: Returns each example as an (image, label) pair.
# with_info=True: Also returns information about the dataset,
# such as the number of classes and dataset features.
dataset, info = tfds.load(
    'cifar10',
    as_supervised=True,
    with_info=True
)

# 3: SPLIT THE DATASET INTO TRAINING AND TESTING
# Training dataset contains images used to train the model.
train_dataset = dataset['train']

# Testing dataset contains images used to evaluate the model.
test_dataset = dataset['test']


# 4: DEFINE THE MODEL PARAMETERS
# CIFAR-10 images have dimensions:
# 32 pixels high, 32 pixels wide and 3 RGB channels.
input_shape = (32, 32, 3)

# Obtain the number of classes from the dataset information.
# CIFAR-10 has 10 image categories.
num_classes = info.features['label'].num_classes

# The model processes 32 images in each training batch.
batch_size = 32



# 5: PREPROCESS THE DATASET
# Define a function to prepare each image and its label.
def preprocess_image(image, label):
    # Resize the image to 32x32 pixels.
    # CIFAR-10 images are already 32x32, but this
    # ensures that all images have the required dimensions.
    image = tf.image.resize(
        image,
        (input_shape[0], input_shape[1])
    )

    # Convert pixel values into float32 numbers.
    # Divide by 255 to normalize pixel values
    # from the range 0-255 into the range 0-1.
    image = tf.cast(image, tf.float32) / 255.0

    # Convert the integer class label into one-hot encoding.
    # For example:
    # Class 0 becomes [1,0,0,0,0,0,0,0,0,0]
    # Class 1 becomes [0,1,0,0,0,0,0,0,0,0]
    # This creates 10 output positions for 10 classes.
    label = tf.one_hot(label, num_classes)

    # Return the processed image and its encoded label.
    return image, label



# 6: APPLY PREPROCESSING TO TRAINING DATA
# map() applies the preprocessing function to every image.
# shuffle(1000) randomly shuffles a buffer of 1000 examples.
# batch(32) groups images into batches of 32.
# This prepares the training data for the CNN.
train_dataset = (
    train_dataset
    .map(preprocess_image)
    .shuffle(1000)
    .batch(batch_size)
)



# 7: APPLY PREPROCESSING TO TESTING DATA
# Apply the same preprocessing to the test images.
# The test dataset is also divided into batches of 32.
# Shuffling is not necessary for evaluation.
test_dataset = (
    test_dataset
    .map(preprocess_image)
    .batch(batch_size)
)



# 8: CREATE THE VGG16 BASE MODEL
# Load the VGG16 architecture.
# weights=None-Initializes the model with random weights.
# It does not use previously trained ImageNet weights.
# include_top=False: Removes the original fully connected classification
# layers of VGG16.
# input_shape:Specifies the dimensions of the input images.
# The VGG16 base model contains:13 convolutional layers and 5 max-pooling layers.
base_model = VGG16(
    weights=None,
    include_top=False,
    input_shape=input_shape
)

# 9: BUILD THE COMPLETE CLASSIFICATION MODEL
# Sequential arranges all model components in order.
model = models.Sequential()

# Add the VGG16 convolutional base.
# This extracts important features from the input images.
model.add(base_model)


# FLATTEN LAYER
# Converts the multidimensional feature maps
# into a one-dimensional vector.
# This prepares the extracted features for Dense layers.
model.add(layers.Flatten())

# FIRST FULLY CONNECTED LAYER
# Creates 4096 neurons.
# Each neuron processes the extracted image features.
# ReLU introduces non-linearity.
model.add(layers.Dense(
    4096,
    activation='relu'
))

# SECOND FULLY CONNECTED LAYER
# Creates another 4096 neurons.
# Further processes the features before classification.
model.add(layers.Dense(
    4096,
    activation='relu'
))

# OUTPUT LAYER
# Creates 10 output neurons because CIFAR-10
# contains 10 different image categories.
# Softmax converts the outputs into probabilities.
# The highest probability represents the predicted class.
model.add(layers.Dense(
    num_classes,
    activation='softmax'
))


# 10: COMPILE THE MODEL
model.compile(
    # Adam optimizer updates weights to reduce errors.
    optimizer=Adam(learning_rate=0.001),

    # Categorical crossentropy is used because
    # the labels have been converted into one-hot encoding.
    loss='categorical_crossentropy',

    # Accuracy measures the percentage of correct predictions.
    metrics=['accuracy']
)



# 11: TRAIN THE MODEL
# Train the VGG16 model using the CIFAR-10 training dataset.
# epochs=10:
# The model goes through the training dataset 10 times.
# validation_data=test_dataset:
# Evaluates the model on the supplied test dataset
# after each epoch.
model.fit(
    train_dataset,
    epochs=10,
    validation_data=test_dataset
)

# 12: SAVE THE TRAINED MODEL
# Save the trained model to a file.
# This allows us to load and reuse it later
# without training the model again.
model.save('vgg16_like_model.h5')
