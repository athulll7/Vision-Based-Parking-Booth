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