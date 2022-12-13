#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Kumara Ritvik Oruganti, Adarsh Malapaka, Sai Sandeep Adapa
# Randomly choose 15% original data
"""

# Initially choose 15% of the total images as the test set randomly

import random
import os
# import shutil

curr_dir = os.getcwd()

frames_path = curr_dir+"/Dataset/Augmented_Images"

frames = os.listdir(frames_path)

folder = curr_dir + "/Dataset/"

# print(len(frames))

train_set = random.sample(frames, int(len(frames)*0.8))

# print(len(test_set))

train_file = open(folder+"train.txt", "w")
test_file = open(folder+"test.txt", "w")
valid_file = open(folder+"valid.txt", "w")

for img in train_set:
    train_file.write(img+"\n")
    frames.remove(img)

valid_set = random.sample(frames, int(len(frames)*0.5))

for img in valid_set:
    valid_file.write(img+"\n")
    frames.remove(img)    

for img in frames:
    test_file.write(img+"\n")
    # frames.remove(img)

# assert len(frames) == 0

print("Done")