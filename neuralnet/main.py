import tensorflow as tf
print("line 1 done")
from tensorflow import keras
print("line 2 done")
from tensorflow.keras import layers
print("line 3 done")

from torch.utils.data.sampler import SubsetRandomSampler
from torch.autograd import Variable
from torchviz import make_dot
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import torch.optim as optim


import matplotlib.pyplot as plt
import numpy as np # we always love numpy
import time

import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

if tf.test.gpu_device_name():
    print('GPU found')
else:
    print("No GPU found")

if __name__ == "__main__":
    model = keras.Sequential(
    [
        layers.Dense(1, activation='relu'),
        layers.Dense(2, activation='relu'),
        layers.Dense(3, activation='relu'),
        layers.Dense(4)
    ]
    )
    model.add(keras.Input(shape = 28*28))