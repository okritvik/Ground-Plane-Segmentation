#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: okritvik
"""

# Initially choose 15% of the total images as the test set randomly

import random
import os
import shutil

curr_dir = os.getcwd()

frames_path = curr_dir+"/Data"

frames = os.listdir(frames_path)

test_folder = curr_dir + "/Dataset/Test"

# print(len(frames))

test_set = random.sample(frames, 83)

# print(len(test_set))

for img in test_set:
    # print(frame)
    shutil.move(frames_path+"/"+img, test_folder+"/"+img)
    
print("Done")