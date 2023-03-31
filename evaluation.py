from google.colab import drive
drive.mount('/content/drive')

import numpy as np 
import matplotlib.pyplot as plt


import os
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

from tensorflow.keras.models import load_model
Detection=load_model(filepath)

img_size=224
batch_size=33
num_class=36




datagen_train=ImageDataGenerator(horizontal_flip=True)
train_generator=datagen_train.flow_from_directory(train_location,target_size=(img_size,img_size),batch_size=batch_size,class_mode='categorical',shuffle=True)

datagen_test=ImageDataGenerator(horizontal_flip=True)
validation_generator=datagen_test.flow_from_directory(test_location,target_size=(img_size,img_size),batch_size=batch_size,class_mode='categorical',shuffle=True)


classes=train_generator.class_indices
classes

category=[]
for i in classes:
          category.append(i)

category

from skimage import io
import os
from tensorflow.keras.preprocessing import image

image_directory=test_location
dataset = []
predict_result=[]
label =[]


my_folders = os.listdir(image_directory)
for i, folder_name in enumerate(my_folders):
    #print(str(i)+': ' +folder_name) 

    loc=0
    for j in category:
      if(j==folder_name):
        lab=loc
      loc+=1
    lab