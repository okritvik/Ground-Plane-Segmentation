#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: okritvik

Random brightness and contrast for the image
"""
import albumentations as A

import os
import cv2

pwd = os.getcwd()

train_path = pwd+"/Dataset/Train"

augmented_path = pwd+"/Dataset/Augmented_Images"


transform = A.Compose([
            A.RandomBrightnessContrast(p=0.7, brightness_limit=0.5)
            ])

train_images = os.listdir(train_path)

print("Train Path: ", train_path)
print("Augmented Images Path: ", augmented_path)

for img in train_images:
    frame = cv2.imread(train_path+"/"+img)
    tf = transform(image=frame)
    tf_image = tf["image"]

    cv2.imwrite(augmented_path+"/"+"C"+img, tf_image)
    
print("done random brightness and contrast on the images")