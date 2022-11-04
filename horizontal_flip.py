#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: okritvik
Horizontal flip
"""

import os
import cv2


pwd = os.getcwd()

train_path = pwd+"/Dataset/Train"

augmented_path = pwd+"/Dataset/Augmented_Images"

train_images = os.listdir(train_path)

print("Train Path: ", train_path)
print("Augmented Images Path: ", augmented_path)

for img in train_images:
    frame = cv2.imread(train_path+"/"+img)
    frame = cv2.flip(frame, 1)
    cv2.imwrite(augmented_path+"/"+"A"+img, frame)
    
print("done flipping the images")