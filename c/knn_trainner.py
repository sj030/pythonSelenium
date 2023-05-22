import os
import cv2
import numpy as np
from warnings import filterwarnings

filterwarnings(action='ignore', category=DeprecationWarning, message='`np.object` is a deprecated alias')

file_name = 'a'
last_filename = 'z'
train = []
train_labels = []

while file_name <= last_filename:
    path = './alphabet/' + file_name + '/'
    file_count = len(next(os.walk(path))[2])
    for i in range(1, 1 + file_count):
        img_path = path + file_name + str(i) + '.png'
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        train.append(img)
        train_labels.append(file_name)
    file_name = chr(ord(file_name) + 1)

x = np.array(train, dtype=object)
train = x[::].reshape(-1, 780).astype(np.object)
train_labels = np.array(train_labels)[:, np.newaxis]

np.savez("trained.npz", train=train, train_labels=train_labels)
