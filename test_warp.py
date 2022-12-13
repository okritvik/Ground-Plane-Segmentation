#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Kumara Ritvik Oruganti, Adarsh Malapaka, Sai Sandeep Adapa
Test bird's eye view perspective
"""
import cv2
import numpy as np

# src = np.float32([[0, IMAGE_H], [1207, IMAGE_H], [0, 0], [IMAGE_W, 0]])
# dst = np.float32([[569, IMAGE_H], [711, IMAGE_H], [0, 0], [IMAGE_W, 0]])

image = cv2.imread("./Dataset/Augmented_Images/B00112.png")
output_pts = np.float32([[469, 719],[811, 719],[0, 0],[1279, 0]])
input_pts = np.float32([[0, 719],[1279, 719],[0, 0],[1279, 0]])

# Compute the perspective transform Matrix M
M = cv2.getPerspectiveTransform(input_pts,output_pts)
out = cv2.warpPerspective(image.copy(), M, (image.shape[1], image.shape[0]), flags=cv2.INTER_LINEAR)
out = cv2.resize(out,(360,1200),interpolation=cv2.INTER_LINEAR) #Resize the image
		

# Display the transformed image
cv2.imshow("Perspective_Transform", out)
cv2.waitKey(0)
cv2.destroyAllWindows()