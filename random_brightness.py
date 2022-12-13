#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Kumara Ritvik Oruganti, Adarsh Malapaka, Sai Sandeep Adapa

Random brightness and contrast for the image
"""
import albumentations as A

import os
import cv2

pwd = os.getcwd()

train_path = pwd+"/Dataset/Train"

augmented_path = pwd+"/Dataset/Augmented_Images"

annotations_path = pwd+"/Dataset/Annotations"
annotations_augmented_path = pwd+"/Dataset/Augmented_Annotations"

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

    # Save same annotation with file name for the file as it is just contrast and brightness
    frame = cv2.imread(annotations_path+"/"+img)
    cv2.imwrite(annotations_augmented_path+"/"+"C"+img, frame)
    
print("done random brightness and contrast on the images")