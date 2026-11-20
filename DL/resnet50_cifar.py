# 1: Import the required libraries

# Tensorflow is the deep learning framework
import tensorflow as tf
# Import layers and model for building the CNN
from tensorflow.keras import layers, models
# Adam optimizer updates the model weights during training
from tensorflow.keras.optimizers import Adam
# Import the predefined ResNet50 architecture
from tesorflow.keras.applications import ResNet50
