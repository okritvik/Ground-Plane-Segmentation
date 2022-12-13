#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Kumara Ritvik Oruganti, Adarsh Malapaka, Sai Sandeep Adapa
Generate binary mask
"""
import os
import cv2

pwd = os.getcwd()

annotations_augmented_path = pwd+"/Dataset/Augmented_Annotations"

bin_dir = pwd+"/Dataset/bin_masks/"

masks = os.listdir(annotations_augmented_path)

for mask in masks:
    frame = cv2.imread(annotations_augmented_path+"/"+mask)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame[frame != 0] = 1
    cv2.imwrite(bin_dir+mask, frame)

print("Done")

