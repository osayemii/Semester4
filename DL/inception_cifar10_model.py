import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.optimizers import Adam
# Import the pre-built InceptionV3 architecture
from tensorflow.keras.applications import InceptionV3
import tensorflow_datasets as tfds

# Load the CIFAR-10 dataset
dataset, info = tfds.load(
    'cifar10',
    as_supervised=True,
    with_info=True
)

train_dataset = dataset['train']
test_dataset = dataset['test']

input_shape = (299, 299, 3)

num_classes = info.features['label'].num_classes

batch_size = 32

def preprocess_image(image, label):
    image = tf.image.resize(
        image,
        (input_shape[0], input_shape[1])
    )
    
    image = tf.cast(image, tf.float32) / 255.0
    
    label = tf.one_hot(label, num_classes)
    
    return image, label

train_dataset = (
    train_dataset
    .map(preprocess_image)
    .shuffle(1000)
    .batch(batch_size)
)

test_dataset = (
    test_dataset
    .map(preprocess_image)
    .batch(batch_size)
)

base_model = InceptionV3(
    Weights=None,
    include_top=False,
    input_shape=input_shape
)

model = models.Sequential()

model.add(base_model)

model.add(layers.GlobalAveragePooling2D())

model.add(layers.Dense(
    1024,
    activation='relu'
))

model.add(layers.Dense(
    num_classes,
    activation='softmax'
))

model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(
    train_dataset,
    epochs=10,
    validation_data=test_dataset
)

model.save('inceptionv3_cifar10_model.h5')