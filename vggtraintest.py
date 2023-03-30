from google.colab import drive
drive.mount('/content/drive')
import numpy as np 
import matplotlib.pyplot as plt
import os
import tensorflow
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, Input, Dropout,Flatten, Conv2D
from tensorflow.keras.layers import BatchNormalization, Activation, MaxPooling2D
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau
from tensorflow.keras.utils import plot_model
from IPython.display import SVG, Image
train_location = "/content/drive/MyDrive/Number plate/Data Set/Testing Data" 
test_location = "/content/drive/MyDrive/Number plate/Data Set/Testing Data"
filepath = '/content/drive/MyDrive/Number plate/CNN/VGG16/Model/numberplate_VGG16_model1.h5'

preprocess_input = tensorflow.keras.applications.mobilenet.preprocess_input
datagen = ImageDataGenerator(preprocessing_function=preprocess_input)

img_size=224
batch_size=33
num_class=35

datagen_train=ImageDataGenerator(horizontal_flip=True)
train_generator=datagen_train.flow_from_directory(train_location,target_size=(img_size,img_size),batch_size=batch_size,class_mode='categorical',shuffle=True)
datagen_test=ImageDataGenerator(horizontal_flip=True)
validation_generator=datagen_test.flow_from_directory(test_location,target_size=(img_size,img_size),batch_size=batch_size,class_mode='categorical',shuffle=True)

from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
vgg = VGG16(input_shape=[img_size,img_size] + [3], weights='imagenet', include_top=False)

vgg.summary()

