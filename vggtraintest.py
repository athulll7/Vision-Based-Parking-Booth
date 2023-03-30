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

for layer in vgg.layers:
  layer.trainable = False
x = Flatten()(vgg.output)
prediction = Dense(num_class, activation='softmax')(x)
detection = Model(inputs=vgg.input, outputs=prediction)
detection.summary()

optimum=Adam(learning_rate=0.005)
detection.compile(optimizer=optimum,loss='categorical_crossentropy',metrics=['accuracy'])

print(train_generator.class_indices)

TRAIN_STEPS=train_generator.n//train_generator.batch_size
TRAIN_STEPS

VALIDATION_STEPS=validation_generator.n//validation_generator.batch_size
VALIDATION_STEPS

checkpoint = ModelCheckpoint(filepath, monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')

reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(monitor='val_accuracy',
                              factor=0.5,
                              patience=2, 
                              verbose=1,
                              mode='max',
                              min_lr=0.00001)

callbacks_list = [checkpoint, reduce_lr]

history = detection.fit(train_generator,
                              steps_per_epoch=TRAIN_STEPS, 
                              validation_data=validation_generator,
                              validation_steps=VALIDATION_STEPS,
                              epochs=5,
                              verbose=1,
                              callbacks=callbacks_list
                             )
detection.metrics_names

detection.evaluate_generator(validation_generator,steps=TRAIN_STEPS)

import matplotlib.pyplot as plt

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc) + 1)

plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()
plt.figure()

plt.plot(epochs, acc, 'bo', label='Training accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
plt.title('Training and validation accuracy')
plt.legend()
plt.figure()

plt.show()

epochs
loss
val_loss
acc
val_acc