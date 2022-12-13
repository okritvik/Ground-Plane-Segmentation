#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Kumara Ritvik Oruganti, Adarsh Malapaka, Sai Sandeep Adapa
Add gaussian noise to the images
"""

import os
import cv2

pwd = os.getcwd()

train_path = pwd+"/Dataset/Train"

augmented_path = pwd+"/Dataset/Augmented_Images"

annotations_path = pwd+"/Dataset/Annotations"
annotations_augmented_path = pwd+"/Dataset/Augmented_Annotations"

train_images = os.listdir(train_path)

print("Train Path: ", train_path)
print("Augmented Images Path: ", augmented_path)

for img in train_images:
    frame = cv2.imread(train_path+"/"+img)
    blur = cv2.blur(frame,(7,7))
    cv2.imwrite(augmented_path+"/"+"G"+img, frame)

    # Save same annotation with file name for the file as it is just gaussian blur
    frame = cv2.imread(annotations_path+"/"+img)
    cv2.imwrite(annotations_augmented_path+"/"+"G"+img, frame)
    
print("Added Gaussian noise to the images")
