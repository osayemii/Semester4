import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.applications import ResNet50
#  Early stopping to prevent unnecessary training and reduce iverfitting
from tensorflow.keras.callbacks import EarlyStopping
import tensorflow_datasets as tfds

dataset, info = tfds.load(
    'cifar10',
    as_supervised=True,
    with_info=True
)

# Load CIFAR-10 and divide its original training data
# into training (90%) and validation (10%) portions.
# The original test dataset is kept separate.
(train_dataset, val_dataset, test_dataset), info = tfds.load(
    'cifar10',
    split=['train[:90%]', 'train[90%:]', 'test'],
    as_supervised=True,
    with_info=True
)

input_shape = (32, 32, 3)

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
    .prefetch(tf.data.AUTOTUNE)
)

val_dataset = (
    val_dataset
    .map(preprocess_image)
    .batch(batch_size)
    .prefetch(tf.data.AUTOTUNE)
)

test_dataset = (
    test_dataset
    .map(preprocess_image)
    .batch(batch_size)
    .prefetch(tf.data.AUTOTUNE)
)

base_model = ResNet50(
    weights=None,
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

early_stopping = EarlyStopping(
    monitor='val_loss',
    patience=3,
    restore_best_weights=True
)

model.summary()

history = model.fit(
    train_dataset,
    epochs=10,
    validation_data=val_dataset,
    callbacks=[early_stopping]
)

test_loss, test_accuracy = model.evaluate(test_dataset)

print('Test loss:', test_loss)

print('Test accuracy:', test_accuracy)

model.save('resnet50_cifar10_model.keras')
print('ResNet50 model saved successfully!')