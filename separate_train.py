#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: okritvik
"""

# Move Remaining data to training set

import random
import os
import shutil

curr_dir = os.getcwd()

frames_path = curr_dir+"/Data"

frames = os.listdir(frames_path)

train_folder = curr_dir + "/Dataset/Train"


# print(len(test_set))

for frame in frames:
    # print(frame)
    shutil.move(frames_path+"/"+frame, train_folder+"/"+frame)
    
print("Done Separating Training Data")