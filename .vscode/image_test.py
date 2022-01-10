import cv2
import matplotlib.pyplot as plt
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow_datasets as tfds
import tensorflow as tf


data_train, ds_info = tfds.load('cats_vs_dogs', split=[tfds.Split.TRAIN], with_info=True, shuffle_files=True)
# print(ds_info)

images = [one['image'].numpy() for one in data_train[0]. take(30)]
len(images)


# plt.imshow(images[13])
# plt.axis('off')