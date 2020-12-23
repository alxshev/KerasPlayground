import tensorflow.keras as keras
from matplotlib import pyplot as plt
import numpy as np

mnist = keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

digit = train_images[4]
# plt.imshow(digit, cmap='binary')
# plt.show()
# print(np.)

