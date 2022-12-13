#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Kumara Ritvik Oruganti, Adarsh Malapaka, Sai Sandeep Adapa
Original Annotated images convert file names
"""

import os
import cv2


pwd = os.getcwd()

root_folder = pwd+"/dataloop"

author_folders = os.listdir(root_folder)

annotations_folder = pwd + "/Dataset/Annotations/"

# print(author_folders)

for author in author_folders:
    inside  =  root_folder + "/" + author

    files = os.listdir(inside)
    # print(files)
    for file in files:
        file_name = file.split(".")
        # print(file_name)
        if file_name[-1] == "png":
            # print("PNG FILE")
            split_name  = file_name[0].split("-")
            # print(split_name)
            if(split_name[1].lstrip().rstrip() == "path"):
                req_file_name = split_name[0].lstrip().rstrip() + ".png"
                os.rename(inside+"/"+file, annotations_folder+req_file_name)
                # print(split_name, req_file_name)

                # img = cv2.imread(req_file_name)
                # cv2.imshow("Frame", img)
                # cv2.imwrite(annotations_folder+req_file_name, img)
